import defusedxml.ElementTree as ET
import xmltodict
import json
import pprint
from treelib import Node, Tree

xml_in_file = '/Users/arajagopalan/PycharmProjects/my-python-doodle/my-python-practice/xmlparse/ssg-ubuntu2004-ds-1.2.xml'

json_data = json.loads(json.dumps(xmltodict.parse(ET.tostring(ET.parse(xml_in_file).getroot())), indent=4))

print(json_data['ns0:data-stream-collection']['ns0:component'][1]['ns5:Benchmark']['ns5:Group'][0].keys())


def get_nested_value(data, keys):
    if not keys:
        return data
    key = keys.pop(0)
    if isinstance(data, dict):
        return get_nested_value(data.get(key), keys)
    elif isinstance(data, list):
        # Here, key should be an integer (string of a digit) for list indexing
        try:
            key = int(key)
            return get_nested_value(data[key], keys)
        except ValueError:
            return None
    else:
        return None


# Define the JSON path
json_path = [
    "ns0:data-stream-collection", "ns0:component", "1",
    "ns5:Benchmark", "ns5:Group", "0", "ns5:Group", "0",
    "ns5:Group", "0", "ns5:Group", "0", "ns5:Group",
    "ns5:Rule", "0", "@id"
]

# Parse the JSON data
data = json.loads(json_data)

# Get the value using the defined path
value = get_nested_value(data, json_path.copy())

# Print the result
print(value)

#print(isinstance(data['ns0:data-stream-collection']['ns0:component'][1]['ns5:Benchmark']['ns5:Group'], list))

#print(data.keys())
# print(data['ns0:asset-report-collection'].keys())
# print(data['ns0:asset-report-collection']['ns0:reports'].keys())
# print(data['ns0:asset-report-collection']['ns0:reports']['ns0:report'][0]['ns0:content']['ns7:TestResult']['ns7:rule-result'][0])

'''
for result in data['ns0:asset-report-collection']['ns0:reports']['ns0:report'][0]['ns0:content']['ns7:TestResult']['ns7:rule-result']:
    print(result['@idref'], result['ns7:result'])
'''

# print(data['ns0:asset-report-collection']['ns0:report-requests']['ns0:report-request']['ns0:content']['ns2:data-stream-collection']['ns2:component'][1]['ns7:Benchmark']['ns7:Group'][0]['ns7:Group'][0].keys())
# print(data['ns0:asset-report-collection']['ns0:report-requests']['ns0:report-request']['ns0:content']['ns2:data-stream-collection']['ns2:component'][1]['ns7:Benchmark']['ns7:Group'][0]['ns7:Group'][0]['ns7:Group'][0]['ns7:Group'][0]['ns7:Group']['ns7:Rule'][0]['ns7:reference'])
'''
for item in data['ns0:asset-report-collection']['ns0:report-requests']['ns0:report-request']['ns0:content']['ns2:data-stream-collection']['ns2:component'][1]['ns7:Benchmark']['ns7:Group'][0]['ns7:Group'][0]['ns7:Group'][0]['ns7:Group'][0]['ns7:Group']['ns7:Rule'][0]['ns7:reference']:
    # print(item.keys())
    if item['@href'] == 'https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=operating-systems%2Cunix-linux':
        print(item['#text'])
'''
# print(data['ns0:asset-report-collection']['ns0:report-requests']['ns0:report-request']['ns0:content']['ns2:data-stream-collection'].keys())
# print(data['ns0:asset-report-collection']['ns0:report-requests']['ns0:report-request']['ns0:content']['ns2:data-stream-collection']['ns2:component'][1]['ns7:Benchmark'].keys())
# print(data['ns0:asset-report-collection']['ns0:report-requests']['ns0:report-request']['ns0:content']['ns2:data-stream-collection']['ns2:component'][1]['ns7:Benchmark']['ns7:Group'][0])
# print(data['ns0:asset-report-collection']['ns0:report-requests']['ns0:report-request']['ns0:content']['ns2:data-stream-collection']['ns2:component'][1]['ns7:Benchmark']['ns7:Group'][0]['ns7:Group'][0].keys())
# print(data['ns0:asset-report-collection']['ns0:report-requests']['ns0:report-request']['ns0:content']['ns2:data-stream-collection']['ns2:component'][1]['ns7:Benchmark']['ns7:Group'][0]['ns7:Group'][0])

'''
reportData = data['ns0:asset-report-collection']['ns0:report-requests']['ns0:report-request']['ns0:content']['ns2:data-stream-collection']['ns2:component'][1]['ns7:Benchmark']['ns7:Group'][0]['ns7:Group'][0]
with open('report1.json', 'w') as json_file:
    json.dump(reportData, json_file, indent=4)
    [0]['ns7:reference'][73]['#text']


def enumerate_data(content):
    if isinstance(content, dict):
        if 'ns7:Rule' in content.keys():
            print('**********')
            if isinstance(content['ns7:Rule'], list):
                for item in content['ns7:Rule']:
                    print(item['@id'])
                    #print(item.keys())
            else:
                print(content['ns7:Rule']['@id'])
        for key, value in content.items():
            if key == '@href' and value == 'https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=operating-systems%2Cunix-linux':
                print(f"Found key: {key} with value: {content['#text']}")
            else:
                enumerate_data(value)
    elif isinstance(content, list):
        for item in content:
            enumerate_data(item)

# Call the function with your data
enumerate_data(data['ns0:asset-report-collection']['ns0:report-requests']['ns0:report-request']['ns0:content'][
                   'ns2:data-stream-collection']['ns2:component'][1]['ns7:Benchmark']['ns7:Group'][0])
'''
