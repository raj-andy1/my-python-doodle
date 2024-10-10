import json

with open("workspaces.json", "r") as file:
    workspaces = json.load(file)

# for key in workspaces['data'][0]["attributes"].keys():
#     print(key)

for workspace in workspaces['data']:
    #print(workspace["attributes"]["name"])
    print("\"https://app.terraform.io/api/v2/organizations/loomhq/workspaces/" + workspace["attributes"]["name"]+"\"," )