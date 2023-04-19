"""
- Crear la función decorador adecuadamente que sumará los elementos de la
función que pasará como parámetro de la función decoradora
"""

import time

def tiempoEjecucion(funcion):
    def decorador(*args, **kwargs):
        start = time.time()
        resultado = funcion(*args, **kwargs)
        end = time.time()
        print("La función {} tardó {} segundos en ejecutarse.".format(funcion.__name__, end - start))
        return resultado
    return decorador


"""
Crear una función, por ejemplo, multiplicación de 4 números para decorarla
con la función anterior.
"""
@tiempoEjecucion


def multiplicar(p, q, x, y):
    resultado = p*q*x*y
    print("El resultado es: {}".format(resultado))
    return resultado


multiplicar(9, 10, -5, 4)

@tiempoEjecucion

def sumar(a, b, x):
    resultado = a + b + x
    print("El resultado es: {}".format(resultado))
    return resultado

sumar(12, 10, 2)

@tiempoEjecucion
def restar(a, b):
    resultado = a - b
    print("El resultado es: {}".format(resultado))
    return resultado
restar(25, 15)
