# EJERCICIO 3 - ECUACION CUADRATICA
import math
class EcuacionCuadratica:

    # a) Los atributos privados a, b y c.
    def __init__(self, a, b, c):

        # b) Constructor que recibe los argumentos a, b y c.
        self.a = a
        self.b = b
        self.c = c

    # c) Metodo getDiscriminante() que devuelve b^2 - 4ac.
    def getDiscriminante(self):
        return self.b * self.b - 4 * self.a * self.c

    # d) Metodo getRaiz1() que retorna la primera raiz.
    def getRaiz1(self):
        if self.getDiscriminante() < 0:
            return 0
        return (-self.b + math.sqrt(self.getDiscriminante())) / (2 * self.a)

    # d) Metodo getRaiz2() que retorna la segunda raiz.
    def getRaiz2(self):
        if self.getDiscriminante() < 0:
            return 0
        return (-self.b - math.sqrt(self.getDiscriminante())) / (2 * self.a)
    
print("Ingrese a b c:")
a, b, c = map(float, input().split())

ecuacion = EcuacionCuadratica(a, b, c)
d = ecuacion.getDiscriminante()

if d > 0:
    print("La ecuacion tiene dos raices:{:.6f}".format( ecuacion.getRaiz1()), "y{:.5f}".format( ecuacion.getRaiz2()))
elif d == 0:
    print("La ecuacion tiene una raiz:", ecuacion.getRaiz1())
else:
    print("La ecuacion no tiene raices reales")