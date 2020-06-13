
texto = len(input("Escribe algo:\n"))

if(texto == 0) :
    print("Escriba algo")
elif(texto <= 280) :
    print("OK")
else:
    print("Texto muy largo")