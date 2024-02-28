import yaml
import json
from jsonschema import validate


def validate_yaml_against_schema(yaml_file, schema):
    with open(yaml_file, 'r') as f:
        yaml_data = yaml.safe_load(f)
        print(yaml.dump(yaml_data, default_flow_style=False))




'''

    validator = jsonschema.Draft7Validator(schema_data)
    errors = list(validator.iter_errors(yaml_data))

    if errors:
        print("Validation Failed:")
        for error in errors:
            print(error)

    else:
        print("Validation Successful")
        
'''


# Provide the paths to your YAML file and JSON schema
yaml_file_path = 'jsonValidation/baseline.yaml'
json_schema_path = 'jsonValidation/jsonschema.json'

validate_yaml_against_schema(yaml_file_path, json_schema_path)
