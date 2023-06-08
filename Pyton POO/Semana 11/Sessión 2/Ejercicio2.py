def insertar_ordenado(lista, numero):
    if numero == 0:
        return
    for i in range(len(lista)):
        if numero < lista[i]:
            lista.insert(i, numero)
            break
    else:
        lista.append(numero)
    print("Lista =", lista)
numeros = []
while True:
    numero = int(input("Ingrese número: "))
    insertar_ordenado(numeros, numero)
    if numero == 0:
        break
print("Lista final = ")
print(numeros)