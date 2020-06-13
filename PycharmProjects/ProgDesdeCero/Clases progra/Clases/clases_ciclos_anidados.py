"""
 Un ciclo dentro de otro (un ejemplo sería el reloj con el minutero y el otro indicador)

 es mejor fijarce en el ciclo interno primero
 ciclo a = m
 coclo b = n

 cantidad de ciclos con ciclo a y b (independientes) anidados: m por n
"""

"""
i = 1
while i < 5:
    j = 1
    while j < 5:
        print(i, ",", j)  # 4 * 4 = 16
        j = j + 1
    i = i + 1

"""

# dependencia de ciclo interno con el externo
"""
i = 1
while i < 5:
    j = 1
    while j <= i // 2 + 1:
        print(f"{i} , {j}")
        j = j + 1
    i = i + 1

# el j en este caso depende del i
"""

"""
M = [[17, 2, 8], [4, 6, 7], [8, 43, 6]]

fila = 17, 2, 8

"""


buscar = int(input('Ingrese el número a buscar: '))

M = [[17, 2, 8], [4, 6, 7], [8, 43, 6]]
for i in range(len(M)):
    fila = M[i]

    for j in range(len(fila)):
        if fila[j] == buscar:
            print(f"{i}, {j}")
