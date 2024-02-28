import json
import jsonschema
import yaml


class JsonValidator:

    def __init__(self, schemafile, debug):
        self.schemafile = schemafile
        self.debug = debug

    def convert_yaml_to_json(self, yamlfile, jsonfile):
        with open(yamlfile, 'r') as stream:
            try:
                datamap = yaml.safe_load(stream)
                with open(jsonfile, 'w') as output:
                    json.dump(datamap, output, indent="")
                return True
            except yaml.YAMLError as exc:
                print(exc)
                return False

    def validate_json_file(self, jsonfile):
        with open(jsonfile, 'r') as file:
            inputjson = json.load(file)

        with open(self.schemafile, 'r') as schema:
            inputschema = json.load(schema)

        try:
            jsonschema.validate(inputjson, schema=inputschema)
            print('Validation successful')
        except jsonschema.exceptions.ValidationError as e:
            print(e)
            return False


JsonValidate = JsonValidator(schemafile='newJsonSchema.json', debug=True)
JsonValidate.convert_yaml_to_json('baseline.yaml', 'outputJsonfile.json')
JsonValidate.validate_json_file('outputJsonFile.json')

