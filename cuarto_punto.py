#Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que definen sus esquinas.
# Agregue métodos a la clase Rectángulo para calcular su perímetro, calcular su área e indicar si el rectángulo es un cuadrado.
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangulo:
    def __init__(self, Primer_punto, Segundo_punto):
        self.Primer_punto = Primer_punto
        self.Segundo_punto = Segundo_punto
    
    #Calcular perimetro

    def Calcular_Perimetro (self):
        Altura = abs(self.Segundo_punto.y - self.Primer_punto.y)
        Base = abs (self.Segundo_punto.x - self.Segundo_punto.x)
        Perimetro = 2 * (Altura + Base )
        return Perimetro
    
    #Calcular su area
    def Calcular_Area (self):
        Altura = abs(self.Segundo_punto.y - self.Primer_punto.y)
        Base = abs (self.Segundo_punto.x - self.Primer_punto.x)
        Area = Altura * Base
        return Area
    
    # determinar si es cuadrado
    def Calcular_sies_cuadrado (self):
        Altura = abs(self.Segundo_punto.y - self.Primer_punto.y)
        Base = abs (self.Segundo_punto.x - self.Segundo_punto.x)
        return Base == Altura
    
Primer_punto = Punto(3,4)
Segundo_punto = Punto(11,8)

rectangulo = Rectangulo(Primer_punto, Segundo_punto)

calcular_area = rectangulo.Calcular_Area()
print( f"El area es {calcular_area}")

perimetro = rectangulo.Calcular_Perimetro()
print( f"El perimetro es {perimetro}")

cuadrado = rectangulo.Calcular_sies_cuadrado()
print( f" Es un cuadrado {cuadrado}")

        