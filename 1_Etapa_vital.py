edad=(input("Ingrese su edad: "))
while not edad.isdigit():
    print("Debe ingresar un número entero mayor o igual a cero")
    edad=(input("Ingrese su edad: "))
edad=int(edad)
if edad<6:
    print("Infante")
elif 6<=edad and edad<=17:
    nivel_escolar=input("¿Estudia?si/no: ").lower()
    while nivel_escolar!="si" or nivel_escolar!="no":
        print("Responda solo con si o no")
        nivel_escolar=input("¿Estudia?si/no: ").lower
    if nivel_escolar=="si":
        print("Estudiante escolar")
    elif nivel_escolar=="no":
        print("No determinado")
elif 18<=edad and edad<=25:
    nivel_escolar=input("¿Estudia?si/no: ").lower()
    while nivel_escolar!="si" or nivel_escolar!="no":
        print("Solo responda con si o no")
        nivel_escolar=input("¿Estudia?si/no: ").lower()
    if nivel_escolar=="si":
        print("Universitario")
    elif nivel_escolar=="no":
        print("No determinado")
elif 25<edad and edad<=60:
    trabajo=input("¿Trabaja?si/no: ").lower()
    while trabajo!="si" or trabajo!="no":
        print("Solo responda con si o no")
        trabajo=input("¿Trabaja?si/no: ").lower()
    if trabajo=="si":
        print("Adulto activo")
    elif trabajo=="no":
        print("No determinado")
elif edad>60:
    trabajo=input("¿Trabaja?si/no: ")
    while trabajo!="si" or trabajo!="no":
        print("Solo responda con si o no")
        trabajo=input("¿Trabaja?si/no")
    if trabajo=="si":
        print("No determinado")
    elif trabajo=="no":
        print("Adulto mayor jubilado")
