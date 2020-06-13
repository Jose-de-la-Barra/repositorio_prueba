numero = int(input("Ingese el número al cual le quiere calcular su raíz cuadrada: "))
y = 1
n = 1
cuociente_1 = 0
promedio = 0
diferencia = 1
lista = []
while diferencia > 0.0001:
    cuociente_1 = numero/y
    y = (y + cuociente_1) / 2
    diferencia = y - (numero ** (1/2))
    lista.append(y)
    print(f"El valor aproximado {n} fue {lista[n-1]}")
    n += 1
print(f"El valor de diferencia final es {round(diferencia, 1)} y se alcanzó en la iteración {n-1}")