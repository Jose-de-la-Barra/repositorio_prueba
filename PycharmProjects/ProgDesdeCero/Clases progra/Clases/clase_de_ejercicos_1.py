# primero hay que pedir cada uno de los número del rut, sin su número verficador y guardarlos en una variable.
lista_rut = []
for i in range(8):
    rut = int(input(f"Ingrese el dígito número {i+1} de su rut: "))
    lista_rut.append(rut)
# recorrer cada elemento de la lista desde adelanta hacia atras y cada número multilicarlo con n
n = [2, 3, 4, 5, 6, 7]
contador = 0
mult = 0
for j in range(len(lista_rut)-1, -1, -1):
    mult = mult + (lista_rut[j] * n[contador])
    contador += 1
    if (contador == 6):
        contador = 0
mult = mult % 11
resultado = 11 - mult
print(f"Su código verificador es {resultado}")



