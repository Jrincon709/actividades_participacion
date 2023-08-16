#Cree una clase Carta que contenga dos propiedades valor y pinta, 
#las cuales son asignadas solo al momento de la construcción del objeto 
#(se pasan como parámetros en el constructor). 
#Defina 4 constantes que representan los nombres de las 4 pintas que puede tener una carta.

class Carta:
    def __init__(self, Valor, Pinta):
        self.Valor = Valor
        self.Pinta = Pinta


    def conseguir_Valor(self):
        return(self.Valor)
    

    def conseguir_Pinta (self):
        return(self.Pinta)
    

diamante = "DIAMANTE"
treboles = "TREBOLES"
picas = "PICAS"
corazones = "CORAZONES"





