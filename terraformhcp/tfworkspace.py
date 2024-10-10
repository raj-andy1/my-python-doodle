import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
# Define the API endpoint
url = "https://app.terraform.io/api/v2/organizations/loomhq/workspaces"

auth_token = "Bearer " + os.getenv("HCP_TOKEN")

# Define the headers
headers = {
    "Authorization": auth_token,
    "Content-Type": "application/vnd.api+json"
}

params = {
    "search[wildcard-name]": "dns-*"
}

# Make the GET request
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Print the response in JSON format
    print(json.dumps(response.json(), indent=4))
else:
    print(f"Failed to retrieve workspaces. Status code: {response.status_code}")
    print(response.text)
