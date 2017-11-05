grupo = {'rick':(172,10),
         'daryl':(136,11),
         'michonne':(80,6),
         'glenn':(73,0),
         'maggie':(55,4),
         'carl':(62,1),
         'tyreese':(35,0),
         'carol':(17,3) }

def total(grupo):
    a = grupo.items()
    suma_walkers = 0.0
    suma_humanos = 0.0
    for i in a:
        nom, tup = i
        walkers, humanos = tup
        suma_humanos += humanos
        suma_walkers += walkers
    b = (suma_walkers, suma_humanos)
    return b

def puntaje(grupo):
    a = total(grupo)
    total_walkers, total_humanos = a
    d = {}
    for i in grupo.items():
        nombre, tup = i
        walkers, humanos = tup
        punt = (walkers/total_walkers + 2*(humanos/total_humanos))
        d[nombre] = punt
    return d

def ranking(grupo):
    a = puntaje(grupo)
    b = a.items()
    c = []
    d = []
    for nom, punt in b:
        c.append((punt,nom))
    c.sort()
    c.reverse()
    for _, nombre in c:
        d.append(nombre)
    return d

print total(grupo)
print puntaje(grupo)
print ranking(grupo)