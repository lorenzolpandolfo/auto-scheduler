"""
Usado para escrever os horários disponíveis na imagem nova.
"""

from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

def escrever_horarios_disponiveis(horarios, draw):
    text_color = (0,0,0)
    fonte = ImageFont.load_default(size=75)
    text_x = 0
    text_y = 100
    
    for horario, i in enumerate(horarios):
        # escrever na imagem o horario
        # print(i, horario)
        
        if horario % 3 == 0:
            text_y += 200
            text_x = 0
        
        text_y += 200
        

        text_pos = (text_x, text_y)
        draw.text(text_pos, str(i), font=fonte, fill=text_color)
