# Escribe un programa en Python que determine si una fecha (se ingresa día, mes y año) ocurre antes o después que otra.

print("Escriba la primera fecha: \n")
dia1, mes1, año1 = int(input("Ingrese un dia: ")), int(input("Ingrese un mes: ")), int(input("Ingrese un año: "))
print()
print("Escriba la seguna fecha: \n")
dia2, mes2, año2 = int(input("Ingrese otro dia: ")), int(input("Ingrese otro mes: ")), int(input("Ingrese otro año: "))

if (año1 > año2) or (mes1 > mes2 and año1 == año2) or (dia1 > dia2 and mes1 == mes2):
    print(f"La fecha {dia1}/{mes1}/{año1} ocurre despues que la fecha {dia2}/{mes2}/{año2}")
elif(año1 < año2) or (mes1 < mes2 and año1 == año2) or (dia1 < dia2 and mes1 == mes2):
    print(f"La fecha {dia2}/{mes2}/{año2} ocurre despues que la fecha {dia1}/{mes1}/{año1}")
else:
    print(f"La fecha {dia2}/{mes2}/{año2} y la fecha {dia1}/{mes1}/{año1} son iguales")








