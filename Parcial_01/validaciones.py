def validar_carga_matriz (matriz: list[list]):
    if len(matriz) != 0:
        return True
    else:
        print('ERROR: Inicializa la matriz en la opcion 1.')
        return False

def validar_input_en_rango (min: int, max: int) -> int:
    eleccion_str = input("Ingrese una opción: ")

    if eleccion_str.isdigit():
        eleccion = int(eleccion_str)
        if eleccion < min or eleccion > max:
            print ("ERROR: Elija una opción válida!")
            return validar_input_en_rango(min, max)
        else:
            return eleccion
    else:
        print("ERROR: Elija una opción válida!")
        return validar_input_en_rango(min, max)
    
def obtener_dato_de_indice(matriz: list[list], indice_fila: int, indice_columna: int):
    return matriz[indice_fila][indice_columna]

def obtener_fila (matriz: list[list], indice_fila: int):
    fila_nueva = []

    for indice_col in range(len(matriz)):
        fila_nueva.append(obtener_dato_de_indice(matriz, indice_col, indice_fila))

    return fila_nueva

def solicitar_dato ():
    '''
    Solicita un dato al usuario
    No recibe parámetros
    Retorna la acción de pedir un dato
    '''
    return input("Ingrese su dato: ")

def validar_dato (dato: str, tipo: str):
    '''
    Valida recursivamente el dato ingresado por el usuario, según el tipo de dato que necesite
    Parámetros: El dato y el tipo de dato buscado (str o num)
    Retorna: El dato validado
    '''
    if tipo == "str":
        if dato.isalpha():
            return dato
        else:
            print("Error! Intente nuevamente")
            nuevo_dato = solicitar_dato()
            return validar_dato(nuevo_dato, "str")

    elif tipo == "num":
        if dato.isdigit():
            dato_fin = int(dato)
            return dato_fin
        else:
            print("Error! Intente nuevamente")
            nuevo_dato = solicitar_dato()
            return validar_dato(nuevo_dato, "num")
