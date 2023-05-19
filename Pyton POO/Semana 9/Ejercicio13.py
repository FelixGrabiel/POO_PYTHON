numero= int(input("Ingrese un número de tres cifras: "))

if numero>=100 and numero<1000:
   c = numero//100
   queda = numero%100
   d= queda//10
   u= numero%10
   if c==u:
       print("El número: ", numero, " es capicua")
   else: 
       print("El numero no es capicua")
else:
    print("El numero debe ser de tres cifras!!")
