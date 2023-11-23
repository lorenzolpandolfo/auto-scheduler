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
import escrever_horarios


if __name__ == "__main__":
    # Carrega todos eventos da agenda
    eventos = quickstart.main()
    
    # Pega apenas eventos no dia de hoje
    agendamentos = agenda.horarios_agendados(eventos)

    # Confere os dias disponíveis de acordo com os horários já reservados
    dias_disponiveis = schedules.horarios_disponiveis(agendamentos)

    # Escrever horários disponiveis
    escrever_horarios.escrever_horarios_disponiveis(dias_disponiveis, image.draw)

    # Gera o dia da semana em que o script está rodando
    dia = day.gerar_dia_da_semana()

    # Escreve o dia atual na imagem
    day.escrever_dia(image.draw, dia)
    
    # Cria a imagem nova
    image.gerar_imagem("new")

    input("\n[!] A imagem foi gerada. O nome do arquivo é 'new.png'" +
          "e está no diretório local do script.\n\n" +
          "> Aperte Enter para terminar o programa.")
