while True:
    n = int(input("Ingrese un número entero, positivo y menor a 10: "))
    if 0 < n < 10:
        break
for i in range(1,n+1):
    if i==1 or i==n:
        for j in range(1,i+1):
            print("*", end="")
    else:
        for j in range(1,i+1):
            if j == 1 or j == n or i == j :
                print("*", end="")
            else:
                print(" ",end="")
 
    print()
