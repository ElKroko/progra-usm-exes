#   A)
def valida(cadena):
    p = 0
    while p < len(cadena):
        if cadena[p] == 'A' or cadena[p] == 'G' or cadena[p] == 'T' or cadena[p] == 'C' or cadena[p] == ' ':
            p += 1
        else:
            return False
    return True

#   B)
def cantidad(cadena, base):
    p = 0
    veces = 0
    while p < len(cadena):
        if base == cadena[p]:
            veces += 1
        p += 1
    return veces

#   C)
def patito(cadena):
    A = cantidad(cadena, 'A')
    G = cantidad(cadena, 'G')
    C = cantidad(cadena, 'C')
    T = cantidad(cadena, 'T')
    CG = C + G
    AT = A + T
    if CG > AT:
        return True
    else:
        return False

total = int(raw_input('Cantidad de cadenas de ADN: '))
i = 0
p = 1
mala = 0
vegetal = 0
animal = 0
while i < total:
    cadena = raw_input('Ingrese cadena'+' '+str(p)+ ':'+' ')
    ok = valida(cadena)
    if not ok:
        mala += 1
    else:
        a = patito(cadena)
        if a:
            vegetal += 1
        else:
            animal += 1
    i += 1
    p += 1
print 'Cantidad animales:', animal
print 'Cantidad vegetales:', vegetal
print 'Cantidad no validas;', mala