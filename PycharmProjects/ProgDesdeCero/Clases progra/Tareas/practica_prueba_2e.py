monto_inicial = float(input("Ingrese monto inicial: "))
n = 0

while monto_inicial >= 0 and n == 0:
    transacción = input("Seleccione el tipo de transacción (D para depósito, P para retiro,"
                        " S para consultar el saldo, E para salir): ")
    if transacción == "D":
        deposito = float(input("Igrese el monto que deseea depositar: "))
        monto_inicial += deposito
    elif transacción == "P":
        retiro = float(input("Igrese el monto que deseea retirar: "))
        if monto_inicial - retiro > 0:
            monto_inicial -= retiro
        else:
            print("No existe dinero suficiente para realizar esta transacción!")
    elif transacción == "S":
        print(f"Su saldo es {monto_inicial}")
    elif transacción == "E":
        n = 1
