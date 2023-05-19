numero = int(input("Ingrese un numero posivo entre 1 a 100: "))

if numero>=1 and numero<1000:
    if numero<10:
        print("1")
    if numero>=10 and numero<100:
        print("2")
    if numero>=100 and numero<1000:
        print("3")
else:
    print("Erro!!!")
