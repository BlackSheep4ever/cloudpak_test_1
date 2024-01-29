import json

def view_form():
    try:
        with open('config.json') as data_file:
            data = json.load(data_file)
            
            print("\nInformações no arquivo.\n")
            print(data)
    except:
        print("\nEste arquivo não contém informações.\nCrie um novo registro e preencha os dados.\n")
        pass 