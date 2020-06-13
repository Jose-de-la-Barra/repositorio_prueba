
ancho = int(input("Ingrese ancho: "))
alto = int(input("Ingrese alto: "))
for i in range(alto):
    if (i == 0) or (i == alto-1):
        print("#" * ancho)
    else:
        if i % 2 == 0:
            if ancho % 2 == 0:
                print(" #" * int((ancho)/2))
            else:
                print(" #" * int((ancho) / 2))
        else:
            if ancho % 2 != 0:
                print("# " * int((ancho + 1)/2))
            else:
                print("# " * int((ancho + 1) / 2))


