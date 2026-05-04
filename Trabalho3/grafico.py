import matplotlib.pyplot as plb
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

    return {
        "Clássico": fim_c - ini_c,
        "Auxiliar": fim_a - ini_a
    }

def criarGrafico(resultados):
    if not resultados:
        print("Sem dados.")
        return
    x = list(resultados.keys())
    y = list(resultados.values())
    plb.bar(x, y, color=["navy", "skyblue"])
    plb.ylabel("Tempo (segundos)")
    plb.show()