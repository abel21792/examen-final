"""
1. Escribir un programa para el manejo de listas el cuál cumplirá los siguientes
requerimientos (4 ptos):
"""
"""
- Crear una función que le permitirá almacenar 10 número aleatorios en una
  lista y finalmente los imprimirá por consola al llamar la función.
"""

# Creacion de la funcion


def almacenar():
    aleatorios = [30, 1, 4, 4, 9, 11, 13, 13, 30, 0, 10]
    print("Estos nos los números aleatorios: {}".format(aleatorios))


# Imprime por consola


almacenar()


"""
Crear una función que le permita almacenar los números no repetidos de la
lista anterior, retornar este valor e imprimirlo por consola.
"""


def noreplica():
    aleatorios = [30, 1, 4, 4, 9, 11, 13, 13, 15, 0, 10]
    aleatorios.pop(2)
    aleatorios.pop(2)
    aleatorios.pop(5)
    aleatorios.pop(5)
    aleatorio2 = aleatorios
    print("Los números que no se repiten son: {}".format(aleatorio2))


noreplica()

"""
Crear una función donde se creará una lista para ordenar de mayor a menor
la lista que se creó en el ítem anterior (número no repetidos) y otra lista
para ordenarlas de menor a mayor, retornar este valor e imprimirlos por
consola.
"""

def menor():
    aleatorios = [30, 1, 4, 4, 9, 11, 13, 13, 15, 0, 10]
    aleatorios.pop(2)
    aleatorios.pop(2)
    aleatorios.pop(5)
    aleatorios.pop(5)
    aleatorio3 = sorted(aleatorios)
    print("Ordenado de menor a mayor: {}".format(aleatorio3))


def mayor():
    aleatorios = [30, 1, 4, 4, 9, 11, 13, 13, 15, 0, 10]
    aleatorios.pop(2)
    aleatorios.pop(2)
    aleatorios.pop(5)
    aleatorios.pop(5)
    aleatorio3 = sorted(aleatorios)
    aleatorio3.reverse()
    print("Ordenado de mayor a menor: {}".format(aleatorio3))


mayor()
menor()

"""
Crear una función para indicar cuál es mayor número de la lista (lista del
ítem 2), retornar este valor e imprimirlo por consola.
"""


def mayorTodos():
    aleatorios = [30, 1, 4, 4, 9, 11, 13, 13, 15, 0, 10]
    aleatorios.pop(2)
    aleatorios.pop(2)
    aleatorios.pop(5)
    aleatorios.pop(5)
    aleatorio2 = aleatorios
    print("El número mayor de la lista es: {}".format(max(aleatorios)))


mayorTodos()
