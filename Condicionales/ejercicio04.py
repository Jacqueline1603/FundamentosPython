#################################################################################
# Crea un programa que pida al usuario dos números y muestre su división 
#si el segundo no es cero, o un mensaje de aviso en caso contrario.
#################################################################################

numero1 = int (input('ingresa un numero'))
numero2 = int (input('Ingresa otro numero'))

if numero2 != 0:
    division = numero1 / numero2
    print ('El resultado es', division)
else:
    print ('El segundo numero no debe ser Cero')

    