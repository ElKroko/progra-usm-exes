# Usted debe escribir un programa que reciba como entrada una unica linea, que contanga
# todas las anotaciones realizadas por un equipo de basquetbol durante un partido.
# Las anotaciones de periodos distintos deben ir separadas por un espacio.
# Como salida, debe mostrar la cantidad de puntos obtenidos en cada periodo y los puntos
# totales, siguiendo el formato.
# Tiro Libre (L) = 1; Doble (D) = 2; Triple (T) = 3

def f1 (a, b):
    i = 0
    while i < len(a):
        if b == a[i]:
            return i
        i = i + 1
    return False

def letras_dentro(a,b):
    i = 0
    veces = 0
    while i < len(a):
        if b == a[i]:
            veces += 1
            i += 1
        else:
            i += 1
    return veces

puntos = raw_input('Ingrese los puntos cumpliendo el formato: ')
a = f1(puntos,' ')
s = ''

if a != False:
    p1 = puntos[0:a]
    print p1
    while a < len(puntos)-1:
        s = s + puntos[a+1]
        a += 1
    b = f1(s,' ')
    print s
    print b
    s1 = ''
    if b != False:
        p2 = s[0:b]
        print p2
        while b < len(s)-1:
            s1 = s1 + s[b+1]
            b += 1
        c = f1(s1,' ')
        print s1
        s2 = ''
        if c != False:
            p3 = s1[0:c]
            print p3
            while c < len(s1):
                s2 += s1[c]
                c += 1
            p4 = s2
            print 'Su primer periodo es', p1            #En caso que las condiciones se cumplan, el programa se ejecutara
            print 'Su segundo periodo es', p2
            print 'Su tercer periodo es', p3
            print 'Su cuarto periodo es', p4
            print 'Presione enter para calcular sus puntajes, de lo contrario, cierre el programa'
            tiempo = raw_input(' ')
            LP1 = letras_dentro(p1,'L')                 #Calcula el puntaje para cada periodo, conciderando diferentes
            DP1 = letras_dentro(p1,'D') * 2             #tipos de variables.
            TP1 = letras_dentro(p1,'T') * 3
            totalp1 = LP1 + DP1 + TP1
            LP2 = letras_dentro(p2, 'L')
            DP2 = letras_dentro(p2, 'D') * 2
            TP2 = letras_dentro(p2, 'T') * 3
            totalp2 = LP2 + DP2 + TP2
            LP3 = letras_dentro(p3, 'L')
            DP3 = letras_dentro(p3, 'D') * 2
            TP3 = letras_dentro(p3, 'T') * 3
            totalp3 = LP3 + DP3 + TP3
            LP4 = letras_dentro(p4, 'L')
            DP4 = letras_dentro(p4, 'D') * 2
            TP4 = letras_dentro(p4, 'T') * 3
            totalp4 = LP4 + DP4 + TP4
            total = totalp1+totalp2+totalp3+totalp4
            print 'El total de puntos por periodo es:'
            print 'Periodo 1: ', totalp1
            print 'Periodo 2: ', totalp2
            print 'Periodo 3: ', totalp3
            print 'Periodo 4: ', totalp4
            print 'Y el total de puntos del partido, es de', total
        else:
            print 'Por favor, vuelva a intentarlo. (Error: 3'
    else:
        print 'Por favor, vuelva a intentarlo. (Error: 2)'
else:
    print ' Por favor, vuelva a intentarlo (Error: 1)'

# NO APLICA PARA LETRAS DIFERENTES A D L T