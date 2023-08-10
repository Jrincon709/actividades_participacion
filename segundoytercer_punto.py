#Cree una clase Punto que represente un punto en el plano cartesiano.

class Punto:
    def __init__(self, x , y):
        self.x = x
        self.y = y


#A la clase del punto anterior, defínale los siguientes métodos:
# Un método mostrar que imprima por consola las coordenadas del punto
    def imprimir_coordenadas (self):
        A=(self.x,self.y)
        print ("La coordenada es " ,A)
# Un método mover que cambie las coordenadas del punto
    def mover_x(self, dx ):
        self.x = self.x + dx
        print (self.x , self.y)
    def mover_y(self, dy):
        self.y = self.y + dy
        print (self.x , self.y)
# Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto
    def calcular_distancia (self, otro_punto):
        dx = self.x - otro_punto.x
        dy = self.y - otro_punto.y
        return ( dx ** 2 +dy  **2 )** 0.5

