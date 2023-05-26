numero = int(input("Ingrese un número entero positivo: "))
suma_divisores = 0
for i in range(1, numero):
    if numero % i == 0:
        suma_divisores += i
    
if suma_divisores == numero:
    print("es un número perfecto.")
else:
    print("no es un número perfecto.")
