print("Bienvenido al programa de control de COVID\n ------------------")
rut = input("Ingrese RUT en formato 12345678-9: ")

datos = ['Andrea Campos', '17345908-7', 1968, 'Raquel Salinas', '4231998-K', 1940, 'Pedro Meza', '12677800-3', 1975,
         'Sergio Pezoa', '9990234-1', 1965, 'Alvaro Vasquez', '18836902-K', 1970, 'Jaime Oliva', '18837903-K', 1997]
contagiados = ['17345908-7', '12677800-3', '9990234-1', '18836902-K']
permisos = ['18837903-K', '18:30', '18836902-K', '19:15']
n = 0
a = 0

for rut_cont in range(len(contagiados)):

    if rut == contagiados[rut_cont]:
        print(f"{datos[datos.index(rut) - 1]} RUT: {rut} REGISTRA COVID")
        n = 1

if n == 0:
    for b in range(1, len(datos), 3):
        for i in range(0, len(permisos), 2):
            if datos[b] == permisos[i] and rut == datos[b]:
                print(f"{datos[b - 1]} RUT: {rut} tiene permiso tempo2ral hasta las"
                      f" {permisos[i + 1]}")
                n = 1
                break
            else:
                a = "no tiene permiso temporal"

if n == 0:
    for c in range(2, len(datos), 3):
        if 2020 - datos[c] > 75:
            print(f"{datos[c - 2]} es mayor de 75 años y {a}")