class Carta:
    def __init__(self,numero,tipo_carta):
        self.numero = numero
        self.carta = tipo_carta
    def __str__(self):
        return str(self.numero) +"de"+str(self.carta)
    
