import math 
class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distancia(self, otro_punto):
        return math.sqrt((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2)

    def __str__(self):
        return f"Punto({self.x}, {self.y})"