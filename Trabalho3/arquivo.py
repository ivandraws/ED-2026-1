"""Módulo responsável pela leitura do arquivo de nomes e também por escrever os nomes ordenados na nova lista"""

def carregarArquivodeNomes(diretorio: str):
    try:
        with open(diretorio, "r", encoding="utf-8") as f:
            return f.read().splitlines()
    except Exception as e:
        print(f"Erro ao carregar: {e}")
        return []

def salvarOrdenados(nomes: list):
    try:
        with open("ordenados.txt", "w", encoding="utf-8") as f:
            for nome in nomes:
                f.write(f"{nome}\n")
    except Exception as e:
        print(f"Erro ao salvar: {e}")