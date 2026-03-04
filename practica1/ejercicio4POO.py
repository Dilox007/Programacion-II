# EJERCICIO 4 - ESTADISTICA (POO)
import math

class Estadistica:

    # a) Atributo privado datos.
    def __init__(self, datos):
        self.datos = datos
    # b) Metodo promedio() que obtiene el promedio de los valores.
    def promedio(self):
        suma = 0
        for i in range(len(self.datos)):
            suma = suma + self.datos[i]
        return suma / len(self.datos)
    # c) Metodo desviacion() que devuelve la desviacion estandar.
    def desviacion(self):
        prom = self.promedio()
        suma = 0
        for i in range(len(self.datos)):
            suma = suma + (self.datos[i] - prom) ** 2
        return math.sqrt(suma / (len(self.datos) - 1))


print("Ingrese 10 numeros:")
datos = list(map(float, input().split()))

est = Estadistica(datos)

print("El promedio es: {:.2f}".format(est.promedio()))
print("La desviacion estandar es: {:.5f}".format(est.desviacion()))