from fedrampIssue import http_request
import json

domain = 'http://fedramp.scalesec.com/'
with open('FedRAMP controls and projects - Sheet2.csv', 'r', encoding='utf-8') as csvfile:
    lines = csvfile.readlines()
    for line in lines:
        item = line.rstrip("\n")
        # print(item)
        columns = item.split(',')
        if '(' in columns[0]:
            url = domain + 'enhancements/' + '-'.join(
                [columns[0].split('(')[0].lower().strip(' '), columns[0].split('(')[1].split(')')[0]]) \
                  + '.html'

        else:
            url = domain + 'controls/' + columns[0].lower() + '.html'
        print(url)
