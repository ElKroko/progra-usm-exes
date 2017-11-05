n = int(raw_input('Ingrese su carta: '))
while n >= 1:
    while n <= 13:
        d = abs(n - 21)
        print 'la diferencia entre su numero y 21 es ', d
        if n < 21:
            m = int(raw_input('Ingrese una nueva carta: '))
            if m != -1:
                if m + d < 21:
                    print 'la diferencia entre su ultima carta y  la diferencia anterior es ', m - d
                else:
                    print 'La suma es mayor que 21, el jugador pierde inmediatamente'
            else:
                print 'El juego ha terminado'
                break
        else:
            print 'El juego ha terminado'
            break
        n = int(raw_input(' Ingrese su carta nuevamente: '))
    n = int(raw_input(' Ingrese su carta nuevamente: '))
