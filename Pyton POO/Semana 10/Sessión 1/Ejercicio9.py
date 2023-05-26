"""Escriba un programa en PYTHON que permita 
invertir el orden de los dígitos de número
entero positivo.
Ejemplo:
Ingrese N: 1234567
El número invertido es: 7654321"""

numero = int(input("Ingrese un número entero positivo: "))
numero_invertido = 0

while numero > 0:
    digito = numero % 10
    numero_invertido = (numero_invertido * 10) + digito
    numero = numero // 10

print("El número invertido es:", numero_invertido)
