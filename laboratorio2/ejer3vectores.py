class Vector3D:

    # inciso a) constructor del vector
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # inciso b) suma de vectores
    def __add__(self, v):
        return Vector3D(
            self.x + v.x,
            self.y + v.y,
            self.z + v.z
        )

    # inciso c) multiplicación por escalar
    def escalar(self, r):
        return Vector3D(
            r*self.x,
            r*self.y,
            r*self.z
        )

    # inciso d) longitud del vector
    def longitud(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

    # inciso e) vector normal
    def normal(self):
        m = self.longitud()
        return Vector3D(
            self.x/m,
            self.y/m,
            self.z/m
        )

    # inciso f) producto escalar
    def producto_escalar(self, v):
        return self.x*v.x + self.y*v.y + self.z*v.z

    # inciso g) producto vectorial
    def producto_vectorial(self, v):
        i = self.y*v.z - self.z*v.y
        j = self.z*v.x - self.x*v.z
        k = self.x*v.y - self.y*v.x
        return Vector3D(i, j, k)

    # inciso h) mostrar vector
    def __str__(self):
        return f"({self.x},{self.y},{self.z})"