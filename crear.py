import validaciones as val

def crear_matriz (*listas: list) -> list[list]:
    '''
    Crea una matriz
    Parámetros: Las listas que compondran la matriz
    Retorna: La matriz creada
    '''
    matriz = list(listas)
    print("Matriz cargada!")
    return matriz

def crear_personaje (matriz:list[list], personaje: list) -> list[list]:
    '''
    Agrega un personaje nuevo a la matriz
    Parámetros: La matriz original, y una lista con los datos del nuevo personaje
    Retorna: La matriz con el nuevo personaje agregado
    '''
    for indice_col in range(len(matriz)):
        matriz[indice_col].append(personaje[indice_col])
    print("Personaje agregado con éxito!")
    return matriz

