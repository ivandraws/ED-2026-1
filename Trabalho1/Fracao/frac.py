# Definição da Classe Fraction
class Fraction:
    
    # Inicializado com numerador e denominador
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
    
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    
    # Método de adição
    def __add__(self, f2):
        if self.den == f2.den:
            return str(self.num + f2.num) + "/" + str(self.den)
        else:
            return str((self.num * f2.den) + (f2.num * self.den)) + "/" + str(self.den * f2.den)
    
    # Método de subtração
    def __sub__(self, f2):
        if self.den == f2.den:
            return str(self.num - f2.num) + "/" + str(self.den)
        else:
            return str((self.num * f2.den) - (f2.num * self.den)) + "/" + str(self.den * f2.den)
    # Método de multiplicação
    def __mul__(self, f2):
        return str(self.num * f2.num) + "/" + str(self.den * f2.den)
    
    # Método de divisão
    def __truediv__(self, f2):
        return str(self.num * f2.den) + "/" + str(self.den * f2.num)
        #return Fraction(self.num * f2.den, self.den * f2.num)