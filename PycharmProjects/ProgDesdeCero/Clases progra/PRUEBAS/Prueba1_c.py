# (ENTRADAS) Se ingresan la cantidad de artículos comprados. Estos se se transforman en números enteros y
# son guardados en distintas variables

cartas = int(input("Ingrese la cantidad de Cartas Dos comprados: "))
dibujanary = int(input("Ingrese la cantidad de Dibujanary comprados: "))
duopoly = int(input("ngrese la cantidad de Duopoly comprados: ​"))
ajedrez = int(input("Ingrese la cantidad de Ajedrez comprados: ​"))
naipe_Español = int(input("Ingrese la cantidad de Naipe Español comprados:"))
guerra_Mundial = int(input("Ingrese la cantidad de Guerra Mundial comprados: "))

# (PROCESO) se analiza cual es el precio a pagar en cada caso
# teniendo en cuenta que cada 50 gramos se tiene que pagar 100 pesos

if cartas > 0:
    cartas = (cartas * 2000) + ((cartas * 50)/50)
if dibujanary > 0:
    dibujanary = (dibujanary * 10000) + ((dibujanary * 320)/50)*100
if duopoly > 0:
    duopoly = (duopoly * 12500) + ((duopoly * 250)/50)*100
if ajedrez > 0:
    ajedrez = (ajedrez * 4000) + ((ajedrez * 400)/50)*100
if naipe_Español > 0:
    naipe_Español = (naipe_Español * 1000) + ((naipe_Español * 75)/50)*100
if guerra_Mundial > 0:
    guerra_Mundial = (guerra_Mundial * 8700) + ((guerra_Mundial * 450)/50)*100

# Se calcula el precio total sumando todos los precios anteriores

precio_total = cartas + dibujanary + duopoly + ajedrez + naipe_Español + guerra_Mundial

# se imprime en pantalla el precio total

print(f"El costo total a pagar es de {precio_total}")

