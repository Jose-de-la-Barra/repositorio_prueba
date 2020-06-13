import random
"""
Palabras ocultas
Una forma de transmitir mensajes de forma segura es dividiéndolo en la mitad y transmitir cada parte por separado.
Supón que recibes dos listas, cada una con la mitad de cada palabra. Por ejemplo:
lista_1 = ['M', 'nom', 'e', 'Miste']
lista_2 = ['i', 'bre', 's', 'rio']
Escribe el código en Python que pregunte las dos listas y genere el mensaje. En el ejemplo, debería mostrar Mi nombre es Misterio

"""
"""
lista_1 = input("Escriba la lista 1 seperada por comas: ")
lista_2 = input("Escriba la lista 2 separada por comas: ")
lista_1 = lista_1.split(', ')
lista_2 = lista_2.split(', ')


for i in range(len(lista_1)):
    print(lista_1[i] + lista_2[i], end=" ")
"""

"""
Escribe un programa en Python que genere una lista de 10 números al azar entre 1 y 100, copie esta lista a otra, 
PERO donde UN elemento AL AZAR dentro de la lista se cambia por su negativo (multiplica por -1). 
Ejemplo: si se genera la lista [1,2,3,4,5,6,7,8,9,0] y se selecciona el tercer elementos, debemos imprimir [1,2-3,4,5,6,7,8,9,0]
"""


"""
lista = []
for i in range(0, 10):
    lista.append(random.randrange(1, 100))
print(lista)

a = random.choice(lista)
b = lista.index(a)
lista.remove(a)
print(lista)

lista.insert(b, -a)
print(lista)
"""

