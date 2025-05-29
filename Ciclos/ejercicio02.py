##################################################################################
## Crea una aplicación que permita adivinar un número. La aplicación genera un 
## número aleatorio del 1 al 100. A continuación va pidiendo números y va 
## respondiendo si el número a adivinar es mayor o menor que el introducido,
## a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). 
## El programa termina cuando se acierta el número (además te dice en cuantos 
##intentos lo has acertado), si se llega al limite de intentos te muestra el 
##número que había generado.
##################################################################################


import random

aleatorio = random.randint(1,100)
intentos = 10

while True:
    numero = int(input('Adivina el numero:'))
    if aleatorio == numero:
        intentos = intentos - 1
        print('Adivina el numero!')
        print(f'Te quedaban { intentos } intentos ')
        break
    elif numero > aleatorio:
        print('Ingresa oto mas pequeño: ')
        intentos = intentos - 1
    else : 
        print('Ingresa otro mas grande: ')
        intentos = intentos - 1

    if intentos == 0: 
        print('Perdistes!!') 
        break
