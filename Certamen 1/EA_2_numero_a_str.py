#crear una funcion llamada numeros, a la cual se le pase como parametro un numero
# entero entre 0 y 4, y la funcion mostrara dicho numero de la forma "cero", "uno"
# "dos", "tres", "cuatro"

def numeros (n):
    if n >= 0 and n < 5:
        if n == 4:
            print "cuatro"
        elif n == 3:
            print "tres"
        elif n == 2:
            print "dos"
        elif n == 1:
            print "uno"
        else:
            print "cero"
    else:
        n = int(raw_input('Por favor vuelva a introducir un numero: '))

n = int(raw_input('Introduzca un numero entre 0 y 4: '))
numeros = numeros (n)
print numeros

