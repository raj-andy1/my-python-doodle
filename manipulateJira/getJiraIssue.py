from fedrampIssue import http_request

url = "https://hello.atlassian.net/rest/api/3/issue/MANTA-15"
#url = "https://hello.atlassian.net/rest/api/3/search"

query = {
    "jql": "project = 'FRCONTROL' AND issuetype = 'Capability Documentation'"
}
"""
query = {
    "jql": "project = 'MANTA' AND issuetype = 'Capability Adoption'"
}
"""

response = http_request(
    method="GET",
    httpurl=url,
    debug=True
)
print(response)


'''
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


with open('fr-tasks.csv', 'w') as file:
    file.write("{},{},{},{},{},{}".format('Documentation Task', 'Document Task Desc', 'Document Task Status',
                                          'Parent Task', 'Parent Task Desc', 'Parent Task Status'))
    for issue in response['issues']:
        for subtask in issue['fields']['subtasks']:
            file.write('\n')
            file.write("{},{},{},{},{},{}".format(subtask['key'], subtask['fields']['summary'],
                                                  subtask['fields']['status']['name'],
                                                  issue['key'], issue['fields']['summary'],
                                                  issue['fields']['status']['name']))
print(f"Total Tasks {response['total']}")
'''

