mayor = None
menor = None
cont=0
contNeg=0
contPos=0
suma = 0
while True:
    num= int(input("Ingrese un numero: "))
    if num==0:
        break
    cont+=1
    if num>0:
        contPos+=1
    else:
        contNeg+=1
    suma+=num
    if mayor is None:
         mayor = num
         menor = num
    else:
        if num>mayor:
            mayor=num
        if num<menor:
            menor=num
promedio = suma/cont
print("Numeros leidos: ",cont)
print("Numero mayor: ",mayor)
print("Numero menor: ",menor)
print("Numeros positivos: ",contPos)
print("Numeros negativos: ",contNeg)
print("Promedio: ",promedio)