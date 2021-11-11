print("Abrindo um arquivo")

try:
    open("teste.txt", 'r')
    print("Arquivo aberto!")
except FileNotFoundError as erro:
    print("Este arquivo não existe")
    print("Descrição ", erro)

print("Fim do Programa")