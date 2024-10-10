import xml.etree.ElementTree as ET
import csv

#tree = ET.parse('ssg-ubuntu2004-ds-1.2.xml')
#tree = ET.parse('report.xml')
tree = ET.parse('hostfsresults.xml')
root = tree.getroot()

# Some XML attributes were omitted for clarity.
#
# <ds:component id="scap_org.open-scap_comp_ssg-ubuntu2004-xccdf.xml">
#   <xccdf-1.2:Benchmark id="xccdf_org.ssgproject.content_benchmark_UBUNTU_20-04">
#     <xccdf-1.2:Group id="xccdf_org.ssgproject.content_group_system">
#       <xccdf-1.2:Group id="xccdf_org.ssgproject.content_group_software">
#         <xccdf-1.2:Group id="xccdf_org.ssgproject.content_group_integrity">
#           <xccdf-1.2:Group id="xccdf_org.ssgproject.content_group_software-integrity">
#             <xccdf-1.2:Group id="xccdf_org.ssgproject.content_group_aide">
#               <xccdf-1.2:Rule id="xccdf_org.ssgproject.content_rule_package_aide_installed" severity="medium">
#                 <xccdf-1.2:reference href="https://public.cyber.mil/stigs/srg-stig-tools/">UBTU-20-010450</xccdf-1.2:reference>

rules = {}
result_list = []
rule_set = set()
target = root.find('.//{*}target')
print(target.text)
for rule in root.findall('.//{*}Rule'):
    rule_dict = {}
    # e.g. xccdf_org.ssgproject.content_rule_package_aide_installed
    rule_id = rule.attrib['id']
    print(rule_id)
    # e.g. medium
    rule_dict['target'] = target.text
    rule_dict['rule_name'] = rule.attrib['id']
    rule_dict['severity'] = rule.attrib['severity']
    severity = rule.attrib['severity']
    references = rule.findall('.//{*}reference')
    for reference in references:
        print(reference.text)
        # Filter for STIG.
        if not reference.attrib['href'].startswith(
                'https://public.cyber.mil/stigs/srg-stig-tools'):
            # print(reference.attrib['href'])
            continue
        # e.g. UBTU-20-010450
        if not reference.text.startswith('SV-'):
            # print(reference.text)
            continue
        rules[rule_id] = (severity, reference.text)
        rule_dict['rule_control_id'] = reference.text
        #print(rules[rule_id])
        #rule_set.add(reference.text)
        #print(rule_dict)
        result_list.append(rule_dict)
#print(result_list)

results = []
for result in root.findall('.//{*}rule-result'):
    # print(result.attrib)
    result_dict = {}
    result_dict['rule_id'] = result.attrib['idref']
    if result is not None:
        result_status = result.find('{*}result')
        # print(result_status.text)
        result_dict['rule_result'] = result_status.text
    results.append(result_dict)

#print(results)

results_lookup = {item['rule_id']: item['rule_result'] for item in results}

# Add 'rule_result' to items in dict1 based on the corresponding 'rule_id' in dict2
for item in result_list:
    rule_id = item['rule_name']
    if rule_id in results_lookup:
        item['rule_result'] = results_lookup[rule_id]
    else:
        item['rule_result'] = 'notselected'  # Or some default value if not found in dict2

# Print the updated dict1
#print(results)
#print(sorted(rule_set))
print(result_list)

fields = ['target', 'rule_name', 'severity', 'rule_control_id', 'rule_result']
filename = 'rule_results.csv'
with open(filename, 'w') as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerows(result_list)

'''
    
rule_id = result.attrib['idref']
        if result is not None:
            result_status = result.find('{*}result')
            #print(result_status.text)
            if result_status.text != 'notselected':
                if rule_id in rules.keys():
                    print(f'{rule_id}|{rules[rule_id][0]}|{rules[rule_id][1]}|{result_status.text}')
                else:
                    print(f'{rule_id}|UNKNOWN|UNKNOWN|{result_status.text}')

rule_id = result.attrib['idref']
    #print(rule_id)
    # e.g. pass
    result = result.attrib['result']
    #print(result)
    if rule_id in rules:
        print(f'{rule_id}|{rules[rule_id][0]}|{rules[rule_id][1]}|{result}')
    else:
        print(f'{rule_id}|UNKNOWN|UNKNOWN|{result}')
for rule_id, (severity, reference) in sorted(rules.items(), key=lambda x: x[0]):
    print(f'{rule_id}|{severity}|{reference}')
'''


"""
Sample Data Structure for dict 1:
rule_id: str
rule_control_id: str
rule_result: str
rule_severity: str
target: str

dict1 = [{'rule_name': 'xccdf_org.ssgproject.content_rule_package_aide_installed', 
'severity': 'medium', 
'rule_control_id': 'UBTU-20-010450'}, 
{'rule_name': 'xccdf_org.ssgproject.content_rule_aide_build_database', 
'severity': 'medium', 
'rule_control_id': 'UBTU-20-010450'}, 
{'rule_name': 'xccdf_org.ssgproject.content_rule_aide_check_audit_tools', 
'severity': 'medium', 
'rule_control_id': 'UBTU-20-010205'}]

Sample Data Structure for dict 2:
rule_id: str
rule_result: str

dict2  = [{'rule_id': 'xccdf_org.ssgproject.content_rule_prefer_64bit_os', 'rule_result': 'notselected'}, 
         {'rule_id': 'xccdf_org.ssgproject.content_rule_package_prelink_removed', 'rule_result': 'notselected'}, 
         {'rule_id': 'xccdf_org.ssgproject.content_rule_package_aide_installed', 'rule_result': 'fail'}]
        
"""
