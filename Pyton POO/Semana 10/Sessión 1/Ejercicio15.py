while True:
    n = int(input("Ingrese un número entero positivo: "))
    if n>0:
        break
suma = 0
signo = 1
factorial = 1
for i in range(1, n + 1):
    factorial *=i
    signo *= -1
    termino = signo * i / factorial
    suma += round(termino,1) 
print("La suma de los", n, "primeros términos de la serie es:", suma)
