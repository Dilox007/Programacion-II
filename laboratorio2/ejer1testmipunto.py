from ejer1mipunto import MiPunto

# inciso f) crear objetos
p1 = MiPunto()
p2 = MiPunto(10, 30.5)

print("Punto 1:", p1.getX(), p1.getY())
print("Punto 2:", p2.getX(), p2.getY())

# inciso g) calcular distancia
print("Distancia =", p1.distancia(p2))
