"""
Checar no Google Agenda horários disponíveis dentre um intervalo de tempo
Criar uma imagem .png organizada informando os horários disponíveis para agendamento.
A imagem será utilizada nas redes sociais do estabelecimento.
"""
from PIL import Image, ImageDraw, ImageFont
import image
import day
import quickstart

if __name__ == "__main__":
    eventos = quickstart.main()
    for event in eventos:
        start = event["start"].get("dateTime", event["start"].get("date"))
        print(start, event["summary"])

    dia = day.gerar_dia_da_semana()
    day.escrever_dia(image.draw, dia)
    image.gerar_imagem("new")
