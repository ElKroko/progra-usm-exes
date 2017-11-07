estafados = [ #(rut, deuda, empresa, fecha),
    ('12.234.567-8', 2000000, 'pelados_furiosos', (25,5,2015)),
    ('9.111.567-k', 5500000,'multibank', (1, 10, 2014)),
    ('14.987.007-1', 100000000,'inversiones_seguras', (30, 11, 2016)),
    ('12.234.567-8', 10000000,'multibank', (2, 7, 2015)),
    ('12.234.567-8', 2500000,'multibank', (18, 1, 2016))
]

def estafado_por(lista,rut):
    estafa = []
    for i in lista:
        rut_l, deuda, empresa, fecha = i
        if rut_l == rut:
            if empresa not in estafa:
                estafa.append(empresa)
    if len(estafa) > 0:
        return estafa
    else:
        return 'Rut no estafado'

def ranking(estafados):
    d = {}
    for i in estafados:
        rut, deuda, empresa, fecha = i
        if empresa not in d:
            d[empresa] = deuda
        else:
            d[empresa] += deuda
    return d

def tupla_inversa(fecha):
    dia, mes, anno = fecha
    fecha_f = (anno,mes,dia)
    return fecha_f

def estafados_por_fecha(estafados, inicial, final):
    inicial_f = tupla_inversa(inicial)
    final_f = tupla_inversa(final)
    estafados_l = []
    for i in estafados:
        rut, deuda, empresa, fecha = i
        fecha_f = tupla_inversa(fecha)
        if fecha_f > inicial_f and fecha_f < final_f:
            estafados_l.append((deuda, rut))
    estafados_l.sort()
    estafados_l.reverse()
    estafados_f = []
    for deuda_i, rut_i in estafados_l:
        estafados_f.append((rut_i,deuda_i))
    return estafados_f



print estafados_por_fecha(estafados,(03,01,2016),(01,01,2017))      # Funcion 3


