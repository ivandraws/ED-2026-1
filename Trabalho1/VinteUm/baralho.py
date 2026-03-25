from carta import Carta
import random
class Baralho():
    def __init__(self):
        self.cartas = []
        tipo_carta = ["Ouros","Paus","Espadas","Copas"]
        for naipes in tipo_carta:
            for numero in range(1,14):
                self.cartas.append(Carta(numero,naipes))
    def show(self):
        for carta in self.cartas:
            print(carta)
        
    def embaralhar(self):
        random.shuffle(self.cartas)
    
    def removerCarta(self):
        return self.cartas.pop(0)

    def adicionarCarta(self, carta:Carta):
        self.cartas.append(carta)
