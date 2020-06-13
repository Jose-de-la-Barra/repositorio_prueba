# while = mientras

#n = 0

#while (n < 10):
#    print(f"El número es {n}\n")
#    n += 1

#print("Ciclo terminado")
#print(n)


###########

# N terminos de la serie de fobonacci

# 0 1 1 2 3 5 8 13

n = int(input("Dame el número de elementos qe quieres evaluar: "))

i = 0
prim = 0
seg = 1
elem = 0

while (i < n):
    if (n == 1):
        print("0")
        elem = prim
    elif(n == 2):
        print(1)
        elem = seg
    else:
        elem = prim + seg
        prim = seg
        prim = elem
    i = i + 1

print(elem)

