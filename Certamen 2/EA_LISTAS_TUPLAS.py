dias_mes = [31,28,31,30,
            31,30,31,31,
            30,31,30,31]
def dia_siguiente(f):
    x,y,z = f
    if z == dias_mes[y-1]:
        z = 1
        y += 1
    else:
        z = z+1
    fe = (x,y,z)
    return fe


def dias_entre(f1, f2):
    a1, m1, d1 = f1
    a2, m2, d2 = f2

    if (f1 < f2):
        mayor = f2
        menor = f1
    else:
        mayor = f1
        menor = f2
    c = 0
    while menor < mayor:
        c += 1
        menor = dia_siguiente(menor)
    return c

dia = int(raw_input('Dia: '))
mes = int(raw_input('Mes: '))
anio = int(raw_input('Anio: '))
nacimiento = (anio,mes,dia)

dia = int(raw_input('Dia: '))
mes = int(raw_input('Mes: '))
anio = int(raw_input('Anio: '))
hoy = (anio,mes,dia)

print dias_entre(nacimiento,hoy)