import validaciones as val
import obtener

def buscar_limite_CM (matriz: list[list], tipo: str, indice_dato: int) -> int:
    '''
    Busca el máximo o mínimo, dentro del indice indicado para matrices CM

    Parámetros: La matriz a analizar, si busca Maximo o Minimo, indice de la columna que contiene los datos a evaluar

    Retorna: El número máximo o mínimo
    '''

    cant_columnas = len(matriz[indice_dato])
    limite_encontrado = 0

    for indice in range(cant_columnas):
        valor_evaluado = obtener.obtener_dato_de_indice(matriz, indice_dato, indice)
        if tipo == "Maximo":
            if limite_encontrado == 0 or limite_encontrado < valor_evaluado:
                limite_encontrado = valor_evaluado
        else:
            if limite_encontrado == 0 or limite_encontrado > valor_evaluado:
                limite_encontrado = valor_evaluado

    print(f"El valor {tipo} encontrado es: {limite_encontrado}")

    return limite_encontrado

def buscar_limite_RM (matriz:list[list], tipo: str, indice_dato: int) -> int:
    '''
    Busca el máximo o mínimo, dentro del indice indicado para matrices RM

    Parámetros: La matriz a analizar, si busca Maximo o Minimo, indice de la columna que contiene los datos a evaluar

    Retorna: El número máximo o mínimo
    '''
    limite_encontrado = 0
    columnas = len(matriz)
    for indice in range(columnas):
        valor_evaluado = matriz[indice][indice_dato]
        if tipo == "Maximo":
            if limite_encontrado == 0 or limite_encontrado < valor_evaluado:
                limite_encontrado = valor_evaluado
        else:
            if limite_encontrado == 0 or limite_encontrado > valor_evaluado:
                limite_encontrado = valor_evaluado
        
    print(f"El valor {tipo} encontrado es: {limite_encontrado}")

    return limite_encontrado