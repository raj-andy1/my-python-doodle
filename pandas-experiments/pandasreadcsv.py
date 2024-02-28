import re
import csv

'''
import pandas as pd

df = pd.read_csv('Compliance_Scan_-_Docker.csv')


df = pd.read_csv('/Users/arajagopalan/Downloads/Baseline_Agent_Scan_-_Docker.csv')
filtered_df = df[df['Plugin ID'] == 21157]
filtered_df.to_csv('Compliance_Scan_-_Docker.csv', index=False)
rules_list = []
rules_list.extend(df['Description'].to_list())
print(rules_list)
'''

with open('Docker_compliance.csv', 'w') as csvfile:
    csvfile.truncate()
    csv_writer = csv.writer(csvfile)
    header = ['Instance Id', 'Rule Id', 'Rule Description', 'Evaluation Result']
    csv_writer.writerow(header)
    print('Header Written')


with open('Compliance_Scan_-_Docker.csv', 'r', encoding='utf-8') as csvfile:
    lines = csv.reader(csvfile)
    headers = next(lines)
    instId = set()
    num=0
    for line in lines:
        num += 1
        result = re.search(r'((\d+\.\d+)|(\d+\.\d+\.\d+))\s+(.*)\s*:', line[9])
        #print(result)
        try:
            rule_id = result.group(2) if result.group(2) else result.group(3)
            rule_desc = result.group(4)
        except AttributeError:
            print(f'Line number: {num}')
            print(result) if result else print(line)
        rule_eval = re.search("\[([A-Z]+)\]", line[9]).group(0).strip('[').strip(']')
        instId.add(line[4])
        #print(rule_id, '+', rule_desc, '+', rule_eval, '+', inst_id)
        with open('Docker_compliance.csv', 'a') as resultsfile:
            results_writer = csv.writer(resultsfile, delimiter=',')
            results_writer.writerow([line[4], rule_id, rule_desc, rule_eval])
print('DONE')
print(f'numer of instances: {len(instId)}')



