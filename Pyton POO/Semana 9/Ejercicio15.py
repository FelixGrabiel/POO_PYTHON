num1= int(input("Ingrese primer valor: "))
num2= int(input("Ingrese segundo valor: "))
num3 =int(input("Ingrese tercer valor: "))

if num1 >0 and num2>0 and num3>0: 
     if num1>num2 and num1>num3:
         print("El mayor numero es: ",num1)
         if num2>num3:
             print("El menor numero es: ",num3)
         else: 
             print("El menor numero es: ",num2)
     if num2>num1 and num2>num3:
         print("El mayor numero es: ",num2)
         if num1>num3:
             print("El menor numero es: ",num3)
         else: 
             print("El menor numero es: ",num1)
     if num3>num1 and num3>num1:
         print("El mayor numero es: ",num3)
         if num1>num2:
             print("El menor numero es: ",num2)
         else: 
             print("El menor numero es: ",num1)       
        
else:
    print("Error!!")