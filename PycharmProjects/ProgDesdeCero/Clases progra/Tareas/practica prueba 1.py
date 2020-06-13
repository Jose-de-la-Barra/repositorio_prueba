
# (ENTRADAS)
# Para poder calculas los valores de X e Y en la inecuacuión es necesario
# pedir al usuario los valores de cada una de sus variables

a = float(input("Introduzca el coeficiente a:"))
b = float(input("Introduzca el coeficiente b:"))
c = float(input("Introduzca el coeficiente c:"))
d = float(input("Introduzca el coeficiente d:"))
e = float(input("Introduzca el coeficiente e:"))
f = float(input("Introduzca el coeficiente f:"))

# (PROCESO)

# Antes de procesar los datos en la ecuación se le ordena al computador impripir un mensaje diciendo
# que los datos ingresados no son permitidos dentro de la ecuación
# en el caso de que la división de la ecuacion sea igual a 0, para que el programa no tire un error

if (a*e - b*d == 0 ) :
    print("Con los valores dados no es posible calcular el sistema de ecuaciones lineales.")
# si los datos ingresados son permitidos, estos datos se procesan en la ecuación para crear la variable X e Y

else:
    x = (c * e - b * f) / (a * e - b * d)
    y = (a * f - c * d) / (a * e - b * d)

# (Salida)

# se imprimen los valores de X e Y 

    print(f"X= {x} y Y= {y}")
