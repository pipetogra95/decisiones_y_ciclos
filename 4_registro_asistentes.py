nombres=[]
repetidos=False
nombre=input("Ingrese nombre hasta palabra fin: ").lower().strip()
while nombre!="fin":
    nombres.append(nombre)
    nombre=input("Ingrese nombre hasta palabra fin: ").lower().strip()
for i in range(len(nombres)):
    for j in range(len(nombres)):
       if i==j:
           continue
       elif nombres[i]==nombres[j]:
           repetidos=True
if repetidos==False:
    print("No hay nombres repetidos")
elif repetidos==True:
    print("Hay repetidos")