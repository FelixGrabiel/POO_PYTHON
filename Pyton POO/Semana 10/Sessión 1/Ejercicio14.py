"""Realizar un programa en PYTHON que solicite 
el ingreso de un número entero positivo
(N) y calcule el factorial de n (n!)."""

while True:
    num = int(input("Ingrese un numero positivo: "))
    if num>0:
        break
factorial=1
for i in range(1,num+1):
    factorial*=i
print("El factorial del número ",num," es : ",factorial)