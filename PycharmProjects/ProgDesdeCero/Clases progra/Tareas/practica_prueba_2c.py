import random


"""
def matriz(f, c, n):
    mat = []
    for i in range(f):
        a = [n] * c
        mat.append(a)
    return mat


print(matriz(3, 5, 8))
"""

"""
lista = []
cont = 0
num_repet = []


for a in range(0,50):
    lista.append(random.randrange(0, 10))


for j in lista:
    if j not in num_repet:
        cont = 0
        for a in lista:
            if j == a:
                cont += 1
        print(f"El número {j} apareció {cont} veces")
        num_repet.append(j)
"""


lista = []

for i in range(0, 50):
    lista.append(random.randrange(1, 10))

lista_rep = []

for number in range(len(lista)):
    if lista[number] not in lista_rep:
        contador = 0

        for number_2 in range(len(lista)):
            if (lista[number] == lista[number_2]) and (number != number_2):
                contador += 1

        print(f"El número {lista[number]} se repitio {contador} veces")
        lista_rep.append(lista[number])
