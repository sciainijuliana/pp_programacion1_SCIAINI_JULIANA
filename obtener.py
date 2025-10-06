import validaciones as val

def obtener_dato_de_indice(matriz: list[list], indice_fila: int, indice_columna: int):
    '''
    Obtiene el dato que se encuentra en una coordenada específica de la matriz
    Parámetros: La matriz a recorrer, el indice_fila del dato buscado, el indice_columna del dato buscado
    Retorna: El dato buscado
    '''
    return matriz[indice_fila][indice_columna]

def obtener_fila (matriz: list[list], indice_fila: int):
    '''
    Obtiene/crea una fila entera para una matriz
    Parámetros: La matriz a recorrer, el indice_fila en el que se buscará la fila
    Retorna: La fila completa
    '''
    fila_nueva = []

    for indice_col in range(len(matriz)):
        fila_nueva.append(obtener_dato_de_indice(matriz, indice_col, indice_fila))

    return fila_nueva

def obtener_info_personaje () -> list:
    '''
    Solicita cada dato que necesito para agregar un nuevo personaje y los valida
    Parámetros: Nada, pide cada dato dentro de la función
    Retorna: Una lista con todos los datos validados del personaje nuevo
    '''

    personaje = []

    print("Para ingresar un nuevo personaje requerimos los siguientes datos: ")

    nombre = input("Nombre: ")
    nombre_val = val.validar_dato(nombre, "str")
    personaje.append(nombre_val)

    alias = input("Alias: ")
    alias_val = val.validar_dato(alias, "str")
    personaje.append(alias_val)

    raza = input("Raza: ")
    raza_val = val.validar_dato(raza, "str")
    personaje.append(raza_val)

    genero = input("Genero: ")
    genero_val = val.validar_dato(genero, "str")
    personaje.append(genero_val)

    inteligencia = input("Inteligencia (en número entero): ")
    inteligencia_val = val.validar_dato(inteligencia, "num")
    personaje.append(inteligencia_val)

    poder = input("Poder (en número entero): ")
    poder_val = val.validar_dato(poder, "num")
    personaje.append(poder_val)

    velocidad = input("Velocidad (en número entero): ")
    velocidad_val = val.validar_dato(velocidad, "num")
    personaje.append(velocidad_val)

    return personaje

def obtener_dato_fila (matriz:list[list], indice_columna):
    '''
    Obtiene el dato de cada coordenada de la matriz y los suma al informe
    Parámetros: La matriz a recorrer, el indice en el que la debe recorrer
    Retorna: Nada, realiza el print del informe
    '''
    info = ""

    for indice_fila in range(len(matriz)):

        dato = str(matriz[indice_fila][indice_columna])
        info += f"{dato[:15]}"
        
        if indice_fila < len(matriz) - 1:
            info = f"{info}, "
    
    print(info)

def obtener_str_filas (filas: list) -> str:
    '''
    Auxiliar de mostrar datos RM: Genera una fila auxiliar, para separar todos los personajes contenidos en una misma fila de la matriz
    Parámetros: Las filas (listas) a recorrer buscando más de un personaje
    Retorna: Un solo personaje de esa lista
    '''
    filas_str = ""
    for fila in filas:
        filas_str += f"{str(fila)}\n"
    return filas_str

def obtener_indice_limite_CM (matriz: list[list], indice_col: int, indice_limite: int, valor_limite: str, modo: str, indice_ordenar: int, tipo_dato: str) -> int:
    '''
    Auxiliar Selection Sort CM: Compara los valores de toda la matriz, para encontrar el límite (sea máximo o minimo)
    Parámetros: La matriz a recorrer, el indice de la columna inicial, el indice_limite, el modo (ASC o DES), el indice a ordenar, el tipo de dato (num o str)
    Retorna: El indice límite encontrado
    '''

    for indice_sig_col in range(indice_col + 1, len(matriz[indice_ordenar])):
        if tipo_dato == "num":
            valor_evaluado = float(obtener_dato_de_indice(matriz, indice_ordenar, indice_sig_col))
        else:
            valor_evaluado = str(obtener_dato_de_indice(matriz, indice_ordenar, indice_sig_col))

        if modo == "DES":
            if valor_evaluado > valor_limite:
                valor_limite = valor_evaluado
                indice_limite = indice_sig_col
        else:
            if valor_evaluado < valor_limite:
                valor_limite = valor_evaluado
                indice_limite = indice_sig_col
        
    return indice_limite

def obtener_indice_limite_RM(matriz: list[list], fila_actual: int, fila_limite: int, valor_limite: str, modo: str, indice_ordenar: int, tipo_dato: str) -> int:
    '''
    Auxiliar Selection Sort RM: Compara los valores de toda la matriz, para encontrar el límite (sea máximo o minimo)
    Parámetros: La matriz a recorrer, la fila que se está analizando, la fila limite, el valor limite, el modo (ASC o DES), el indice a ordenar, el tipo de dato (num o str)
    Retorna: La fila que será el límite para el selection sort
    '''
    for fila_sig in range(fila_actual + 1, len(matriz)):
        if tipo_dato == "num":
            valor_evaluado = float(matriz[fila_sig][indice_ordenar])
        else:
            valor_evaluado = str(matriz[fila_sig][indice_ordenar])

        if modo == "DES":
            if valor_evaluado > valor_limite:
                valor_limite = valor_evaluado
                fila_limite = fila_sig
        else:
            if valor_evaluado < valor_limite:
                valor_limite = valor_evaluado
                fila_limite = fila_sig

    return fila_limite

def obtener_razas (matriz: list[list], indice_a_evaluar) -> list: 
    '''
    Recorre la matriz, creando una lista con todas las razas
    Parámetros: La matriz a recorrer, el indice donde se encuentra el dato raza
    Retorna: La lista de razas
    '''

    razas = [] 
    columnas = len(matriz[indice_a_evaluar]) 
    for indice in range(columnas): 
        dato = obtener_dato_de_indice(matriz, indice_a_evaluar, indice) 
        if dato not in razas: 
            razas.append(dato) 
    return razas 

def obtener_indice_mayor_lista (lista: list, indice_actual: int, largo_lista: int, modo: str) -> int:
    '''
    Auxiliar Selection Sort Listas: Encuentra el indice en el que se encuentra el elemento mayor de la lista
    Parámetro: La lista a recorrer, el indice en el que se inicia, el largo de la lista, el modo en el que se ordenará (ASC o DES)
    ''' 
    indice_mayor_elemento = indice_actual
    for siguiente_indice in range(indice_actual + 1, largo_lista): 
        elemento_mayor = lista[indice_mayor_elemento] 
        siguiente_elemento = lista[siguiente_indice] 
        if elemento_mayor > siguiente_elemento and modo == "ASC": 
            indice_mayor_elemento = siguiente_indice 
        elif elemento_mayor < siguiente_elemento and modo == "DES": 
            indice_mayor_elemento = siguiente_indice 

    return indice_mayor_elemento

def obtener_nueva_fila (matriz:list[list], indice_columna:int) -> list:
    '''
    Obtiene la fila para agregar al momento de trasponer
    Parámetros: La matriz inicial, el indice columna: Donde encontrará cada dato de ese personaje
    Retorna: La fila obtenida con todos los datos de un personaje
    '''
    nueva_fila = []
    for indice_fila in range(len(matriz)):
        nueva_fila.append(matriz[indice_fila][indice_columna])

    return nueva_fila