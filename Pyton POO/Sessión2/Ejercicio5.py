num = int(input("Ingrese un número entero positivo de 4 dígitos:"))
cont = 0
if num>=1000 and num<=9999:
    d1= num//1000
    queda= num%1000
    d2= queda//100
    queda1= num%100
    d3= queda1//10
    d4= num%10
    suma = d1+d2+d3+d4
    print("La suma de los digitos es: ",suma)
    if d1==d4 and d2==d3: 
         print("Numero es capicua")
    else:
        print("El número no es capicua")
    if d1 == 2 or d1 == 3 or d1 == 5 or d1 == 7:
        cont += 1
    if d2 == 2 or d2 == 3 or d2 == 5 or d2 == 7:
         cont += 1
    if d3 == 2 or d3 == 3 or d3 == 5 or d3 == 7:
         cont += 1
    if d4 == 2 or d4 == 3 or d4 == 5 or d4 == 7:
         cont += 1        
    print("La cantidad de dígitos primos es:", cont)

else:
    print("Error, el número ingrese no es posivo y de 4 digitos")
