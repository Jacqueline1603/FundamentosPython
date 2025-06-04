#################################################################################
#Realizar un programa que defina un vector llamado "vector_numeros" de 10 enteros,
# a continuación lo inicialice con valores aleatorios (del 1 al 10) 
#y posteriormente muestre en pantalla cada elemento del vector junto con 
#su cuadrado y su cubo.
#################################################################################
import random

numbers = []

for i in range(10):
    numbers.append(random.randint(1,100))

    for number in numbers:
        print (number, number ** 2, number ** 3)
