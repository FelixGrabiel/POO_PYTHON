import math
num = int(input("Ingrese N: "))
suma = 0
signo = 1
for i in range(num):
    termino = 1/(math.pow(2, i)) *signo
    suma=suma+termino
    signo*=-1
print("El resultado es: ",suma)