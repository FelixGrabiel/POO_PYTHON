gb= int(input("Ingrese la cantidad de GB consumidas: "))
if gb>0 and gb<=4:
    pagar =50
    print("Total a pagar: S/",pagar)
if gb> 4 and gb<=8:
     pagar =80
     print("Total a pagar: S/",pagar)
if gb>8:
    adicional= (gb-8)*4.50
    pagar = 80+adicional
    print("Total a pagar: S/",pagar)
