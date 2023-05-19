"""Elabore un programa en Python que teniendo como 
dato una hora expresada en segundos (t),
nos calcule y muestre la cantidad de horas, 
minutos y segundos contenidos en dicha hora.
Por ejemplo, si t fuese 3879, entonces el número 
de horas sería 1, los minutos serían 4 y los
segundos serían 39. """


segundos = int(input("Ingrese la hora en segundos: "))

if segundos>60:
    # un minuto tiene 60 segundos y una hora tiene 3600 segundos
    hora = segundos//3600
    queda = segundos% 3600
    minutos = queda//60
    queda1 = segundos%60
    segundos = queda1
    print("La hora es: ",hora)
    print("Los minutos son: ",minutos)
    print("Los segundos son: ", segundos)
else:
    print("Error!!!")


