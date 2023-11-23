"""
Checar no Google Agenda horários disponíveis dentre um intervalo de tempo
Criar uma imagem .png organizada informando os horários disponíveis para agendamento.
A imagem será utilizada nas redes sociais do estabelecimento.
"""
import tkinter as tk
from tkinter import messagebox
import image
import day
import quickstart
import agenda
import schedules
import escrever_horarios


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto scheduler")
        self.init_ui()

        self.btn_criar_imagem = tk.Button(root, text="Criar imagem", command=self.criar_imagem())
        

    def init_ui(self):
        self.label = tk.Label(self.root, text="Olá, Mundo!")
        self.label.pack()
    
    
    def criar_imagem(self):
        try:
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

        except Exception as e:
            messagebox.showerror("Erro", f"Um erro aconteceu: {str(e)}")
            



if __name__ == "__main__":
    # criando a janela principal
    root = tk.Tk()
    # mandando a janela principal pro MainApp
    app = MainApp(root)
    # iniciando o loop
    root.mainloop()
"""    
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
          "> Aperte Enter para terminar o programa.")"""
