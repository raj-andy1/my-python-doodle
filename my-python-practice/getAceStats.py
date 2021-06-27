import json
import datetime
import dateutil.parser

xaceFile = 'newAllAce.csv'
with open(xaceFile, 'w') as x:
    x.write('xnId, cloudName, time')
    x.write('\n')
    with open('/Users/arajagopalan/Downloads/x_ace_history.json', 'r') as f:
        contents = json.load(f)
        for content in contents:
            # print(content)
            # print(content.get('xnId'), content.get('cloudDetails',{'cloudName': 'No cloudName'}).get('cloudName'))
            try:
                date = datetime.datetime.strptime(content.get('time'), "%m/%d/%Y, %H:%M:%S").strftime("%m/%d/%y")
            except TypeError:
                # print(f'invalid date: {content.get("time")}')
                continue
            except ValueError:
                date = (dateutil.parser.parse(content.get('time')).strftime("%m/%d/%y"))
            with open(xaceFile, 'a') as xfile:
                if content.get('cloudDetails', {'lastName': 'No name'}).get('lastName').title() not in ['Factory',
                                                                                                        'Muranjan',
                                                                                                        'Jenkins',
                                                                                                        'No Name',
                                                                                                        'Rajagopalan',
                                                                                                        'Raj']:
                    xfile.write("{},{},{},{},{},{}".format(content.get('xnId'),
                                                           content.get('cloudDetails',
                                                                       {'cloudName': content.get('cloudName')}).get(
                                                               'cloudName'),
                                                           content.get('cloudDetails', {'firstName': 'No Name'}).get(
                                                               'firstName').title(),
                                                           content.get('cloudDetails', {'lastName': 'No Name'}).get(
                                                               'lastName').title(),
                                                           content.get('partnerEmail'),
                                                           date))
                    xfile.write('\n')

