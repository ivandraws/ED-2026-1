from baralho import Baralho
from jogador import Jogador

class Jogo():
    def __init__(self):
        self.jogador = Jogador()
        self.baralho = Baralho()
        self.baralho.embaralhar()
        self.vitoria = 0
        self.derrota = 0

    def distribuir(self):
        for i in range(2):
            self.jogador.mão.append(self.baralho.removerCarta())

    def verificarVitória(self):
        soma = 0
        for carta in self.jogador.mão:
            if carta.numero in range(11,14):
                soma +=10
            else: 
                soma += carta.numero

        if soma == 21:
            print("Você Ganhou!")
            self.vitoria += 1
        else:
            print("Você foi moggado")
            self.derrota += 1
            
        self.resetar()

    def resetar(self):
        self.jogador.devolverParaOBaralho(self.baralho)



# jogo = Jogo()
# jogo.distribuir()
# jogo.jogador.mostrarMão()
# jogo.baralho.show()
# jogo.verificarVitória()
# jogo.jogador.mostrarMão()
# jogo.baralho.show()