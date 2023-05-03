from fedrampIssue import http_request
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
import json
import os
import csv


def main():
    """

    """
    load_dotenv(dotenv_path='envvars.env')
    with open('Controls for Rev4_Rev5 FR Mod_FR Low - Copy of Sheet2.csv', 'r', encoding='utf-8') as csvfile:
        lines = csv.reader(csvfile)
        headers = next(lines)
        for line in lines:
            # removing a label  in an existing Jira Issue
            result = http_request(httpurl='https://hello.atlassian.net/rest/api/3/issue/' + line[2],
                                  method='PUT',
                                  payload=json.dumps({
                                      "update": {
                                          "labels": [
                                              {
                                                  "remove": line[3]

                                              },

                                          ]
                                      },
                                  }),
                                  httpauth=HTTPBasicAuth(os.getenv('EMAIL'), os.getenv('API_KEY'))
                                  )
            print(result)


if __name__ == '__main__':
    main()
