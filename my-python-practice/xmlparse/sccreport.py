import xml.etree.ElementTree as ET
import csv
from more_itertools import unique_everseen

tree = ET.parse('IP-10-9-189-232_SCC-5.9_2024-08-09_232620_XCCDF-Results_Canonical_Ubuntu_20-04_LTS_STIG-1.9.6.xml')
root = tree.getroot()


results = []
for result in root.findall('.//{*}rule-result'):
    # print(result.attrib)
    result_dict = {'rule_name': result.attrib['version'], 'severity': result.attrib['severity']}
    for check in result.findall('.//{*}result'):
        # print(check.text)
        result_dict['result'] = check.text
    results.append(result_dict)
print(results)

fields = ['rule_name', 'severity', 'result']
filename = 'sccreport.csv'
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerows(results)
