#teste luiz
import os, subprocess, arquivo, insertion,timeit
import numpy as np
import matplotlib.pyplot as plb

def limpa_tela():
    """Função responsável por limpar o terminal para uma
    melhor visualização"""

    if os.name == 'nt':
        subprocess.call('cls', shell=True)
    else:
        subprocess.call('clear', shell=True)

def mostrar_menu():
    """Mostra o menu de opções para o usuário"""
    limpa_tela()
    print(
    "=================== AGENDA DE CONTATOS ===================\n"

    "Digite a opção desejada:\n"  
    "1 - Carregar outro arquivo de nomes\n" \
    "2 - Ordenar Arquivo e listar os nomes\n" \
    "3 - Listar dados originais\n" \
    "5 - Salvar lista ordenada\n" \
    "6 - Mostrar estatísticas\n"\
    "0 - Sair"
    )


def carregar_NovoArquivo():
    diretorio = input("Insira o diretório com os nomes: ")
    return arquivo.carregarArquivodeNomes(diretorio)

def ordenar_lista_nomes(nomes:list):
    while True:
        limpa_tela()
        print(
        """Qual Algoritmo deseja utilizar?:
            1 - Insertion clássico
            2 - Insertion com ListaAuxiliar
            3 - ambos
            0 - cancelar
        """    
        )

        opc = input()
        match opc:
            case 1:
                return insertion.insertionSort(nomes.copy())

            case 2:
                return insertion.insertionSortAux(nomes)
            case 3:
                #TODO
                pass
            case 0:
                #TODO
                pass
            case _:
                input("Opção inválida, aperte qualquer botão para continuar...")

def listarNomesArquivo(nomes:list):
    for i,nome in enumerate(nomes):
        print(nome, end=" ")
        if i%10 == 0:
            print("\n")

def salvarOrdenados(nomes:list):
    arquivo.salvarOrdenados(nomes)

def mostrarEstatísticas(resultados):
    # Aqui eu vou ter um dicionário para armazenar o meu tipo de algoritmo de ordenacao ( chave ) e o tempo que levou para ordenar ( valor )
    tiposAlgoritmo = resultados.keys()
    tempoAlgoritmo = resultados.values()
    x = np.array(tiposAlgoritmo)
    y = np.array(tempoAlgoritmo)
    plb.bar(x,y)
    plb.show()

    pass



def main():
    
    while True:
        limpa_tela()
        mostrar_menu()
        opc = input()
        resultados = {}
        match opc:
            case 1:
                arquivoOriginal = carregar_NovoArquivo()
    
            case 2:
                ordenar_lista_nomes(novoArquivo)

                
            case 3:
                listarNomesArquivo(novoArquivo)
        
            case 4:
                listarNomesArquivo(novoArquivo)
                pass
            case 5:
                pass
            case 6:
                mostrarEstatísticas(resultados)
                pass
            case 0:
                print("Fim do programa!")
                return
            case _:
                input("Opção inválida, aperte qualquer botão para continuar...")