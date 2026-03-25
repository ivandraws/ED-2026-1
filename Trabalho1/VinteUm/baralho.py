from carta import Carta
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



