# Aprovechamiento de programas hechos anteriormente por otras personas.
# import llama a módulos (los módulos más básicos bienen por defecto en python)

############################

# Import <nombreMódulo>
# nombre.Módulo.nombre.Función(<parámetros>)

############################

# Módulos comunes:

# math: operaciones matemáticas
# random: generar números aleatorios
# matplotlib: Para graficar
# numpy y pandas para alálisis de datos

############################

# Dir(módilo) para que muestre las funciónes de el módulo
# help(módulo) para explicar un determinado módulo

############################

# math.factorial(x): retoma el factorial de x
# math.pow(x, y): retoma x elevado a y

############################

# sumatoria desde k = 0 hasta numIlter de Z elevado a K dividido en K factorial

#import math
#z = int(input("ingrese un número: "))
#numIter = int(input("Ingrese número de iteraciones: "))
#suma = 0
#for k in range(0, numIter+1):
#  suma = suma + ((math.pow(z, k) / (math.factorial(k))

#print(f"El valor de la sumatoria es {suma}")


############################

# Import time

# time.sleep(x): el proprama se pausa por x segundos
# time.time( ): devuelve el númer de segundos

# Import ramdom


############################

# Random.randint(x, y) retorna un número aleatorioentero entre x e y

import random
import time

n1 = random.randint(1, 10)
n2 = random.randint(1, 10)
# mult = 0
# mult = int(input(f"Ingrese el resultado de la multiplicación entre {n1} y {n2}: "))
# if mult == n1*n2:
#  print("Correcto")
# else:
#  print("Intente nuevamente")
mult = 0
mult = int(input(f"Ingrese el resultado de la multiplicación entre {n1} y {n2}: "))
i = 0
segundos = 1
while mult != 0:

    time.sleep(segundos)
    i += 1
    if mult != 0:
        print("Respondiste")
        break


