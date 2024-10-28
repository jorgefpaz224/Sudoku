import numpy as np
import random

tablero = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])

def imprimir_tablero(tablero):
    for fila in range(9):
        if fila % 3 == 0 and fila != 0:
            print("-----------------------")
        for columna in range(9):
            if columna % 3 == 0 and columna != 0:
                print(" | ", end="")
            if columna == 8:
                print(tablero[fila][columna])
            else:
                print(str(tablero[fila][columna]) + " ", end="")


def es_valido(tablero, num, fila, columna):

    if num in tablero[fila, :] or num in tablero[:, columna]:
        return False

    
    inicio_fila, inicio_col = (fila // 3) * 3, (columna // 3) * 3
    if num in tablero[inicio_fila:inicio_fila + 3, inicio_col:inicio_col + 3]:
        return False
    return True


imprimir_tablero(tablero)