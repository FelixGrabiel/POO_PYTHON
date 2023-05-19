import math

num= int(input("Ingrese un número entero positivo de tres cifas: "))

if num>=100 and num<1000:
   c = num//100
   queda = num%100
   d= queda//10
   u= num%10
   print("Número inverso es: ",u,d,c)
if num>1000:
      print("-1")
if num<100:
      print("-1")