# Ejercicio 9
# A usted lo contratan para que programe una máquina que cobra en los estacionamientos de un mall.
# Cree un programa que reciba las horas y minutos dadas por el usuario y retorne el valor que éste debe pagar.
# Debe considerar lo siguiente:
# 1.-Los primeros 30 minutos son gratis.
# 2.-Si está entre los 31 minutos y una hora se calculará el precio con 28 pesos el minuto.
# 3.-Sobre una hora el valor de cada minuto es de 15 pesos.

# horas = int(input("Intrudizca la cantidad de horas que uso el estacionamiento: "))
# minutos = int(input("Intrudizca la cantidad de minutos que uso el estacionamiento: "))

# horas_minutos = (28 * 30) + (minutos * 15) + ((horas*60) * 15)

#if (minutos <= 30) and (horas == 0):
#    print("No tienes que pagar por el estacionamiento")
#elif minutos >= 31 and minutos < 60 and horas == 0:
#    precio1 = ((minutos-30) * 28)
#    print(f"Tienes que pagar {precio1} pesos")
#elif (horas == 1) and(minutos == 0):
#    precio1 = 28*30
#    print(f"Tienes que pagar {precio1} pesos")
#else:
#    print(f"Tienes que pagar {(horas_minutos)} pesos")


#################################
# (ENTRADAS) se le piden las notas de las pruebas a el usuario y estas se convierten en un número decimal para
# luego almacenaras en variabes
# nota1 = float(input(" Ingrese la nota de la prueba 1: "))
# nota2 = float(input(" Ingrese la nota de la prueba 2: "))
# nota3 = float(input(" Ingrese la nota de la prueba 3: "))

# (PROCESO) para discriminar cuaes son las dos notas mas altas de las 3 entregadas se crean una serie de
# instrucciones con sus respectivas respuestas (SALIDAS) en cada caso.

# if (nota1 < nota2 and nota1 < nota3) or (nota2 == nota3 and nota2 > nota1):
#    print(f"Considerando solo sus dos mejores notas ({nota2}/{nota3}) su promedio es {(nota2 + nota3) / 2}")
#elif (nota2 < nota1 and nota2 < nota3) or (nota1 == nota3 and nota1 > nota1):
#    print(f"Considerando solo sus dos mejores notas ({nota1}/{nota3}) su promedio es {(nota1 + nota3) / 2}")
#elif (nota3 < nota1 and nota3 < nota2) or (nota1 == nota2 and nota2 > nota1):
#    print(f"Considerando solo sus dos mejores notas ({nota1}/{nota2}) su promedio es {(nota1 + nota2) / 2}")
#elif nota1 == nota2 == nota3:
#    print(f"Su promedio es {nota1}")
#else:
#    print("ERROR")

################################


#Una compañía de rent a car cobra un valor de $30.000 hasta un máximo de 250 km de distancia recorrida.
#Para más de 250 km y hasta 750km, cobra los $30.000 de base más un monto adicional de $ 150 por cada kilómetro
# recorrido en exceso por sobre los 250. Para más de 750 km cobra los $30.000 de base más el tramo de 250 a 750
# cobrando $150 por km recorrido, y por sobre los 750 cobra un adicional de $ 100 por cada kilómetro en exceso sobre
# 750 km. Diseñe un programa que determine el monto a pagar por el arriendo de un vehículo. Se ingresará por teclado
# los km de la distancia recorrida y deberá entregar el monto total a pagar. Como se ve en la siguiente imagen.

#km = int(input("Ingrese los kilomtros recorridos: "))

#cobro = 30000 + ((km - 250)*150)

#if km <= 250:
#    print("Tiene que pagar 30000")
#elif (km > 250) and (km <= 750):
#    print(f"Tiene que pagar {cobro}")
#elif (km > 750):
#    cobro = 30000 + 500*150 + ((km - 750) * 100)
#    print(f"{cobro}")

