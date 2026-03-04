# EJERCICIO 1 - CRONOMETRO
import time
import random

class Cronometro:
    # a) Los atributos privados inicia y finaliza con metodos getter.
    def __init__(self): 
        # b) Constructor sin argumentos que inicializa inicia con la hora actual.
        self._inicia = time.time() * 1000
        self._finaliza = 0
    # c) Metodo inicia() que restablece inicia a la hora actual.
    def inicia(self):
        self._inicia = time.time() * 1000
    # d) Metodo detener() que establece finaliza a la hora actual.
    def detener(self):
        self._finaliza = time.time() * 1000
    # e) Metodo lapsoDeTiempo() que retorna el tiempo transcurrido en milisegundos.
    def lapsoDeTiempo(self):
        return self._finaliza - self._inicia

    def getInicia(self):
        return self._inicia
    
    def getFinaliza(self):
        return self._finaliza

def ordenamiento_seleccion(lista):
    for i in range(len(lista)):
        minimo = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[minimo]:
                minimo = j
        temp = lista[i]
        lista[i] = lista[minimo]
        lista[minimo] = temp

lista = []
for i in range(10000):
    lista.append(random.randint(1, 100000))

c = Cronometro()
c.inicia()
ordenamiento_seleccion(lista)
c.detener()

print("Tiempo en milisegundos:{:.3f}".format(c.lapsoDeTiempo()))