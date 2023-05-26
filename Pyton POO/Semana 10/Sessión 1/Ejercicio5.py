cont1=0
cont2=0
cont3=0
cont4=0
while True:
    num = int(input("Ingrese el numero de alumnos: "))
    if num>0:
       break
for i in range(num):
     print("Peso alumno: ",i+1)
     peso=int(input("Ingrese peso alumno: "))
     if peso<40:
        cont1+=1
     if peso>=40 and peso<=50:
        cont2+=1
     if peso>50 and peso<60:
        cont3+=1
     if peso>=60:
        cont4+=1
print("Alumnos de menos de 40 kg: ",cont1)
print("Alumnos de entre de 40 y 50 kg: ",cont2)
print("Alumnos de más de 50 y 60 kg: ",cont3)
print("Alumnos de 60 kg o más: ",cont4)
    