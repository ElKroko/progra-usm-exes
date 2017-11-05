voto = [(1,0,0), (0,0,1), (0,1,0), (1,0,0), (1,0,1), (0,0,0)]

def a_quien_voto(l_t):
    l = list()
    for voto in l_t:
        p, c, d = voto
        if p ==1:
            if c == 0 and d == 0:
                print voto, 'Voto para Pedro'
                l.append('Pedro')
            else:
                print voto, 'Voto nulo'
                l.append('nulo')
        elif c == 1:
            if p == 0 and d == 0:
                print voto, 'Voto para Claudio'
                l.append('Claudio')
            else:
                print voto, 'Voto nulo'
                l.append('nulo')
        elif d == 1:
            if p == 0 and c == 0:
                print voto, 'Voto para Darcy'
                l.append('Darcy')
            else:
                print voto, 'Voto nulo'
                l.append('nulo')
        else:
            print voto, 'Voto blanco'
            l.append('Blanco')
    return l

def resultados_votacion(lista_votos):
    a = a_quien_voto(lista_votos)
    d = {}
    d['Darcy'] = a.count('Darcy')
    d['Blanco'] = a.count('Blanco')
    d['nulo'] = a.count('nulo')
    d['Claudio'] = a.count('Claudio')
    return d

def ganador(lista_votos):
    a = resultados_votacion(lista_votos)
    lista = a.items()
    c = -1  
    cont_votos = 0
    empate = False
    nombreganador = ''
    for nom, votos in lista:
        if votos > c:
            c = votos
            nombreganador = nom
            cont_votos += 1
            empate = False
        elif votos == c:
            cont_votos +=1
            empate = True
    porcentaje = float(c * 100 / cont_votos)
    if empate :
        print 'Empate, con un ', porcentaje, '% de votos.'
    print nombreganador, 'ha ganado las elecciones con un ', porcentaje, '% de votos.'
''
a_quien_voto(voto)
resultados_votacion(voto)
ganador(voto) 
'''