
asignaturas = ["Progra", "Calculo", "Algebra"]
promedio_asignaturas = []
for j in range(len(asignaturas)):
    lista = []
    numero_notas = int(input(f"Ingrese el número de notas de {asignaturas[j]}: "))
    for i in range(0, numero_notas):
        nota = int(input(f"Ingrese la nota numero {i+1} de {asignaturas[j]}: "))
        lista.append(nota)
    suma = 0
    for a in lista:
        suma = a + suma
    promedio_asignaturas.append(suma/len(lista))
sumador = 0
for s in range(0, len(asignaturas)):
    print(f"Tu promedio en {asignaturas[s]} es {promedio_asignaturas[s]}")
    sumador += promedio_asignaturas[s]
print(f"Su promedio de las notas es {sumador / len(asignaturas)}")







