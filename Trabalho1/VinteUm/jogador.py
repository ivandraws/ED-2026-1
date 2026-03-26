from baralho import Baralho 

class Jogador():
    def __init__(self):
        self.mão = []
    
    def comprar(self, baralho: Baralho):
        self.mão.append(baralho.removerCarta())
    
    def mostrarMão(self):
        print("Mão Atual: ")
        for carta in self.mão:
            print(f"{carta},", end=" ")
        print()

    def devolverParaOBaralho(self, baralho: Baralho):
        for carta in self.mão:
            print(f"removendo carta: {carta}")
            baralho.adicionarCarta(carta)
        self.mão.clear()

# baralho = Baralho()
# jogador = Jogador()
# baralho.embaralhar()
# jogador.comprar(baralho)
# jogador.comprar(baralho)
# jogador.comprar(baralho)
# jogador.mostrarMão()
# baralho.show()
# jogador.devolverParaOBaralho(baralho)
# baralho.show()