from utn_fra.datasets import (
lista_nombre_heroes_pp, lista_alias_pp,
    	lista_razas_pp, lista_generos_pp,
    	lista_poderes_pp, lista_inteligencias_pp,
lista_velocidades_pp
 )

import validaciones as val
import crear
import buscar
import calcular
import filtrar
import mostrar
import obtener
import trasponer
import os
import ordenar

def aplicacion (lista_nombre_heroes_pp, lista_alias_pp,lista_razas_pp, lista_generos_pp,lista_poderes_pp, lista_inteligencias_pp,lista_velocidades_pp):
    '''
    Corre la aplicación completa
    Parámetros: Las listas que utilizará durante todo el proceso
    Retorna: Nada, solo corre el programa hasta que se rompa el bucle While
    '''

    matriz_inicial = []
    corriendo = True
    while corriendo:

        menu = '''
            1- Crear Matriz:
            2- Agregar un personaje nuevo
            3- Mostrar existencias
            4- Mostrar existencias de personajes Human
            5- Mostrar existencias de personajes que no sean Human
            6- Mostrar detalle de cada personaje
            7- Mostrar información de los Saiyan
            8- Mostrar el personaje más poderoso
            9- Mostrar el personaje más inteligente
            10- Filtrar personajes con menor velocidad
            11- Filtrar personajes más débiles
            12- Filtrar los personajes No-Binario más veloces
            13- Promedio de inteligencia de la raza Android
            14- Filtrar personajes más débiles que los Kryptonian
            15- Filtrar Saiyan Power
            16- Ordenar por a todos por Inteligencia
            17- Ordenar por Menos Inteligente a los not Human
            18- Ordenar por Más Poderosos a los personajes not Human
            19- Ordenar por Más Veloces
            20- Ordenar personalizado: 
                -Todos los personajes deben estar agrupados por Raza
                -Cada personaje de cada raza, debe estar ordenado según poder DES en su raza.
                -Las Razas en la matriz deben aparecer de forma Alfabética
            21- Trasponer la matriz
            22- Salir
            '''
        print(menu)
        opcion = val.validar_input_en_rango(1, 25)
        
        match opcion:
            case 1:
                matriz_inicial = crear.crear_matriz(lista_nombre_heroes_pp, lista_alias_pp,lista_razas_pp, lista_generos_pp,lista_poderes_pp, lista_inteligencias_pp,lista_velocidades_pp)
            case 2:
                if val.validar_carga_matriz(matriz_inicial):
                    personaje = obtener.obtener_info_personaje()
                    matriz_inicial = crear.crear_personaje(matriz_inicial, personaje)
                else:
                    continue
            case 3:
                if val.validar_carga_matriz(matriz_inicial):
                    mostrar.mostrar_existencias_CM(matriz_inicial)
                else:
                    continue
            case 4:
                if val.validar_carga_matriz(matriz_inicial):
                    matriz_aux = filtrar.filtrar_str(matriz_inicial, "Human", 2, True)
                    mostrar.mostrar_existencias_RM(matriz_aux)
                else:
                    continue
            case 5:
                if val.validar_carga_matriz(matriz_inicial):
                    matriz_aux = filtrar.filtrar_str(matriz_inicial, "Human", 2, False)
                    mostrar.mostrar_existencias_RM(matriz_aux)
                else:
                    continue
            case 6:
                if val.validar_carga_matriz(matriz_inicial):
                    mostrar.mostrar_datos_CM(matriz_inicial)
                else:
                    continue
            case 7:
                if val.validar_carga_matriz(matriz_inicial):
                    matriz_aux = filtrar.filtrar_str(matriz_inicial, "Saiyan", 2, True)
                    mostrar.mostrar_datos_RM(matriz_aux)
                else:
                    continue
            case 8:
                if val.validar_carga_matriz(matriz_inicial):
                    limite = buscar.buscar_limite_CM(matriz_inicial, "Maximo", 4)
                    matriz_filtrada = filtrar.filtrar_por_limite(matriz_inicial, 4, limite, "mayor")
                else:
                    continue
            case 9:
                if val.validar_carga_matriz(matriz_inicial):
                    limite = buscar.buscar_limite_CM(matriz_inicial, "Maximo", 5)
                    matriz_filtrada = filtrar.filtrar_por_limite(matriz_inicial, 5, limite, "mayor")
                else:
                    continue
            case 10:
                if val.validar_carga_matriz(matriz_inicial):
                    promedio = calcular.calcular_promedio_CM(matriz_inicial, 6)
                    matriz_filtrada = filtrar.filtrar_valores_CM(matriz_inicial, 6, "menor", promedio)
                    print("Los personajes que no superan el promedio de inteligencia son: \n")
                    mostrar.mostrar_datos_RM(matriz_filtrada)
                else:
                    continue
            case 11:
                if val.validar_carga_matriz(matriz_inicial):
                    matriz_filtrada = filtrar.filtrar_str(matriz_inicial, "Saiyan", 2, True)
                    limite = buscar.buscar_limite_RM(matriz_filtrada, "Minimo", 5)
                    matriz_filtrada = filtrar.filtrar_valores_CM(matriz_inicial, 5, "menor", limite)
                    print("Los personajes que no superan el poder de los saiyan son: \n")
                    mostrar.mostrar_datos_RM(matriz_filtrada)
                else:
                    continue
            case 12:
                if val.validar_carga_matriz(matriz_inicial):
                    matriz_filtrada = filtrar.filtrar_str(matriz_inicial, "No-Binario", 3, True)
                    limite = buscar.buscar_limite_RM(matriz_filtrada, "Maximo", 6)
                    matriz_filtrada = filtrar.filtrar_valores_RM(matriz_filtrada, 6, "mayor o igual", limite)
                    mostrar.mostrar_datos_RM(matriz_filtrada)
                else:
                    continue
            case 13:
                if val.validar_carga_matriz(matriz_inicial):
                    matriz_filtrada = filtrar.filtrar_str(matriz_inicial, "Android", 2, True)
                    promedio_inteligencia = calcular.calcular_promedio_RM(matriz_filtrada, 4)
                    promedio_poder = calcular.calcular_promedio_RM(matriz_filtrada, 5)
                    print(f"Los promedios de la raza Android son: \n Poder: {promedio_poder} \n Inteligencia: {promedio_inteligencia}")
                else:
                    continue
            case 14:
                if val.validar_carga_matriz(matriz_inicial):
                    matriz_filtrada = filtrar.filtrar_str(matriz_inicial, "Kryptonian", 2, True)
                    promedio = calcular.calcular_promedio_RM(matriz_filtrada, 5)
                    print(f"El promedio obtenido es: {promedio:.2f}")
                    matriz_filtrada_2 = filtrar.filtrar_str(matriz_inicial, "Kryptonian", 2, False)
                    matriz_filtrada_3 = filtrar.filtrar_valores_RM(matriz_filtrada_2, 5, "mayor o igual", promedio)
                    print("Los personajes no Kryptonian que superan el promedio de poder de dicha raza son: \n")
                    mostrar.mostrar_datos_RM(matriz_filtrada_3)
                else:
                    continue
            case 15:
                if val.validar_carga_matriz(matriz_inicial):
                    matriz_filtrada = filtrar.filtrar_str(matriz_inicial, "Saiyan", 2, True)
                    filtro = calcular.calcular_saiyan_power(matriz_filtrada)
                    print(f"El Saiyan Power es: {filtro:.2f}")
                    matriz_filtrada_2 = filtrar.filtrar_str(matriz_inicial, "Saiyan", 2, False)
                    matriz_filtrada_perso = filtrar.filtrar_personalizado(matriz_filtrada_2, filtro)
                    mostrar.mostrar_datos_RM(matriz_filtrada_perso)
                else:
                    continue
            case 16:
                if val.validar_carga_matriz(matriz_inicial):
                    matriz_ordenada = ordenar.ordenar_matriz_ss_col(matriz_inicial, 4, "DES", "num")
                    mostrar.mostrar_datos_CM(matriz_ordenada)
                else:
                    continue
            case 17:
                if val.validar_carga_matriz(matriz_inicial):
                    matriz_filtrada = filtrar.filtrar_str(matriz_inicial, "Human", 2, False)
                    matriz_ordenada = ordenar.ordenar_matriz_ss_RM(matriz_filtrada, 4, "ASC", "num")
                    mostrar.mostrar_datos_RM(matriz_ordenada)
                else:
                    continue
            case 18:
                if val.validar_carga_matriz(matriz_inicial):
                    matriz_filtrada = filtrar.filtrar_str(matriz_inicial, "Human", 2, False)
                    matriz_ordenada = ordenar.ordenar_matriz_ss_RM(matriz_filtrada, 5, "DES", "num")
                    mostrar.mostrar_datos_RM(matriz_ordenada)                    
                else:
                    continue
            case 19:
                if val.validar_carga_matriz(matriz_inicial):
                    matriz_ordenada = ordenar.ordenar_matriz_ss_col(matriz_inicial, 6, "ASC", "num")
                    mostrar.mostrar_datos_CM(matriz_ordenada)
                else:
                    continue
            case 20:
                if val.validar_carga_matriz(matriz_inicial):
                    matriz_ordenada = ordenar.ordenar_personalizado(matriz_inicial)
                    mostrar.mostrar_datos_RM_lista_compuesta(matriz_ordenada)
                else:
                    continue
            case 21:
                if val.validar_carga_matriz(matriz_inicial):
                    matriz_ordenada = ordenar.ordenar_matriz_ss_col(matriz_inicial, 2, "ASC", "str")
                    matriz_t = trasponer.trasponer_matriz_CM(matriz_ordenada)
                    print("La matriz transpuesta se visualiza asi: \n")
                    mostrar.mostrar_datos_RM(matriz_t)
                else:
                    continue
            case 22:
                corriendo = False

        os.system("pause")
        os.system("cls")