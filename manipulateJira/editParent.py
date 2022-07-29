import json
import os
import csv
from dotenv import load_dotenv
from fedrampIssue import http_request, gen_payload
from requests.auth import HTTPBasicAuth

url = 'https://hello.atlassian.net/rest/api/3/issue/'

"""
---to clear out epic---
"fields": {
                                          "parent": {
                                              "key": None
                                          },
                                      }
"""


def main():
    load_dotenv()
    print(os.getenv('EMAIL'))
    with open('/Users/arajagopalan/PycharmProjects/my-python-doodle/manipulateJira/Controls Regrouping - Sheet2.csv',
              'r', encoding='utf-8') as csvfile:
        lines = csv.reader(csvfile)
        for line in lines:
            result = http_request(httpurl=url + line[3],
                                  method='PUT',
                                  payload=json.dumps({
                                      "update": {},
                                      "fields": {
                                          "parent": {
                                              "key": line[4]
                                          },
                                      }
                                  }
                                  ),
                                  httpauth=HTTPBasicAuth(os.getenv('EMAIL'), os.getenv('API_KEY')))


if __name__ == '__main__':
    main()
