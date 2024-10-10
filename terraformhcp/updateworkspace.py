import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
auth_token = "Bearer " + os.getenv("HCP_TOKEN")
headers = {
    "Authorization": auth_token,
    "Content-Type": "application/vnd.api+json"
}

urls = ["https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loom-codes"]

# urls = [
#         "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loom-com",
#         "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-useloom-dev",
#         "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loom-test-com",
#         "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loom-net",
#         "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loom-org",
#         "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loom-tools",
#         "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loominternaltest2-com",
#         "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loomstatus-com",
#         "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-useloom-com",
#         "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loom-email",
#         "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loompreview-com",
#         "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loomlocal-com",
#         "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loom-dev",
#         "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loom-new",
#         "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-opentest-co",
#         "https://app.terraform.io/api/v2/organizations/loomhq/workspaces/dns-loomsdk-com"]
for url in urls:
    payload = {
        "data": {
            "attributes": {
                "working-directory": "terraform/dns/" + url.split('/')[-1].replace('dns-', '').replace('-', '.'),
                "vcs-repo": {
                    "identifier": "loomhq/infra-terraform",
                    "display-identifier": "loomhq/infra-terraform",
                    "oauth-token-id": "ot-PMPjC3ismG6c5q5E",
                    "repository-http-url": "https://github.com/loomhq/infra-terraform",
                    "service-provider": "github"
                },
                "vcs-repo-identifier": "loomhq/infra-terraform",
                "oauth-client-name": "github",
                }
            },
        }

    response = requests.patch(url=url,
                              headers=headers,
                              json=payload)

    if response.status_code == 200:
        # Print the response in JSON format
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"Failed to retrieve workspaces. Status code: {response.status_code}")
        print(response.text)