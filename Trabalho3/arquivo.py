"""Módulo responsável pela leitura do arquivo de nomes e também por escrever os nomes ordenados na nova lista"""

def carregarArquivodeNomes(diretorio:str):
    try:
        with open(diretorio,"r") as f:
            nomes = f.read().split("\n")
    except Exception as e:
        print("Erro ao carregar arquivo")
        print(e)
    
    return nomes

def salvarOrdenados(nomes:list):
    with open("ordenados.txt", "w") as f:
        for nome in nomes:
            f.write(f"{nome}\n")
        
