"""Elabore un programa en Python que permita 
mostrar el estado del alumno, según la nota final
del curso. Para ello debe tener en cuenta los siguientes criterios:
 Si la nota es menor de 12.50 está desaprobado, por lo que mostrará 
una Desaprobado.
 Si la nota es mayor o igual de 12.50 y menor o igual a 20 
está aprobado, entonces
mostrará una Aprobado"""

nota= float(input("Ingrese la nota: "))
if nota>=0 or nota<=20:
    if nota<12.5: 
        print("Alumno desaprobado con: ",nota)
    if nota>=5 and nota<=20:
        print("Alumno aprobado con: ",nota)
else:
    print("Error al ingresar la nota")