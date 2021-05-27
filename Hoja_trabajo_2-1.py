#INGRESAR NUMERO ENTERO Y QUE DEVUELVA UN TRIANGULO ACORDE AL NUMERO INDICADO
n= int(input("INTRODUCE UN NUMERO ENTERO POSITIVO: "))
for n in range(n):
    print("*"*(n+1))
if n <= 0:
    print("NO ES VALIDO")
