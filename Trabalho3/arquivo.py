"""Módulo responsável pela leitura do arquivo de nomes e também por escrever os nomes ordenados na nova lista"""

def carregarArquivodeNomes(diretorio: str):
    try:
        with open(diretorio, "r", encoding="utf-8") as f:
            size = 625
            nomes = [None] * size
            for i,nome in enumerate(f):
                if i == size:
                    aux = [None]*(size*2)
                    for j in range(size):
                        aux[j] = nomes[j]
                    nomes = aux
                    size *= 2

                nomes[i]= nome.rstrip('\n')

            print(nomes)
            return nomes

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


carregarArquivodeNomes("/home/heder/Estudos/Estrutura de Dados/ED-2026-1/Trabalho3/nomes.txt")