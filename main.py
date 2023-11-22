"""
Checar no Google Agenda horários disponíveis dentre um intervalo de tempo
Criar uma imagem .png organizada informando os horários disponíveis para agendamento.
A imagem será utilizada nas redes sociais do estabelecimento.
"""
import image
import day
import quickstart
import agenda

if __name__ == "__main__":
    eventos = quickstart.main()
    horarios_agendados = agenda.horarios_agendados(eventos)

    dia = day.gerar_dia_da_semana()
    day.escrever_dia(image.draw, dia)
    image.gerar_imagem("new")
