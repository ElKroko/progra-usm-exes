datos = {
        'Destructor': [('A', 1), ('F', 7)],
        'Caza' : [('B', 1), ('E', 4), ('H', 7), ('A', 3), ('C', 6)],
        'Bombardero': [('H', 8), ('G', 4), ('F', 1)]
}

'''Implementar un programa que sea capaz de analizar la informacion y representarla
en un plano. Para ello debe utilizar una Lista de listas, donde en cada casilla se
guarda la letra inicial del tipo de nave o un espacio (''), en caso de que no haya
una nave en esa posicion. ASUMA que no es posible que existan 2 naves en una misma
posicion.'''

# Cree la funcion annadir_nave(nombre, cordenada, plano) que reciba el nombre del
# tipo de nave, sus coordenadas en una tupla y una lista de listas. La funcion debe
# retornar la misma lista de listas (plano) con la nave annadida.

plano = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ',  ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ',  ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ',  ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ',  ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ',  ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ',  ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ',  ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ',  ' ']
]

def annadir_nave(nombre, coordenada, plano):
    x, y = coordenada           #Definimos el espacio de la lista de listas que ocupa la coordenada
    if x == 'A':
        x = 0
    elif x == 'B':
        x = 1
    elif x == 'C':
        x = 2
    elif x == 'D':
        x = 3
    elif x == 'E':
        x = 4
    elif x == 'F':
        x = 5
    elif x == 'G':
        x = 6
    elif x == 'H':
        x = 7
    lista = plano[x]
    if nombre == 'Bombardero':      #Reemplazamos el valor
        lista[y-1] = 'B'
    elif nombre == 'Caza':
        lista[y-1] = 'C'
    elif nombre == 'Destructor':
        lista[y-1] = 'D'
    plano[x] = lista                # Reincorporamos la lista modificada a la lista de listas
    return plano

def annadir_naves(datos):
    a = datos.items()
    for nom, coord in a:
        for coordenadas in coord:
            naves = annadir_nave(nom, coordenadas, plano)
    return naves

def dibujar_plano(plano):
    for list in plano:
        for i in range(len(list)):
            if list[i] == ' ':
                list[i] = '-'
    for i in range(8):
        lista = plano[i]
        for espacio in lista:
            print espacio,
        print ''



print annadir_nave('Caza', ('B',8), plano)
print ''
print annadir_naves(datos)
print ''
dibujar_plano(annadir_naves(datos))
