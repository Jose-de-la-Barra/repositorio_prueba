minimo = int(input("Escriba el mínimo: "))
maximo = int(input("escriba el máximo: "))
n = 1

while n:
    numero = int(input("Ingrese un número: "))

    if (numero > minimo) and (numero < maximo):
        if numero % 2 != 0:
            print("Numero impar!!")
        else:
            n += 1

    else:
        print(f"El número de númreos ingresados fue de {n-1}")
        n = 0
