# El concurso consta de una serie de turnos, en los cuales cada alianza debe ingresar una palabra.
# La palabra con mayor cantidad de vocales gana. Si dos o mas alianzas igualan en el maximo de vocales
# nadie gana esa ronda. El concurso termina cuando una alianza logre ganar x juegos (meta), la cual se
# debe definir al incio del juego.

# A)    Escriba la funcion ganador(c1,c2,c3,meta) la cual recibe 4 parametros, la cantidad de juegos
#       ganados por alianza 1, 2 y 3 y la meta a lograr en el juego. La funcion debe retornar el numero
#       de la alianza ganadora. En caso de no existir ganador, debe retornar el valor entero 0.
#       NOTA: tener en cuenta que no pueden existir empates en las alianzas al momento de alcanzar la meta.

# B)    Escriba la funcion contar(palabra) que reciba uns tring palabra. La funcion debe retornar la cantidad
#       de vocales existentes en la palabra recibida.
#       NOTA: no puede utilizar el metodo count de procesamiento de texto.

def ganador(c1,c2,c3,meta):
    if c1 == meta:
        return 1
    elif c2 == meta:
        return 2
    elif c3 == meta:
        return 3
    else:
        return 0

def contar(palabra):
    vocales = 'aeiou'
    p = 0
    puntos = 0
    while p < len(palabra):
        if palabra[p] in vocales:
            puntos += 1
        p += 1
    return puntos

def ronda(a,b,c):       # En esta funcion comparamos los puntajes y vemos el mayor.
    if a > b and a > c:
        return 1
    elif b > a and b > c:
        return 2
    elif c > a and c > b:
        return 3
    else:
        return 0

meta = int(raw_input('Ingrese la meta del juego: '))
print 'El orden de las alianzas sera: '
print ' Alianza 1 -> Alianza 2 -> Alianza 3'
palabra1 = raw_input('alianza 1: ')
palabra2 = raw_input('alianza 2: ')
palabra3 = raw_input('alianza 3: ')
pc1 = contar(palabra1)
pc2 = contar(palabra2)
pc3 = contar(palabra3)
gana = ronda(pc1,pc2,pc3)
sc1 = 0
sc2 = 0
sc3 = 0
while gana == 0:
    palabra1 = raw_input('alianza 1: ')
    palabra2 = raw_input('alianza 2: ')
    palabra3 = raw_input('alianza 3: ')
    pc1 = contar(palabra1)
    pc2 = contar(palabra2)
    pc3 = contar(palabra3)
    gana = ronda(pc1, pc2, pc3)
if gana == 1:
    sc1 += 1
elif gana == 2:
    sc2 += 1
else:
    sc3 += 1
total = ganador(sc1,sc2,sc3,meta)
while total == 0:
    palabra1 = raw_input('alianza 1: ')
    palabra2 = raw_input('alianza 2: ')
    palabra3 = raw_input('alianza 3: ')
    pc1 = contar(palabra1)
    pc2 = contar(palabra2)
    pc3 = contar(palabra3)
    gana = ronda(pc1, pc2, pc3)
    while gana == 0:
        palabra1 = raw_input('alianza 1: ')
        palabra2 = raw_input('alianza 2: ')
        palabra3 = raw_input('alianza 3: ')
        pc1 = contar(palabra1)
        pc2 = contar(palabra2)
        pc3 = contar(palabra3)
        gana = ronda(pc1, pc2, pc3)
    if gana == 1:
        sc1 += 1
    elif gana == 2:
        sc2 += 1
    else:
        sc3 += 1
    total = ganador(sc1, sc2, sc3, meta)
print 'La alianza ganadora es:',total

