# EJERCICIO 4 - ESTADISTICA
# PROGRAMACION MODULAR - ESTRUCTURADA
import math
# a) promedio() obtiene el promedio de los valores en punto flotante
def promedio(lista):
    suma = 0
    for i in range(len(lista)):
        suma = suma + lista[i]
    return suma / len(lista)
# b) desviacion() devuelve la desviacion estandar de los valores
def desviacion(lista):
    prom = promedio(lista)
    suma = 0
    for i in range(len(lista)):
        suma = suma + (lista[i] - prom) ** 2
    return math.sqrt(suma / (len(lista) - 1))

print("Ingrese 10 numeros:")
valores = input()
datos = list(map(float, valores.split()))

print("El promedio es: {:.2f}".format(promedio(datos)))
print("La desviacion estandar es: {:.5f}".format(desviacion(datos)))