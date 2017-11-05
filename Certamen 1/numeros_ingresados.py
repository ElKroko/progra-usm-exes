c = 0
p = 0
n = int(raw_input('Ingrese un valor: '))
while n != 0:
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (n * 3 ) + 1
        p = p + 1
    c = c + 1
    p = p + 1
    n = int(raw_input('Ingrese un nuevo valor: '))

print 'La cantidad de numeros ingresada fue ', c, ' y la cantidad de pasos fue ', p
