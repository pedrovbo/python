import os

try:
    os.rmdir("meu_diretorio")
    print("Arquivo removido")

except PermissionError as erro:
    print("Sem permissão para remover diretório")
    print("Descrição do erro -> ", erro)
except FileNotFoundError as erro:
    print("Diretório inexistente")
    print("Descrição do erro -> ", erro)
except OSError as erro:
    print("Outro erro.")
    print("O diretório está vazio?")
    print("Descrição do erro -> ", erro)
