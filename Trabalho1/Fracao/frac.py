#função que retorna o máximo divisor comum entre a e b
def mdc(a,b):
    if a > b: 
        a, b = b, a
    
    while True: 
        r = a%b
        if r == 0: 
            return b
        else: 
            a = b
            b = r


class Fraction: 
    def __init__(self, numer, denom):
        self.num = numer
        self.den = denom

#método que muda o que o objeto fração mostra
    def __str__(self):
        return str(int(self.num)) + "/" + str(int(self.den)) 
    
#método para tornar a fração irredutível
    def reduc(self):
        res = mdc(self.num, self.den)
        self.num = int(self.num / res)
        self.den = int(self.den / res)
        return

#método de adição
    def __add__(self, other):
        n = self.num * other.den + self.den * other.num
        d = self.den * other.den
        self.num = n
        self.den = d
        self.reduc()
        return str(self.num) + "/" + str(self.den)

#Método de subtração
    def __sub__(self, other):
        n = self.num * other.den - self.den * other.num
        d = self.den * other.den
        self.num = n
        self.den = d

        self.reduc()
        return str(self.num) + "/" + str(self.den)

#Método de multiplicação
    def __mul__(self, other):
        self.num *= other.num
        self.den *= other.den

        self.reduc()

        return str(self.num) + "/" + str(self.den)

#Método de divisão 
    def __truediv__(self, other):
        self.num *= other.den
        self.den *= other.num

        self.reduc()

        return str(self.num) + "/" + str(self.den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

# Função de teste de mdc. TODO, remove later
def main():

    #criação de duas frações para teste
    n, d = map(int, input("insira o numerador e o denominador: ").split())
    frac = Fraction(n, d)
    x, y = map(int, input("insira o numerador e o denominador 2: ").split())
    frac2 = Fraction(x, y)
    
    frac.__truediv__(frac2)
    print(frac)
    
    return
if __name__ == "__main__":
    main()