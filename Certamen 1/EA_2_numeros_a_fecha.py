# escriba un programa que dada una cadena de caracteres de la forma "dd mm aaaa"
# devuelva su correspondiente en texto

date = raw_input('Introduzca una fecha de la forma "dd-mm-aaaa": ')

d = int(date[0:2])
m = int(date[3:5])
a = int(date[6:10])
if d >= 1 and d <= 30:
    if m >= 1 and m <= 12:
        if m == 1:
            mes = 'enero'
        elif m == 2:
            mes = 'febrero'
        elif m == 3:
            mes = 'Marzo'
        elif m == 4:
            mes = 'Abril'
        elif m == 5:
            mes = 'Mayo'
        elif m == 6:
            mes = 'Junio'
        elif m == 7:
            mes = 'Julio'
        elif m == 8:
            mes = 'Agosto'
        elif m == 9:
            mes = 'Septiembre'
        elif m == 10:
            mes = 'Octubre'
        elif m == 11:
            mes = 'Noviembre'
        else:
            mes = 'Diciembre'
    else:
        date = raw_input('Por favor vuelva a introducir la fecha con valores validos: ')
else:
    date = raw_input('Por favor vuelva a introducir la fecha con valores validos: ')
print 'La fecha es', d,'de', mes, 'del', a
