import os

try:
    os.mkdir("meu_diretorio")
    print("Diretório criado!")

except PermissionError as erro:
    print("Sem permissão para criar diretório")
    print("Descrição do erro -> ", erro)
except FileExistsError as erro:
    print("Diretório já existe")
    print("Descrição do erro -> ", erro)