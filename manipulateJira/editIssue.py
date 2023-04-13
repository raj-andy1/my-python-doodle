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


def gen_desc_url(control):
    """

    """
    if '(' in control:
        control_url = 'http://fedramp.scalesec.com/enhancements/' + '-'.join(
            [control.split('(')[0].lower().strip(' '), control.split('(')[1].split(')')[0]]) \
                      + '.html'

    else:
        control_url = 'http://fedramp.scalesec.com/controls/' + control.lower() + '.html'

    return control_url


def main():
    load_dotenv(dotenv_path='envvars.env')
    print(os.getenv('EMAIL'))
    with open('FedRAMP controls and projects - Sheet2.csv',
              'r', encoding='utf-8') as csvfile:
        lines = csv.reader(csvfile)
        # lines = csvfile.readlines()
        for line in lines:
            # item = line.rstrip("\n")
            #  print(line[0])
            #  print(gen_desc_url(line[0].split(',')[0]))
            result = http_request(httpurl=url + line[2],
                                  method='PUT',
                                  payload=json.dumps({
                                      "fields": {
                                          "description": {
                                              "type": "doc",
                                              "version": 1,
                                              "content": [
                                                  {
                                                      "type": "paragraph",
                                                      "content": [
                                                          {
                                                              "text": "For more information on this control, refer to: ",
                                                              "type": "text"
                                                          },
                                                          {
                                                              "type": "text",
                                                              "text": gen_desc_url(line[0].split(',')[0]),
                                                              "marks": [{
                                                                  "type": "link",
                                                                  "attrs": {
                                                                      "href": gen_desc_url(line[0].split(',')[0])
                                                                  }
                                                              }]
                                                          }
                                                      ]
                                                  }
                                              ]
                                          },
                                      },
                                  }
                                  ),
                                  httpauth=HTTPBasicAuth(os.getenv('EMAIL'), os.getenv('API_KEY')))
            print(result)


if __name__ == '__main__':
    main()
