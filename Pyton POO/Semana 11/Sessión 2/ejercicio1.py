import random

def generar_lista_aleatoria(n):
    lista = []
    for _ in range(n):
        numero = random.randint(1, 10)
        lista.append(numero)
    return lista
def ordenar_lista_descendente(lista):
    lista.sort(reverse=True)
    return lista
def eliminar_repeticiones(lista):
    lista_sin_repeticiones = []
    for elemento in lista:
        if elemento not in lista_sin_repeticiones:
            lista_sin_repeticiones.append(elemento)
    return lista_sin_repeticiones
numeros = generar_lista_aleatoria(200)
numeros_ordenados = ordenar_lista_descendente(numeros)
numeros_sin_repeticiones = eliminar_repeticiones(numeros_ordenados)

print("Lista generada:")
print(numeros)
print("Lista ordenada:")
print(numeros_ordenados)
print("Lista sin repeticiones:")
print(numeros_sin_repeticiones)
