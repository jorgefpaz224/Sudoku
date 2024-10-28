import numpy as np
import random


def generar_tablero_sudoku(celdas_vacias=40):
    tablero = np.zeros((9, 9), dtype=int)
    llenar_tablero(tablero)
    celdas = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(celdas)
    for _ in range(celdas_vacias):
        i, j = celdas.pop()
        tablero[i, j] = 0
    return tablero


def llenar_tablero(tablero):
    for i in range(9):
        for j in range(9):
            if tablero[i, j] == 0:
                numeros = list(range(1, 10))
                random.shuffle(numeros)
                for numero in numeros:
                    if es_valido(tablero, i, j, numero):
                        tablero[i, j] = numero
                        if llenar_tablero(tablero):
                            return True
                        tablero[i, j] = 0
                return False
    return True


def mostrar_tablero(tablero):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        fila = ""
        for j in range(9):
            if j % 3 == 0 and j != 0:
                fila += " | "
            fila += f"{tablero[i, j] if tablero[i, j] != 0 else '.'} "
        print(fila)


def es_valido(tablero, fila, columna, numero):
    # Verificar fila
    if numero in tablero[fila, :]:
        return False
    # Verificar columna
    if numero in tablero[:, columna]:
        return False
    # Verificar subcuadro 3x3
    inicio_fila, inicio_columna = (fila // 3) * 3, (columna // 3) * 3
    if numero in tablero[inicio_fila:inicio_fila+3, inicio_columna:inicio_columna+3]:
        return False
    return True
