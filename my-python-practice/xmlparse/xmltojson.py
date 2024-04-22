import defusedxml.ElementTree as ET
import xmltodict
import json

xml_in_file = '/Users/arajagopalan/PycharmProjects/my-python-doodle/my-python-practice/xmlparse/anupam_dey01193825149361.xml'

data = json.loads(json.dumps(xmltodict.parse(ET.tostring(ET.parse(xml_in_file).getroot()))))
# print(data)
# print(data['Log']['Message'])
for msg in data['Log']['Message']:
    # print(msg)
    # print(msg.keys())
    # print(msg['From'].keys())
    # print(msg['From']['User']['@FriendlyName'])
    try:
        print(f'From: {msg["From"]["User"]["@FriendlyName"]}, '
              f'To: {msg["To"]["User"]["@FriendlyName"]}, '
              f'Message: {msg["Text"]["#text"]}')
    except TypeError:
        print(msg)
        print(f'From: {msg["From"]["User"]["@FriendlyName"]}, '
              f'To: {msg["To"]["User"]["@FriendlyName"]}, '
              f'Message: {msg["Text"]}')
