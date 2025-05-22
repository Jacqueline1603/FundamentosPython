################################################################################
#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
################################################################################

#Hipotenusa ** 2 = cateto 1 ** 2 + cateto 2 ** 2 
#El operador doble asterisco ** permite elevar un numero
## a una potencia n

##Para operaciones matematicas avanzadas importamos la 
##libreria math
import math

cateto1 = int(input ('Ingresa valor del Cateto 1: '))
cateto2 = int(input ('Ingresa valor del Cateto 2: '))

#sqrt es para la raiz cuadrada
hipotenusa = math.sqrt (cateto1 ** 2 + cateto2 ** 2)

print ('La hipotenusa del triangulo es: ' + str(hipotenusa))