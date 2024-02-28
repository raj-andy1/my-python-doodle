import yaml
import json

with open('baseline.yaml', 'r') as f:
    data = yaml.safe_load(f)

index = next((i for i, d in enumerate(data["baselines"]) if "rules" in d), None)

# Extract rules and create a new dictionary with "rules" key
rules_dict = {"rules": data["baselines"][index].pop("rules")}

# Update the original data with the new dictionary
data["baselines"].append(rules_dict)

# Convert to JSON
json_data = json.dumps(data, indent=2)

print(json_data)


