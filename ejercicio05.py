################################################################################
#Escribir un programa que convierta un valor dado en grados Fahrenheit a grados 
#Celsius.
################################################################################
#Análisis
#Tenemos que leer una temperatura en grados Fahrenheit y devolverla en grados 
#celsius.
#Datos de entrada: grados Fahrenheit (real)
#Información de salida: grado Celsius (real)
#Variables: fahrenheit, celsius (Real).
#################################################################################
#Diseño
#1. Leer la temperatura en grados Fahrenheit
#2. Calcular los grados celsius (C = (F-32)*5/9)
#3. Mostrar grados celsius
################################################################################

fahrenheit = float(input ('Escribe grados Fahrenheit: '))
celsius = (fahrenheit -32) * 5 / 9

# 100ºF equivalen a 36ºC
#Formas Strings 
# f'{}'
print (f'{ fahrenheit }ºF equivalen a { celsius }ºC')
