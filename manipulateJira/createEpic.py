import json
import os
from dotenv import load_dotenv
from fedrampIssue import http_request, gen_payload
from requests.auth import HTTPBasicAuth

epicL = ['PRGB', 'Vulnerability Mgmt. - SAST-DAST', 'Contingency Planning', 'Audit-Trails-Other',
         'Vulnerability Mgmt. - Malicious Code', 'Inventory and Reporting - ConMon', 'Configuration Mgmt. - EcoSystem',
         'Native Characteristics', 'Documentation', 'Risk and Compliance'
         ]
url = 'https://hello.atlassian.net/rest/api/2/issue'


def main():
    load_dotenv()
    print(os.getenv('EMAIL'))
    for epicName in epicL:
        result = http_request(httpurl=url,
                              payload=json.dumps({
                                  "update": {},
                                  "fields": {
                                      "summary": epicName,
                                      "project": {
                                          "id": "32582",
                                      },
                                      "description": "Epic matches bubbles in the MantaRays execution plan",
                                      "reporter": {
                                          "id": "5beb6f363b5b4b116a9ef4ff"
                                      },
                                      "issuetype": {
                                          "id": "30792"
                                      },
                                  }
                              }
                              ),
                              httpauth=HTTPBasicAuth(os.getenv('EMAIL'), os.getenv('API_KEY')))


if __name__ == '__main__':
    main()
