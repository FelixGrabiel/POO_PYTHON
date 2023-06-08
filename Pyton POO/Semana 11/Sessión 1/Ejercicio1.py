#apeend es para agregar
#insert
# in para ver si se encuentra o no 
# sort modifica la lista ordenandola de menor a mayor 
# len la longitud, max el máximo, min = minimo, sum = suma
# split
def generar_lista(n):
   lista = list()
   for i in range (n):
       valor = int(input("Ingrese un numero: "))
       lista.append(valor)
   return lista 
while True:
    n= int(input("Ingrese la cantidad de elementos: "))
    if n>0:
        break
lfinal = generar_lista(n)
print("lista creada: ",lfinal)
print("Maximo elmento: ",max(lfinal))
print("Minimo elemento: ", min(lfinal))
print("Suma elementos: ",sum(lfinal))
print("Cantidad de elementos: ",len(lfinal))
print("Promedio: ",sum(lfinal)/len(lfinal))
lista2= [10,11,12,13,14]
lista3 = lfinal+lista2
print("Lista 3 = ", lista3)
lista4 = [1,2,3]
lista4*=3 #repeti los elementos
print("Lista 4 = ",lista4)
#invertir una lista
lista5=[1,3,5,7,9]
lista6=list(reversed(lista5))
print("Lista 5 =",lista5)
print("Lista invertida = ",lista6)
#insertar un elemento
# lista.insert(posicion,elemento)
insertar=int(input("Ingrese el numero a insertar: "))
posicion = int(input("Ingrese la posicion a insertar: "))
lfinal.insert(posicion,insertar)
print("Lista con funcion luego de insertar: ",lfinal)
# extend para agregar varios elementos ejemplo LFINAL.extend([200,300,400])
#para modificar lista
print("Lista 5 = ",lista5)
lista5[2]=18
print("Lista modificada = ",lista5)
lista5[1:3]=[500,1000]
print("Lista modificada = ",lista5)
lista5.extend([11,7,13,15])
print("Lista  5 con extend = ",lista5)
#remover la primera ocurrencia del valor dado como parametro
lista5.remove(7)
print("Lista 5 con remove = ",lista5)
# pop eleimina el ulitmo elemento de la lista
lista5.pop()
print("Lista 5 con pop = ",lista5)
lista7=[1,3,4,1,5,6,8,1,9,1]
#count contar el numero de ocurrecnias de un valor
repeteciones = lista7.count(1)
print("Repeticiones del 1 = ",repeteciones)
#index retorna la posicion de un elemento en la lista
#lista.index(valor)
#sort para ordenar
print("Lista 7 = ",lista7)
lista8=sorted(lista7,reverse=True)
print("Lista 8 (lista 7 ordenada) = ",lista8)
lista7.sort()
print("Lista 7 ordenada = ",lista7)
# del elimina un elementdo dada su posicion 
del(lista7[7])
print("Lista 7 eliminado elemento de indice 7 = ",lista7)
 