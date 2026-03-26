#Classe que cria o baralho do jogo
from carta import Carta
import random

class Baralho():
    def __init__(self):
        #Cria uma lista de cartas e também uma lista para cada naipe
        self.cartas = []
        tipo_carta = ["Ouros","Paus","Espadas","Copas"]

        for naipes in tipo_carta: #Preenche a lista de cartas
            for numero in range(1,14):
                self.cartas.append(Carta(numero,naipes))

    def show(self): #Mostra todas as cartas presentes no baralho
        print("Baralho: ")
        for carta in self.cartas:
            print(carta, end =", ")
        print()
        
    def embaralhar(self): #Embaralha a lista de Cartas
        random.shuffle(self.cartas)
    
    def removerCarta(self): #Remove e retorna a carta no topo da lista
        return self.cartas.pop(0)

    def adicionarCarta(self, carta:Carta): #Adiciona a carta no final da lista
        self.cartas.append(carta)
