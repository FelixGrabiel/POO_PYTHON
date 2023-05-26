import math

while True:
    n = int(input("Ingrese un número entero positivo: "))
    if n > 0:
        break

suma = 0
for i in range(1, n + 1):
    factorial = math.factorial(i)
    potencia = n + 1
    termino = math.pow(i, potencia) / factorial
    suma += termino
    
print("La suma de los", n, "primeros términos de la serie es:", suma)
