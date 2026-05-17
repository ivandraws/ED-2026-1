import csv
import os
import subprocess
import tratamentoDeDados


ARQUIVO_CSV = "resultadosNLogN.csv"

algoritmos = {
    "me": "merge",
    "qu": "quick",
    "he": "heap",
    "sh": "shell"  
}

arquivos = [
    "nomes100k.txt",
    "nomes250k.txt",
    "nomes500.txt",
    "nomes1m.txt"
]

def inicializa_csv():
    if not os.path.exists(ARQUIVO_CSV):
        with open(ARQUIVO_CSV, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "Arquivo",
                "Algoritmo",
                "Exec1",
                "Exec2",
                "Exec3",
                "Exec4",
                "Exec5",
                "Media"
            ])


def linha_ja_existe(arquivo, algoritmo):
    if not os.path.exists(ARQUIVO_CSV):
        return False

    with open(ARQUIVO_CSV, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Arquivo"] == arquivo and row["Algoritmo"] == algoritmo:
                return True
    return False


def executa_algoritmo(arquivo, codigo_algoritmo):

    processo = subprocess.run(
        ["./main", f"min{arquivo}", codigo_algoritmo],
        capture_output=True,
        text=True
    )

    if processo.returncode != 0:
        print(f"Erro ao executar {codigo_algoritmo} em {arquivo}")
        print(processo.stderr)
        return None


    nome_saida = {
        "me": "resMerge.txt",
        "qu": "resQuick.txt",
        "he": "resHeap.txt",
        "sh": "resShell.txt"  
    }

    arquivo_saida = nome_saida[codigo_algoritmo]

    try:
        with open(arquivo_saida, "r") as f:
            tempos = [float(linha.strip()) for linha in f.readlines()]
            return tempos
    except FileNotFoundError:
        print(f"Arquivo {arquivo_saida} não encontrado")
        return None


def salva_resultado(arquivo, algoritmo, tempos):
    media = sum(tempos) / len(tempos)

    with open(ARQUIVO_CSV, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            arquivo,
            algorithm := algoritmo,
            f"{tempos[0]:.6f}",
            f"{tempos[1]:.6f}",
            f"{tempos[2]:.6f}",
            f"{tempos[3]:.6f}",
            f"{tempos[4]:.6f}",
            f"{media:.6f}"
        ])


def main():
    inicializa_csv()

    for arq in arquivos:
        print(f"\n========== PROCESSANDO {arq} ==========\n")
        
        tratamentoDeDados.trataArquivo(arq)

        for codigo, nome_alg in algoritmos.items():
            if linha_ja_existe(arq, nome_alg):
                print(f"{nome_alg} em {arq} já existe no CSV")
                continue

            print(f"Executando {nome_alg} em {arq}...")
            tempos = executa_algoritmo(arq, codigo)

            if tempos is None:
                continue

            salva_resultado(arq, nome_alg, tempos)
            print(f"{nome_alg} concluído em {arq}")


if __name__ == "__main__":
    main()