import os, subprocess, arquivo, insertion, grafico
import numpy as np
import matplotlib.pyplot as plb

def limpa_tela():
    """Função responsável por limpar o terminal  para uma 
    melhor visualização"""
    if os.name == 'nt':
        subprocess.call('cls', shell=True)
    else:
        subprocess.call('clear', shell=True)

def mostrar_menu():
    """"Mostrar o menu de opções para o usuário"""
    limpa_tela()
    print(
    "=================== AGENDA DE CONTATOS ===================\n"
    "Digite a opção desejada:\n"  
    "1 - Carregar outro arquivo de nomes\n"
    "2 - Ordenar Arquivo e listar os nomes\n"
    "3 - Listar dados originais\n"
    "4 - Listar dados ordenados\n"
    "5 - Salvar lista ordenada\n"
    "6 - Mostrar estatísticas\n"
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
            0 - cancelar
        """)
        opc = input()
        match opc:
            case "1":
                # Retorna a tupla (lista, comp, trocas)
                return insertion.insertionSort(nomes.copy())
            case "2":
                return insertion.insertionSortAux(nomes.copy())
            case "0":
                return None, 0, 0 
            case _:
                input("Opção inválida...")

def listarNomesArquivo(nomes:list):
    for i, nome in enumerate(nomes):
        print(nome, end=" ")
        if (i + 1) % 10 == 0:
            print("\n")

def main():
    arrayOriginal = []
    arrayOrdenado = []
    resultados = {}

    while True:
        mostrar_menu()
        opc = input()
        match opc:
            case "1":
                arrayOriginal = carregar_NovoArquivo()
    
            case "2":
                if not arrayOriginal:
                    input("Carregue o arquivo primeiro!")
                
                else:
                    arrayOrdenado, comp, troc = ordenar_lista_nomes(arrayOriginal)
                    
                    if arrayOrdenado:
                        print(f"\nOrdenação concluída!\nComparações: {comp}\nTrocas: {troc}\n")
                        listarNomesArquivo(arrayOrdenado)
                        input("\nPressione Enter para continuar...")

            case "3":
                if not arrayOriginal:
                    input("Array vazio. Tente carregar um arquivo ( Opção 1 )")
                else:
                    listarNomesArquivo(arrayOriginal)
                    input("\nEnter para voltar...")
        
            case "4":
                if not arrayOrdenado:
                    input("Nada ordenado ainda.")
                else:
                    listarNomesArquivo(arrayOrdenado)
                    input("\nEnter para voltar...")
            
            case "5":
                if not arrayOrdenado:
                    input("Nada para salvar.")
                else:
                    arquivo.salvarOrdenados(arrayOrdenado)
                    print("Arquivo salvo com sucesso.")
                    input()
            
            case "6":
                if not arrayOriginal:
                    input("Sem dados para estatística.")
                else:
                    resultados = grafico.medicaoDeTempo(arrayOriginal)
                    grafico.criarGrafico(resultados)
            
            case "0":
                print("Fim do programa!")
                return
            case _:
                input("Opção inválida...")

if __name__ == "__main__":
    main()