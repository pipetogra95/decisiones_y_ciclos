luces=False
calefaccion=False
temperatura=18
while True:
    print("="*30)
    print("1. Encender luces")
    print("2. Activar calefacción")
    print("3. Ver estado")
    print("4. Salir")
    opcion=input("Escoja una opción: ")
    if opcion=="1":
        noche=input("¿Es de noche?si/no: ")
        while noche!="si" and noche!="no":
            print("Solo conteste si o no")
            noche=input("¿Es de noche?si/no: ")
        if noche=="si":
            luces=True
            print("Luces encendidas")
        else:
            luces=False
            print("Aún no es posible")
    elif opcion=="2":
        temperatura=input("¿Cuál es la temperatura en °C: ")
        while not temperatura.lstrip("-").isdigit():
            print("Debe ser un valor numérico")
            temperatura=float(input("¿Cuál es la temperatura en °C: "))
        temperatura=float(temperatura)
        if temperatura<18:
            if luces==False:
                print("No es posible, aún no es de noche")
            else:
                calefaccion=True
                print("Calefacción encendida")
        else:
            print("No permitido, temperatura no apta")
    elif opcion=="3":
        if luces==True and calefaccion==True:
            print("Luces: encendidas")
            print("Calefacción: encendida")
            print(f"Temperatura: {temperatura}")
        elif luces==True and calefaccion==False:
            print("Luces: encendidas")
            print("Calefaccion: apagada")
            print(f"Temperatura: {temperatura}")
        else:
            print("Luces: apagadas")
            print("Calefaccion: apagada")
            print(f"Temperatura: {temperatura}")
    elif opcion=="4":
        print("Salida con exito")
        break
    else:
        print("Opcion no válida")
