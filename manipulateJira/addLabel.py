from fedrampIssue import http_request
import json

with open('Controls for Rev4_Rev5 FR Mod_FR Low - Sheet2.csv', 'r', encoding='utf-8') as csvfile:
    lines = csvfile.readlines()
    for line in lines:
        item = line.rstrip("\n")
        # print(item)
        columns = item.split(',')
        result = http_request(httpurl='https://hello.atlassian.net/rest/api/2/issue/' + columns[5],
                              method='PUT',
                              payload=json.dumps({
                                  "update": {
                                      "labels": [
                                          {
                                              "add": 'rev-4',

                                          },
                                          {
                                              "add": columns[7] if columns[7] else '',

                                          },
                                      ]
                                  }, })
                              )
        print(result)
