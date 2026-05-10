import random
from abc import ABC, abstractmethod
#CLASE ABSTRACTA
class Juego(ABC):
    def __init__(self, vidas):
        self.numeroDeVidas = vidas
        self.record = 0
    def reiniciaPartida(self):
        print("Partida reiniciada")
        self.numeroDeVidas = 3
    def actualizaRecord(self):
        self.record += 1
        print("Record:", self.record)
    def quitaVida(self):
        self.numeroDeVidas -= 1
        print("Te quedan", self.numeroDeVidas, "vidas")
        return self.numeroDeVidas > 0
    
#CLASE PRINCIPAL
class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.numeroAAdivinar = 0
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        print("Adivina un numero entre 0 y 10")
        while True:
            num = int(input("Numero: "))
            if num == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                break
            else:
                if num < self.numeroAAdivinar:
                    print("El numero es MAYOR")
                else:
                    print("El numero es MENOR")
                if not self.quitaVida():
                    print("Perdiste")
                    break
#APLICACION
class Aplicacion:
    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(3)
        juego.juega()
if __name__ == "__main__":
    Aplicacion.main()