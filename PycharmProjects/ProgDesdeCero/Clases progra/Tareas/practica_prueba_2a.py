"""
ejercicio 4: convertir nombre en nickname cambiando sus vocales por números y las demas letras haciendolas mayúsculas.
"""

import random


name = input(("Ingrese su nombre en minùsculas: "))
name_1 = []


for i in name:
    name_1.append(i)


for letra in range(len(name_1)):

    if (name_1[letra] == "a") or (name_1[letra] == "e") or (name_1[letra] == "i") or (name_1[letra] == "o") or (name_1[letra] == "u"):
        numero = random.randrange(1, 10)
        name_1.pop(letra)
        name_1.insert(letra, numero)
    else:
        name_1[letra] = name_1[letra].upper()


for element in name_1:
    print(element, end="")
