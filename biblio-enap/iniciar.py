import os
import requests

def baixar_planilha(url):
    # Verifica se a planilha já existe
    if not os.path.exists("Exemplo_Dados.xlsx"):
        # Faz o download da planilha
        r = requests.get(url)
        with open("Exemplo_Dados.xlsx", "wb") as f:
            f.write(r.content)
    print("Planilha baixada e disponível como 'Exemplo_Dados.xlsx'")

def iniciar():
    # URL do arquivo no GitHub
    url = "https://github.com/seu_usuario/biblio-enap/raw/main/Exemplo_Dados.xlsx"
    baixar_planilha(url)