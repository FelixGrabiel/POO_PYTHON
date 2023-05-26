numero = int(input("Ingrese un número entero positivo: "))
termino1 = 1
termino2 = 1
suma_terminos = termino1 + termino2
for _ in range(3, numero + 1):
    siguiente_termino = termino1 + termino2
    suma_terminos += siguiente_termino
    termino1 = termino2
    termino2 = siguiente_termino 

print("La suma es", suma_terminos)
