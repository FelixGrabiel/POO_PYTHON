zona = int(input("Ingrese zona (1 - Comercial, 2 - Residencial): "))
consumo = int(input("Ingrese consumo: "))

if zona == 1:
    tarifa_fija = 50
    if consumo <= 100:
        monto_a_pagar = tarifa_fija + consumo * 0.75
        print("El monto a pagar es: ",monto_a_pagar)
    else:
        monto_a_pagar = tarifa_fija + 100 * 0.75 + (consumo - 100) * 0.9
        print("El monto a pagar es: ",monto_a_pagar)
if zona == 2:
    tarifa_fija = 25
    if consumo <= 100:
        monto_a_pagar = tarifa_fija + consumo * 0.30
        print("El monto a pagar es: ",monto_a_pagar)
    else:
        monto_a_pagar = tarifa_fija + 100 * 0.30 + (consumo - 100) * 0.7
        print("El monto a pagar es: ",monto_a_pagar)

if zona!=1 and zona!=2 and consumo>0:
    print("Zona inválida. Por favor, ingrese 1 para Zona Comercial o 2 para Zona Residencial y consumo positivo.")
