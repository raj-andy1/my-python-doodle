# sample program to extract values from CSV file
# https://stackoverflow.com/questions/10588644/how-can-i-see-the-entire-http-request-thats-being-sent-by-my-python-application
import csv
import requests
from requests.auth import HTTPBasicAuth
from requests import Request, Session
import json
import os
from dotenv import load_dotenv
import re


def gen_payload(summary: str, desc: str, project: str, reporter: str, issuetype: str, labels: list = None):
    payload = json.dumps({
        "update": {

        },
        "fields": {
            "summary": summary,
            "project": {
                "id": project,
            },
            "description": desc,
            "reporter": {
                "id": reporter
            },
            "issuetype": {
                "id": issuetype
            },
            "labels": labels,
        }
    }
    )
    return payload


def http_request(httpurl, httpauth=None, method='POST', headers=None, payload=None, debug=False, **kwargs):
    if not headers:
        headers = ({
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
    if not httpauth:
        load_dotenv(dotenv_path='envvars.env')
        httpauth = HTTPBasicAuth(os.getenv('EMAIL'), os.getenv('API_KEY'))
    r = Session()
    req = Request(
            method=method,
            url=httpurl,
            data=payload,
            headers=headers,
            auth=httpauth,
            **kwargs
        )
    try:
        response = r.send(req.prepare())
        if debug:
            print(response.request.url)
            print(response.request.headers)
            print(response.request.body)
            print(response.status_code)
        if re.match(r'20[0-4]', str(response.status_code)):
            return json.dumps(json.loads(response.text), sort_keys=True, indent=4,
                              separators=(",", ": ")) if response.text else True
        else:
            print(f'Received code {response.status_code}')
            if response.text:
                print(f'Received text: {response.text}')
    except requests.exceptions.Timeout:
        print(f'Connection to {httpurl} timed out')
        return False
    except requests.exceptions.RequestException:
        print(f'Error connecting to {httpurl}')
        return False


def test_gen_payload(fileName):
    with open(fileName, 'r', encoding='utf-8') as csvfile:
        lines = csv.reader(csvfile)
        headers = next(lines)
        for line in lines:
            print(gen_payload(
                summary=(line[0] + ' ' + line[1]).upper(),
                desc=line[2],
                project='32731',
                reporter='5beb6f363b5b4b116a9ef4ff',
                issuetype='31127',
            ))


def test_create_issue(url, filename):
    load_dotenv()
    print(os.getenv('EMAIL'))
    http_request(httpurl=url,
                 payload=test_gen_payload(filename),
                 auth=HTTPBasicAuth(os.getenv('EMAIL'), os.getenv('API_KEY')))


def main():
    """
    print(test_gen_payload('Sheet 2-Table 1.csv'))

    print(test_create_issue("https://hello.atlassian.net/rest/api/3/issue",
                            '/Users/arajagopalan/PycharmProjects/my-python-doodle/manipulateJira'
                            '/Controls Regrouping - Sheet4.csv'))
    """
    with open('Sheet 2-Table 1.csv', 'r', encoding='utf-8') as csvfile:
        lines = csv.reader(csvfile)
        headers = next(lines)
        for line in lines:
            # creating a Jira issue
            result = http_request(httpurl='https://hello.atlassian.net/rest/api/2/issue',
                                  payload=gen_payload(
                                      summary=(line[0] + ' ' + line[1]).upper(),
                                      desc='New FedRAMP Rev-5 control',
                                      project='32731',
                                      reporter='5beb6f363b5b4b116a9ef4ff',
                                      issuetype='31127',
                                      labels=['FedRAMP-Moderate', 'rev5']
                                  ), debug=True)
            
            print(line[0] + ',' + result['key'])
            """
            # adding a label/updating a field(add epic) in an existing Jira Issue
            result = http_request(httpurl='https://hello.atlassian.net/rest/api/2/issue/' + line[3],
                                  method='PUT',
                                  payload=json.dumps({
                                      "update": {
                                          "labels": [
                                              {
                                                  "add": 'FedRAMP-Moderate',

                                              },
                                              {
                                                  "add": line[5] if line[5] else '',

                                              },
                                              {
                                                  "add": line[7] if line[7] else '',

                                              },
                                              {
                                                  "add": line[8] if line[8] else '',

                                              },

                                          ]
                                      },
                                      "fields": {
                                          "parent": {
                                              "key": line[4],
                                          }
                                      }}),
                                  httpauth=HTTPBasicAuth(os.getenv('EMAIL'), os.getenv('API_KEY'))
                                  )
            print(result)
"""


if __name__ == '__main__':
    main()
