# 1 pechuga de pollo
# 6 leches semidescremadas sin lactosa
# 1/2 kilo de tomates
# 4 yogur de frambuesa
# 2 paquetes de fideos espirales
# 3 paquetes de salsa de tomates natural

# (ENTRADAS)

pechuga_de_pollo = int(input("Dime el precio de una pechuga de pollo: "))
leches = int(input("Dime el precio de la leche semidescremada sin lactosa: "))
tomate = int(input("Dime el precio de 1 kilo de tomate: "))
yogur = int(input("Dime el precio de 1 yogur de frambuesa: "))
fideos = int(input("Dime el precio del paquetes de fideos espirales: "))
salsa_tomate = int(input("Dime el precio de la salsas de tomates natural: "))

# (PROCESO)

leches = (leches * 6)
tomate = (tomate * 0.5)
yogur = (yogur * 4)
fideos = (fideos * 2)
salsa_tomate = (salsa_tomate * 3)

costo_total = leches + tomate + yogur + fideos + salsa_tomate + pechuga_de_pollo

vuelto = (20000 - costo_total)

# (Salida)

print(f"El vuelto es de {vuelto}")

