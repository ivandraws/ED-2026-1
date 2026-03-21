from frac import Fraction



frac1 = Fraction(3, 5)
frac2 = Fraction(2, 5)

if __name__ == "__main__":
    frac3 = Fraction(frac1.num + frac2.num, frac1.den)
    print(frac3)
    print(frac1 + frac2)


