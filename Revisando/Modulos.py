import math

PI = math.pi

def dobrar_lista(lista):
    return [x*2 for x in lista]

def mutiplicar(lista):
    r = 1
    for i in lista:
        r *= i
    return r