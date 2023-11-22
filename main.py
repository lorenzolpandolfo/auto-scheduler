"""
Checar no Google Agenda horários disponíveis dentre um intervalo de tempo
Criar uma imagem .png organizada informando os horários disponíveis para agendamento.
A imagem será utilizada nas redes sociais do estabelecimento.
"""
from PIL import Image, ImageDraw, ImageFont
import image
import day

if __name__ == "__main__":
    dia = day.gerar_dia_da_semana()
    day.escrever_dia(image.draw, dia)
    image.gerar_imagem("new")
