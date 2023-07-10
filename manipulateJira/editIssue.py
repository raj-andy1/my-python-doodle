import json
import csv
from fedrampIssue import http_request

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
    with open('Sheet 3-Table 1.csv',
              'r', encoding='utf-8') as csvfile:
        lines = csv.reader(csvfile)
        headers = next(lines)
        # lines = csvfile.readlines()
        for line in lines:
            if not line[1]:
                print(line[4] + ' Not in Rev5')
                result = http_request(httpurl=url + line[6],
                                      method='PUT',
                                      payload=json.dumps({
                                          "update": {
                                              "labels": [
                                                  {
                                                      "add": 'not-in-rev5'

                                                  }]
                                          }}),
                                      debug=True)
            else:
                result = http_request(httpurl=url + line[6],
                                      method='PUT',
                                      payload=json.dumps({
                                          "update": {
                                              "labels": [
                                                  {
                                                      "add": 'rev5'

                                                  }]
                                          },
                                          "fields": {
                                              "description": {
                                                  "type": "doc",
                                                  "version": 1,
                                                  "content": [
                                                      {
                                                          "type": "paragraph",
                                                          "content": [
                                                              {
                                                                  "text": line[3],
                                                                  "type": "text"
                                                              }
                                                          ]
                                                      }
                                                  ]
                                              },
                                          },
                                      }
                                      ),
                                      debug=True)


if __name__ == '__main__':
    main()
