import math
def generar_cuadro_magico(n):
    if n % 2 == 0:
        print("El número debe ser impar")
        return None
    matriz = [[0] * n for _ in range(n)]
    valor = 1
    fila = 0
    columna = n // 2   
    while valor <= math.pow(n, 2):
        matriz[fila][columna] = valor
        valor += 1        
        if valor % n == 1:
            fila += 1
        else:
            fila -= 1
            columna += 1       
        if fila < 0:
            fila = n - 1
        elif columna == n:
            columna = 0
    return matriz
def imprimir_cuadro_magico(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()
def calcular_suma(n):
    suma = round((math.pow(n, 2) * (math.pow(n, 2) + 1)) / (2 * n)) 
    return suma 
n = int(input("Ingrese un número impar: "))
if n % 2 != 1:
    print("El número debe ser impar")
else:
    cuadro_magico = generar_cuadro_magico(n)
    if cuadro_magico is not None:
        imprimir_cuadro_magico(cuadro_magico)
        suma_total = calcular_suma(n)
        print("Suma es ", suma_total)
