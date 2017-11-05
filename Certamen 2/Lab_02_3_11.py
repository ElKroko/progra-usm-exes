paises = {
        # pais: (mensual_comida, mensual_alojamiento, pasajes, seguro, divisa)
        'Alemania' : (400, 250, 2000, True, 'euro'),
        'Japon' : (55000, 70000, 220000, False, 'yen'),
        'Francia' : (350, 200, 1900, True, 'euro'),
        'USA': (500, 400, 1200, True, 'dolar')
}

divisas = {'euro' : 740.0, 'dolar' : 630.0, 'yen' : 5.5}

''' Desarrolle una funcion llamada gasto_total(meses, monedas, informacion), que recibe un entero
 con la cantidad de meses, un diccionario con el valor de cada divisa en pesos chilenos
 y un diccionario con la informacion de los paises.
La funcion debe retornar un nuevo diccionario cuya clave es el nombre de un pais y valor el costo asociado en base 
a la informacion.

El seguro tiene un valor de 1000 dolares, siempre.
'''

def gasto_total(meses, monedas, informacion):
    a = informacion.items()
    total_pais = 0
    total = 0
    div_d = monedas.items()
    gasto = {}
    for pais, info in a:
        comida, alojo, pasaje, seguro, divisa = info
        total_pais = (comida + alojo) * meses + pasaje
        for moneda, precio in div_d:
            if moneda == divisa:
                total = total_pais * precio        #conversion a pesos chilenos
        if seguro:
            total += 1000 * monedas['dolar']
        gasto[pais] = total
    return gasto
'''
b) Desarrolle la funcion ranking(periodo, monedas, informacion), la cual recibe los mismos
parametros que la funcion anterior, pero retorna una lista con los nombres de los paises
ordenados por el costo total de vivir en el. (mas barato al mas caro)
'''

def ranking(periodo, monedas, informacion):
    a = gasto_total(periodo, monedas, informacion)
    tupla = a.items()
    ranking_valor = []
    ranking = list()
    for i in tupla:
        pais, valor = i
        ranking_valor.append((valor,pais))
    ranking_valor.sort()
    for i in ranking_valor:
        val, pa = i
        ranking.append(pa)
    return ranking


print gasto_total(3, divisas, paises)
print ranking(3, divisas, paises)