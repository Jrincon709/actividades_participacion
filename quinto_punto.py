#Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con parámetros en el constructor.
import math
class Punto:
    def __init__(self, x , y):
        self.x = x
        self.y = y

class Circulo:
    def __init__(self,centro,radio):
        self.centro = centro
        self.radio = radio
# Defina métodos en la clase para calcular el área    
    def Calcular_Area(self):
        area = math.pi * self.radio ** 2
        return area
    #Calcular Perimetro
    def Calcular_perimetro (self):
        perimetro = 2 * math.pi * self.radio 
        return perimetro
    #indicar si un punto pertenece al círculo o no.
    def Pertenece_punto (self,otro_punto):
        Distancia = math.sqrt((otro_punto.x  - self.centro.x)**2 + (otro_punto.y - self.centro.y)**2)
        return Distancia <= self.radio


centro = Punto(2,3)
radio = 8
P1 = Punto(2,4)
circulo = Circulo(centro,radio)
Pertenece = circulo.Pertenece_punto(P1)
print( f"¿El punto pertenece al circulo? {Pertenece}")

Calcular_area = circulo.Calcular_Area()
print( f"El area es {Calcular_area}")

