codigo = int(input("Ingrese código: "))

if codigo>1000000000000000 and codigo<9999999999999999:
     ppc1 = codigo // 100000000000000
     queda1 = codigo % 100000000000000
     ppc2 = queda1 // 1000000000000
     queda2 = codigo % 1000000000000
     hhc1 = queda2 // 10000000000
     queda3 = codigo % 10000000000
     mmc1 = queda3 // 100000000
     queda4 = codigo % 100000000
# Fijo
     ppf1 = queda4 // 1000000
     queda5 = codigo % 1000000
     ppf2 = queda5 // 10000
     queda6 = codigo % 10000
     hhf2 = queda6 // 100
     mmf2 = codigo % 100
     
     if ppc1==67 and ppc2==69: 
          pago1= mmc1*0.35
          pago_por_hora= 60*0.35
          pago2 = hhc1*pago_por_hora
          pagoT= pago1+pago2
          print("Total a pagar celular: ",pagoT)
          
     if ppf1== 70 and ppf2==73:
             pagoF= mmf2*0.15
             pago_h_F= 60*0.15
             pagoTh= hhf2*pago_h_F
             pagoT2= pagoF+pagoTh
             print("Total a pagar fijo: ",pagoT2)     
             suma = pagoT+pagoT2    
     print("PPPP", ppc1, ppc2)
     print("HH", hhc1)
     print("MM", mmc1)
     print("Fijo")
     print("PPPP", ppf1, ppf2)
     print("HH", hhf2)  # Convertir a entero
     print("MM", mmf2)
     print("Pago total por el consumo es: ",suma)
else:
    print("ERROR!!")

    
"""PPPP: Códigos ASCII de las dos 
PPPPHHMMPPPPHHMM
0000000000000000
letras que identifican el tipo de llamada. 
FI: fijo; CE: celular
HH: Horas del consumo.
MM: Minutos del consumo.
"""
""" costo llamada fijo =0.15 y celular 0.35"""

""" Entonces el programa debe imprimir:
6769150770731042
Cantidad de horas a Fijo: 10
Cantidad de minutos a Fijo: 42
Cantidad de horas a Celular: 15
Cantidad de minutos a Celular: 7
Monto a pagar por el consumo: 413.75
El mayor gasto lo tuvo al realizar llamadas a (F: fijo; C: celular): C
"""