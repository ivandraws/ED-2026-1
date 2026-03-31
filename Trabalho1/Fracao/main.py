from frac import Fraction
import os

def limpa_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def setNum():
    n = int(input("Digite o numerador da fração: "))
    return n
def setDen():
    n = int(input("Digite o denominador da fração: "))
    return n



def menu():
    while True:
        limpa_tela()
        print("------Demonstração de Operações com a Classe Fração------\n" \
        "1. Configurar frações\n" \
        "2. Mostrar Fração 1\n" \
        "3. Mostrar Fração 2\n" \
        "4. Mostrar operações básicas entre as frações\n" \
        "0. Sair\n")
        
        
        choice = int(input())
        
        print()

        match (choice):
            case 1:
                print("Primeira fração:")
                n1 = setNum()
                d1 = setDen()
                frac1 = Fraction(n1,d1)
                print("\nSegunda Fração: ")
                n2 = setNum()
                d2 = setDen()
                frac2 = Fraction(n2, d2)
                print()
            case 2:
                print(f"{frac1.getNum()}/{frac1.getDen()}")
                input("Aperte enter para continuar...")
            case 3:
                print(f"{frac2.getNum()}/{frac2.getDen()}")
                input("Aperte enter para continuar...")
            case 4:
                print()
                print(f"Adição: {frac1 + frac2}")
                print(f"Subtração: {frac1 - frac2}")
                print(f"Multiplicação: {frac1 * frac2}")
                print(f"Divisão: {frac1 / frac2}")
                input("Aperte enter para continuar...")
            case 0:
                return



if __name__ == "__main__":    
    menu()


