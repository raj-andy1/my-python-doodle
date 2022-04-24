# sample program to extract values from CSV file
import csv
import requests
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv

load_dotenv()


url = "https://hello.atlassian.net/rest/api/3/issue"

auth = HTTPBasicAuth(os.getenv('EMAIL'), os.getenv('API_KEY'))

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}


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


'''
def create_issue(httpurl, httpauth):
        response = requests.request(
            "POST",
            httpurl,
            data=payload,
            headers=headers,
            auth=httpauth
        )
        print(str(response.status_code) + ',' + line[1] + ' ' + line[2] + ',' + ' ' + json.loads(response.text)['key'])
'''


def main():
    fileName = '/Users/arajagopalan/PycharmProjects/my-python-doodle/manipulateJira/Controls Regrouping - Sheet3.csv'
    with open(fileName, 'r', encoding='utf-8') as csvfile:
        lines = csv.reader(csvfile)
        for line in lines:
            print(gen_payload(
                summary=line[1] + ' ' + line[2],
                desc=line[2],
                project='32582',
                reporter='5beb6f363b5b4b116a9ef4ff',
                issuetype='30841',
            ))


if __name__ == '__main__':
    main()
