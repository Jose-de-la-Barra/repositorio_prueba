# ENTRADAS
# se le pide 3 números al usuario y estos son convertidos en números enteros y almacenados
# en variables distintas

print("Ingrese 3 Números: ")
numero1 = int(input())
numero2 = int(input())
numero3 = int(input())

# PROCESO y SALIDA
# se verifica si uno de ellos es producto o no de la suma de los otros dos y de ser asi,
# se muestra el mensaje correspondiente en pantalla

if numero1 == (numero2 + numero3):
    print(f"El número {numero1} es igual a {numero2} + {numero3}")
elif numero2 == (numero1 + numero3):
    print(f"El número {numero2} es igual a {numero1} + {numero3}")
elif numero3 == (numero2 + numero1):
    print(f"El número {numero3} es igual a {numero2} + {numero1}")

# Si no se cumple que uno de ellos es producto de la suma de los otros
# dos se imprime en pantalla el mensaje correspondiente
else:
    print("No se cumple lo buscado")