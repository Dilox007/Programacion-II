from ejer3vectores import Vector3D

# inciso i) crear vectores
v1 = Vector3D(1,2,3)
v2 = Vector3D(4,5,6)

print("Vector 1 =", v1)
print("Vector 2 =", v2)
print("Suma =", v1 + v2)
print("Longitud v1 =", v1.longitud())
print("Producto escalar =", v1.producto_escalar(v2))
print("Producto vectorial =", v1.producto_vectorial(v2))