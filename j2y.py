import json
import yaml

def import_json_data(file_path):
    with open(file_path, 'r') as data:
        json_file = json.load(data)
    return json_file
    

def convert_to_yaml(file_path, file_name):
    data = import_json_data(file_path)
    with open(file_name, 'w') as yaml_file:
        yaml.dump(data, yaml_file)
        

convert_to_yaml('/Users/nikki/Documents/Labs/Intros/PyJsonYaml/donuts.json', 'yaml_donuts')
convert_to_yaml('/Users/nikki/Documents/Labs/Intros/PyJsonYaml/emojis.json', 'yaml_emojis')
