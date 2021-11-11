print("Abrindo um arquivo")

try:
    open("teste.pdf", 'w')

    print("Arquivo aberto!")
except FileNotFoundError as erro:
    print("Arquivo inexistente")
    print("Descrição do problema ->", erro)
except PermissionError as erro:
    print("Sem permissão para acessar o arquivo")
    print("Descrição do problema ->", erro)

print("Fim do Programa")