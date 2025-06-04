#################################################################################
#Pide una cadena y un carácter por teclado (valida que sea un carácter) 
#y muestra cuantas veces aparece el carácter en la cadena.
#################################################################################

phrase = input ('Escribe una frase: ')
char = input ('Escribe una letra: ')

times = 0

# for i in range (len(phrase)):
#     if char == phrase[i]:
#         times += 1

for letra in phrase:
    if char == letra:
        times += 1
        
print (f'la letra { char } se encuentra { times } veces!')