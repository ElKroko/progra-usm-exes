canciones = {125:['River', 'Leon Bridges', {'R&B'}],
              1458: ['My Silver Lining', 'First Aid Kit', {'Folk', 'Rock'}],
              1502: ['Stay Gold', 'First Aid Kit', {'Folk', 'Rock'}],
              32: ['Sinnerman', 'Nina Simone', {'R&B', 'Jazz'}]
              }
mensual = [(1502, 607), (125, 54), (32, 607), (1502, 13)]  #En el ejercicio original, faltaba una tupla (cancion, repro)

''' Crear la funcion reproducciones(p1,p2) la cual reciba los diccionarios p1 (canciones)
y p2 (mensual). La funcion debe retornar un diccionario cuya llave sea el nombre de la cancion
y el valor sea la cantidad de veces reproducidas. Este diccionario entrega solo las canciones
que han sido reproducidas dicho mes.
'''

def reproducciones(p1,p2):
    match_id = []
    d = {}
    nombre = list()
    for id, repr in p2:
        if repr > 0:
            if id in p1:
                f = p1[id]
                nombre.append((f[0],repr))
    for i in nombre:
        d[i[0]] = i[1]
    return d
''' Crear la funcion pago_mes (p1,p2) donde p1 es canciones y p2 es lista mensual. La funcion debe retornar
el monto a pagar a cada artista en un diccionario, donde la llave es el nombre del artista y el valor
el monto a pagar. Por cada vez que se reproduce una cancion, Pytify paga $0.05.
'''
def pago_mes(p1,p2):
    artista = list()
    d = {}
    for id, repr in p2:
        if repr > 0:
            f = p1[id]
            artista.append((f[1],repr))
    for i in artista:
        d[i[0]] = i[1] * 0.05
    return d

''' Crear la funcion genero_mas_escuchado(p1,p2), donde p1 es canciones y p2 es lista mensual. La funcion
debe retornar una lista de los generos de musica escuchados en el mes, ordenados de forma descendente por nro
de reproducciones de canciones de cada genero. Si una cancion tiene mas de un genero, se debe considerar una
reproduccion de todos estos. 
'''
def genero_mas_escuchado(p1,p2):
    lista_repr = list()
    lista_final = {}
    lista_f = list()
    final = list()
    for id, repr in p2:
        f = p1[id]
        lista_repr.append((repr,f[2]))
    lista_repr.sort()
    lista_repr.reverse()
    for i in lista_repr:
        r, g = i
        for gen in g:
            if gen not in lista_final:
                lista_final[gen] = r
            else:
                lista_final[gen] += r
    lista = lista_final.items()
    for nom, rep in lista:
           lista_f.append((rep, nom))
    lista_f.sort()
    lista_f.reverse()
    for rep, nom in lista_f:
        final.append(nom)
    return final



print reproducciones(canciones, mensual)
print pago_mes(canciones,mensual)
print genero_mas_escuchado(canciones,mensual)