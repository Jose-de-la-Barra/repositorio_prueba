# En el caso de que el puente funcione escriba 1 en caso contrario 0

p1 = bool(input("Estado de p1: "))
p2 = bool(input("Estado de p2: "))
p3 = bool(input("Estado de p3: "))
p4 = bool(input("Estado de p4: "))
p5 = bool(input("Estado de p5: "))
p6 = bool(input("Estado de p6: "))
p7 = bool(input("Estado de p7: "))

if( ((p1 and p4) or (p2) or (p3 and p5)) and (p6 or p7) ) :
    print("Es posible llegar desde A a B")
else:
    print("No es posible llegar desde A a B")