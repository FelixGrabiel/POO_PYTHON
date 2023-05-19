num1= int(input("Ingrese primer valor: "))
num2= int(input("Ingrese segundo valor: "))
num3 =int(input("Ingrese tercer valor: "))

if num1 >0 and num2>0 and num3>0: 
     if num1>num2 and num1>num3 and num2>num3:
         print("Orden de mayor a menor: ", num1, " - ",num2," - ",num3)
     if num1>num2 and num1>num3 and num3>num2:
         print("Orden de mayor a menor: ", num1, " - ",num3," - ",num2)
         
     if num2>num1 and num2>num3 and num1>num3:
         print("Orden de mayor a menor: ", num2, " - ",num1," - ",num3)
     if num2>num1 and num2>num3 and num3>num1:         
         print("Orden de mayor a menor: ", num2, " - ",num3," - ",num1)
         
     if num3>num1 and num3>num1 and num1>num2:
         print("Orden de mayor a menor: ", num3, " - ",num1," - ",num3)
     if num3>num1 and num3>num2 and num2>num1:
         print("Orden de mayor a menor: ", num3, " - ",num2," - ",num1)  
else:
    print("Error!!")
    
    
    
    