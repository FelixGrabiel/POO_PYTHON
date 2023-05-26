import math
num = int(input("Ingrese N: "))
suma = 0
for i in range(num):
    termino = 1/(math.pow(2, i)) 
    suma=suma+termino
print("El resultado es: ",suma)