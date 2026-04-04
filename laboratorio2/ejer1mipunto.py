class MiPunto:

    # inciso a) constructor con valores por defecto
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    # inciso b) obtener coordenada X
    def getX(self):
        return self.__x

    # inciso c) obtener coordenada Y
    def getY(self):
        return self.__y

    # inciso d) calcular distancia entre dos puntos
    def distancia(self, p):
        dx = self.__x - p.__x
        dy = self.__y - p.__y
        return (dx**2 + dy**2) ** 0.5

    # inciso e) distancia entre el punto y coordenadas (x,y)
    def distanciaXY(self, x, y):
        dx = self.__x - x
        dy = self.__y - y
        return (dx**2 + dy**2) ** 0.5