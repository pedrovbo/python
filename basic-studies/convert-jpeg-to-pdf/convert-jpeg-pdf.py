from PIL import Image

image1 = Image.open(r'caminho-para-o-arquivo-origem')
im1 = image1.convert('RGB')
im1.save(r'caminho-para-o-arquivo-destino')