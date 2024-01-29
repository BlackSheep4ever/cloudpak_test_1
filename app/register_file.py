import json
import os

def update_form():
    filename = "config"

    if not os.path.splitext(filename)[1]:
        filename += ".json"
        print("\nArquivo vazio criado. Preencha seu dados.")

    with open(filename, "w") as new_file:
        
        data = {
            "server_name": input("\nInsira seu Nome: "),
            "server_ip": input("Insira seu IP: "),
            "server_password": input("Insira seu Password: ")
        }

        new_data = json.dump(data, new_file, indent=4)
        
        print("\n dados salvos com sucesso! \n")
        print(data)