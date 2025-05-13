################################################################################
#Calcular el perí­metro y área de un rectángulo dada su base y su altura.
################################################################################

print ("Programa que calcula el area y perimetro de un Rectangulo")

altura = input ('Ingresa la altura: ')
altura = int(altura)
base = int (input ('Ingresa la base: '))

perimetro =  base + altura + base + altura 
area = base * altura 

print ("EL area del Rectangulo es: " + str (area))
print ("El perimetro del Recatngulo es: " + str (perimetro))

