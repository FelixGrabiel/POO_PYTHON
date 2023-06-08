import random
def generar_matriz(n):
    matriz = []
    for _ in range(n):
        fila = []
        for _ in range(n):
            fila.append(random.randint(1, 10))
        matriz.append(fila)
    return matriz
def es_simetrica(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)
while True: 
     n = int(input("Ingrese el tamaño de la matriz cuadrada (N) no debe ser mayor que 25 : "))
     
     if n <= 25:
        matriz = generar_matriz(n)
        print("Matriz generada:")
        imprimir_matriz(matriz)
        if es_simetrica(matriz):
           print("La matriz es simétrica.")
        else:
            print("La matriz no es simétrica.")
     else:
         print("El tamaño de la matriz no debe ser mayor a 25.")
