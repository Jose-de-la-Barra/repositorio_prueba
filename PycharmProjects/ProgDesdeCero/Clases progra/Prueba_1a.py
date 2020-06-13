# preguntar al usuario por el largo y ancho de cada una de las piezas (ENTRADAS)

largo_cocina = float(input("Ingrese el largo de la cocina en metros: "))
ancho_cocina = float(input("Ingrese el ancho de la cocina en metros: "))
largo_baño = float(input("Ingrese el largo del baño en metros: "))
ancho_baño = float(input("Ingrese el ancho del baño en metros:  "))
largo_pieza = float(input("Ingrese el largo de la pieza en metros: "))
ancho_pieza = float(input("Ingrese el ancho de la pieza en metros: "))
largo_espacioabierto = float(input("Ingrese el largo del espacio abierto en metros: "))
ancho_espacioabierto = float(input("Ingrese el ancho del espacio abierto en metros: "))

# (PROCESO)

cocina = largo_cocina * ancho_cocina
baño = largo_baño * ancho_baño
pieza = largo_pieza * ancho_pieza
espacio_abierto = largo_espacioabierto * ancho_espacioabierto

metros_cuadrados_totales = cocina + baño + pieza + espacio_abierto

# (SALIDA)

print(f"Los metros cuandrados totales de la casa son: {metros_cuadrados_totales}")





