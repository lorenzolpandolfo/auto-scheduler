"""
Usado para escrever os horários disponíveis na imagem nova.
"""

from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os


def carregar_diretorio_fonte(fonte):
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    
    # retorna o diretório da fonte
    print(os.path.join(diretorio_atual, fonte + ".ttf"))
    return os.path.join(diretorio_atual, fonte + ".ttf")


def escrever_horarios_disponiveis(horarios, draw):
    text_color = (0,0,0)
    fonte = ImageFont.truetype(carregar_diretorio_fonte("HKGrotesk"), size=75)
    text_y = 420
    text_x = 135

    for i, horario in enumerate(horarios):
        if i % 3 == 0:
            text_x = 135
            text_y += 175
        else:
            text_x += 300

        text_pos = (text_x, text_y)
        draw.text(text_pos, horario.strftime("%H:%M"), font=fonte, fill=text_color)
    return 0