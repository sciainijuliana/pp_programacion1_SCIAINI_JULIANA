def solicitar_dato ():
    '''
    Solicita un dato al usuario
    No recibe parámetros
    Retorna la acción de pedir un dato
    '''
    return input("Ingrese su dato: ")

def insertar_dato (fila: list, matriz: list[list]) -> list[list]:
    '''
    Auxiliar de trasponer: Inserta el dato obtenido en la matriz, en el indice correspondiente
    Parámetros: Fila (una fila que contiene los datos del personaje), matriz (la matriz a la cual se lo añadirá)
    Retorna: La matriz con el dato añadido
    '''
    for indice_columna in range(len(fila)):
        matriz[indice_columna].append(fila[indice_columna])
    return matriz