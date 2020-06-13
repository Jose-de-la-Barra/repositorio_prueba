import time

print(dir(time))  # funciones de time
print(time.time())  # tiempo en segundos desde el 1 de enero de 1970

# apl¡cación de time.time
inicio = time.time()

while True:
    print("Estamos jugando")
    final = time.time()

    if final - inicio >= 5:  # hacemos que el programa dure 5 segundos
        break
print("Fin del juego")
print(f"tienpo del juego = {final - inicio}")


"""
print(random.choice(["+", "*"]))
>>> imprime (+) o (*)
"""
