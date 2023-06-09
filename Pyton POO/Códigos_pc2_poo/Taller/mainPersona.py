from Persona import Persona
n = -1 
personas = []
dni_utilizados = []

while n < 0:
    n = int(input("Ingrese cantidad de personas: "))

for x in range(n):
    edad = -1
    peso = -1.0
    altura = -1.0
    dni = ""
    sexo = ""
    nombre = input("Ingrese nombre: ")
    """ 
! len para ver la longitud del valor ingresado 
    """
    while len(dni) != 8: 
        dni = input("Ingrese dni: ")

        if dni in dni_utilizados:
            print("Error: Este DNI ya ha sido utilizado. Ingrese un DNI diferente.")
            dni = ""

    dni_utilizados.append(dni)

    while sexo != "M" and sexo != "F":
        sexo = input("Ingrese sexo (M: Masculino, F: Femenino): ")
        sexo.capitalize() 
    """ 
! capitalize comvierte el primer caracter en mayusculas y las demas en minusculas
    """   
    while edad < 0:
        edad = int(input("Ingrese edad: "))

    while peso < 0:
        peso = float(input("Ingrese peso: "))

    while altura < 0:
        altura = float(input("Ingrese altura: "))

    persona = Persona(nombre, edad, sexo, dni, peso, altura)
    personas.append(persona)
print("REPORTE")
for x in personas:
    print("Peso ideal: ", x.analizarPesoIdeal())
    print("Mayor de edad: ", x.esMayorDeEdad())

print("dni\tnombre\tsexo\tpeso\taltura\tedad")
for x in personas:
    print(x.toString())
