import xml.etree.ElementTree as ET
import csv
from more_itertools import unique_everseen

tree = ET.parse('hostfsresults.xml')
root = tree.getroot()

rules = {}
result_list = []

for rule in root.findall('.//{*}Rule'):
    rule_dict = {}
    rule_id = rule.attrib['id']  # e.g. xccdf_org.ssgproject.content_rule_package_aide_installed
    severity = rule.attrib['severity']  # e.g. medium
    # print(rule_id)
    rule_dict['rule_name'] = rule.attrib['id']
    rule_dict['severity'] = rule.attrib['severity']
    references = rule.findall('.//{*}reference')
    for reference in references:
        # Filter for STIG.
        if not reference.attrib['href'].startswith(
                'https://public.cyber.mil/stigs/srg-stig-tools'):
            # print(reference.attrib['href'])
            continue
        if reference.text.startswith('UBTU-20'):  # e.g. UBTU-20-010450
            # print(reference.text)
            rule_dict['rule_control_id_1'] = reference.text
        elif reference.text.startswith('SV-'):
            rule_dict['rule_control_id_2'] = reference.text
        result_list.append(rule_dict)
print(result_list)

fields = ['rule_name', 'severity', 'rule_control_id_1', 'rule_control_id_2']
filename = 'rule_map.csv'
with open(filename, 'w') as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerows(unique_everseen(result_list))
