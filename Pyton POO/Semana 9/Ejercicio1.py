a= float(input("Ingrese el lado a: "))
b= float(input("Ingrese el lado b: "))
c= float(input("Ingrese el lado c: "))

if a>0 and b> 0 and c>0:
    area= (a-c)*b/2+b*c
    print("Area = ", area)
else:
    print("Error!! , los valores deben ser positivos")