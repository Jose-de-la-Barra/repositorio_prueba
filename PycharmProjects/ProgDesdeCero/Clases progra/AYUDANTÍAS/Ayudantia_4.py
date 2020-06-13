######## PHYTON

#var = "foobar"
#for i in var:
#    print(i, end=" ")


##############

#var = [[1, 2, 3], ["a", "b"], [45, 3]]
#print(var[1][1])

# imprime en la losta uero 1 (segunda), el elemento número 1 (segundo elemento)

############

# append = agrega elemntos al final de la lista
# pop = eliminar elementos de una lista


#lista = [1, 3, 5, 7, 9]
#print(list[2:])
#print(list[:2])
#print(list[1: 3])
#print(list[2: 3])

###########

#lista = [1, 3, 9]
#print(lista)
#lista[2:2] = ["palabra", 5, 7]
#print(lista)

# agrrgar elementos en posiciones específicas

##########

# las listas funcionan hacia los dos lados

#lis =[1, 3, 9]

#print(lis[-2])

# lista = [1, 4, 6, 8, 10]
#          0  1  2  3  4
#        -5 -4  -3 -2 -1


#################

#pal = "murcielago"

#for i in range(len(pal)-1, -1, -1):
#    print(pal[i])

##################

n = 5
for i in range(n):
    for j in range(i):
        print("*", end=" ")
    print("")
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print("")

