import validaciones as val
import obtener
import filtrar

def ordenar_filas_CM (matriz:list[list], indice_col: int, indice_limite: int) -> list[list]:
    '''
    Auxiliar del Selection Sort CM: Ordena las filas para el selection sort
    Parámetros: La matriz a ordenar, el indice de la columna a analizar, el indice límite obtenido en el for del selection sort
    Retorna: La matriz con las filas ordenadas
    '''
    for indice_fila in range(len(matriz)):
        matriz[indice_fila][indice_col], matriz[indice_fila][indice_limite] = \
            matriz[indice_fila][indice_limite], matriz[indice_fila][indice_col]
        
    return matriz

def ordenar_matriz_ss_col(matriz: list[list], indice_ordenar: int, modo: str, tipo_dato: str) -> list[list]:
    '''
    Ordena las columnas según el dato a evaluar (para matrices COLUMN MAJOR)
    Parámetros: La matriz a ordenar, el índice que debe usar para ordenarla, el modo en que se quiere ordenar (ASC o DES)
    Retorna: La matriz ordenada
    '''

    for indice_col in range(len(matriz[indice_ordenar]) - 1):
        indice_limite = indice_col
        if tipo_dato == "num":
            valor_limite = float(obtener.obtener_dato_de_indice(matriz, indice_ordenar, indice_col))
        else:
            valor_limite = str(obtener.obtener_dato_de_indice(matriz, indice_ordenar, indice_col))

        indice_limite = obtener.obtener_indice_limite_CM(matriz, indice_col, indice_limite, valor_limite, modo, indice_ordenar, tipo_dato)

        if indice_limite != indice_col:
            matriz = ordenar_filas_CM(matriz, indice_col, indice_limite)

    return matriz

def ordenar_fila_RM(matriz: list[list], fila_actual: int, fila_limite: int) -> list[list]:
    '''
    Auxiliar del Selection Sort RM: Ordena las filas para el selection sort
    Parámetros: La matriz a ordenar, el indice de la fila que se está analizando, la fila límite obtenida en el for del selection sort
    Retorna: La matriz con las filas ordenadas
    '''

    matriz[fila_actual], matriz[fila_limite] = matriz[fila_limite], matriz[fila_actual]

    return matriz

def ordenar_matriz_ss_RM(matriz: list[list], indice_ordenar: int, modo: str, tipo_dato: str) -> list[list]:
    '''
    Ordena las filas según el dato a evaluar (para matrices ROW MAJOR)
    Parámetros: La matriz a ordenar, el índice de columna que debe usar para ordenarla, el modo en que se quiere ordenar (ASC o DES), el tipo de dato que será ordenado (num o str)
    Retorna: La matriz ordenada
    '''

    for fila_actual in range(len(matriz) - 1):
        fila_limite = fila_actual
        valor_limite = float(matriz[fila_actual][indice_ordenar])

        fila_limite = obtener.obtener_indice_limite_RM(matriz, fila_actual, fila_limite, valor_limite, modo, indice_ordenar, tipo_dato)

        if fila_limite != fila_actual:
            matriz = ordenar_fila_RM(matriz, fila_actual, fila_limite)

    return matriz

def ordenar_ss_lista (lista: list, modo: str) -> list: 
    '''
    Selection sort para listas
    Parámetros: La lista a ordenar, el modo en que se quiere ordenar (ASC o DES)
    Retorna: La lista ordenada
    '''
    largo_lista = len(lista) 
    for indice_actual in range(largo_lista - 1): 
        indice_mayor_elemento = obtener.obtener_indice_mayor_lista(lista, indice_actual, largo_lista, modo) 
        if indice_mayor_elemento != indice_actual: 
            auxiliar = lista[indice_actual] 
            lista[indice_actual] = lista[indice_mayor_elemento] 
            lista[indice_mayor_elemento] = auxiliar 
    return lista 

def ordenar_personalizado (matriz: list[list]) -> list[list]:
    '''
    Especifica para el orden solicitado. Primero crea la lista de razas, luego la ordena alfabéticamente, 
    en base a esta lista filtra cada raza y la ordena esa última matriz por poder asc. 

    Parámetros: La matriz a ordenar

    Retorna: La matriz ordenada en base al orden personalizado
    '''

    razas = obtener.obtener_razas(matriz, 2)
    razas = ordenar_ss_lista(razas, "ASC") 
    matriz_filtrada = []
    for raza in razas:
        matriz_aux = filtrar.filtrar_str(matriz, raza, 2, True)
        matriz_aux = ordenar_matriz_ss_RM(matriz_aux, 5, "ASC", "num")

        matriz_filtrada.append(matriz_aux)

    return matriz_filtrada