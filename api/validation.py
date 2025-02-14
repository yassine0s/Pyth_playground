from openapi_spec_validator import validate_spec

import yaml

def validate_openapi_spec(file_path):
    with open(file_path,"r") as file:
        spec = yaml.safe_load(file)
        validate_spec(spec)
        print("api is validated")
