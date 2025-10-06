import validaciones as val
import obtener
def filtrar_str (matriz: list[list], dato_a_filtrar: str, indice_a_filtrar: int, contiene: bool) -> list[list]:
    '''
    Filtra la matriz según el dato brindado (dato de tipo str)
    Parámetros: La matriz a filtrar, el dato a buscar en la matriz
    Retorna: Una matriz auxiliar, con los personajes que cumplen
    '''
    personajes_filtrados = []
    personajes = matriz[indice_a_filtrar]

    for indice in range(len(personajes)):
        dato = obtener.obtener_dato_de_indice(matriz, indice_a_filtrar, indice)
        if contiene:
            if dato_a_filtrar in dato:
                fila_filtrada = obtener.obtener_fila(matriz, indice)
                personajes_filtrados.append(fila_filtrada)
        else:
            if dato_a_filtrar not in dato:
                fila_filtrada = obtener.obtener_fila(matriz, indice)
                personajes_filtrados.append(fila_filtrada)

    return personajes_filtrados

def filtrar_por_limite (matriz: list[list], indice_dato: int, limite: int, condicion: str) -> list[list]:
    '''
    Filtra la matriz segun el límite indicado
    Parámetros: La matriz a filtrar, el indice del dato que evaluará, el límite (max o min), la condicion (mayor o menor)
    Retorna: Una matriz con los que cumplan la condición
    '''

    cant_columnas = len(matriz[indice_dato])
    matriz_filtrada = []
    for indice in range(cant_columnas):
        if condicion == "mayor":
            valor_evaluado = obtener.obtener_dato_de_indice(matriz, indice_dato, indice)
            if valor_evaluado == limite:
                fila_nueva = obtener.obtener_fila(matriz, indice)
                matriz_filtrada.append(fila_nueva)
                print(f"{fila_nueva} con un valor de: {valor_evaluado}")
        else:
            valor_evaluado = obtener.obtener_dato_de_indice(matriz, indice_dato, indice)
            if valor_evaluado == limite:
                fila_nueva = obtener.obtener_fila(matriz, indice)
                matriz_filtrada.append(fila_nueva)
                print(f"{fila_nueva} con un valor de: {valor_evaluado}")

    return matriz_filtrada

def filtrar_valores_CM (matriz: list[list], indice_dato: int, condicion: str, valor: float) -> list[list]:
    '''
    Filtra los personajes que cumplan la condicion brindada de una matriz COLUMNA x Fila
    Parámetros: La matriz a filtrar, el indice a evaluar, que condicion debe cumplirse (mayor o menor), el valor a comparar
    Retorna: La matriz filtrada
    '''

    matriz_filtrada = []
    cant_columnas = len(matriz[indice_dato])

    for indice in range(cant_columnas):
        valor_evaluado = obtener.obtener_dato_de_indice(matriz, indice_dato, indice)
        if condicion == "mayor":
            iguales = "El/los personaje/s con el mismo valor es/son: \n"
            if valor_evaluado == valor:
                fila_nueva = obtener.obtener_fila(matriz, indice)
                iguales += f"{fila_nueva}\n"
            elif valor_evaluado > valor:
                fila_nueva = obtener.obtener_fila(matriz, indice)
                matriz_filtrada.append(fila_nueva)
        else:
            iguales = "El/los personaje/s con el mismo valor es/son: \n"
            if valor_evaluado == valor:
                fila_nueva = obtener.obtener_fila(matriz, indice)
                iguales += f"{fila_nueva}\n"
            elif valor_evaluado < valor:
                fila_nueva = obtener.obtener_fila(matriz, indice)
                matriz_filtrada.append(fila_nueva)

    return matriz_filtrada         

def filtrar_valores_RM(matriz: list[list], indice_dato: int, condicion: str, valor: float) -> list[list]:
    '''
    Filtra los personajes que cumplan la condicion brindada de una matriz FILA x Columna
    Parámetros: La matriz a filtrar, el indice a evaluar, que condicion debe cumplirse (mayor o menor), el valor a comparar
    Retorna: La matriz filtrada
    '''

    matriz_filtrada = []

    cant_filas = len(matriz)

    for indice in range(cant_filas):
        dato_evaluado = matriz[indice][indice_dato]
        if condicion == "mayor":
            if dato_evaluado > valor:
                fila_nueva = matriz[indice]
                matriz_filtrada.append(fila_nueva)
        elif condicion == "menor":
            if dato_evaluado < valor:
                fila_nueva = matriz[indice]
                matriz_filtrada.append(fila_nueva)
        elif condicion == "mayor o igual":
            if dato_evaluado >= valor:
                fila_nueva = matriz[indice]
                matriz_filtrada.append(fila_nueva)
        else:
            if dato_evaluado <= valor:
                fila_nueva = matriz[indice]
                matriz_filtrada.append(fila_nueva)

    return matriz_filtrada

def filtrar_personalizado (matriz: list[list], filtro: float) -> list[list]:
    '''
    Funcion especifica para el orden personalizado: filtra la matriz brindada en 3 columnas diferentes
    Parámetros: La matriz a filtrar, el valor por el cual debo filtrar
    Retorna: La matriz filtrada final
    '''
    matriz_aux = filtrar_valores_RM(matriz, 5, "menor", filtro)
    matriz_aux_2 = filtrar_valores_RM(matriz_aux, 4, "menor", filtro)
    matriz_aux_3 = filtrar_valores_RM(matriz_aux_2, 6, "menor", filtro)

    return matriz_aux_3

