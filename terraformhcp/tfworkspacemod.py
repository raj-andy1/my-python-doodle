import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
auth_token = "Bearer " + os.getenv("HCP_TOKEN")

urls = ["https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loom-co",
        "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loom-app",
        "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loom-af",
        "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loom-com",
        "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-useloom-dev",
        "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loom-test-com",
        "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loom-net",
        "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loom-org",
        "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loom-tools",
        "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loominternaltest2-com",
        "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loomstatus-com",
        "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-useloom-com",
        "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loom-email",
        "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loompreview-com",
        "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loomlocal-com",
        "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loom-dev",
        "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loom-new",
        "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-opentest-co",
        "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loomsdk-com",]

url = "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loominternaltest2-com"

headers = {
    "Authorization": auth_token,
    "Content-Type": "application/vnd.api+json"
}

response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Print the response in JSON format
    print(json.dumps(response.json(), indent=4))
else:
    print(f"Failed to retrieve workspaces. Status code: {response.status_code}")
    print(response.text)