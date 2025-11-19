usuario_correcta="nazarena"
contraseña_correcta="12345678"
intentos=0
while intentos<3:
    usuario=input("Ingrese usuario\n").strip().lower()
    contraseña=input("Ingrese contraseña\n").strip().lower()
    if usuario==usuario_correcta and contraseña==contraseña_correcta:
        print("Acceco autorizado")
        break
    elif usuario=="" and contraseña=="":
        print("Debe llenar los espacios")
    elif usuario!=usuario_correcta and contraseña==contraseña_correcta:
        print("Usuario incorrecto")
        intentos=intentos+1        
    elif usuario==usuario_correcta and contraseña!=contraseña_correcta:
        print("Contraseña incorrecta")
        intentos=intentos+1
    elif usuario!=usuario_correcta and contraseña!=contraseña_correcta:
        print("Ambos incorrectos")
        intentos=intentos+1
if intentos==3:
    print("Acceso denegado")