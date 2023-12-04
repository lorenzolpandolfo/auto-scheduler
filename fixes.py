import os

def token(messagebox):
    try:
        if os.path.exists("token.json"):
            os.remove("token.json")
            
    except Exception as err:
        messagebox.showerror("Erro no conserto automático", f"Houve um erro ao realizar o conserto automático. Tente remover o " +
                            f"arquivo 'token.json' do diretório do programa.\n{str(err)}")



