import json
import yaml

def import_yaml_data(file_path):
    with open(file_path, 'r') as data:
        yaml_file = yaml.load(data)
    return yaml_file
    

def convert_to_json(file_path, file_name):
    data = import_yaml_data(file_path)
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file)
        

convert_to_json('/Users/nikki/Documents/Labs/Intros/PyJsonYaml/verify.yaml', 'json_verify')
convert_to_json('/Users/nikki/Documents/Labs/Intros/PyJsonYaml/xmas.yaml', 'json_xmas')
