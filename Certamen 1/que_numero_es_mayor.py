a = int(raw_input('Ingrese un numero '))
b = int(raw_input('Ingrese otro numero '))
es_mayor = True
if a == b:
    print a, 'es igual a ', b
elif a - b > 0:
    print a, 'es mayor a ', b
else:
    print b, 'es mayor a ', a

