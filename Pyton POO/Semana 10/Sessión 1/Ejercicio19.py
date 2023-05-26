while True:
    N = int(input("Ingrese un número entero positivo (menor que 10): "))
    if N > 0 and N < 10:
        break
caracter = input("Ingrese un carácter: ")
for i in range(N, 0, -1):
    print(caracter * i)