import random


lista = []
puntaje = 0
lista_p = []
promedio = 0
n = 0

for i in range(0, 1000):
    lista.append(random.randint(1, 7))
for number in lista:

    if number <= 4:
        puntaje = -1
        lista_p.append(puntaje)

    elif number == 5:
        puntaje = 0
        lista_p.append(puntaje)

    elif (number == 6) or (number == 7):
        puntaje = 1
        lista_p.append(puntaje)


for element in lista_p:
    promedio += element
    n += 1

promedio /= n
nps = promedio * 100


print(f"El NPS resultante es {nps}")