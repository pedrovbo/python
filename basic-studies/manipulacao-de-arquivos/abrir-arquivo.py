import os

arquivo = open("teste.txt")  # caminho relativo
arquivo2 = open("/home/pedrovbo/PycharmProjects/python-projects/basic-studies/manipulacao-de-arquivos/teste.txt")
# caminho absoluto

print(os.path.relpath(arquivo.name))
print(os.path.abspath(arquivo.name))
print(arquivo)
print(arquivo.read())
print(arquivo2.read())
