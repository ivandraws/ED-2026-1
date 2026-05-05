import matplotlib.pyplot as plt
import  numpy as np
import timeit
import insertion

def medicaoDeTempo(nomes):
    # Clássico
    ini_c = timeit.default_timer()
    _, comp_c, troc_c = insertion.insertionSort(nomes.copy())
    fim_c = timeit.default_timer()

    # Auxiliar
    ini_a = timeit.default_timer()
    _, comp_a, troc_a = insertion.insertionSortAux(nomes.copy())
    fim_a = timeit.default_timer()

    algoritmos = ("Clássico", "Auxiliar")
    metricas = {
        "Tempo": (fim_c - ini_c,fim_a - ini_a),
        "Comparações": (comp_c, comp_a),
        "Trocas": (troc_c , troc_a)
    }

    return algoritmos, metricas


def criarGrafico(algoritimos, resultados):
    if not resultados or not algoritimos:
        print("Sem dados.")
        return
    x = np.arange(len(algoritimos))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')
    fig, ay = plt.subplots(layout='constrained')

    for attribute, measurement in resultados.items():
        offset = width * multiplier
        
        if multiplier == 0:
            rects = ax.bar(x + offset, measurement, width, label=attribute)
            ax.bar_label(rects, padding=3)
        else:
            rects = ay.bar(x + offset, measurement, width, label=attribute)
            ay.bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Segundos(s)')
    ax.set_title('Comparação da eficiência dos algorítmos')
    ax.set_xticks(x, algoritimos)
    ax.legend(loc='upper left', ncols=1)
    ax.set_ylim(0, int(resultados["Tempo"][1]) * 4)

    print(resultados["Comparações"][0])
    print(resultados["Comparações"][1])
    print(resultados["Trocas"][0])
    print(resultados["Trocas"][1])
    
    

    #Refazer


    ay.set_ylabel('Quantidade')
    ay.set_title('Quantidade de comparações e trocas entre algorítimos de insertion')
    ay.set_xticks(x + width + 0.13, algoritimos)
    ay.legend(loc='upper left', ncols = 2)
    ay.set_ylim(0, 1000000000)
    plt.show()