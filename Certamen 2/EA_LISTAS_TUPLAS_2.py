def todos_iguales(lista):
    b = len(lista)
    i = 1
    while i < b:
        if lista[i-1] != lista[i]:
            return False
        i += 1
    return True

def todos_distintos(lista):
    b = len(lista)
    i = 1
    while i < b:
        if lista[i-1] == lista[i]:
            return False
        i += 1
    return True

a = raw_input('Ingrese numeros: ')
lista = list(a)
if todos_iguales(lista):
    print 'Son todos iguales.'
elif todos_distintos(lista):
    print 'Son todos diferentes '

