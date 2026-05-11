# SISTEMA DE BIBLIOTECA UNIVERSITARIA
# ENTIDADES PRINCIPALES
# INCISO a)
class Biblioteca:

    class Horario:
        def __init__(self, dias, hora_apertura, hora_cierre):
            self.dias = dias
            self.hora_apertura = hora_apertura
            self.hora_cierre = hora_cierre
        def mostrar_horario(self):
            print(f"Horario: {self.dias} de {self.hora_apertura} a {self.hora_cierre}")
    def __init__(self, nombre, dias, apertura, cierre):
        self.nombre = nombre

        self.libros = []
        self.autores = []
        self.prestamos = []

        self.horario = Biblioteca.Horario(
            dias,
            apertura,
            cierre
        )

    def agregar_libro(self, libro):
        self.libros.append(libro)
    def agregar_autor(self, autor):
        self.autores.append(autor)
    def prestar_libro(self, estudiante, libro):
        prestamo = Prestamo(estudiante, libro)
        self.prestamos.append(prestamo)
    def mostrar_estado(self):

        print(f"\n=== Biblioteca: {self.nombre} ===")
        self.horario.mostrar_horario()
        print("\nLibros:")
        for l in self.libros:
            print("-", l.titulo)
        print("\nAutores:")
        for a in self.autores:
            a.mostrar_info()
        print("\nPrestamos:")
        for p in self.prestamos:
            p.mostrar_info()
    def cerrar_biblioteca(self):
        print("\nLa biblioteca esta cerrada.")
        self.prestamos.clear()
# ENTIDADES PRINCIPALES
# INCISO b)
class Libro:
    class Pagina:
        def __init__(self, numero, contenido):

            self.numero = numero
            self.contenido = contenido

        def mostrar_pagina(self):

            print(f"Pagina {self.numero}: {self.contenido}")
    def __init__(self, titulo, isbn, contenidos):

        self.titulo = titulo
        self.isbn = isbn

        self.paginas = []

        for i, texto in enumerate(contenidos):

            self.paginas.append(
                Libro.Pagina(i + 1, texto)
            )
    def leer(self):

        for p in self.paginas:

            p.mostrar_pagina()
# ENTIDADES PRINCIPALES
# INCISO c)
class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
    def mostrar_info(self):
        print(f"Autor: {self.nombre} ({self.nacionalidad})")
# ENTIDADES PRINCIPALES
# INCISO d)
class Estudiante:
    def __init__(self, codigo, nombre):

        self.codigo = codigo
        self.nombre = nombre
    def mostrar_info(self):
        print(f"Estudiante: {self.nombre} - Codigo: {self.codigo}")
# ENTIDADES PRINCIPALES
# INCISO e)
class Prestamo:
    def __init__(self, estudiante, libro):
        self.estudiante = estudiante
        self.libro = libro

        self.fecha_prestamo = "05/05/2026"
        self.fecha_devolucion = "12/05/2026"
    def mostrar_info(self):
        print(f"Prestamo: {self.libro.titulo}")
        self.estudiante.mostrar_info()
        print(f"Desde: {self.fecha_prestamo} hasta: {self.fecha_devolucion}")
# PRUEBA DEL PROGRAMA
b = Biblioteca(
    "UMSA",
    "Lunes a Viernes",
    "08:00",
    "18:00"
)
a1 = Autor(
    "Andrew S. Tanenbaum",
    "Estados Unidos"
)
a2 = Autor(
    "Herbert Schildt",
    "Estados Unidos"
)
b.agregar_autor(a1)
b.agregar_autor(a2)
l1 = Libro(
    "Redes de Computadoras",
    "INF-121",
    [
        "Introduccion a redes",
        "Modelo OSI",
        "Protocolos de comunicacion"
    ]
)
l2 = Libro(
    "Python Programacion",
    "INF-222",
    [
        "Variables y tipos de datos",
        "Estructuras de control"
    ]
)
b.agregar_libro(l1)
b.agregar_libro(l2)

e1 = Estudiante(
    "2025",
    "Dilan Thomas Chura Cala"
)
b.prestar_libro(
    e1,
    l1
)
b.mostrar_estado()
print("\nLeyendo libro:")
l1.leer()
b.cerrar_biblioteca()