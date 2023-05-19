#SEDAPAL
metros= int(input("Ingrese el consumo en metros cubitos: "))
precio= float(input("Ingrese el precio por metro cubito: "))

if metros>0 and precio>0:
    total= metros*precio
    print("El total a pagar por metro cubico es = S/ ", total)
else:
    print("Error!!!")