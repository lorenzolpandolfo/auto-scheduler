from PIL import Image, ImageDraw, ImageFont

image = Image.open("imagem.png")
draw = ImageDraw.Draw(image)

def gerar_imagem(title):
    image.save(title + ".png")
