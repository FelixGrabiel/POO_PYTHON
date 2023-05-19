#sueldo básico* horas trabajadas
#suedlo básico * 0.18 bonificación del mismo sueldo 
# y se obtiene el sueldo bruto
# sueldo bruto * 0.12, se obtiene el sueldo neto
# Prgrama que calcule y muestre el sueldo b, bruto y neto

horasT= int(input("Ingrese el total de horas trabajadas: "))
sueldo= float(input("Ingrese el monto por hora: "))

if horasT>0 and sueldo>0:
    sb= horasT*sueldo
    sbr= sb+ (sb*0.18)
    sn= sbr - (sbr*0.12)
    print("El sueldo básico es: S/",sb)
    print("El sueldo bruto es: S/", sbr)
    print("El sueldo neto es: S/",sn)
    
else:
    print("Error!!!") 