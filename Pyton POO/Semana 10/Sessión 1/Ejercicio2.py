num = int(input("Ingrese la cantidad de numeros: "))
suma =0
for i in range(num+1):
    if i%2!=0:
        suma+=i
print("La suma es: ",suma)