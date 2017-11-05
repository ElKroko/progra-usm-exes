n = int(raw_input('Ingrese un numero: '))
suma = 0
d = 1
while d < n:
    if n % d == 0:
        suma = suma + d
        d = d + 1
    else:
        d = d + 1

if n == suma:
    print n, 'es magico'
else:
    print n, 'no es magico'
print suma
print d
