"""
Checar no Google Agenda horários disponíveis dentre um intervalo de tempo
Criar uma imagem .png organizada informando os horários disponíveis para agendamento.
A imagem será utilizada nas redes sociais do estabelecimento.
"""
import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import Calendar

import subprocess
import os
import customtkinter as ctk

import image
import day
import quickstart
import agenda
import schedules
import escrever_horarios
import dnm

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class MainApp:
    def __init__(self, root):
        self.end = True
        self.root = root
        self.root.title("Auto scheduler")
        root.geometry("600x370")
        root.resizable(width=False, height=False)
        root.configure(bg="#7289da")
        self.init_gui()
        
    def init_gui(self):
        self.output_area = ctk.CTkTextbox(root, height=20, width=54)
        self.output_area.place(x=120, y=20)

        self.sidebar_frame = ctk.CTkFrame(root, width=170, height=370, corner_radius=10)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")


        self.title = ctk.CTkLabel(self.sidebar_frame, text="Auto Scheduler",font=ctk.CTkFont(size=23, weight="bold"))
        self.title.grid(row=0, column=0, padx=20, pady=(20, 20))


        self.text_dia = ctk.CTkLabel(self.sidebar_frame, text="Dia",font=ctk.CTkFont(size=18))
        self.text_dia.grid(row=1, column=0)

        self.text_mes = ctk.CTkLabel(self.sidebar_frame, text="Mês",font=ctk.CTkFont(size=18))
        self.text_mes.grid(row=3, column=0,pady=(20,0))
        

        self.input_dia = ctk.CTkTextbox(self.sidebar_frame, height=1, width=30)
        self.input_mes = ctk.CTkTextbox(self.sidebar_frame, height=1, width=30)
        self.combobox_dia = ctk.CTkComboBox(self.sidebar_frame,
                                                    values=dnm.dias)
        self.combobox_mes = ctk.CTkComboBox(self.sidebar_frame,
                                                    values=dnm.meses)
        self.combobox_dia.grid(row=2, column=0, padx=20)
        self.combobox_mes.grid(row=4, column=0, padx=20)
        
        #self.input_dia.place(x=50, y=55)
        #self.input_mes.place(x=10, y=79)

        self.input_dia.insert(tk.END, str(day.dia_atual()))
        self.input_mes.insert(tk.END, str(day.mes_atual()))


        self.btn_criar_imagem = ctk.CTkButton(self.sidebar_frame, text="Criar imagem",
        command=lambda: self.criar_imagem(int(self.input_mes.get("1.0", tk.END)), int(self.input_dia.get("1.0", tk.END))))

        self.btn_criar_imagem.grid(row=9,column=0,padx=20,pady=90)

        estilo = ttk.Style()
        estilo.configure("TButton", font=("Arial", 9))
    

    def criar_imagem(self, mes, dia):
        self.output_area.delete("1.0", tk.END)

        self.output_area.insert(tk.END, "Iniciando Auto Scheduler...\n")
        self.root.update()
        try:
            # Carrega todos eventos da agenda
            eventos = quickstart.main(tk, messagebox, self.output_area, mes, dia)
            
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
            dia = day.gerar_dia_da_semana(mes, dia)

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
        self.btn_abrir_diretorio = ctk.CTkButton(root, text="Abrir Diretório", command=self.open_image_directory)
        self.btn_abrir_diretorio.place(x=10,y=230)

        self.btn_sair = ctk.CTkButton(root, text="Sair", command=exit)
        self.btn_sair.place(x=10,y=260)

        # Não está funcionando na terceira vez que cria a imagem.
        # O texto anterior não é resetado...
        image.resetar_imagem()


    def open_image_directory(self):
        diretorio_script = os.path.dirname(os.path.abspath(__file__))
        subprocess.Popen(['explorer', diretorio_script], shell=True)
        exit()


if __name__ == "__main__":
    # criando a janela principal
    # root = tk.Tk()
    root = ctk.CTk()
    # mandando a janela principal pro MainApp
    app = MainApp(root)
    # iniciando o loop
    root.mainloop()
