luces=False
calefaccion=False

while True:
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
                break
            else:
                luces=False
                print("Aún no es posible")
                break
    elif opcion=="2":
        temperatura=input("¿Cuál es la temperatura en °C: ")
        while not temperatura.lstrip("-").isdigit():
            print("Debe ser un valor numérico")
            temperatura=float(input("¿Cuál es la temperatura en °C: "))
            temperatura=float(temperatura)
            if temperatura<18:
                if luces==False:
                    print("No es posible, aún no es de noche")
                    break
                else:
                    print("Calefacción encendida")
                    break
        
