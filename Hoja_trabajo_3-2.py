#PROGRAMA QUE ALMACENA LA CONTRASEÑA Y LUEGO LA VALIDA PREGUNTANDOLE DE NUEVO AL USUARIO.
Contraseña = input("Ingrese la contraseña a Guardar ")
Validacion = input("Ingrese nuevamente la contraseña para validar que este correcta ")
if Validacion == Contraseña:
    print("Usted a ingresado su contraseña de forma satisfactoria")
else:
    print("La contraseña es incorrecta" )