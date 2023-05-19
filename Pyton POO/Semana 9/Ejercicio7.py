"""Elabore un programa en Python que calcule y muestre el menor número de monedas de 5, 2 y
1 para desglosar una cantidad K, de Soles.
Por ejemplo, si K fuese 37 entonces la cantidad de monedas de 5 sería 7, de 2 sería 1 y de 1
sería 0"""

monedas= int(input("Ingrese la cantidad: "))

if monedas>0:
    m5= monedas//5 
    resto = monedas%5
    m2= resto//2
    m1= resto%2
    print("Mondeas de 5 soles: ", m5)
    print("Monedas de 2 soles: ",m2)
    print("Monedas de 1 sol: ",m1)
else:
    print("Error!!!")