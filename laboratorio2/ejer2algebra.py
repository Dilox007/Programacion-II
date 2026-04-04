class AlgebraVectorial:

    # inciso a) constructor del vector
    def __init__(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    # inciso b) producto escalar
    def producto_escalar(self, v):
        return self.a1*v.a1 + self.a2*v.a2 + self.a3*v.a3

    # inciso c) magnitud del vector
    def magnitud(self):
        return (self.a1**2 + self.a2**2 + self.a3**2) ** 0.5

    # inciso d) verificar si son perpendiculares
    def perpendicular(self, v):
        return self.producto_escalar(v) == 0

    # inciso e) verificar si son paralelos
    def paralela(self, v):
        r1 = self.a1 / v.a1
        r2 = self.a2 / v.a2
        r3 = self.a3 / v.a3
        return r1 == r2 and r2 == r3

    # inciso f) proyección de un vector sobre otro
    def proyeccion(self, v):
        return self.producto_escalar(v) / (v.magnitud()**2)

    # inciso g) componente de un vector sobre otro
    def componente(self, v):
        return self.producto_escalar(v) / v.magnitud()