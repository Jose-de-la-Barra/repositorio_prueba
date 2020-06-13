#for i in ["Hola", "Chao", "Buenos dias"]:
#    print(i, end=" ")


# Imprime la palabra hola tantas veces como caracteres tenga lo escrito despues de for i in
#for i in "jose.delabarra2@gmail.com":
#    print("Hola", end=" ")



#evaluar si un correo es correcto segùn si tiene o no una @ y un punto
#for i in hace que la variable i tome todos los valores de que nosotros introducimos una y otra vez

#contador = False
#mi_email = input("Ingrese su correo: ")

#for i in mi_email:

#    if(i == "@" or i == ".") :

#        contador = contador + 1

#if contador >= 2:
#    print("email correcto")
#else:
#    print("email incorrecto")




#
# 1

#palabra = input("Escribe algo: ")

#for i in range(10):
#    print(palabra)



# 2

#years = int(input("¿cuantos años tienes?\n"))

#for i in range(years):
#    print(f"has cumplido {i + 1} años")



# 3

#numero = int(input("Escriba un número entero positivo: "))
#for i in range(1, numero+1, 2):
#    print(i, end=", ")
#número = int(input("introduce un  número: "))
#for i in range(1, número + 1, 2):
#    print(i, end=", ")



# 4

#número = int(input("introduce un  número: "))

#for i in range(número, -1, -1):
#    print(i, end =", ")




# 5

#amount = float(input("¿Cantidad a invertir? "))
#interest = float(input("¿Interés porcentual anual? "))
#years = int(input("¿Años? "))

#for i in range(years):
#    amount *= 1+interest/100
#    print(f"Capital tras {i+1} años: {round(amount, 2)}")


# 6

#alto = int(input("Escriba un número: "))

#for i in range(alto+1):
#    for a in range(i):
#        print("*", end="")
#    print("")



# 7


numero1 = int(input("Ingrese un número entero positivo: "))

for i in range(numero1+1):
    for j in range(i):
        print("*", end="")
    print("")



