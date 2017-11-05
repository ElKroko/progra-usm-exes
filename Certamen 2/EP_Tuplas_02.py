### Supermercado ###

productos = [
    (41419, 'Fideos',        450, 210),     #codigo, nombre, precio, unidades.
    (70717, 'Cuaderno',      900, 119),
    (78714, 'Jabon',         730, 708),
    (30877, 'Desodorante',  2190,  79),
    (47470, 'Yogur',          99, 832),
    (50809, 'Palta',         500,  55),
    (75466, 'Galletas',      235,   0),
    (33692, 'Bebida',        700,  20),
    (89148, 'Arroz',         900, 121),
    (66194, 'Lapiz',         120, 900),
    (15982, 'Vuvuzela',    12990,  40),
    (41235, 'Chocolate',    3099,  48),
]

clientes = [
    ('11652624-7', 'Perico Los Palotes'),       #Rut, nombre
    ( '8830268-0', 'Leonardo Farkas'),
    ( '7547896-8', 'Fulanita de Tal'),
]

ventas = [
    (1, (2010,  9, 12),  '8830268-0'),      # Numero de boleta, fecha de venta, rut cliente
    (2, (2010,  9, 19), '11652624-7'),
    (3, (2010,  9, 30),  '7547896-8'),
    (4, (2010, 10,  1),  '8830268-0'),
    (5, (2010, 10, 13),  '7547896-8'),
    (6, (2010, 11, 11), '11652624-7'),
]

itemes = [
    (1, 89148,  3),     # Numero de boleta, codigo de producto, cantidad
    (2, 50809,  4),
    (2, 33692,  2),
    (2, 47470,  6),
    (3, 30877,  1),
    (4, 89148,  1),
    (4, 75466,  2),
    (5, 89148,  2),
    (5, 47470, 10),
    (6, 41419,  2),
]

def producto_mas_caro(productos):
    valor = list()
    for _, nombre, precio, _ in productos:
        valor.append((precio, nombre))
    valor.sort ()
    valor.reverse()
    i = valor[0]
    p, n = i
    return n

def valor_total_bodega(productos):
    sum = 0
    for _, _, precio, cant in productos:
        sum += precio * cant
    return sum

def ingreso_total_por_ventas(itemes, productos):
    d = {}
    s = 0
    for _, codigo, cantidad in itemes:
        if codigo not in d:
            d[codigo] = cantidad
        else:
            d[codigo] += cantidad
    lista = d.items()
    for cod, cant in lista:
        for codi, _, precio, _ in productos:
            if cod == codi:
                s += cant * precio
    return s

def producto_con_mas_ingresos(itemes, productos):
    d = {}
    for _, codigo, cantidad in itemes:
        if codigo not in d:
            d[codigo] = cantidad
        else:
            d[codigo] += cantidad
    lista = d.items()
    l_nombre = list()
    for cod, cant in lista:
        for codi, nombre, precio, _ in productos:
            if cod == codi:
                if codi not in l_nombre:
                    l_nombre.append((cant*precio, nombre))
    l_nombre.sort()
    l_nombre.reverse()
    _, name = l_nombre[0]
    return name

def cliente_que_mas_pago(itemes, productos, clientes):
    pago_cliente = {}
    for boleta, codigo, cantidad in itemes:
        for bol, _, rut in ventas:
            if boleta == bol:
                for rut_cliente, nombre in clientes:
                    if rut_cliente == rut:
                        if nombre not in pago_cliente:
                            pago_cliente[nombre] = (codigo, cantidad)
                        else:
                            code, cant = pago_cliente[nombre]
                            cant += cantidad
                            pago_cliente[nombre] = (code, cant)
    lista_pagos = list()
    for i in pago_cliente:
        code_1, cant_1 = pago_cliente[i]
        for codigo_p, _, precio, _ in productos:
            if code_1 == codigo_p:
                lista_pagos.append((cant_1 * precio, i))
    lista_pagos.sort()
    lista_pagos.reverse()
    _, cliente = lista_pagos[0]
    return cliente

def total_ventas_del_mes(anno, mes, itemes, productos):
    total = 0
    for boleta, fecha, rut in ventas:
        f_anno, f_mes, _ = fecha
        if f_anno == anno and f_mes == mes:
            for i_boleta, i_codigo, i_cant in itemes:
                if i_boleta == boleta:
                    for p_codigo, _, p_precio, _ in productos:
                        if i_codigo == p_codigo:
                            total += p_precio * i_cant
    return total

def fecha_ultima_venta_producto(codigo, itemes, ventas):
    ult_fecha = (0,)
    for i_bol, i_cod, i_cant in itemes:
        if i_cod == codigo:
            for v_bol, v_fecha, _ in ventas:
                if v_bol == i_bol:
                    if v_fecha > ult_fecha:
                        ult_fecha = v_fecha
    return ult_fecha

print fecha_ultima_venta_producto(47470, itemes, ventas)