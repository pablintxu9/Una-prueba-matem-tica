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
        # caso por seguridad (no suele alcanzarse)
        return "Desconocido"