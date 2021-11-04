import os

# Para o arquivo dados1.txt
arquivo1 = open("dados1.txt")  # Caminho relativo
arquivo2 = open("/basic-studies/scripts-curso/dados1.txt")  # Caminho absoluto

# Para o arquivo dados2.txt
arquivo3 = open("documentos/dados2.txt")  # Caminho relativo
arquivo4 = open("/basic-studies/scripts-curso/documentos/dados2.txt")  # Caminho absoluto

print(os.path.relpath(arquivo1.name))
print(os.path.abspath(arquivo1.name))

print(os.path.relpath(arquivo2.name))
print(os.path.abspath(arquivo2.name))

print(os.path.relpath(arquivo3.name))
print(os.path.abspath(arquivo3.name))

print(os.path.relpath(arquivo4.name))
print(os.path.abspath(arquivo4.name))

print(arquivo1.read())
print(arquivo2.read())
print(arquivo3.read())
print(arquivo4.read())
