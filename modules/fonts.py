import os

def carregar_diretorio_fonte(fonte):
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    
    # retorna o diretório da fonte
    return os.path.join(diretorio_atual, fonte + ".ttf")
