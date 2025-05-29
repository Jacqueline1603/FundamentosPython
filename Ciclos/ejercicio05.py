#################################################################################
#Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' 
#en caso contrario, el programa termina cuando se introduce un espacio.
#################################################################################

while True:
    letra = input('Ingresa una letra minuscula:')
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        print ('Vocal')
    else:
       if letra == ' ':
           break
       print ('No es vocal')
