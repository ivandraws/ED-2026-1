from frac import Fraction


frac1 = Fraction(3,5)

frac2 = Fraction(2, 5)

if __name__ == "__main__":
    
    print("Primeira fração:")
    print(frac1.getNum())
    print("-")
    print(frac1.getDen())

    print("Segunda Fração: ")
    print(frac2.getNum())
    print("-")
    print(frac2.getDen())

    print()

    print(frac1 + frac2)
    print(frac1 - frac2)
    print(frac1 * frac2)
    print(frac1 / frac2)


