#################################################################################
#Pide una cadena y un carácter por teclado (valida que sea un carácter) 
#y muestra cuantas veces aparece el carácter en la cadena.
#################################################################################

phrase = input ('Escribe una frase: ')

words = phrase.split(" ")

print (f'La frase contiene { len(words) } palabras')