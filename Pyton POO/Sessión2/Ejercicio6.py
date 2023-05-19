fabricante = input("Ingrese el fabricante: [M]. Microsoft, [A]. Apple, [L]. Linux: ")
sistema = input("Ingrese tipo de programa: [S]. Sistema Operativo, [L]. Lenguaje de programación: ")
fabricante = fabricante.upper()
sistema = sistema.upper()

if fabricante == 'M' or fabricante == 'A' or fabricante == 'L':
    if fabricante == 'M':
        if sistema == 'S':
            print("Monto a pagar es: 1500")
        if sistema == 'L':
            dispositivo = input("Ingrese el dispositivo: [C]. Celular, [T]. Tabla, [O]. Otros: ")
            dispositivo = dispositivo.upper()
            if dispositivo == 'C':
                print("Monto a pagar es: 1800")
            if dispositivo == 'T':
                print("Monto a pagar es: 1200")
            if dispositivo == 'O':
                print("Monto a pagar es: 900")
    if fabricante == 'A':
        if sistema == 'S':
            print("Monto a pagar es: 2500")
        if sistema == 'L':
            dispositivo = input("Ingrese el dispositivo: [C]. Celular, [T]. Tabla, [O]. Otros: ")
            dispositivo = dispositivo.upper()
            if dispositivo == 'C':
                print("Monto a pagar es: 1900")
            if dispositivo == 'T':
                print("Monto a pagar es: 1800")
            if dispositivo == 'O':
                print("Monto a pagar es: 1600")
    if fabricante == 'L':
        if sistema == 'S':
            print("Monto a pagar es: 1000")
        if sistema == 'L':
            dispositivo = input("Ingrese el dispositivo: [C]. Celular, [T]. Tabla, [O]. Otros: ")
            dispositivo = dispositivo.upper()
            if dispositivo == 'C':
                print("Monto a pagar es: 100")
            if dispositivo == 'T':
                print("Monto a pagar es: 150")
            if dispositivo == 'O':
                print("Monto a pagar es: 50")
else:
    print("Error!!!, al ingresar los datos")
