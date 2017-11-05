def saldo_critico(umbral, saldo, personas):
    a = list()
    b = list()
    for id, cash in saldo:
        if cash < umbral:
            a.append(id)
    for rut, id in personas:
        if id in a:
            b.append(rut)
    return b

def actualizar_saldo(monto, umbral, saldo, personas):
    saldo1 = list()
    for id, cash in saldo:
        if cash < umbral:
            cash += monto
        saldo1.append((id,cash))
    return saldo1

saldo = [(1212,10500), (78461,7200), (45,500)]
personas = [('12.345.678-9', 1212),('9.876.432-5', 78461), ('18663658-5', 45)]
umbral = int(raw_input('Ingrese valor minimo: '))
monto = int(raw_input('Ingrese monto a cargar: '))
print saldo_critico(umbral,saldo,personas)
print actualizar_saldo(monto,umbral,saldo,personas)