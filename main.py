"""
Checar no Google Agenda horários disponíveis dentre um intervalo de tempo
Criar uma imagem .png organizada informando os horários disponíveis para agendamento.
A imagem será utilizada nas redes sociais do estabelecimento.
"""
import tkinter as tk
from tkinter import messagebox
import subprocess
import os

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


    def init_ui(self):
        root.geometry("500x400")
        root.resizable(width=False, height=False)

        self.output_area = tk.Text(root, height=10, width=60)
        self.output_area.pack(pady=20)
        # self.output_area.config(state=tk.DISABLED)
        
        self.btn_criar_imagem = tk.Button(root, text="Criar imagem", command=self.criar_imagem)
        self.btn_criar_imagem.pack()
    
    
    def criar_imagem(self):
        self.output_area.insert(tk.END, "Iniciando Auto Scheduler...\n")
        self.root.update()
        try:
            # Carrega todos eventos da agenda
            eventos = quickstart.main(tk, messagebox, self.output_area)
            
            
            # Pega apenas eventos no dia de hoje
            agendamentos = agenda.horarios_agendados(tk, eventos, self.output_area)

            self.output_area.insert(tk.END, "Carregando horários disponíveis...\n")
            self.root.update()

            # Confere os dias disponíveis de acordo com os horários já reservados
            dias_disponiveis = schedules.horarios_disponiveis(agendamentos)

            self.output_area.insert(tk.END, "Iniciando criação de imagem. Escrevendo horários...\n")
            
            # Escrever horários disponiveis
            escrever_horarios.escrever_horarios_disponiveis(dias_disponiveis, image.draw)

            self.output_area.insert(tk.END, "Carregando dia da semana...\n")
            
            # Gera o dia da semana em que o script está rodando
            dia = day.gerar_dia_da_semana()

            self.output_area.insert(tk.END, "Escrevendo dia da semana na imagem...\n")
            
            # Escreve o dia atual na imagem
            day.escrever_dia(image.draw, dia)
            
            self.output_area.insert(tk.END, "Gerando imagem final...\n")
            self.root.update()
            # Cria a imagem nova
            image.gerar_imagem("new")
            self.output_area.insert(tk.END, "Processo finalizado com sucesso.\n")
            
            messagebox.showinfo("Sucesso!", "A imagem está pronta.")
            diretorio_script = os.path.dirname(os.path.abspath(__file__))
            subprocess.Popen(['explorer', diretorio_script], shell=True)

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
