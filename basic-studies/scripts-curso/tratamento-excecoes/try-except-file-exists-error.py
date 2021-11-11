import os

try:
    os.rename("teste_alfa.txt", "teste_beta.txt")
    print("Arquivo renomeado")
except FileNotFoundError as erro:
    print("Arquivo inexistente")
    print("Descrição do erro -> ", erro)
except PermissionError as erro:
    print("Sem permissão para acessar o arquivo")
    print("Descrição do erro -> ", erro)
except FileExistsError as erro:
    print("Arquivo destino já existe")
    print("Descrição do erro -> ", erro)