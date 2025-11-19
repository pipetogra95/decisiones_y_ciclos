num1=input("Ingrese el primer número: ")
while not num1.lstrip("-").isdigit():
    print("Debe ser un número entero")
    num1=input("Ingrese el primer número: ")
num1=int(num1)
num2=input("Ingrese el segundo número: ")
while not num2.lstrip("-").isdigit():
    print("Debe ser un número entero")
    num2=input("Ingrese el segundo número: ")
num2=int(num2)
num3=input("Ingrese el tercer número: ")
while not num3.lstrip("-").isdigit():
    print("Debe ser un número entero")
    num3=input("Ingrese el tercer número: ")
num3=int(num3)
if num1>0 and num2>0 and num3>0:
    print("Los tres números son positivos")
elif (num1==0 and num2!=0 and num3!=0) or (num1!=0 and num2==0 and num3!=0) or (num1!=0 and num2!=0 and num3==0):
    print("Exactamente uno de los números es cero")
elif num1<0 or num2<0 or num3<0:
    print("Hay al menos un número negativo")
else:
    print("No cumple ninguna condición exigida")
  