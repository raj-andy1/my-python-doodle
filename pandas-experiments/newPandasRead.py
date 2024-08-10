import pandas as pd

exclude_controls = ['UBTU-20-010042',
 'UBTU-20-010411',
 'UBTU-20-010416',
 '1.1.2','1.1.7','2.13','2.17','2.8',
'3.7','3.8','4.1','4.5',
 '4.8','4.9','5.14','5.28','5.4','5.6','5.9','6.1',
 '6.2','5.13','UBTU-20-010449','2.14','2.16','5.19','5.15','5.7',
 'UBTU-20-010429','UBTU-20-010431','5.25','1.2','UBTU-20-010036',
 'UBTU-20-010043','UBTU-20-010044','UBTU-20-010045','UBTU-20-010100',
 'UBTU-20-010101','UBTU-20-010102','UBTU-20-010103','UBTU-20-010104',
 'UBTU-20-010117','UBTU-20-010118','UBTU-20-010122','UBTU-20-010123',
 'UBTU-20-010124','UBTU-20-010133','UBTU-20-010134','UBTU-20-010135',
 'UBTU-20-010136','UBTU-20-010137','UBTU-20-010138','UBTU-20-010139',
 'UBTU-20-010140','UBTU-20-010141','UBTU-20-010142','UBTU-20-010148',
 'UBTU-20-010152','UBTU-20-010155','UBTU-20-010161','UBTU-20-010162',
 'UBTU-20-010163','UBTU-20-010164','UBTU-20-010165','UBTU-20-010166',
 'UBTU-20-010167','UBTU-20-010168','UBTU-20-010169','UBTU-20-010170',
 'UBTU-20-010171','UBTU-20-010172','UBTU-20-010173','UBTU-20-010174',
 'UBTU-20-010175','UBTU-20-010176','UBTU-20-010177','UBTU-20-010178',
 'UBTU-20-010179','UBTU-20-010181','UBTU-20-010182','UBTU-20-010198',
 'UBTU-20-010199','UBTU-20-010200','UBTU-20-010201','UBTU-20-010211',
 'UBTU-20-010244','UBTU-20-010267','UBTU-20-010277','UBTU-20-010278',
 'UBTU-20-010279','UBTU-20-010296','UBTU-20-010297','UBTU-20-010298',
 'UBTU-20-010436','1.1.10','1.1.11','1.1.12','1.1.13','1.1.14','1.1.15',
 '1.1.16','1.1.17','1.1.18','1.1.3','1.1.4','1.1.5','1.1.6','1.1.8',
 '1.1.9','5.8','3.16','UBTU-20-010458']

df = pd.read_csv('tickets_csv.csv')
df[['Rule ID', 'Text']] = df['control'].str.extract(r'([A-Z]+-\d+-\d+|\d+\.\d+\.\d+|\d+\.\d+) (.*)')
df['Text'] = df['Text'].str.replace('-', '', 1)
#print(df)
df = df[df['Rule ID'].isin(exclude_controls)]
# Assuming df is your DataFrame and 'resource' is your column
df['micros_column'] = df.apply(lambda row: 'micros' if 'micros' in row['resource'] else row['owner'], axis=1)
df.drop(columns=['control'], inplace=True)
df.to_csv('new_tickets_csv_1.csv', index=False)
unique_rule_ids = df['Rule ID'].unique()
print(unique_rule_ids)
print(len(unique_rule_ids))
print (unique_rule_ids == exclude_controls)
