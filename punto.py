import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def cuadrante(self):
        x, y = self.x, self.y
        if x == 0 and y == 0:
            return "Origen"
        if x == 0:
            return "Eje Y"
        if y == 0:
            return "Eje X"
        if x > 0 and y > 0:
            return "Primer cuadrante"
        if x < 0 and y > 0:
            return "Segundo cuadrante"
        if x < 0 and y < 0:
            return "Tercer cuadrante"
        if x > 0 and y < 0:
            return "Cuarto cuadrante"
        return "Desconocido"

    def vector(self, otro):
        return Punto(otro.x - self.x, otro.y - self.y)

    def distancia(self, otro):
        dx = otro.x - self.x
        dy = otro.y - self.y
        dist = math.sqrt(dx * dx + dy * dy)
        print(f"Distancia entre {self} y {otro}: {dist}")
        return dist


class Rectangulo:
    def __init__(self, inicial=None, final=None):

        self.inicial = inicial if inicial is not None else Punto()
        self.final = final if final is not None else Punto()

    def base(self):
        b = abs(self.final.x - self.inicial.x)
        print(f"Base del rectángulo (|x2 - x1|)/ {b}")
        return b

    def altura(self):
        h = abs(self.final.y - self.inicial.y)
        print(f"Altura del rectángulo (|y2 - y1|)/ {h}")
        return h

    def area(self):
        a = self.base() * self.altura()
        print(f"Área del rectángulo: {a}")
        return a


if __name__ == "__main__":
    A = Punto(2, 3)
    B = Punto(5, 5)
    C = Punto(-3, -1)
    D = Punto(0, 0)

    print("Puntos:")
    print("A =", A)
    print("B =", B)
    print("C =", C)
    print("D =", D)
    print()

    print("Cuadrantes:")
    print("A ->", A.cuadrante())
    print("C ->", C.cuadrante())
    print("D ->", D.cuadrante())
    print()

    print("Vectores:")
    AB = A.vector(B)
    BA = B.vector(A)
    print("Vector AB =", AB)
    print("Vector BA =", BA)
    print()

    print("Distancias:")
    A.distancia(B)
    B.distancia(A)
    print()


    distancias_origen = {
        'A': A.distancia(D),
        'B': B.distancia(D),
        'C': C.distancia(D)
    }
    mas_lejos = max(distancias_origen, key=distancias_origen.get)
    print(f"El punto más lejano del origen entre A, B y C es: {mas_lejos}")
    print()

    rect = Rectangulo(A, B)
    print("Rectángulo formado por A y B:")
    rect.base()
    rect.altura()
    rect.area()