# sample program to extract values from CSV file
import pycountry
import pandas as pd

fields = ['Date',
          'UserID',
          'Lifetime Net Processing Volume (NPV)',
          'Last 19 months NPV',
          'Last Month NPV (Net Processing Volume)',
          'Segment',
          'User Country',
          'Intended Processor',
          'Reason for Migration Request',
          'Outcome']

Reason_for_Migration_Request = []
Intended_Processor = []
User_Country = []
new_User_Country = []
Segment = []


with open('/Users/arajagopalan/Downloads/NAM_Stripe_cleaned.csv', 'r', encoding='utf-8') as csvfile:
    lines = csvfile.readlines()
    for line in lines:
        item = line.rstrip("\n").split(',')
        Reason_for_Migration_Request.append(item[fields.index('Reason for Migration Request')])
        Intended_Processor.append(item[fields.index('Intended Processor')])
        Segment.append(item[fields.index('Segment')])

Reason_for_Migration_Request.remove('Reason for Migration Request')
Segment.remove('Segment')
"""
print('***********')
print('Total:', len(set(Reason_for_Migration_Request)))
print(*set(sorted(Reason_for_Migration_Request)), sep='\n')
print('##')
for reason in set(Reason_for_Migration_Request):
    print(reason, Reason_for_Migration_Request.count(reason), sep='\t')
print('***********')
print(*set(sorted(Intended_Processor)), sep='\n')
print('##')
print('Total:', len(set(Intended_Processor)))
for processor in set(Intended_Processor):
    print(processor, Intended_Processor.count(processor), sep='\t')
print('***********')
print(*set(sorted(Segment)), sep='\n')
print('##')
for segment in set(Segment):
    print(segment, Segment.count(segment), sep='\t')
"""

df = pd.read_csv('/Users/arajagopalan/Downloads/NAM_Stripe_cleaned.csv', sep=',')
#print(df)
#df.groupby(['Name', 'Fruit'])['Number'].sum()
print('Lifetime Net Processing Volume (NPV)')
print(df.groupby(['Segment'])['Lifetime Net Processing Volume (NPV)'].sum())
print('Last 19 months NPV')
print(df.groupby(['Segment'])['Last 19 months NPV'].sum())
print('Last Month NPV (Net Processing Volume)')
print(df.groupby(['Segment'])['Last Month NPV (Net Processing Volume)'].sum())

print(df.groupby(['Segment', 'Reason for Migration Request'])['Reason for Migration Request'].count())
df.groupby(['Segment', 'Reason for Migration Request'])['Reason for Migration Request'].count().to_csv('stripe_output.csv')

