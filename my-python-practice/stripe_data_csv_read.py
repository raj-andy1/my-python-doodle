# sample program to extract values from CSV file
import pycountry
import pycountry
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


with open('/Users/arajagopalan/Downloads/PM Interview Churn Data - Sept 21.csv', 'r', encoding='utf-8') as csvfile:
    lines = csvfile.readlines()
    for line in lines:
        item = line.rstrip("\n").split(',')
        Reason_for_Migration_Request.append(item[fields.index('Reason for Migration Request')])
        Intended_Processor.append(item[fields.index('Intended Processor')])
        User_Country.append(item[fields.index('User Country')])
        Segment.append(item[fields.index('Segment')])


Reason_for_Migration_Request.remove('Reason for Migration Request')
Intended_Processor.remove('Intended Processor ')
User_Country.remove('User Country')
Segment.remove('Segment ')
for country in User_Country:
    try:
        new_User_Country.append(pycountry.countries.lookup(country).name)
    except LookupError as e:
        print(e)
#print(new_User_Country)
print('***********')
print('Total:', len(set(Reason_for_Migration_Request)))
print(*set(sorted(Reason_for_Migration_Request)), sep='\n')
print('##')
for reason in set(Reason_for_Migration_Request):
    print(reason, Reason_for_Migration_Request.count(reason), sep='\t')
print('***********')
print(*set(sorted(Intended_Processor)), sep='\n')
print('***********')
print(*set(sorted(new_User_Country)), sep='\n')
print('##')
for country in set(User_Country):
    print(country, User_Country.count(country), sep='\t')
print('***********')
print(*set(sorted(Segment)), sep='\n')