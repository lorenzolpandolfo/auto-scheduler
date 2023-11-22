
# gerar o dia da semana atual em portugues
#

from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import escrever_horarios

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
    text_color = (151, 195, 102)

    text_lenght = draw.textlength(dia)
    text_pos = (440 - (text_lenght*2),400)

    fonte = ImageFont.truetype(escrever_horarios.carregar_diretorio_fonte("Antonio-Bold"), size=100)

    draw.text(text_pos, dia.upper(), font=fonte, fill=text_color)
