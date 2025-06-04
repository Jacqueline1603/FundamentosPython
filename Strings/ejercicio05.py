#################################################################################
#Si tenemos una cadena con un nombre y apellidos, realizar un programa que 
#muestre las iniciales en mayúsculas.
#################################################################################

full_name = input ('Escribe tu nombre completo: ')

words = full_name.split(' ')

initials = ''


for word in words:
    print (word[0].upper(), end='.')
print(initials)

