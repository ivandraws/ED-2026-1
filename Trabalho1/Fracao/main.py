from frac import Fraction

def getNum():
    num = int(input("Digite o numerador da fração: "))
    return num

def getDen():
    den = int(input("Digite o denominador da fração: "))
    return den

print("Primeira fração:")
frac1 = Fraction(getNum(),getDen())
print("Segunda Fração: ")
frac2 = Fraction(getNum(), getDen())

if __name__ == "__main__":
    
    
    print(frac1 + frac2)
    print(frac1 - frac2)
    print(frac1 * frac2)
    print(frac1 / frac2)


