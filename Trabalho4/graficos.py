import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


N2      = ["bubble", "selection", "insertion"]
NLOGN   = ["shell", "heap", "merge", "quick"]

ORDEM_TAMANHO = {"500": 0, "100k": 1, "250k": 2, "500k": 3, "1m": 4}

CORES_TAMANHO = ["#3498db", "#2ecc71", "#e67e22", "#e74c3c", "#9b59b6"]


def lerCSV():
    caminho = os.path.join(os.path.dirname(__file__), "resultadoProvisorio.csv")
    df = pd.read_csv(caminho)
    df.columns = df.columns.str.strip()
    df["Algoritmo"] = df["Algoritmo"].str.strip().str.lower()
    df["Arquivo"]   = df["Arquivo"].str.strip()
    df["tamanho"]   = df["Arquivo"].str.extract(r"nomes(\w+)\.txt")
    df["ordem"]     = df["tamanho"].map(ORDEM_TAMANHO).fillna(99)
    df = df.sort_values("ordem")
    return df


def criarGrafico(ax, df, algoritmos, titulo):
    subset = df[df["Algoritmo"].isin(algoritmos)]
    if subset.empty:
        print(f"Nenhum dado para: {algoritmos}")
        return

    algs_presentes = [a for a in algoritmos if a in subset["Algoritmo"].values]
    tamanhos       = list(dict.fromkeys(subset["tamanho"]))

    x     = np.arange(len(algs_presentes))
    width = 0.8 / len(tamanhos)

    for i, tamanho in enumerate(tamanhos):
        medias = []
        for alg in algs_presentes:
            linha = subset[(subset["Algoritmo"] == alg) & (subset["tamanho"] == tamanho)]
            medias.append(linha["Media"].values[0] if not linha.empty else 0)

        offset = width * i - (width * len(tamanhos) / 2) + width / 2
        cor    = CORES_TAMANHO[i % len(CORES_TAMANHO)]
        rects  = ax.bar(x + offset, medias, width, label=tamanho.upper(), color=cor, alpha=0.88)
        ax.bar_label(rects, fmt="%.3f", padding=2, fontsize=7, rotation=45)

    ax.set_title(titulo, fontsize=13, fontweight="bold", pad=12)
    ax.set_ylabel("Tempo médio (s)", fontsize=11)
    ax.set_xticks(x, [a.capitalize() for a in algs_presentes], fontsize=11)
    ax.legend(title="Tamanho", fontsize=9)
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    ax.set_ylim(bottom=0)


df = lerCSV()

fig, (ax1, ax2) = plt.subplots(1, 2, layout="constrained", figsize=(18, 6))

criarGrafico(ax1, df, N2,    "Algoritmos O(n²)")
criarGrafico(ax2, df, NLOGN, "Algoritmos O(n log n)")

plt.show()