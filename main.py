"""
Checar no Google Agenda horários disponíveis dentre um intervalo de tempo
Criar uma imagem .png organizada informando os horários disponíveis para agendamento.
A imagem será utilizada nas redes sociais do estabelecimento.
"""
import image
import day
import quickstart
import agenda
import schedules

if __name__ == "__main__":
    eventos = quickstart.main()
    agendamentos = agenda.horarios_agendados(eventos)
    final = schedules.horarios_disponiveis(agendamentos)
    print(final)

    dia = day.gerar_dia_da_semana()
    day.escrever_dia(image.draw, dia)
    image.gerar_imagem("new")
