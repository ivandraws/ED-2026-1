from baralho import Baralho
from jogo import Jogo



def main():

    
    print("----------Jogo do Vinte Um----------\n" \
        "Regras: Para ganhar, tem que conseguir exatamente uma pontuação de 21\n" \
        "Cada carta vale seu número base, com exceção do Valete, Rainha e Rei, que valem 10\n")
    opt = int(input("Deseja começar o jogo ?\n1. Iniciar\n0. Sair\n"))
    if opt == 1:
        #iniciar jogo
        Jooj = Jogo()
    elif opt == 0:
        return
    
    
    while True:    
        
        player = Jooj.jogador
        bar = Jooj.baralho
        Jooj.distribuir()
        
        while True:
            player.mostrarMão()
            if escolha() == 1:
                player.comprar(bar)
            else:
                break
        Jooj.verificarVitória()    
        
        return
            


def escolha():
    escol = int(input("Você quer\n1. Comprar\n2. Parar\n"))
    return escol

if __name__ == "__main__":
    
    main()