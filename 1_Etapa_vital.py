while True:
    try:
        edad=int(input("Ingrese su edad: "))
        if edad<0:
            print("valor inválido")        
        elif edad<6:
            print("Infante")
            break
        elif 6<=edad and edad<=17:
            while True:
                nivel_escolar=input("¿Estudia?si/no: ").lower()
                if nivel_escolar=="si":
                    print("Estudiante escolar")
                    break
                elif nivel_escolar=="no":
                    print("No determinado")
                    break
                else:
                    print("Responda solo con si o no")
            break
        elif 18<=edad and edad<=25:
            while True:
                nivel_escolar=input("¿Estudia?si/no: ").lower()
                if nivel_escolar=="si":
                    print("Universitario")
                    break
                elif nivel_escolar=="no":
                    print("No determinado")
                    break
                else:
                    print("Responda solo con si o no")
            break
        elif 25<edad and edad<=60:
            while True:
                trabajo=input("¿Trabaja?si/no: ").lower()
                if trabajo=="si":
                    print("Adulto activo")
                    break
                elif trabajo=="no":
                    print("No determinado")
                    break
                else:
                    print("Responda solo con si o no")
            break
        elif edad>60:
            while True:
                trabajo=input("¿Trabaja?si/no: ")
                if trabajo=="si":
                    print("No determinado")
                    break
                elif trabajo=="no":
                    print("Adulto mayor jubilado")
                    break
                else:
                    print("Responda solo con si o no")
            break
    except ValueError:
        print("Ingrese numeros enteros mayores o iguales a cero")