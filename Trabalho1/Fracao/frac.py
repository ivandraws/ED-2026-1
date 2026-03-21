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
            return str("TODO: Calculo de adição com DEN diferente")
    # Método de subtração
    def __sub__(self, f2):
        if self.den == f2.den:
            if self < f2:
                # Caso do NUM de f2 ser maior que NUM de self
                return "-" + str(self.num - f2.num) + "/" + str(self.den)
        else:
            return str("TODO: Calculo de adição com DEN diferente")
        
    # Método de multiplicação
    def __mul__(self, f2):
        return str(self.num * f2.num) + "/" + str(self.den * f2.den)
    # Método de divisão inteira
    def __truediv__(self, f2):
        
        return str(self.num * f2.den) + "/" + str(self.den * f2.num)
    