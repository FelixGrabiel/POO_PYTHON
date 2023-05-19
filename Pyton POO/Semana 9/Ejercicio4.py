accion1= int(input("Ingresa la accion 1: "))
accion2= int(input("Ingrese la accion 2: "))
accion3= int(input("Ingrese la accion 3: "))
ganancia= float(input("Ingrese la ganancia del año: "))
if accion1>0 and accion2> 0 and accion3>0 and ganancia>0:
   accionTotal= accion1+accion2+accion3
   monto1= accion1*ganancia/accionTotal
   monto2= accion2*ganancia/accionTotal
   monto3= accion3*ganancia/accionTotal
   print("El monto del primer socio es: ", monto1)
   print("El monto del segundo socio es: ", monto2)
   print("El monto del tercer socio es: ",monto3)
else:
    print("Error!!!!")