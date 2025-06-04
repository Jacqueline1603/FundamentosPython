#################################################################################
#Realizar un programa que comprueba si una cadena leída por teclado comienza por 
#una subcadena introducida por teclado.
#################################################################################

# my_string = 'Este es un texto'

# print (my_string.capitalize())
# print (my_string.lower())  
# print (my_string.title())
# print (my_string.startswith('Este'))
# print (my_string.startswith('Esta'))

my_str_1 = input ('Ingresa una cadena de texto:')
my_str_2 = input ('Ingresa las primeras letras de la cadena anterior:')

if my_str_1.startswith(my_str_2):
    print (f'"{my_str_1}"comienza con "{my_str_2}"')
else: 
    print (f'"{my_str_1}" No comienza con " {my_str_2}"')
