import validaciones as val
import obtener
import auxiliares as aux

def trasponer_matriz_CM (matriz: list[list]) -> list[list]:
    '''
    Traspone la matriz, que inicialmente se encuentra en formato COLUMN MAJOR
    Parametros: matriz
    Retorna: La matriz Traspuesta
    '''
    matriz_nueva = []

    cant_columnas = len(matriz[0])
    for indice_columna in range(cant_columnas):
        nueva_fila = obtener.obtener_nueva_fila(matriz, indice_columna)
        matriz_nueva.append(nueva_fila)

    return matriz_nueva

def trasponer_matriz_RM (matriz: list[list]) -> list[list]:
    '''
    Traspone la matriz, que inicialmente se encuentra en formato ROW MAJOR
    Parametros: matriz
    Retorna: La matriz Traspuesta
    '''

    matriz_t = [[],[],[],[],[],[],[]]
    for indice_fila in range(len(matriz)):
        fila = matriz[indice_fila]
        matriz_t = aux.insertar_dato(fila, matriz_t)
    return matriz_t