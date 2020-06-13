# permiten compartir código con otros
# son independientes de nuestro programa
# pueden recibir cero o más variables

"""
def suma(n1, n2):
    return print(n1 + n2)


suma(2, 4)


def hola_mundo(nombre):
    print('hola', nombre, 'desde la función')


nombre_usuarios = input('nombre: ')

hola_mundo(nombre_usuarios)
"""


def num_primo(num):

    for i in range(2, num, 1):
        if num % i == 0:
            print("NO primo")
            return
    print("SI primo")
    return


num_primo(7)


def repetir_texto(texto, num_veces):

    for i in range(num_veces):
        print(texto)


texto_a_ingresar = 'hola'
veces = 5

repetir_texto(texto_a_ingresar, 5)