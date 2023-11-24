from PIL import Image, ImageDraw


def gerar_imagem(title):
    image.save(title + ".png")


def resetar_imagem():
    global image
    global draw

    image = root_image.copy()
    draw = ImageDraw.Draw(image)

root_image = Image.open("imagem.png")

image = root_image.copy()
draw = ImageDraw.Draw(image)
