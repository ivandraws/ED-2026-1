#import node

import os
import subprocess
from lerArquivo import lerArquivos
from listaEncadeadaSimples import Fila

semPrio = Fila()
comPrio = Fila()

def limpa_tela():
    if os.name == 'nt':
        subprocess.call('cls', shell=True)
    else:
        subprocess.call('clear', shell=True)

def mostrarMenu():
    limpa_tela()
    print("------Atendimento do Mercado da Memória RAM------")
    print("1. Ver prioridade da pessoa")
    print("2. Atendimento de pessoa")
    print("3. Listar a fila toda")
    print("4. Carregar arquivo TXT")
    print("5. Adicionar pessoa manualmente")
    print("0. Sair\n")

def verPrioridade(estado):
    if estado["contPadrao"] == 0 and comPrio.len() > 0:
        print(f"Próxima pessoa: {comPrio.firstQueue()}")
        print("É prioridade")
    elif semPrio.len() > 0:
        print(f"Próxima pessoa: {semPrio.firstQueue()}")
        print("Não é prioridade")
    else:
        print("Fila vazia")

def atendepessoa(estado, comPrio, semPrio):
    if estado["pessoa_count"] > 0:

        if estado["contPadrao"] == 0 and comPrio.len() > 0:
            estado["atendPref"] += 1
            print(f"Atendimento PRIORIDADE: {comPrio.firstQueue()}")
            comPrio.dequeue()

            if semPrio.len() > 0:
                estado["contPadrao"] += 1

        elif semPrio.len() > 0:
            print(f"Atendimento NORMAL: {semPrio.firstQueue()}")
            semPrio.dequeue()

            if (estado["contPadrao"] == 3 and comPrio.len() > 0) or semPrio.len() == 0:
                estado["contPadrao"] = 0
            else:
                estado["contPadrao"] += 1

        else:
            print("Erro inesperado!")
            return

        estado["pessoa_count"] -= 1
        estado["atendTotal"] += 1

    else:
        print("Não existe mais pessoas na fila")

def adicionarPessoa(estado, comPrio, semPrio):
    pes = input("Nome: ")

    while True:
        prioridade = input("É prioridade? (Y/N): ").strip().upper()

        if prioridade == "Y":
            comPrio.enqueue(pes)
            break
        elif prioridade == "N":
            semPrio.enqueue(pes)
            break
        else:
            print("Digite apenas Y ou N!")

    estado["pessoa_count"] += 1

def finalizarAtendimento(estado):
    if estado["pessoa_count"] <= 0:
        print("\nFim de atendimento")

        if estado["atendTotal"] > 0:
            porc = (estado["atendPref"] / estado["atendTotal"]) * 100
            print(f"Total: {estado['atendTotal']}")
            print(f"Prioridade: {porc:.2f}%")
            print(f"Normal: {100 - porc:.2f}%")
        else:
            print("Ninguém foi atendido")

        return True
    else:
        print(f"Tem {estado['pessoa_count']} pessoa(s) na fila!")
        input("Enter...")
        return False

def menu():
    estado = {
        "pessoa_count": 0,
        "atendTotal": 0,
        "atendPref": 0,
        "contPadrao": 0,
    }

    while True:
        mostrarMenu()

        try:
            choice = int(input())
        except ValueError:
            input("Valor inválido. Enter...")
            continue

        match choice:
            case 1:
                verPrioridade(estado)
                input("Enter...")

            case 2:
                atendepessoa(estado, comPrio, semPrio)
                input("Enter...")

            case 3:
                semPrio.show(False)
                comPrio.show(True)
                input("Enter...")

            case 4:
                lerArquivos(comPrio, semPrio)
                estado["pessoa_count"] = semPrio.len() + comPrio.len()
                input("Enter...")

            case 5:
                adicionarPessoa(estado, comPrio, semPrio)
                input("Enter...")

            case 0:
                if finalizarAtendimento(estado):
                    return

if __name__ == "__main__":
    menu()