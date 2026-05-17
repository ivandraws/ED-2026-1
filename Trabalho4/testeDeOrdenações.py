import csv
import os
import subprocess
import tratamentoDeDados

ARQUIVO_CSV = "iterações.csv"

algoritmos = {
    "bu": "bubble",
    "se": "selection",
    "in": "insertion",
    "sh": "shell",
    "he": "heap",
    "me": "merge",
    "qu": "quick"
}

arquivos = [
    "nomes100k.txt",
    "nomes250k.txt",
    "nomes500k.txt",
    "nomes1m.txt"
]


def inicializa_csv():

    if not os.path.exists(ARQUIVO_CSV):

        with open(ARQUIVO_CSV, "w", newline="") as f:

            writer = csv.writer(f)

            writer.writerow([
                "Arquivo",
                "bubble",
                "selection",
                "insertion",
                "shell",
                "heap",
                "merge",
                "quick"
            ])


def carregar_existentes():

    existentes = set()

    if not os.path.exists(ARQUIVO_CSV):
        return existentes

    with open(ARQUIVO_CSV, "r") as f:

        reader = csv.DictReader(f)

        for row in reader:

            chave = (
                row["Arquivo"],
                row["bubble"],
                row["selection"],
                row["insertion"],
                row["shell"],
                row["heap"],
                row["merge"],
                row["quick"]
            )

            existentes.add(chave)

    return existentes


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
        "bu": "resBubble.txt",
        "se": "resSelect.txt",
        "in": "resInsert.txt",
        "sh": "resShell.txt",
        "he": "resHeap.txt",
        "me": "resMerge.txt",
        "qu": "resQuick.txt"
    }

    arquivo_saida = nome_saida[codigo_algoritmo]

    try:

        with open(arquivo_saida, "r") as f:

            linhas = f.readlines()

            tempos = [linha.strip() for linha in linhas]

            return tempos

    except FileNotFoundError:

        print(f"Arquivo {arquivo_saida} não encontrado")
        return None


def main():

    inicializa_csv()

    existentes = carregar_existentes()

    for arq in arquivos:

        print(f"Tratando {arq}...")

        tratamentoDeDados.trataArquivo(arq)

        linha = {
            "Arquivo": arq,
            "bubble": "",
            "selection": "",
            "insertion": "",
            "shell": "",
            "heap": "",
            "merge": "",
            "quick": ""
        }

        for codigo, nome_alg in algoritmos.items():

            print(f"Executando {nome_alg} em {arq}...")

            tempos = executa_algoritmo(arq, codigo)

            if tempos is None:
                continue

            media = sum(map(float, tempos)) / len(tempos)

            linha[nome_alg] = f"{media:.6f}"

        chave = (
            linha["Arquivo"],
            linha["bubble"],
            linha["selection"],
            linha["insertion"],
            linha["shell"],
            linha["heap"],
            linha["merge"],
            linha["quick"]
        )

        if chave not in existentes:

            with open(ARQUIVO_CSV, "a", newline="") as f:

                writer = csv.writer(f)

                writer.writerow([
                    linha["Arquivo"],
                    linha["bubble"],
                    linha["selection"],
                    linha["insertion"],
                    linha["shell"],
                    linha["heap"],
                    linha["merge"],
                    linha["quick"]
                ])

            print(f"Resultado salvo para {arq}")

        else:

            print(f"{arq} já estava no CSV")


if __name__ == "__main__":
    main()