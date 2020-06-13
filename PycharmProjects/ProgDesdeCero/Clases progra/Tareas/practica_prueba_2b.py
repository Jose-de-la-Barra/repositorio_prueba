"""
Agregar 10 números a una lista pero si se llega a repetir uno en el proceso,
mostrar mensaje de advertencia diciendo que no se pueden repetir
"""

lista = []
n = 0


while n < 10:
    n += 1
    numero = int(input(f"Ingrese el {n}º número que desee agregar a la lista: "))
    lista.append(numero)
    lista.sort()

    if len(lista) > 1:
        for i in range(len(lista)):
            if i < len(lista):
                if lista[i-1] == lista[i]:
                    print("Número repetido, por favor ingrese otro distinto")
                    lista.remove(lista[i])
                    n -= 1


print(lista)
