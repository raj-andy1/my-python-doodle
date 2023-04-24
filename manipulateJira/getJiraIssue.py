from requests.auth import HTTPBasicAuth
from fedrampIssue import http_request
from dotenv import load_dotenv
import os

# url = "https://hello.atlassian.net/rest/api/3/issue/MANTA-365"
url = "https://hello.atlassian.net/rest/api/3/search"
load_dotenv(dotenv_path='envvars.env')

query = {
    "jql": "project = 'MANTA' AND issuetype = 'Capability Documentation'"
}
"""
query = {
    "jql": "project = 'MANTA' AND issuetype = 'Capability Adoption'"
}
"""

response = http_request(
    method="GET",
    httpurl=url,
    httpauth=HTTPBasicAuth(os.getenv('EMAIL'), os.getenv('API_KEY')),
    params=query,
)

print(f"Total Tasks {response['total']}")
for issue in response['issues']:
    # print(issue['key'], issue['fields']['summary'])
    print(f"Sub Tasks for {issue['key']} - {issue['fields']['summary']} - Status: {issue['fields']['status']['name']} ")
    for subtask in issue['fields']['subtasks']:
        print(f"{subtask['key']} - {subtask['fields']['summary']} - Status: "
              f"{subtask['fields']['status']['name']}")
    print(f"Total SubTasks: {len(issue['fields']['subtasks'])}")
