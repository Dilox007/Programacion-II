import random
from abc import ABC, abstractmethod
# CLASE ABSTRACTA
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
#CLASE BASE
class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.numeroAAdivinar = 0
    def validaNumero(self, num):
        return 0 <= num <= 10
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        print("Adivina un numero")
        while True:
            num = int(input("Numero: "))
            if not self.validaNumero(num):
                print("Numero invalido")
                continue
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
# CLASE PAR
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, num):
        if 0 <= num <= 10 and num % 2 == 0:
            return True
        if num % 2 != 0:
            print("Error: el numero debe ser PAR")
        return False
#CLASE IMPAR
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, num):
        if 0 <= num <= 10 and num % 2 != 0:
            return True
        if num % 2 == 0:
            print("Error: el numero debe ser IMPAR")
        return False
#APLICACION
class Aplicacion:
    @staticmethod
    def main():
        print("=== Juego Normal ===")
        juego1 = JuegoAdivinaNumero(3)
        juego1.juega()
        
        print("\n=== Juego PAR ===")
        juego2 = JuegoAdivinaPar(3)
        juego2.juega()
        
        print("\n=== Juego IMPAR ===")
        juego3 = JuegoAdivinaImpar(3)
        juego3.juega()
if __name__ == "__main__":
    Aplicacion.main()