import json
import re
import datetime

aaceFile = 'aace_history.csv'
paceFile = 'pace_history.csv'
xaceFile = 'xace_history.csv'
with open('/Users/arajagopalan/Downloads/x_ace_history.json', 'r') as f:
    contents = json.load(f)
with open(paceFile, 'w') as p:
    p.write('xnId, cloudName, time')
    p.write('\n')
with open(aaceFile, 'w') as a:
    a.write('xnId, cloudName, time')
    a.write('\n')
with open(xaceFile, 'w') as x:
    x.write('xnId, cloudName, time')
    x.write('\n')

    for content in contents:
        # print(content.keys())
        print(content.get('xnId'))
        '''
        date = content.get('time')
        print(date)
        try:
            print(datetime.datetime.strptime(date, "%m/%d/%Y, %H:%M:%S").strftime("%m/%d/%y"))
        except TypeError:
            print(f'invalid date: {date}')
            continue
        except ValueError:
            print(dateutil.parser.parse(date).strftime("%m/%d/%y"))
            continue
        '''
        if re.match(r'^PACE-\d*$', content.get('xnId', 'TEST')):
            with open(paceFile, 'a') as pfile:
                if content.get('cloudDetails', {'lastName': 'No name'}).get('lastName').title() not in ['Factory',
                                                                                                        'Muranjan',
                                                                                                        'Jenkins',
                                                                                                        'No name',
                                                                                                        'Rajagopalan']:
                    pfile.write("{},{},{},{},{},{}".format(content.get('xnId'),
                                                           content.get('cloudDetails',
                                                                       {'cloudName': content.get('cloudName')}).get(
                                                               'cloudName'),
                                                           content.get('cloudDetails', {'firstName': 'No Name'}).get(
                                                               'firstName').title(),
                                                           content.get('cloudDetails', {'lastName': 'No Name'}).get(
                                                               'lastName').title(),
                                                           content.get('partnerEmail'),
                                                           content.get('time')))
                pfile.write('\n')
        elif re.match(r'^DEMO-\d*$', content.get('xnId', 'TEST')):
            with open(aaceFile, 'a') as afile:
                if content.get('cloudDetails', {'lastName': 'No name'}).get('lastName').title() not in ['Factory',
                                                                                                        'Muranjan',
                                                                                                        'Jenkins',
                                                                                                        'Rajagopalan']:
                    afile.write("{},{},{},{},{},{}".format(content.get('xnId'),
                                                           content.get('cloudDetails',
                                                                       {'cloudName': content.get('cloudName')}).get(
                                                               'cloudName'),
                                                           content.get('cloudDetails', {'firstName': 'No Name'}).get(
                                                               'firstName').title(),
                                                           content.get('cloudDetails', {'lastName': 'No Name'}).get(
                                                               'lastName').title(),
                                                           content.get('partnerEmail'),
                                                           content.get('time')))
                    afile.write('\n')
        elif content.get('partnerEmail') in ['university-demo-bot@atlassian.com']:
            with open(xaceFile, 'a') as xfile:
                xfile.write("{},{},{},{},{},{}".format('UNI',
                                                       content.get('cloudDetails',
                                                                   {'cloudName': content.get('cloudName')}).get(
                                                           'cloudName'),
                                                       content.get('cloudDetails', {'firstName': 'No Name'}).get(
                                                           'firstName').title(),
                                                       content.get('cloudDetails', {'lastName': 'No Name'}).get(
                                                           'lastName').title(),
                                                       content.get('partnerEmail'),
                                                       content.get('time')))
                xfile.write('\n')