"""
PRUEBA ES HASTA MÓDULOS
(LISTAS, CICLOS, MÓDULOS, ETC.)

descargar import requests

"""
"""
import math


datos = [4, 1, 11, 13, 2, 7]


def d_est():
    suma = 0
    varianza = 0

    for i in datos:
        suma += float(i)
    media = suma / len(datos)

    for j in datos:
        varianza += (math.pow((float(j) - media), 2)) / len(datos)

    return math.sqrt(varianza)


print(d_est())
"""
"""
ramdom.choise(lista, número de carácteres a elegir aleatoriamente)
"""


