# EJERCICIO 2 - ECUACION LINEAL 2x2
class EcuacionLineal:
    # a) Los atributos privados a, b, c, d, e y f.
    def __init__(self, a, b, c, d, e, f):

        # b) Constructor que recibe los argumentos a, b, c, d, e y f.
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
    # c) Metodo tieneSolucion() que devuelve True si ad - bc no es cero.
    def tieneSolucion(self):
        return (self.a * self.d - self.b * self.c) != 0
    # d) Metodo getX() que retorna la solucion de x.
    def getX(self):
        return (self.e * self.d - self.b * self.f) / (self.a * self.d - self.b * self.c)
    # d) Metodo getY() que retorna la solucion de y.
    def getY(self):
        return (self.a * self.f - self.e * self.c) / (self.a * self.d - self.b * self.c)

print("Ingrese a b c d e f:")
a, b, c, d, e, f = map(float, input().split())

ecuacion = EcuacionLineal(a, b, c, d, e, f)

if ecuacion.tieneSolucion():
    print("x =", ecuacion.getX(), "y =", ecuacion.getY())
else:
    print("La ecuacion no tiene solucion")