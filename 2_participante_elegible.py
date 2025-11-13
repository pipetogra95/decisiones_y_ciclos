while True:
    try:
        edad=int(input("Ingrese su edad: "))
        licencia=(input("¿Tiene licencia de conducción vigente?si/no"))
        vehiculo=(input("¿Tiene vehículo propio?si/no"))
        if edad<0:
            print("Valor inválido")
        elif edad<18:
            print("No puede participar")
            break
    except ValueError:
        print("Debe ser un número entero mayor a cero ")
        