import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://hello.atlassian.net/rest/api/3/issue/FRCP-4"

auth = HTTPBasicAuth("arajagopalan@atlassian.com", "DmOh5p7wbdWT0ovHOWYMDE4A")

headers = {
   "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))