import validaciones as val
import filtrar
import obtener

def calcular_promedio_CM (matriz:list[list], indice_a_evaluar: int) -> float:
    '''
    Toma todos los valores de la columna a evaluar, los suma y calcula el promedio de una matriz Columna x Fila
    Parámetros: La matriz a evaluar, el indice donde encontrará los datos
    Retorna: El promedio
    '''

    cant_columnas = len(matriz[indice_a_evaluar])
    acumulador = 0

    for indice in range(cant_columnas):
        valor_obtenido = obtener.obtener_dato_de_indice(matriz, indice_a_evaluar, indice)
        acumulador += valor_obtenido

    promedio = acumulador / cant_columnas

    print(f"El promedio obtenido es: {promedio:.2f}")

    return promedio

def calcular_promedio_RM (matriz:list[list], indice_a_evaluar: int) -> float:
    '''
    Toma todos los valores de la columna a evaluar, los suma y calcula el promedio de una matriz Fila x Columna
    Parámetros: La matriz a evaluar, el indice donde encontrará los datos
    Retorna: El promedio
    '''

    cant_columnas = len(matriz)
    acumulador = 0

    for indice in range(cant_columnas):
        valor_obtenido = obtener.obtener_dato_de_indice(matriz, indice, indice_a_evaluar)
        acumulador += valor_obtenido

    promedio = acumulador / cant_columnas

    return promedio

def calcular_saiyan_power (matriz: list[list]) -> float:
    '''
    Calcula el saiyan power
    Parámetros: La matriz a utilizar (solo debe contener a los Saiyan)
    Retorna: El resultado de la ecuación del saiyan power
    '''
    promedio_poder = calcular_promedio_RM(matriz, 5)
    promedio_inteligencia = calcular_promedio_RM(matriz, 4)
    promedio_velocidad = calcular_promedio_RM(matriz, 6)

    saiyan_power = (promedio_poder + promedio_inteligencia + promedio_velocidad) / 3

    return saiyan_power

