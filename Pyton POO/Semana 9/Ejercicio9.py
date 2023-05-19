"""Elabore un programa en Python que teniendo como dato 
una hora expresada en horas, minutos
y segundos (h, m, s) nos calcule y muestre la nueva hora luego 
de un segundo.
Por ejemplo, si h fuese 11, m fuese 59 y s fuese 59 entonces 
la nueva hora sería 12:0:0"""

hora = int(input("Ingrese la hora: "))
minutos= int(input("Ingrese los minutos: "))
segundos = int(input("Ingrese los segundos: "))

if hora > 0 or hora <25 and minutos>0 or minutos<=60 and segundos>0 or segundos<=60:
    segundos= segundos+1
    if segundos==60:
      segundos= 0
      minutos=minutos + 1
    if minutos==60:
       minutos=0
       hora = hora + 1
    if hora==24:
        hora=0
    
    print("La hora es: ",hora,": ",minutos,": ",segundos)
    
else:
    print("Error")