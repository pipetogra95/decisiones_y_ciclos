si=0
no=0
edad=input("Ingrese su edad o cero para salir:  ")
while not edad.isdigit():
    print("Debe ser un número entero mayor a cero o cero para salir")
    edad=input("Ingrese su edad o cero para salir:  ")
edad=int(edad)
while edad>0:
    pregunta=input("¿Te gusta programar?si/no: ")
    while pregunta!="si" and pregunta!="no":
        print("Solo responda si o no")
        pregunta=input("¿Te gusta programar?si/no: ")
    if pregunta=="si":
        si +=1
    elif pregunta=="no":
        no +=1
    edad=input("Ingrese su edad o cero para salir:  ")
    while not edad.isdigit():
        print("Debe ser un número entero mayor a cero o cero para salir")
        edad=input("Ingrese su edad o cero para salir:  ")
    edad=int(edad)
else:
    print(f"Le gusta programar a: {si} persona")
    print(f"No le gusta programar a: {no} persona")