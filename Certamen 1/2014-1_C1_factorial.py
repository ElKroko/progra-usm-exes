# calculo de n!
n = int(raw_input('Numero: '))
r = 1
while n > 0:
    r = r * n 
    n = n - 1
print r
