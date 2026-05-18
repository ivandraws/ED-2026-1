import subprocess
import csv
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

ARQUIVO_QUADRATICOS = "resultadosQuadraticos.csv"
ARQUIVO_NLOGN       = "iterações.csv"
ARQUIVO_FINAL       = "resultadoProvisorio.csv"


def consolidarCSVs():
    linhas = []

    if os.path.exists(ARQUIVO_QUADRATICOS):
        with open(ARQUIVO_QUADRATICOS, "r") as f:
            for row in csv.DictReader(f):
                linhas.append(dict(row))

    if os.path.exists(ARQUIVO_NLOGN):
        with open(ARQUIVO_NLOGN, "r") as f:
            reader = csv.DictReader(f)
            reader.fieldnames = [c.strip() for c in reader.fieldnames]
            for row in reader:
                row = {k.strip(): v for k, v in row.items()}
                arquivo = row.get("Arquivo") or row.get("Arquivos", "")
                for alg in ["shell", "heap", "merge", "quick"]:
                    if row.get(alg, "").strip() == "":
                        continue
                    linhas.append({
                        "Arquivo": arquivo, "Algoritmo": alg,
                        "Exec1": row[alg], "Exec2": row[alg],
                        "Exec3": row[alg], "Exec4": row[alg],
                        "Exec5": row[alg], "Media": row[alg]
                    })

    if not linhas:
        print("Nenhum resultado encontrado. Rode as simulacoes primeiro.")
        return False

    with open(ARQUIVO_FINAL, "w", newline="") as f:
        campos = ["Arquivo", "Algoritmo", "Exec1", "Exec2", "Exec3", "Exec4", "Exec5", "Media"]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(linhas)

    return True


def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Rodar simulacao n2 (Bubble, Selection, Insertion)")
        print("2. Rodar simulacao nlogn (Shell, Heap, Merge, Quick)")
        print("3. Ver graficos do CSV final, caso não queria rodar cada simulacao")
        print("0. Sair")

        opcao = input("\nOpcao: ").strip()

        if opcao == "1":
            subprocess.run(["python3", "ordenaçãoQuadraticos.py"])

        elif opcao == "2":
            subprocess.run(["python3", "ordenaçãoNLogN.py"])

        elif opcao == "3":
            if os.path.exists(ARQUIVO_FINAL):
                subprocess.run(["python3", "graficos.py"])
            else:
                print(f"Arquivo {ARQUIVO_FINAL} nao encontrado.")

        elif opcao == "0":
            break


menu()