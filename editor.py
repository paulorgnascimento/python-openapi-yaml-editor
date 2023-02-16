import yaml

with open('openapi.yaml') as file:
    openapi_dict = yaml.safe_load(file)

if openapi_dict is not None:
    openapi_dict['paths']['/users']['get']['x-new-key'] = 'new-value'

    with open('openapi.yaml', 'w') as file:
        yaml.dump(openapi_dict, file)
else:
    print('O arquivo openapi.yaml está vazio ou contém um erro de sintaxe.')
