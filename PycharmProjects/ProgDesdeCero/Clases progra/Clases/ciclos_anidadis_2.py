import time
"""
ciclo externo (se ejecuta n veces)
    ciclo interno (se ejecuta F(n) veces)
"""
"""
for i in range(0, 5):
    for j in range(0, i):
        print(i, ",", j)
"""
"""
i toma el valor de 0
se entra al ciclo interno
siendo i = 0, no se ingresa al ciclo interno
se vuelve al ciclo externo
i = 1
se entra al ciclo interno
siendo i = 1, j toma el valor 0
se impirime 1, 0
se vuelve al ciclo externo
i = 2
se entra al ciclo interno
siendo i = 2, j = 0, se imprime (2, 0)
vuelve a ejecutarse en ciclo interno
siendo i = 2, j = 1, se imprime (2, 1)
...

ruteo es escribir lo que aparece en pantalla
"""


"""
# 2

alto = int(input("Alto: "))
ancho = int(input("Ancho: "))
for i in range(1, alto + 1):
    for j in range(1, alto + 1):
        print("#", end="")
    print()
"""
"""
alto = n
ancho = a

#       #       #       #       a veces hacia 
#       #       #       #       # la derecha
#       #       #       #       #
#       #       #       #       #
n veces
hacia abajo
"""

# 3

"""
alto = int(input("Ingrese el alto: "))
n = 0

for i in range(alto):
    n += 1

    for j in range(n):
        print('#', end='')

    print()

"""


#4
#a = 0
#p = time.time()

#while a < 180:
#    time.sleep(1)
#    t = time.time()
#    cont = round(t-p)

#    if t - p > 60:
#        b = round(cont / 60)
#        print(f"{b}: {abs(cont - 60 * round(cont / 60))}")
#    else:
#        print(f"{cont}")
#    a += 0



"""
limit = 3
for i in range(limit):
    for j in range(0, 60):
        print(f'{i}: {j}')
print(f'{limit}: 00')

"""
