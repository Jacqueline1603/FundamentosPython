#################################################################################
#Escribir por pantalla cada carácter de una cadena introducida por teclado.
#################################################################################

my_string = input('ingresa un texto: ')

print (my_string)

for letra in my_string:
    print (letra, end ='-')

print ()

#La funcion len nos da el tamaño de un string 

for index in range(len(my_string)):
    print (f'[{index}] = {my_string[index]}')

other_string = 'prueba'

print (other_string[0])
print (other_string[3])
print (other_string[5])