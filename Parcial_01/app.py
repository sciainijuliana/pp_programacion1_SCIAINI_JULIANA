from utn_fra.datasets import (
lista_nombre_heroes_pp, lista_alias_pp,
    	lista_razas_pp, lista_generos_pp,
    	lista_poderes_pp, lista_inteligencias_pp,
lista_velocidades_pp
 )

import validaciones as val
import funciones as fun
import os

def aplicacion (*listas: list):

    matriz_inicial = []
    corriendo = True

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

    while corriendo:
        pass


    
    os.system("pause")
    os.system("cls")