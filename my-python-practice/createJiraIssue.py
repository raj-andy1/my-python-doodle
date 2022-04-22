# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://hello.atlassian.net/rest/api/3/issue"

auth = HTTPBasicAuth("arajagopalan@atlassian.com", "DmOh5p7wbdWT0ovHOWYMDE4A")

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

payload = json.dumps({
    "update": {},
    "fields": {
        "summary": "Automated Test Issue",
        "project": {
            "id": "32582",
        },
        "description": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "text": "test test.",
                            "type": "text"
                        }
                    ]
                }
            ]
        },
        "reporter": {
            "id": "5beb6f363b5b4b116a9ef4ff"
        },
        "issuetype": {
            "id": "30841"
        },
        "parent": {
            "fields": {
                "issuetype": {
                    "avatarId": 16627,
                    "description": "Epics track collections of related bugs, stories, and tasks.",
                    "entityId": "3d79d676-ec31-4c62-ac2d-5e018541a917",
                    "hierarchyLevel": 1,
                    "iconUrl": "https://hello.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/16627?size=medium",
                    "id": "30792",
                    "name": "Epic",
                    "self": "https://hello.atlassian.net/rest/api/3/issuetype/30792",
                    "subtask": False
                },
                "priority": {
                    "iconUrl": "https://hello.atlassian.net/images/icons/priorities/major.svg",
                    "id": "3",
                    "name": "Major",
                    "self": "https://hello.atlassian.net/rest/api/3/priority/3"
                },
                "status": {
                    "description": "",
                    "iconUrl": "https://hello.atlassian.net/",
                    "id": "34687",
                    "name": "To Do",
                    "self": "https://hello.atlassian.net/rest/api/3/status/34687",
                    "statusCategory": {
                        "colorName": "blue-gray",
                        "id": 2,
                        "key": "new",
                        "name": "To Do",
                        "self": "https://hello.atlassian.net/rest/api/3/statuscategory/2"
                    }
                },
                "summary": "FedRAMP Configuration Management"
            },
            "id": "2835582",
            "key": "FRCP-6",
            "self": "https://hello.atlassian.net/rest/api/3/issue/2835582"
        },
        "assignee": {
            "id": "5beb6f363b5b4b116a9ef4ff"
        }
    }
})

response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
