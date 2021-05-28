#asignacion de grupos segun la letra inicial de su nombre
Nombre= input("Ingresa tu primer nombre ")
Genero= input("Ingresa el sexo al que perteneces (M 0 F) ")
if Genero == "F":
    if Nombre <= "M":
        grupo = "A"
    else:
        grupo = "B"
else:
    if Genero == "M":
        if Nombre >="N":
            grupo = "A"
        else:
            Nombre < "N"
            grupo = "B"
print("Tu grupo es:" + grupo)


