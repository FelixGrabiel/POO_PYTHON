zona = input("Zona elegida (V: vip; P: platea; O: popular): ")
tipo = input("Tipo de pago (C: contado; T: tarjeta): ")
zona = zona.upper()
tipo = tipo.upper()
if zona=='V' or zona=='P' or zona=='O':
     if zona=='V':
        if tipo=='C' or tipo=='T':
           if tipo=='C':
               precio= 1500
               print("Precio de entrada: S/", precio)
           else: 
               tarjeta= input("Tarjeta de que banco (C: crédito; N: continental; O: otros) ")
               tarjeta = tarjeta.upper()
               if tarjeta=='C' or tarjeta=='N' or tarjeta=='O':
                    if tarjeta=='C':
                       precio = 2000
                       print("Precio de entrada: S/", precio)
                    if tarjeta =='N':
                        precio = 1900
                        print("Precio de entrada: S/", precio)
                    if tarjeta=='O':
                        precio =2100
                        print("Precio de entrada: S/", precio)      
        else:
            print("Error al ingresa el tipo de pago!!!")    
     if zona=='P':
        if tipo=='C' or tipo=='T':
           if tipo=='C':
               precioP= 750
               print("Precio de entrada: S/", precioP)
           else: 
               tarjeta= input("Tarjeta de que banco (C: crédito; N: continental; O: otros) ")
               tarjeta = tarjeta.upper()
               if tarjeta=='C' or tarjeta=='N' or tarjeta=='O':
                    if tarjeta=='C':
                       precioP = 950
                       print("Precio de entrada: S/", precioP)
                    if tarjeta =='N':
                        precioP = 875
                        print("Precio de entrada: S/", precioP)
                    if tarjeta=='O':
                        precioP = 1020
                        print("Precio de entrada: S/", precioP)      
        else:
            print("Error al ingresa el tipo de pago!!!")    
     if zona=='O':
        if tipo=='C' or tipo=='T':
           if tipo=='C':
               precioC= 265
               print("Precio de entrada: S/", precioC)
           else: 
               tarjeta= input("Tarjeta de que banco (C: crédito; N: continental; O: otros) ")
               tarjeta = tarjeta.upper()
               if tarjeta=='C' or tarjeta=='N' or tarjeta=='O':
                    if tarjeta=='C':
                       precioC = 320
                       print("Precio de entrada: S/", precioC)
                    if tarjeta =='N':
                        precioC = 300
                        print("Precio de entrada: S/", precioC)
                    if tarjeta=='O':
                        precioC = 335
                        print("Precio de entrada: S/", precioC)      
        else:
            print("Error al ingresa el tipo de pago!!!")   
else:
    print("Error al ingresar la zona!!")