num = int(input("Ingrese número de tarjetas del censo del 2018: "))
while True:
    if num>0:
        break;
contMujeres_Viudas =0
contHombres_30_S_D = 0
contM=0
contH=0
suma = 0
for i in range(num):
    sexo = input("Ingrese Sexo (F: Femenino - M: Masculino): ")
    edad = int(input("Ingrese su Edad: "))
    estado = input("Ingrese estado Civil ((a: Soltero; b: Casado; c: Viudo; d: Divorciado): ")
    sexo= sexo.upper()
    estado = estado.upper()
    if estado=='C':
        if edad>=16 and edad<=21:
            contMujeres_Viudas+=1
    if sexo=='M':
        contH+=1
    else:
         contM+=1
    if estado=='A' or estado=='D':
        if edad>30:
            contHombres_30_S_D+=1
porcentajeH = round((contH*100)/num)
porcentajeM = round((contM*100)/num)
print("Número de jóvenes viudas entre 16 y 21 años: ",contMujeres_Viudas)
print("Porcentaje de Hombres: ",porcentajeH,"%")
print("Porcentaje de Mujeres: ",porcentajeM,"%")
print("Número de hombres mayores de 30 años solteros o divorciados: ",contHombres_30_S_D)

    