#import node

import os
import subprocess
from lerArquivo import lerArquivos
from listaEncadeadaSimples import Fila

'''
Copyright © 2026 ivandraws, HederPerreira, realuzli

UNDER MIT LICENCE
'''
# Não esqueça, essa fila é 1 prioridade, 3 não prioridade

semPrio = Fila()
comPrio = Fila()

def limpa_tela():
    if os.name == 'nt':
        # Roda só no Windows
        subprocess.call('cls', shell=True)
    else:
        # Só sobra POSIX (Mac e Linux)
        subprocess.call('clear', shell=True)

def mostrarMenu():
    limpa_tela()
    print("------Atendimento do Mercado da Memória RAM------")
    print("1. Ver prioridade da pessoa") # Dizer se é ou não prioridade
    print("2. Atendimento de pessoa") # Chamar a pessoa para atendimento
    print("3. Listar a fila toda") # Listar todas as pessoas na fila
    print("4. Carregar arquivo TXT para armazenamento de fila") # Ler arquivos TXT contendo pessoas para colocar na fila
    print("5. Carregar manualmento as pessoas") # Opção de DEBUG para adicionar pessoas manualmente
    print("0. Sair\n") # Preciso mesmo que comentar isso ?

def verPrioridade(contPadrao):
    if contPadrao == 0:
        print(f"Próxima pessoa a ser atendida: {comPrio.firstQueue()}")
        print("É prioridade")
        
    else:
        print(f"Próxima pessoa a ser atendida: {semPrio.firstQueue()}")
        print("Não é prioridade")


    
def menu():
    '''
    ### Função do Menu de Terminal
    '''
    pessoa_count = 0 # Conta a qntd de pessoas presentes na fila
    atendTotal = 0 # Guarda o numero total de atendimentos
    atendPref = 0 # Guarda quantas prioridades foram atendidas
    contPadrao = 0 #Variável de teste para manter o pradrão 1\3
    while True:

        mostrarMenu()
        try:
            choice = int(input())
        except ValueError:
            input("Valor inválido. Presione Enter e tente novamente...")
            continue

        
        match (choice):
            case 1:
                verPrioridade(contPadrao)
                input("Presione Enter para continuar....")
            
            case 2:
                if pessoa_count > 0:

                    # Verifica se: o contador da prioridade e se existem elementos nos grupos de pessoa
                    if(contPadrao == 0 and comPrio.len() > 0):
                        atendPref += 1
                        print(f"Atendimento Com Prioridade para {comPrio.firstQueue()}")
                        comPrio.dequeue()
                        if semPrio.len() > 0:
                            contPadrao += 1
                        pessoa_count -= 1
                    elif contPadrao > 0 or semPrio.len() > 0:
                        print(f"Atendimento Sem Prioridade para {semPrio.firstQueue()}")
                        semPrio.dequeue()
                        if (contPadrao == 3 and comPrio.len() > 0) or semPrio.len() == 0:
                            contPadrao = 0
                        else:
                            contPadrao += 1
                        pessoa_count -= 1
                        
                    else:
                        print("Houston, temos problemas. Erro Inesperado no atendimento!")

                    atendTotal += 1
                    
                else:
                    print("Não existe mais pessoas na fila")

                input("Presione Enter para continuar....")
                print()
            
            case 3:
                semPrio.show(False)
                comPrio.show(True)
                input("Presione Enter para continuar....")
            
            case 4:
                lerArquivos(comPrio, semPrio)
                pessoa_count = semPrio.len() + comPrio.len()
                input("Presione Enter para continuar....")
            
            case 5:
                pes = input("Digite o nome da pessoa: ")
                if input("É prioridade ? (Y/N)") == "Y":
                    comPrio.enqueue(pes)
                else:
                    semPrio.enqueue(pes)
                pessoa_count += 1
                input("Presione Enter para continuar....")
            case 0:
                
                if pessoa_count == 0 or pessoa_count < 0:
                    # Garante que o programa só vai fechar se todos forem atendidos
                    print("\n\n\n")
                    print("Fim de atendimento")
                    
                    if atendTotal > 0:
                        # Evita divisão por zero
                        porcAtendPref = (atendPref / atendTotal) * 100
                        print(f"Total de atendimentos: {atendTotal}")
                        print(f"Porcentagem de pessoas de prioriade: {porcAtendPref:.2f}%")
                        print(f"Porcentagem de pessoas sem prioridade: {100.00 - porcAtendPref :.2f}%")
                    
                    else:
                        print("Ninguém foi atendido. Dia bem produtivo....")
                    return
                else:
                    print(f"Não é possível sair. Tem {pessoa_count} pessoa(s) na fila!")
                    input("Pressione enter para continuar...")
                    print() 
    
        
    
if __name__ == "__main__":
    menu()
