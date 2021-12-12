import glob
from PIL import Image
import os
from fnmatch import fnmatch

origem = input('Digite o caminho da pasta contendo os arquivos para serem convertidos: ')
destino = input('Digite o caminho da pasta onde serão salvos os arquivos convertidos:')
extensao = ".pdf"
file_list = [file for file in os.listdir(origem) if fnmatch(file, '*.jpeg')]
contador = int(0)

for i in file_list:
    arquivoConverter = origem + i
    image1 = Image.open(fr'{arquivoConverter}')
    arquivoDestino = destino + "jpegConvertido" + contador.__str__() + extensao
    im1 = image1.convert('RGB')
    im1.save(fr'{arquivoDestino}')
    contador = contador + 1

print("Fim do Programa")