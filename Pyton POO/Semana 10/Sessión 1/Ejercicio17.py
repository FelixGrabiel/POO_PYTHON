import math

while True:
    n = int(input("Ingrese un número entero positivo: "))
    if n >= 0 and n<=21:
        break
while True:
    a = float(input("Ingrese el valor entre 0.5 y 2: "))
    if a>=0.5 and a<=2:
        break 
suma = 0
signo = 1
for i in range(1, n + 1):
    termino = signo * (2 * i - 1) * math.pow(a, math.pow(2, i - 1)) / (2 * i)
    suma +=termino
    signo *= -1

print("La suma de los", n, "primeros términos de la serie es:", suma)
