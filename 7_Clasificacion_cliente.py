total=input("Ingrese el valor total de la compra: ")
while not total.replace(".","",1).isdigit() or float(total)<=0:
    print("Debe ser un número mayor a cero")
    total=input("Ingrese el valor total de la compra: ")
total=float(total)
if total<30000:
    print("Cliente regular")
else:
    membresia=input("Tiene membresia vitalicia, temporal o ninguna?: ").lower().strip()
    while membresia!="vitalicia" and membresia!="temporal" and membresia!="ninguna":
        print("Opción inválida")
        membresia=input("Tiene membresia vitalicia, temporal o ninguna?: ").lower().strip()
    if membresia!="ninguna" and total>=50000:
            print("Cliente Premium")
    elif 30000<=total<50000 or membresia=="temporal":
            print("Cliente frecuente")
    else:
        print("Cliente regular")