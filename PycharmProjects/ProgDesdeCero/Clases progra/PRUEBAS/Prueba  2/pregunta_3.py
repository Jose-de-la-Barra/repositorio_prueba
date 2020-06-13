import random


caras = int(input("Ingrese el número de caras a obtener: "))
lista = []
par = 0
impar = 0


while par < caras:
    a = random.randrange(1, 100)

    if a % 2 == 0:
        par += 1

    else:
        impar += 1


print(f"Obtuve {par} caras de {par + impar} lanzamientos. Eso equivale a un {(par / (impar + par)) * 100}%")


"""
Cuando el número es mayor, la probabilodad se acerca más al 50% de caras y 50% de sellos

número de caras             prueba 1              prueba 2               prueba 3       

10                          22 lanzamientos       19 lanzamientos        19 lanzamientos 
                            45,45%                52,63%                 52.63%   

100                         191 lanzamientos      200 lanzamientos       186 lanzamientos
                            52.35%                50.0%                  53.76%
                            
1000                        2068 lanzamientos     1993 lanzamientos      1945 lanzamientos
                            48.35%                50.17%                 51.41%
"""
