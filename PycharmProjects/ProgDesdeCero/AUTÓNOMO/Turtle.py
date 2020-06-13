import turtle
import time

posponer = 0.1

# Configuración de la ventana
wn = turtle.Screen()
wn.title("Juego")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# cabeza serpiente
cabeza = turtle.Turtle()
# Para que empieze queto
cabeza.speed(0)
#forma de cuadrado
cabeza.shape("square")
cabeza.color("white")
#quitar rastro
cabeza.penup()

cabeza.goto(0, 0)
cabeza.direction = "up"

#Funciones
def mov():
    # Para que se vaya hacia arriba hay que modificar el eje y y lo mismo con las demas direcciones
    if cabeza == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
while True:
    # actualización de la pantalla
    wn.update()
    mov()
    time.sleep(posponer)





