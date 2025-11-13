edad=input("Ingrese su edad: ")
while not edad.isdigit():
    print("Debe ingresar un valor entero igual o mayor a cero")
    edad=input("Ingrese su edad:")
edad=int(edad)
if edad<18:
    print("No apto")
elif edad>=18:
    licencia=input("¿Tiene licencia de conducción vigente?si/no: ").lower()
    while licencia!="si" and licencia!="no":
        print("Solo conteste si o no")
        licencia=input("¿Tiene licencia de conducción vigente?si/no: ")
    if licencia=="no":
        print("No apto")
    else:
        vehiculo=input("¿Tiene vehiculo propio?si/no: ").lower()
        while vehiculo!="si" and vehiculo!="no":
            print("Solo conteste si o no")
            vehiculo=input("¿Tiene vehiculo propio?si/no: ")
        if vehiculo=="no":
            prestamo=input("¿Tiene manera de competir con un auto prestado?si/no: ")
            while prestamo!="si" and prestamo!="no":
                print("Solo conteste si o no")
                prestamo=input("¿Tiene manera de competir con un auto prestado?si/no: ")
            if prestamo=="si":
                print("Apto")
            else:
                print("No apto")
