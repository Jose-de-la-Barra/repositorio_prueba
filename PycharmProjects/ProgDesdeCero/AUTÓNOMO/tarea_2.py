number = int(input("Escriba un número: "))
while number != 1:
    if number % 2 == 0:
        print(int(number), end=" ")
        number /= 2
    else:
        print(int(number), end=" ")
        number = (number * 3) + 1
print(int(number), end=" ")