escala=input("Ingrese la escala(A,B,C,D): ")
numcursos=int(input("Ingrese la cantidad de cursos: "))
escala=escala.upper()#convirtiendo a mayusculas
if escala=="A" or escala=="B" or escala=="C" or escala=="D" and numcursos>0:
    if escala=="A":
        if numcursos<6:
            cuotavariable=400
        elif numcursos<9:
            cuotavariable=600
        else:
            cuotavariable=900
    if escala=="B":
        if numcursos<4:
            cuotavariable=350
        elif numcursos<8:
            cuotavariable=500
        else:
            cuotavariable=700
    if escala=="C":
        if numcursos<4:
            cuotavariable=320
        else:
            if numcursos<8:
             cuotavariable=480
            else:
             cuotavariable=685
    if escala=="D":
        if numcursos<5:
            cuotavariable=310
        elif numcursos<9:
            cuotavariable=475
        else:
            cuotavariable=680
    importe=350+cuotavariable
    print("Importe=",importe)
else:
    print("Error en los datos")