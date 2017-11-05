def valida(cadena):
    i = 0
    while i < len(cadena):
        if cadena[i] != 'C' and cadena[i] != 'G' and cadena[i] != 'T' and cadena [i] != 'A' and cadena [i] != ' ':
            return False
        i +=1
    return True
def cantidad(cadena,base):
    n = 0
    i = 0
    while i < len(cadena):
        if cadena [i] == base:
            n += 1
        i +=1
    return n
cantidad_cadenas = int(raw_input('Cantidad de cadenas de ADN:'))
animal = 0
vegetal = 0
no_valida = 0
i = 1
while i <= cantidad_cadenas:
    cadena = str(raw_input('Ingrese cadena'+str(i)+':'))
    if valida(cadena):
        A = cantidad(cadena,'A')
        T = cantidad(cadena,'T')
        G = cantidad(cadena,'G')
        C = cantidad(cadena,'C')
        if C + G < A + T:
            animal +=1
        else:
            vegetal +=1
    else:
        no_valida +=1
    i +=1
print 'Cantidad animales:',animal
print 'Cantidad vegetales:',vegetal
print 'Cantidad no validas:',no_valida

    
            
