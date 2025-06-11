#################################################################################
#Crear un vector de 5 elementos de cadenas de caracteres, inicializa el vector 
#con datos leídos por el teclado. Copia los elementos del vector en otro vector 
#pero en orden inverso, y muéstralo por la pantalla.
#################################################################################

words = []
words2 = []

for i in range(5):
    words.append(input('Ingresa una letra: '))
    words2.append('') 

end = 5 
for word in words:
    words2[end - 1] =word
    end -= 1

print (words)
print (words2)