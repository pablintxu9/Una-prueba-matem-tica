import math 
class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distancia(self, otro_punto):
        return math.sqrt((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2)

    def __str__(self):
        return f"Punto({self.x}, {self.y})"
    
class rectangulo:
    def __init__(self, punto_inferior_izquierdo, punto_superior_derecho):
        self.punto_inferior_izquierdo = punto_inferior_izquierdo
        self.punto_superior_derecho = punto_superior_derecho

    def area(self):
        ancho = self.punto_superior_derecho.x - self.punto_inferior_izquierdo.x
        alto = self.punto_superior_derecho.y - self.punto_inferior_izquierdo.y
        return ancho * alto

    def __str__(self):
        return f"Rectangulo({self.punto_inferior_izquierdo}, {self.punto_superior_derecho})"