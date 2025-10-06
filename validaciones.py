import auxiliares as aux

def validar_carga_matriz (matriz: list[list]):
    '''
    Valida que la matriz no se encuentre vacía
    Parámetros: La matriz a analizar
    Retorna: Un booleano según el resultado de la condición
    '''
    if len(matriz) != 0:
        return True
    else:
        print('ERROR: Inicializa la matriz en la opcion 1.')
        return False

def validar_input_en_rango (min: int, max: int) -> int:
    '''
    Solicita una elección al usuario, y valida recursivamente dicha elección, para confirmar que es un número, 
    y a su vez se encuentra en el rango indicado por los índices del menú

    Parámetros: min (el valor minimo a utilizar), max (el valor maximo a utilizar)
    
    Retorna: El número, validado, elegido por el usuario
    '''
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
            nuevo_dato = aux.solicitar_dato()
            return validar_dato(nuevo_dato, "str")

    elif tipo == "num":
        if dato.isdigit():
            dato_fin = int(dato)
            return dato_fin
        else:
            print("Error! Intente nuevamente")
            nuevo_dato = aux.solicitar_dato()
            return validar_dato(nuevo_dato, "num")
