# guía 2

# Escribe un algoritmo que resuelva el siguiente problema: mostrar por pantalla las primeras 4 potencias de 2.
# Resuelve este problema usando ciclo While.

#numero = 2
#potencia = 1
#for i in range(potencia):
#    while potencia <= 3:
#        print(numero ** potencia)
#        potencia += 1


##########

#Escribe un algoritmo que resuelva el siguiente problema: desplegar por pantalla todos los números enteros que existen
# entre los números A y B (ambos inclusive) que ingresa el usuario. Nota que si A es menor que B, se despliegan los
# números en orden creciente. Pero si A es mayor que B, los números se despliegan en orden decreciente. A continuación


#numero_1 = int(input("Ingrese el primer número: "))
#numero_2 = int(input("Ingrese el segundo número: "))

#while numero_1 != numero_2:
#    if numero_1 > numero_2:
#        print(numero_1)
#        numero_1 -= 1
#    else:
#        print(numero_2)
#        numero_2 -= 1
#print(numero_1)



###########

# Escribe un algoritmo en Python que emule la solicitud de clave en una cajero automático:
# si el usuario equivoca la clave 3 veces consecutivas, el cajero muestra el mensaje “Tarjeta retenida”,
# se “traga” la tarjeta (esta última acción no la puedes emular en Python ya que la instrucción “Tragar tarjeta”
# no existe) y termina la ejecución del algoritmo. Si el usuario logra ingresar la clave válida en uno de los 3
# primeros intentos, entonces aparece el mensaje “Bienvenido al servicio”. Supón que la clave válida se encuentra
# almacenada en una variable.

#clave = input("Guarde clave: ")
#n = 0
#while n < 3:
#    clave_guardada = input("ingrese clave: ")
#    if clave_guardada != clave:
#        n +=1
#        print(f"Clave Incorrecta, intento número {n} gastado")
#    if clave_guardada == clave:
#        print("Clave correcta")
#        break


##################

# Escribe un algoritmo en Python que solicite números enteros al usuario, y vaya calculando la suma de todos ellos.
# La solicitud de números al usuario termina cuando se ingresa un -1, en cuyo caso se muestra por pantalla el
# resultado de la suma. Está permitido que el usuario ingrese como primer valor un -1, en cuyo caso el algoritmo
# termina inmediatamente,

#n = 0
#suma = 0
#while n == False:
#    numero = int(input("Ingrese un número: "))
#    if numero == -1:
#        n = 1
#    else:
#        suma += numero
#else:
#    print(suma)


###########

# Escribe el código que permite resolver la siguiente serie: 1!+ 2! + 3! + ...+ N!. El valor de N se solicita al usuario.

n = int(input("Escriba un número: "))
fact = 1
for i in range(n, -1, -2):
    while i > 0:
        fact = fact * (i * (i-1))
    break
print(fact)


########

# numbers = int(input("Ingrese el número de elementos que desea ingresar: "))

# elements = int(input("Ingrese el número de elmentos: "))
# list_1 = []

# for i in range(elements):
#    print(f"Ingrese el elemento número {i + 1}")
#    number = int(input())
#    list_1.append(number)
# menor = list_1[0]
# for j in list_1:
#    if(j < menor):
#        menor = j
# else:
#    print(f"El menor número de la lista es {j}")



























