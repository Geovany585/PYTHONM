#PROGRAMA QUE SOLICITA AL USUARIO UN NUMERO POSITIVO Y MUESTRA EN PANTALLA SI ES PRIMO O NO
n=int(input("INGRESE NUMERO POSITIVO ENTERO, "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " Es primo")
else:
    print(str(n) + " No es primo")