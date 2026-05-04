def insertionSort(arr: list):
    comparacoes = 0
    trocas = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        comparacoes += 1
    
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            trocas += 1
            j -= 1
    
            if j >= 0: comparacoes += 1
        arr[j + 1] = key
    return arr, comparacoes, trocas

def insertionSortAux(arr: list):
    """Implementação do insertion sort que retorna uma nova lista e mantém a original"""

    total_comp = 0
    total_trocas = 0
    aux = [None] * len(arr)
    
    for i in arr:
        comp, troc = insertOrdered(aux, i)
        total_comp += comp
        total_trocas += troc
    
    return aux, total_comp, total_trocas

def insertOrdered(arr: list, elem):
    """Insere um elemento ordenadamente em uma lista"""

    comp = 0
    troc = 0
    if arr[0] is None:
        arr[0] = elem
        return comp, troc
    
    for i in range(len(arr)):
        if arr[i] is None: break
        comp += 1
    
        if elem <= arr[i]:
            prev = arr[i]
    
            for j in range(i + 1, len(arr)):
                temp = arr[j]
                arr[j] = prev
                troc += 1
                prev = temp
            arr[i] = elem
    
            return comp, troc
    arr[i] = elem
    return comp, troc