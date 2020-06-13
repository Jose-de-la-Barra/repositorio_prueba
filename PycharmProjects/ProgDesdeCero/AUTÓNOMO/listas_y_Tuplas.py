# 1
# lista = ["Matemática", "Física", "Química", "Leguaje", "Historia"]
# print(lista)

############################################################################################################

# 2
# asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# for i in asignaturas:
#    print(f"Yo estudio {i}")

############################################################################################################
# 3
# asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# lista = []
# n = 0
# for asignatura in asignaturas:
#    nota = float(input(f"¿Que nota te has sacado en {asignatura}?\n"))
#    lista.append(nota)
# for i in range(len(asignaturas)):
#    print(f"En {asignaturas[i]} has sacado {lista[i]}")

#####################
# 4
# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva,
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene
# en una lista y los muestre por pantalla ordenados de menor a mayor.

# n_digitos = int(input("Ingrese la cantidad de digitos de la loteria: "))
# lista = []
# for digito in range(n_digitos):
#    n = int(input(f"Ingrese en dígito {digito + 1} de la lotería ganadora: "))
#    lista.append(n)
# lista.sort()
# print(f"Los números ordenados son {lista}")


############################################

# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden
# inverso separados por comas.

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(len(lista)-1, -1, -1):
#    print(lista[i], end=", ")

#######################################
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
# Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado
# en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe
# mostrar por pantalla las asignaturas que el usuario tiene que repetir.


# lista = []
# ramos = int(input("Ingrese la cantidad de ramos: "))
# for i in range(ramos):
#    agregador = input(f"Ingrese el nombre del ramo número {i+1}: ")
#    lista.append(agregador)
# nota = 0
# n = 0
# for elem in range(len(lista)):
#    nota = float(input(f"¿Que nota has sacado en {lista[n]}?\n"))
#    if nota >= 4:
#        lista.remove(lista[n])
#    else:
#        n += 1
# for j in range(len(lista)):
#    print(f"Tienes que repetir {lista[j]}")

#########################################

# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las
# letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

# abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t",
#              "u", "v", "w", "x", "y", "z"]
# m = 3
# n = 1
# while m * n <= len(abecedario) - 1:
#    n = (n * m)
#    abecedario.pop(n-1)
#    m += 2
#    n = 1
# print(abecedario)

###########################

# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

# palabra = input("Ingrese una palabra para contar sus vocales: ")
# vocales = ["a", "e", "i", "o", "u"]
# for vocal in vocales:
#    n = 0
#    for letra in palabra:
#        if letra == vocal:
#            n += 1
#    print(f"La vocal {vocal} aparece {n} veces")


########################

# Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
"""
lista = [50, 75, 46, 22, 80, 65, 8]
mayor = 0
menor = 1000
n = 0
for i in lista:
    while n != 7:
        if (lista[n] < i) and (menor > lista[n]):
            menor = lista[n]
        if (lista[n] > i) and (mayor < lista[n]):
            mayor = lista[n]
        n += 1
print(menor)
print(mayor)

"""



"""

Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) 
en dos listas y muestre por pantalla su producto escalar.

vector_1 = [1, 2, 3]
vector_2 = [-1, 0, 2]
prod_escalar = 0
for i in range(len(vector_1)):
    prod_escalar += vector_1[i] * vector_2[i]
print(prod_escalar)

"""

"""
Escribir un programa que pregunte por una muestra de números, separados 
por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.
"""



# para la media sumar todos los números y dividirlos por la catidad de numeros.
cant_numeros = len(muestra)
media = 0
for i in muestra:
  media += float(i)
media /= cant_numeros
print(media)

# Para la desviación a cada elemento de la lista se le resta la media, se eleva a dos
# y se suma con los otros resultantes y todo esto se divide en len(muestra) y se le saca raíz cuadrada.
elemento = 0
suma = 0
for j in muestra:
  elemento = (float(j) - media) ** 2
  suma += elemento
desviación = (suma / len(muestra)) ** 0.5
print(desviación)

