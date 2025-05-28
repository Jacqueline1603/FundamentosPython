#################################################################################
#Realiza un programa que pida el dí­a de la semana (del 1 al 7) y escriba 
#el dí­a correspondiente. 
# Si introducimos otro número nos da un error.
#################################################################################

dia = int (input('Escribe un día del 1 al 7'))

match dia:
    case 1: 
        print ('Lunes')
    case 2: 
        print ('Martes')
    case 3:
        print ('Miercoles')
    case 4: 
        print ('Jueves')
    case 5: 
        print ('Viernes')
    case 6: 
        print ('Sabado')
    case 7:
        print ('Domingo')
    case _:
        print ('El dia elegido no existe')
        