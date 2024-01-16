import yaml

with open('meta.yaml','r') as file:
    yaml_data = yaml.safe_load(file)

print(yaml_data)
