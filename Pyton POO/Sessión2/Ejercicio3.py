a= float(input("Ingrese lado a: "))
b= float(input("Ingrese lado b: "))
c= float(input("Ingrese lado c: "))

if a>0 and b>0 and c>0: 
     if a==b and b==c:
         print("Triangulo equilatero")
     else:
         if a!=b and b!=c and a!=c:
             print("Triangulo escaleno")
         else:
             print("Traingulo isosceles")
else:
    print("Error")