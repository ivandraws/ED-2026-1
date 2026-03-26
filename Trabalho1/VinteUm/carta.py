class Carta:
    def __init__(self,numero,tipo_carta):
        self.numero = numero
        self.naipe = tipo_carta
    def __str__(self):
        if self.numero == 11:
            return "Valete" +" de "+ str(self.naipe)
        elif self.numero == 12:
            return "Rainha" +" de "+ str(self.naipe)
        elif self.numero == 13:
            return "Rei" +" de "+ str(self.naipe)
        elif self.numero == 1:
            return "Ás" +" de "+ str(self.naipe)
        else:
            return str(self.numero) +" de "+ str(self.naipe)    
