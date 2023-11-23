"""
Checar no Google Agenda horários disponíveis dentre um intervalo de tempo
Criar uma imagem .png organizada informando os horários disponíveis para agendamento.
A imagem será utilizada nas redes sociais do estabelecimento.
"""
import tkinter as tk
from tkinter import messagebox, ttk
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
        self.end = True
        self.root = root
        self.root.title("Auto scheduler")
        root.geometry("500x500")
        root.resizable(width=False, height=False)
        root.configure(bg="#7289da")

        self.output_area = tk.Text(root, height=20, width=60)
        self.output_area.pack(pady=20)
        
        self.btn_criar_imagem = ttk.Button(root, text="Criar imagem", command=self.criar_imagem)
        self.btn_criar_imagem.pack()

        estilo = ttk.Style()
        estilo.configure("TButton", font=("Arial", 9))
    
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
            
            if self.end:
                self.final_window()

            messagebox.showinfo("Sucesso!", "A imagem new.png está pronta. Aperte em Abrir Diretório para abrir o diretório da imagem.")


        except Exception as e:
            messagebox.showerror("Erro", f"Um erro aconteceu: {str(e)}")


    def final_window(self):
        self.end = False
        self.btn_abrir_diretorio = ttk.Button(root, text="Abrir Diretório", command=self.open_image_directory)
        self.btn_abrir_diretorio.pack()

        self.btn_sair = ttk.Button(root, text="Sair", command=exit)
        self.btn_sair.pack()


    def open_image_directory(self):
        diretorio_script = os.path.dirname(os.path.abspath(__file__))
        subprocess.Popen(['explorer', diretorio_script], shell=True)
        exit()


if __name__ == "__main__":
    # criando a janela principal
    root = tk.Tk()
    # mandando a janela principal pro MainApp
    app = MainApp(root)
    # iniciando o loop
    root.mainloop()
