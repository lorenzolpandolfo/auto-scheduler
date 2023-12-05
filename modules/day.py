from PIL import ImageFont
from datetime import datetime, timezone
from modules import fonts


def gerar_dia_da_semana(mes, dia):
    """
    Carregar o dia da semana atual em português
    """
    agora = datetime.now()
    fuso_horario = timezone.utc

    data = datetime(agora.year, mes, dia, tzinfo=fuso_horario)
    dia = data.strftime("%A").lower()

    all_days = {
        "monday":       "segunda",
        "tuesday":      "terça",
        "wednesday":    "quarta",
        "thursday":     "quinta",
        "friday":       "sexta",
        "saturday":    "sábado",
        "sunday":       "domingo"
    }

    if dia in all_days:
        dia = all_days[dia]
    
    return dia


def escrever_dia(draw, dia):
    text_color = (151, 195, 102)

    text_lenght = draw.textlength(dia)
    text_pos = (440 - (text_lenght*2),400)

    fonte = ImageFont.truetype(fonts.carregar_diretorio_fonte("Antonio-Bold"), size=100)

    draw.text(text_pos, dia.upper(), font=fonte, fill=text_color)

def dia_atual():
    return datetime.now().day

def mes_atual():
    return datetime.now().month

