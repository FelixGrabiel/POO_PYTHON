numero = int(input("Ingrese un número entero positivo: "))
termino1 = 1
termino2 = 1
print(termino1, end=", ")
print(termino2, end=", ")
for _ in range(3, numero + 1):
    siguiente_termino = termino1 + termino2
    print(siguiente_termino, end=", ")
    termino1 = termino2
    termino2 = siguiente_termino

