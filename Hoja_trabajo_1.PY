#CALCULO DE INDICE DE MASA CORPORAL.
"""
CALCULO DE INDICE DE MASA CORPORAL
"""
Peso = input ("¿Cual es su peso en Kilogramos?")
Estatura = input ("¿Cual es su estatura en metros?")
#CALCULO DEL INDICE PESO / ESTATURA *2
IMC = round(float(Peso)/float(Estatura)**2,2)
print ("Su Indice de Masa Corporal es", IMC)