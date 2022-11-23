from requests.auth import HTTPBasicAuth
from fedrampIssue import http_request
from dotenv import load_dotenv
import os

url = "https://hello.atlassian.net/rest/api/3/issue/MANTA-196"
load_dotenv(dotenv_path='envvars.env')
response = http_request(
   method="GET",
   httpurl=url,
   httpauth=HTTPBasicAuth(os.getenv('EMAIL'), os.getenv('API_KEY'))
)
print(response)
