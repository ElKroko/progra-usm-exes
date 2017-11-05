def f(x):
    x = str(x)
    y = ''
    i = 0
    while i < len(x):
        y = x[i] + y
        i = i + 1
    while i >= 0:
        i = i - 1
        if not (y[i]==x[i]):        # negacion de preposicion
            return False
    return True

x = raw_input('holi')
y = f(x)

if y:
    print 'Sirve'
else:
    print 'No Sirve'