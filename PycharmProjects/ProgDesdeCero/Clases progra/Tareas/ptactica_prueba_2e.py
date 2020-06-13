"""
100 elementos random
imprimir el mayor
inprimir el menor
imprimir pares
"""

import random

lista = []
lista_pares = []
lista_mayor = []
lista_menor = []
mayor = 0
menor = 0

for i in range(100):
    lista.append(random.randrange(0, 101))

for element in lista:

    if element % 2 == 0:
        lista_pares.append(element)

    for element_2 in lista:

        if element < element_2 and mayor < element_2:
            mayor = element_2

        if ((element > element_2) and (menor > element_2)) or (menor == 0):
            menor = element_2

print(lista)
print(lista_pares)
print(mayor)
print(menor)
