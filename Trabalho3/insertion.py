import time, random
def insertionSortAux(arr: list):
    """Implementação do insertion sort que retorna uma nova lista e mantém a original"""
    aux = [None] * len(arr)
    for i in arr:
        insertOrdered(aux,i)
    
    return aux

def insertOrdered(arr:list, elem):
    """Insere um elemento ordenadamente em uma lista"""
    if arr[0]==None:
        arr[0]=elem
        return

    for i in range(len(arr)):
        if arr[i] is None:
            break
        if elem <= arr[i]:
            prev = arr[i]
            for j in range(i+1,len(arr)):
                temp = arr[j]
                arr[j]=prev
                prev=temp
            arr[i] = elem
            return
        
    arr[i]=elem
    
def insertionSort(arr:list):
    """Insertion sort clássico"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

