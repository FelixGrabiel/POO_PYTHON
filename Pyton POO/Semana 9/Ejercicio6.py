import math
r= float(input("Ingrese el valor de r: "))
h= float(input("Ingrese el valor de h: "))

altura1= (h**2-r**2)**0.5
area1= math.pi*math.pow(r, 2)/ 2+ r*altura1
print("Area 2 es: ", area1)