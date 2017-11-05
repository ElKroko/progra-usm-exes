# hacer un programa que simule el proceso de evaluacion crediticia de un banco
# se debe validar que la edad minima de la persona es 18 anos, que sus ingresos son mayores a sus egresos,
# y que al final del mes la persona pueda pagar la cuota de su prestamo.
# La cuota esta definida como el monto pedido entre el numero de meses
# en que se desea pagar dicho prestamo.

edad = int(raw_input('Ingrese su edad: '))
ing = int(raw_input('Ingrese sus ingresos: '))
out = int(raw_input('Ingrese sus egresos: '))
saldo = ing - out
import math

if edad >= 18:
    if saldo > 0:
        print 'El cliente esta aprobado para pedir un credito con una cuota de valor maximo ',saldo,'mensuales.'
        total = float(raw_input('Ingrese el monto de su credito a pedir: '))
        min_cuotas = total / saldo
        print 'La cantidad minima de cuotas que usted debe pedir es de ', math.ceil(min_cuotas), 'para poder pedir su credito.'
        cuota = int(raw_input('Por favor ingrese la cantidad de cuotas que desea pedir: '))
        pagar = total / cuota
        if cuota >= min_cuotas:
            print 'Felicidades, su credito ha sido aprobado.'
            print 'Usted debera pagar un total de ', pagar, 'mensual.'
        else:
            print 'Lo sentimos, la cantidad de cuotas ingresada no es suficiente.'
    else:
        print 'Lo sentimos, usted no cumple los requisitos para pedir un credito'
else:
    print 'Lo sentimos, usted no cumple el requisito minimo de edad.'