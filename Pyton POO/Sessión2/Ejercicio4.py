import math
a = float(input("Ingrese el valor de A: "))
b = float(input("Ingrese el valor de B: "))
c = float(input("Ingrese el valor de C: "))

discriminante = b**2 - 4*a*c
if discriminante > 0:
    raiz_1 = (-b + math.sqrt(discriminante)) / (2*a)
    raiz_2 = (-b - math.sqrt(discriminante)) / (2*a)
    print("Raíz 1:", round(raiz_1, 2))
    print("Raíz 2:", round(raiz_2, 2))
elif discriminante == 0:
    raiz = -b / (2*a)
    print("La ecuación tiene una raíz real:", raiz)
else:
    print("Las raíces son complejas:")
    print("Raíz 1:", raiz_1)
    print("Raíz 2:", raiz_2)