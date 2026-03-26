from baralho import Baralho
from jogo import Jogo
import os



def main():
    
    os.system("clear")
    print("----------Jogo do Vinte Um----------\n" \
        "Regras: Para ganhar, tem que conseguir exatamente uma pontuação de 21\n" \
        "Cada carta vale seu número base, com exceção do Valete, Rainha e Rei, que valem 10\n")
    while True:
        opt = int(input("Deseja começar o jogo do 21 ?\n1. Iniciar\n2. Mostrar estatísticas\n0. Sair\n\n"))
        
        match (opt):
            case(1):
                gameplay()
                break
            case(2):
                print(f"\nVitórias: {Game.vitoria}\nDerrotas: {Game.derrota}\n")
                input("Pressione alguma tecla para continuar...")
            case(0):
                return 0
    

def gameplay():
    while True:    
        print()
        Game.distribuir()
        
        while True:
            os.system("clear")
            player.mostrarMão()
            if escolha() == 1:
                player.comprar(bar)
            else:
                break
        Game.verificarVitória()    
        
        o = int(input("Você quer começar uma nova partida ?\n1. Sim\n0. Não\n"))
        if o == 0:
            return   
    
    
        
            


def escolha():
    escol = int(input("Você quer\n1. Comprar\n2. Parar\n"))
    return escol

if __name__ == "__main__":
    Game = Jogo()
    player = Game.jogador
    bar = Game.baralho
    while True:
        if main() == 0:
            break