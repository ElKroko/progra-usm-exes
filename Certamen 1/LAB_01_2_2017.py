print '..:: CAJA ::..'
print '1.- Realizar Pedido'
print '2.- Finalizar'
pedido = int(raw_input('Ingrese opcion: '))
cont_1_1 = 0
cont_1_2 = 0
cont_1_3 = 0
cont_2_1 = 0
cont_2_2 = 0
cont_3_1 = 0
cont_3_2 = 0
cont_combo = 0
precio = 0
preciocombo = 0
preciototal = 0
preciofiesta = 0
hamb = 0
bebida = 0
papas = 0
combo = False
hambur = False          #Para determinar su existencia dentro del pedido, y asi aplicar el descuento si las 3 se cumplen.
bebi = False
papasf = False
fiesta = False
while pedido == 1:
    print 'Productos'
    print '1.- Hamburguesas'
    print '2.- Papas Fritas'
    print '3.- Bebida'
    producto = int(raw_input('Ingrese producto: '))
    if producto == 1:
        hambur = True
        print 'Seleccione hamburguesa'
        print '1.- BigMac'
        print '2.- Tasty'
        print '3.- Fiesta'
        hamb = int(raw_input('Ingrese hamburguesa: '))
        if hamb == 1:
            precio += 2300
            cont_1_1 += 1
        elif hamb == 2:
            precio += 2750
            cont_1_2 += 1
        elif hamb == 3:
            fiesta = True
            precio += 1850
            cont_1_3 += 1
        else:
            print 'Por favor ingrese una opcion valida.'
    elif producto == 2:
        papasf = True
        precio += 1100
        print 'Agrandar papas: '
        print '1.- Si'
        print '2.- No'
        papas = int(raw_input('Desea agrandar las papas fritas? '))
        if papas == 1:
            precio += 200
            cont_2_2 += 1
        else:
            cont_2_1 += 1
    elif producto == 3:
        bebi = True
        precio += 900
        print 'Agrandar bebida: '
        print '1.- Si'
        print '2.- No'
        bebida = int(raw_input('Desea agrandar la bebida? '))
        if bebida == 1:
            precio += 200
            cont_3_2 += 1
        else:
            cont_3_1 += 1
    else:
        print 'Por favor ingrese una opcion valida.'

    print '..:: CAJA ::..'
    print '1.- Realizar Pedido'
    print '2.- Finalizar'
    pedido = int(raw_input('Ingrese opcion: '))

if hambur and bebi and papasf:
    preciocombo = precio * 0.8
    cont_combo += 1
    preciototal += preciocombo
    hambur = False
    bebi = False
    papasf = False
else:
    preciototal = precio

if fiesta and not bebi and not papasf:
    preciototal += preciofiesta
    fiesta = False
else:
    preciototal = precio

print '..:: RESUMEN PEDIDO ::..'
if hamb == 1:
    print cont_1_1, 'Hamburguesa BigMac'
elif hamb == 2:
    print cont_1_2, 'Hamburguesa Tasty'
else:
    print cont_1_3, 'Hamburguesa Fiesta'
if bebida == 1:
    print cont_3_2, 'Bebida Agrandada'
else:
    print cont_3_1, 'Bebida'
if papas == 1 and not combo:
    print cont_2_2, 'Papas Fritas Agrandadas'
elif papas == 2 and not combo:
    print cont_2_1, 'Papas Fritas'
if combo:
    print cont_combo, 'Combo',
    if hamb == 1:
        print 'BigMac'
    elif hamb == 2:
        print 'Tasty'
    else:
        print 'Fiesta'

print 'TOTAL BOLETA: '+ '$'+str(preciototal)