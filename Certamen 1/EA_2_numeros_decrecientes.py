#Dado 3 numeros entregados por teclado, imprimirlos decrecientemente
n1 = int(raw_input('Ingrese el primer numero: '))
n2 = int(raw_input('Ingrese el segundo numero: '))
n3 = int(raw_input('Ingrese el tercer numero: '))

print 'El orden es',
if n1 > n2 and n1 > n3:
    print n1,
    if n2 > n3:
        print n2, n3
    else:
        print n3, n2
elif n2 > n1 and n2 > n3:
    print n2,
    if n1 > n3:
        print n1, n3
    else:
        print n3, n1
else:
    print n3,
    if n1 > n2:
        print n1, n2
    else:
        print n2, n1
