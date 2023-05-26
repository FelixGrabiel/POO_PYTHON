while True:
    num = int(input("Ingrese el numero de estudiante: "))
    if num>0:
       break
for i in range(num):
    print("Ingrese la nota del alumno",i+1)
    nota=float(input("Ingrese el EF del alumno: "))
    ep= float(input("Ingrese el EP del alumno: "))
    tf= float(input("Ingrese el TF del alumno: "))
    promedio = (nota*0.55)+(ep*0.3)+(tf*0.15)
    print("El promedio es: ", promedio)