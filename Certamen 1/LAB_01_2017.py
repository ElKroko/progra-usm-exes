# A

def nivel_contaminante(contaminante, valor_emision):
    if 'C' in contaminante:
        if valor_emision < 1000:
            return 'BAJO'
        elif valor_emision < 25000:
            return 'MEDIO'
        else:
            return 'CRITICO'
    else:
        if valor_emision < 200:
            return 'BAJO'
        elif valor_emision < 500:
            return 'MEDIO'
        else:
            return 'CRITICO'

# B

def impuesto(contaminante, valor_emision):
    nivel = nivel_contaminante(contaminante, valor_emision)
    if valor_emision < 200 and nivel == 'BAJO':
        valor = valor_emision * 1000
    elif valor_emision < 500 and nivel == 'MEDIO':
        valor = valor_emision * 3000
    elif valor_emision > 500 and 'M' in contaminante:        # Solo funciona para MP < 25000
        valor = valor_emision * 5000
    elif valor_emision < 1000 and nivel == 'BAJO':
        valor = valor_emision * 5000
    elif valor_emision < 25000 and nivel == 'MEDIO':
        valor = valor_emision * 7000
    elif valor_emision >= 25000 and nivel == 'CRITICO':
        valor = valor_emision * 10000
    return valor

# C
CO2_total = 0
while CO2_total < 50000:
    nombre = raw_input('Ingrese la central: ')      # Para primera central
    per1 = int(raw_input('Periodo: '))
    CO2_1 = int(raw_input('Emision CO2: '))
    MP1 = int(raw_input('Emision MP: '))
    per2 = int(raw_input('Periodo: '))
    CO2_2 = int(raw_input('Emision CO2: '))
    MP2 = int(raw_input('Emision MP: '))
    CO2_total_a = CO2_1 + CO2_2
    MP_total_a = MP1 + MP2
    MP_MAX = 0
    CO2_MAX = 0
    NAME_MAX = ''
    if CO2_total_a > CO2_MAX:
        CO2_MAX = CO2_total_a
        MP_MAX = MP_total_a
        NAME_MAX = nombre
    CO2_total += CO2_total_a
print 'Central que mas contamino:', NAME_MAX
total_impuesto = impuesto('CO2', CO2_MAX) + impuesto('MP', MP_MAX)
print 'Impuesto a pagar:', total_impuesto
