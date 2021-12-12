from PIL import Image

leitura = input('Digite a quantidade de arquivos para converter:')
quantidade = int(leitura)

#TODO: implementar conversão em massa por extensão de arquivo
for i in range(quantidade):
    caminhoOrigem = input('Digite o caminho de origem:')
    caminhoDestino = input('Digite o caminho de destino:')
    image1 = Image.open(fr'{caminhoOrigem}')
    im1 = image1.convert('RGB')
    im1.save(fr'{caminhoDestino}')


print("Fim do Programa")