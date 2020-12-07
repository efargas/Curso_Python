import numpy

# Numpy Array 2-D
sudoku = numpy.array([[0,9,0,0,0,0,0,6,0],
                       [0,0,0,7,0,3,0,0,0],
                       [2,0,8,9,0,1,3,0,5],
                       [4,5,0,1,3,7,0,8,6],
                       [0,0,0,0,0,0,0,0,0],
                       [7,6,0,4,2,8,0,9,3],
                       [9,0,4,6,0,2,7,0,1],
                       [0,0,0,8,0,4,0,0,0],
                       [0,7,0,0,0,0,0,5,0]])

s = \
        """\
        +-------+-------+-------+
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        +-------+-------+-------+
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        +-------+-------+-------+
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        +-------+-------+-------+
        """
def unpack(iterable):
    """
    list(unpack([[1, 2], [3, 4]]))
    [1, 2, 3, 4]
    """
    for item in iterable:
        yield from item

print(s.format(*(unpack(sudoku))))

def posible(tablero,fila,columna,numero):   
    if numpy.sum(tablero[:,columna] == numero) !=0: return False                            # Si se repite el número en la columna return False
    if numpy.sum(tablero[fila,:] == numero) !=0: return False                               # Si se repite el número en la fila return False
    fila0, columna0 = (fila//3)*3, (columna//3)*3                                           # Buscamos las coordenadas del cuadrado 3x3
    if numpy.sum(tablero[fila0:fila0+3,columna0:columna0+3] == numero) !=0: return False    # Si se repite el número en el cuadrado return False
    return True                                                                             # Se cumplen las normas del juego, número posible return True


def solucionador(tablero):
    filas, columnas = numpy.where(tablero == 0)             #crea dos arrays con coordenadas de las posiciones donde hay ceros
    for fila in filas:
        for columna in columnas:
            for num in range(1,10):
                if posible(tablero,fila,columna,num):       # Comprobar el numero
                    tablero[fila,columna] = num             # Si el numero es válido para la posición lo añadimos al array
                    solucionador(tablero)                   # Función recursiva para encontrar el siguiente número
                    tablero[fila, columna] = 0              # Si no encuentra el número ponemos un 0 en el array y empezamos de nuevo
            return
    print(s.format(*(unpack(sudoku))))

solucionador(sudoku)
