# digite el año:
print("Digite el año: ")

# capture el año
año = int(input())

# si año es multiplo de 4 y año no es multiplo de 100 o el año es multiplo de 400 : SI
if(año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
    print("Año bisiesto")
# y si no : NO
else:
    print("Año NO bisiesto")




