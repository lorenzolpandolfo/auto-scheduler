import subprocess
import tkinter as tk
import customtkinter as ctk


class UpdaterApp:
    def __init__(self, root):
        self.end = True
        self.root = root
        self.root.title("Atualizando Auto Scheduler...")
        root.geometry("400x100")
        root.resizable(width=False, height=False)
        self.style()
        self.git_pull()
    
    def style(self):
        self.main_frame = ctk.CTkFrame(self.root, width=380, height=80, corner_radius=10)
        self.main_frame.grid(row=0, column=0, padx=10,pady=(10,10))

        self.title = ctk.CTkLabel(self.main_frame, text="Atualizando...",font=ctk.CTkFont(size=23, weight="bold"))
        self.title.grid(row=0, column=0, padx=20, pady=(20, 20))


    def git_pull(self):
        try:
            subprocess.run(['git','pull','origin','master'], check=True, creationflags=subprocess.CREATE_NO_WINDOW)
            self.root.after(50, self.root.destroy)
        
        except Exception as e:
            print(f"Erro: {e}")
            self.root.after(50, self.root.destroy)
            

def atualizar():
    try:
        subprocess.run(['git','pull','origin','master'], check=True, creationflags=subprocess.CREATE_NO_WINDOW)

    except Exception as e:
        print(f"Erro: {e}")


def criar_janela():
    root = ctk.CTk()
    app = UpdaterApp(root)
    root.mainloop()
