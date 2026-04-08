#import node

import os
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
        os.system('cls')
    else:
        # Só sobra POSIX (Mac e Linux)
        os.system('clear')

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
    if contPadrao != 3:
        print(f"Próxima pessoa a ser atendida: {semPrio.firstQueue()}")
        print("Não é prioridade")
    else:
        print(f"Próxima pessoa a ser atendida: {comPrio.fistQueue}")
        print("É prioridade")
        
    
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

        
        match (choice):
            case 1:
                verPrioridade(contPadrao)
                input("Presione Enter para continuar....")
            
            case 2:
                if pessoa_count > 0:
                    pessoa_count -= 1
                    # Verifica se: o contador da prioridade e se existem elementos nos grupos de pessoa
                    if(contPadrao != 3) and len(semPrio) > 0:
                        print(f"Atendimento Sem Prioridade para {semPrio.pop(0)}")
                        contPadrao += 1
                    elif len(comPrio) > 0:
                        atendPref += 1
                        print(f"Atendimento Com Prioridade para {comPrio.pop(0)}")
                        contPadrao = 0
                    else:
                        print("Houston, temos problemas. Erro Inesperado no atendimento!")
                        input("Presione Enter para continuar....")

                    atendTotal += 1
                    input("Presione Enter para continuar....")
                else:
                    print("Não existe mais pessoas na fila")
                print()
            
            case 3:
                print(f"Sem prioridade: {semPrio}")
                print(f"Com prioridade: {comPrio}")
                input("Presione Enter para continuar....")
            
            case 4:
                lerArquivos(comPrio, semPrio)
                pessoa_count = len(semPrio) + len(comPrio)
                input("Presione Enter para continuar....")
            
            case 5:
                pes = input("Digite o nome da pessoa: ")
                if input("É prioridade ? (Y/N)") == "Y":
                    comPrio.append(pes)
                pessoa_count += 1
                input("Presione Enter para continuar....")
            case 0:
                
                if pessoa_count == 0 or pessoa_count < 0:
                    # Garante que o programa só vai fechar se todos forem atendidos
                    print("\n\n\n")
                    print("Fim de atendimento")
                    
                    if atendTotal > 0:
                        # Evita divisão por zero
                        print(f"Total de atendimentos: {atendTotal}")
                        print(f"Porcentagem de pessoas de prioriade: {(atendPref / atendTotal) * 100:.2f}%")
                    
                    else:
                        print("Ninguém foi atendido. Dia bem produtivo....")
                    return
                else:
                    print("Não é possível sair. Tem pessoas na fila!")
                    input("Pressione enter para continuar...")
                    print() 
    
        
    
if __name__ == "__main__":
    menu()
