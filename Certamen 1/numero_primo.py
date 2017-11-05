primo = True
d = 2
n = int(raw_input('Ingrese un numero: '))
while d < n:
    if n % d == 0:
        primo = False
        d = d + 1
    else:
        d = d + 1
if primo == True:
    print n, 'es primo'
else:   
    print n, 'no es primo'