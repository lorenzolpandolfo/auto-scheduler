
# gerar o dia da semana atual em portugues
#

from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

def gerar_dia_da_semana():
    data = datetime.now()
    dia = data.strftime("%A").lower()

    all_days = {
        "monday":       "segunda",
        "tuesday":      "terça",
        "wednesday":    "quarta",
        "thursday":     "quinta",
        "friday":       "sexta"  
    }

    if dia in all_days:
        dia = all_days[dia]
    
    return dia


def escrever_dia(draw, dia):
    text_color = (0,0,0)

    text_lenght = draw.textlength(dia)
    text_pos = (440 - (text_lenght*2),400)

    fonte = ImageFont.load_default(size=75)

    draw.text(text_pos, dia, font=fonte, fill=text_color)
