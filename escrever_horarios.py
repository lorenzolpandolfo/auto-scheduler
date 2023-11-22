"""
Usado para escrever os horários disponíveis na imagem nova.
"""

from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

def escrever_horarios_disponiveis(horarios, draw):
    text_color = (0,0,0)
    fonte = ImageFont.load_default(size=75)
    text_y = 420
    text_x = 120
    
    for i, horario in enumerate(horarios):
        if i % 3 == 0:
            text_x = 120
            text_y += 175
        else:
            text_x += 300

        text_pos = (text_x, text_y)
        draw.text(text_pos, str(horario), font=fonte, fill=text_color)

    return 0