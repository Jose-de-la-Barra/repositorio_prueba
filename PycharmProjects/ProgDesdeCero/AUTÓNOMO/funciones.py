import math

# def saludo():
#    print('¡Hola Amiga!')
#    return
# saludo()

###################

"""
Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.

def saludo(nombre):
    print(f'¡Hola {nombre}!')
    return
nombre_1 = input("Escribe tu nombre: ")
saludo(nombre_1)
"""

"""
# Escribir una función que reciba un número entero positivo y devuelva su factorial

def factorial(numero):
    fact = 1
    for i in range(numero):
        fact *= (i + 1)
    return fact
entero = int(input("Escriba un número entero positivo: "))
print(f"El factorial de {entero} es {factorial(entero)}")

"""

"""
Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir 
la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la 
función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.


factura = float(input('Total de la factura sin IVA: '))
porcentaje = float(input('Porcentaje de IVA: '))
def iva():
    if porcentaje != 0:
        factura_con_IVA = ( (porcentaje/100)*factura ) + factura
        return factura_con_IVA
    else:
        factura_con_IVA = (0.21 * factura) + factura
        return factura_con_IVA
print(f"La factura sin iva es {factura}")
print(f"La factura con iva es {iva()}")

Otra manera de hacerlo:
def invoice(amount, vat=21):
    return amount + amount*vat/100
print(invoice(1000,10))
print(invoice(1000))
"""

"""
# Escribir una función que calcule el área de un círculo y otra que calcule
# el volumen de un cilindro usando la primera función.
radius = 5
altura = 8


def area_circ(radius):
    area = math.pi * (math.pow(radius, 2))
    return area


def vol_cili(high, radius):
    return math.pi * (math.pow(radius, 2)) * high


print(area_circ(radius))
print(vol_cili(altura, radius)
      
      
"""

"""
# Escribir una función que reciba una muestra de números en una lista y devuelva su media.


muestra = input("Introduce una muestra de números separados por comas: ")
muestra = muestra.split(",")


def media(suma=0):
    for i in muestra:
        suma += float(i)
    return suma / len(muestra)
print(media())
"""

"""
# Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.


numeros = input("Introduzca los numeros separados por comas: ")
numeros = numeros.split(",")

def cuadrados():
    lista = []
    for i in numeros:
        lista.append(math.pow(float(i), 2))
    return lista


print(cuadrados())
"""

"""
# Escribir una función que reciba una muestra de números en una lista y devuelva
# un diccionario con su media, varianza y desviación típica.


datos = input("Esriba los datos: ")
datos = datos.split(",")


def estadistics():
    suma = 0
    suma_2 = 0
    stat = {}
    for i in datos:
        suma += float(i)
        stat['media'] = suma/len(datos)
    for j in datos:
        suma_2 += math.pow(float(j) - (suma/len(datos)), 2)
        stat['varianza'] = suma_2/len(datos)
        stat['desviación típica'] = math.sqrt(suma_2/len(datos))
    return stat


print(estadistics())

"""

# Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.


def mcm(n_1, n_2):
    n = 1
    while (n <= n_2) and (n <= n_1):
        n += 1
        if (n_1 % n == 0) and (n_2 % n == 0):
            return n


# print(mcm(49, 3829))


def mcd(n_1, n_2):

    while (n_1 % 2 == 0) or (n_2 % 1 == 0):

        cont_1 = 0
        cont_2 = 0

        if (n_1 % 2 == 0):
            cont_1 += 1
            n_1 = n_1 / 2

        if (n_2 % 2 == 0):
            cont_2 += 1
            n_2 = n_2 / 2

print(mcd(8, 16))
# def mcd():
range