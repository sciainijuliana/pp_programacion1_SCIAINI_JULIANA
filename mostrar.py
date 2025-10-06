import validaciones as val
import obtener

def mostrar_existencias_CM (matriz: list[list]):
    '''
    Muestra la cantidad de personajes que hay en la matriz completa de tipo CM
    Parámetros: La matriz a contar
    Retorna: Nada, hace un print con la cantidad de existencias
    '''

    existencias = len(matriz[0])
    print (f"Hay {existencias} existencias!")

def mostrar_existencias_RM (matriz: list[list]):
    '''
    Muestra la cantidad de personajes contenidos en una matriz RM
    Parámetros: La matriz a recorrer
    Retorna: Nada, hace un print de la cantidad de existencias
    '''
    existencias = len(matriz)
    print(f"Hay {existencias} existencias!")

def mostrar_datos_CM (matriz: list[list]):
    '''
    Muestra los datos de una matriz CM
    Parámetros: La matriz a mostrar
    Retorna: Nada, solo hace un print de la matriz acomodada
    '''
    columnas = len(matriz[0])

    nombre_columna = "|Nombre|Alias|Raza|Género|Inteligencia|Poder|Velocidad|"
    print(nombre_columna)

    for indice_columna in range(columnas):
        obtener.obtener_dato_fila(matriz, indice_columna)


def mostrar_datos_RM_lista_compuesta (matriz:list[list]):
    '''
    Muestra los datos de una matriz RM, que contiene listas dentro de listas
    Parámetros: La matriz a mostrar
    Retorna: Nada, solo hace un print de la matriz acomodada
    '''
    nombre_columna = "|Nombre|Alias|Raza|Género|Inteligencia|Poder|Velocidad|"
    print(nombre_columna)
    info = ""
    for indice_fila in range(len(matriz)):
        if len(matriz[indice_fila]) > 1:
            info += obtener.obtener_str_filas(matriz[indice_fila])
        else: 
            dato = str(matriz[indice_fila])
            info += f"{dato}\n"
    print (info)

def mostrar_datos_RM (matriz: list[list]):
    '''
    Muestra los datos de una matriz RM
    Parámetros: La matriz a mostrar
    Retorna: Nada, solo hace un print de la matriz acomodada
    '''
    nombre_columna = "|Nombre|Alias|Raza|Género|Inteligencia|Poder|Velocidad|"
    print(nombre_columna)
    info = ""
    for indice_fila in range(len(matriz)):
        dato = str(matriz[indice_fila])
        info += f"{dato}\n"
    print (info)