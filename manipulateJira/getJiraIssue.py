import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://hello.atlassian.net/rest/api/3/issue/FRCP-71"

auth = HTTPBasicAuth(os.getenv('EMAIL'), os.getenv('API_KEY'))

headers = {
   "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)
print(response.status_code)
print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
