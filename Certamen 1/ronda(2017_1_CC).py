def ronda(a,b,c):       # En esta funcion comparamos los puntajes y vemos el mayor.
    if a > b:
        if a > c:
            return a
        else:
            return c
    elif b > a:
        if b > c:
            return b
        else:
            return c

a = int(raw_input('Ingrese un puntaje: '))
b = int(raw_input('Ingrese un puntaje: '))
c = int(raw_input('Ingrese un puntaje: '))

print ronda(a,b,c)
