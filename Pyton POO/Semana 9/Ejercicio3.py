#Ejercicio 3 unidad 2
"""Carmela, Javier y Eulogio aportan cantidades de dinero para formar 
un capital. Elabore un
programa en Python que permita determinar el capital total formado 
y el porcentaje de dicho
capital que aporta cada uno."""
carmela= float(input("Ingrese el aporte de Carmela: "))
Javier= float(input("Ingrese el aporte de Javier: "))
Eulogio= float(input("Ingrese el aporte de Eulogio: "))

if carmela>0 and Javier>0 and Eulogio > 0:
     capitalTotal= carmela+Javier+Eulogio
     p1=(carmela/capitalTotal)*100
     p2= (Javier/capitalTotal)*100
     p3= (Eulogio/capitalTotal)*100
     print("La capital total es: S/", capitalTotal)
     print("El porcentaje de Carmela es: ", p1)  
     print("El porcentaje de Javier es: ",p2)
     print("El porcentaje de Eulogio es: ",p3)
else:
     print("Error!!!")