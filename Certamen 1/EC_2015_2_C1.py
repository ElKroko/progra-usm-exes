def codigo_palabra(codigo):
    d = ''
    p = -1
    while len(d)<(len(codigo)/2.0):
        d = d + codigo[p]
        p += -2
    return d

def codigo_hora(codehora):
    i = 0
    hh = 0
    mm = 0
    leyo_dos_puntos = False
    while i < len(codehora):
        if codehora[i] == ':':
            leyo_dos_puntos = True
        else:
            if leyo_dos_puntos:
                mm += int(codehora[i])
            else:
                hh += int(codehora[i])
        i += 1
    hh = hh % 24
    mm = mm % 60
    hora = str(hh) + ':' + str(mm)
    return hora

code1 = raw_input('Ingrese codigo: ')
code2 = raw_input('Ingrese codigo: ')
code3 = raw_input('Ingrese codigo: ')
code4 = raw_input('Ingrese codigo: ')

decode1 = codigo_palabra(code1)
decode2 = codigo_palabra(code2)
decode3 = codigo_hora(code3)
decode4 = codigo_palabra(code4)

print 'El mensaje es:', decode1, decode2, decode3
print decode4