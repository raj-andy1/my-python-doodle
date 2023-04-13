# sample program to extract values from CSV file
import csv

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
with open('/Users/arajagopalan/Downloads/NAM_Stripe_cleaned.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(fields)

with open('/Users/arajagopalan/Downloads/PM Interview Churn Data - Sept 21.csv', 'r', encoding='utf-8') as csvfile:
    lines = csvfile.readlines()
    for line in lines:
        item = line.rstrip("\n").split(',')
        if item[fields.index('User Country')] in ['US', 'CA'] and \
                item[fields.index('Reason for Migration Request')] not in ['Business Shutting down']:
            # print(item[fields.index('Reason for Migration Request')])
            item[fields.index('Lifetime Net Processing Volume (NPV)')] = int(
                float((item[fields.index('Lifetime Net Processing Volume (NPV)')])))
            item[fields.index('Last 19 months NPV')] = int(
                float((item[fields.index('Last 19 months NPV')])))
            item[fields.index('Last Month NPV (Net Processing Volume)')] = int(
                float((item[fields.index('Last Month NPV (Net Processing Volume)')])))
            if item[fields.index('Reason for Migration Request')] in ['"Lack of Capabilities - Insights (declines']:
                # print(item[fields.index('Outcome')])
                item[fields.index(
                    'Reason for Migration Request')] = 'Lack of Capabilities - Insights (declines fraud etc.)'
                if item[fields.index('UserID')] == 0.2334319957:
                    item[fields.index('Outcome')] = 'Saved'
                else:
                    item[fields.index('Outcome')] = 'Churning'
            with open('/Users/arajagopalan/Downloads/NAM_Stripe_cleaned.csv', 'a') as f:
                write = csv.writer(f)
                write.writerow(item)
