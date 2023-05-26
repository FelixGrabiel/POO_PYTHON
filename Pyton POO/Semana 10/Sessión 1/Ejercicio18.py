while True:
    N = int(input("Ingrese un número entero positivo (menor que 10): "))
    if N > 0 and N < 10:
        break
for i in range(1, N + 1):
    for j in range(1, i + 1):
        print(j, " ", end="")
    print()
