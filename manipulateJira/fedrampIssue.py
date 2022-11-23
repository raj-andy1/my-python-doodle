# sample program to extract values from CSV file
# https://stackoverflow.com/questions/10588644/how-can-i-see-the-entire-http-request-thats-being-sent-by-my-python-application
import csv
import requests
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv
import re


def gen_payload(summary: str, desc: str, project: str, reporter: str, issuetype: str, ):
    payload = json.dumps({
        "update": {},
        "fields": {
            "summary": summary,
            "project": {
                "id": project,
            },
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "text": desc,
                                "type": "text"
                            }
                        ]
                    }
                ]
            },
            "reporter": {
                "id": reporter
            },
            "issuetype": {
                "id": issuetype
            },
        }
    }
    )
    return payload


def http_request(httpurl, httpauth=None, method='POST', headers=None, payload=None, **kwargs):
    if not headers:
        headers = ({
            "Accept": "application/json",
            "Content-Type": "application/json"
        })
    if not httpauth:
        load_dotenv(dotenv_path='envvars.env')
        httpauth = HTTPBasicAuth(os.getenv('EMAIL'), os.getenv('API_KEY'))
    try:
        response = requests.request(
            method=method,
            url=httpurl,
            data=payload,
            headers=headers,
            auth=httpauth
        )
        print(response.request.url)
        print(response.request.headers)
        print(response.request.body)
        if re.match(r'20[0-4]', str(response.status_code)):
            return json.loads(response.text) if response.text else True
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
        for line in lines:
            return (gen_payload(
                summary=line[1] + ' ' + line[2],
                desc=line[2],
                project='32582',
                reporter='5beb6f363b5b4b116a9ef4ff',
                issuetype='30841',
            ))


def test_create_issue(url, filename):
    load_dotenv()
    print(os.getenv('EMAIL'))
    http_request(httpurl=url,
                 payload=test_gen_payload(filename),
                 auth=HTTPBasicAuth(os.getenv('EMAIL'), os.getenv('API_KEY')))


def main():
    """
    print(test_gen_payload(
        '/Users/arajagopalan/PycharmProjects/my-python-doodle/manipulateJira/Controls Regrouping - Sheet4.csv'))
    print(test_create_issue("https://hello.atlassian.net/rest/api/3/issue",
                            '/Users/arajagopalan/PycharmProjects/my-python-doodle/manipulateJira'
                            '/Controls Regrouping - Sheet4.csv'))
    """
    filename = '/Users/arajagopalan/PycharmProjects/my-python-doodle/manipulateJira/Controls Regrouping - Sheet2.csv'
    load_dotenv()
    with open(filename, 'r', encoding='utf-8') as csvfile:
        lines = csv.reader(csvfile)
        for line in lines:
            """
            url = 'https://hello.atlassian.net/rest/api/2/issue'
            # creating a Jira issue
            result = http_request(httpurl=url,
                                  auth=HTTPBasicAuth(os.getenv('EMAIL'), os.getenv('API_KEY')),
                                  payload=gen_payload(
                                      summary=line[1] + ' ' + line[2],
                                      desc=line[2],
                                      project='32582',
                                      reporter='5beb6f363b5b4b116a9ef4ff',
                                      issuetype='30841',
                                      headers = {
                                        "Accept": "application/json",
                                        "Content-Type": "application/json"
                                    }
                                  ))
            print(line[1] + ',' + result['key'])
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


if __name__ == '__main__':
    main()
