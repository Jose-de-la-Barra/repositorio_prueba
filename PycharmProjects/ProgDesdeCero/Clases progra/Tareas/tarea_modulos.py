import random


numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letras = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z"
letras = letras.split(" ")
contraseña = []

# “d” dígitos (con un mínimo de 3 y un máximo de 5) y por “c” caracteres (con un mínimo de 5 y un máximo de 10).

d = random.randint(3, 5)
c = random.randint(5, 10)


for i in range(d):
    contraseña.append(random.choice(numeros))
for j in range(c):
    contraseña.append(random.choice(letras))

random.shuffle(contraseña)

for a in contraseña:
    print(a, end="")


