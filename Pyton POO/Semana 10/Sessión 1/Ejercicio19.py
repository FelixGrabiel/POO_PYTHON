while True:
    n= int(input("Ingrese un número entero positivo (menor que 10): "))
    if n > 0 and n < 10:
        break
caracter = input("Ingrese un carácter: ")
for i in range(n, 0, -1):
    print(caracter * i)