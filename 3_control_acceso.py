lista=["juan", "carlos", "ana", "pedro", "luisa"]
nombre=input("Ingrese su nombre: ").lower()
if nombre in lista:
    print("Entrada prohibida, está en la lista restringida")
else:
    codigo=input("Ingrese su código: ")
    while not codigo.isdigit():
        print("Debe ingresar un valor entero mayor a cero")
        codigo=input("Ingrese su código: ")
    codigo=int(codigo)
    if codigo%2==0:
        print("Bienvenido")
    else:
        codigo=str(codigo)
        if codigo[-1]=="7":
            print("Bienvenido")
        else:
            print("Acceso denegado")