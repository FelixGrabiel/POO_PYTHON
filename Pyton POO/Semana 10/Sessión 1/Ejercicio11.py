def fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        fib1=1
        fib2=1
        for i in range(3,n+1):
            fib=fib1+fib2
            fib1=fib2
            fib2=fib
        return fib

while True:
    n=int(input("Ingrese N: "))
    if n>0:
        break    
print("Secuencia de fibonacci")
for i in range(1,n+1):
    print(fibonacci(i),end=" ")
print()
