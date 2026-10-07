""" Archivo sencillo para medir tiempos de ejecucion se metodos de busqueda y ordenamiento,
se puede mejorar visualmente, pero a,os fines de medicion e implementacoin se deja asi."""
import copy
import random
import timeit

from event import Event
from event_store import EventStore
from metodos import *


def medir_ordenamientos(lista_eventos):
    # medicion de lso emtodos de ordenamiento
    for n in [50, 100, 250, 500, 1000]:
        lista_acortada = primeros_n(lista_eventos, n)       

        tiempo_sorted = timeit.timeit(lambda: ordenar_sorted(lista_acortada), number=10)
        tiempo_sorted = timeit.timeit( lambda: ordenar_sorted( copy.deepcopy(lista_acortada) ) , globals=globals(), number=10)
        tiempo_sort = timeit.timeit(lambda:ordenar_listsort( copy.deepcopy(lista_acortada) ) , globals=globals(),number=10)
        tiempo_bubble = timeit.timeit(lambda: bubble_sort( copy.deepcopy(lista_acortada) ) , globals=globals(),number=10)

        print(" \n -------------------------------------------------------------")        
        print(f"Tiempo de ejecución para una cantidad de {n} evebtos es de: ") 
        print(f"El tiempo de ejecucion del metodo de ordenamiento sorted:  {tiempo_sorted:.8f}")
        print(f"El tiempo de ejecucion del metodo de ordenamiento sort():  {tiempo_sort:.8f}")
        print(f"El tiempo de ejecucion del metodo de ordenamiento bubble:  {tiempo_bubble:.8f}")


def medir_busquedas(lista_eventos):
    # medicion de lso emtodos de busuqeda
    for n in [50, 100, 250, 500, 1000]:
        lista_acortada = primeros_n(lista_eventos, n)     
        list_ordenada = ordenar_sorted(lista_acortada)    

         # elegimos 10 ids que existen + 1 que no existe
        ids_existentes = [random.choice(list_ordenada).id for _ in range(10)]
        ids_a_buscar = ids_existentes + [-1]   # -1 nunca existe

        for key in ids_a_buscar:
            tiempo_secuencial = timeit.timeit(lambda: busqueda_secuencial(lista_acortada, key), number=10)
            tiempo_binaria = timeit.timeit(lambda: busqueda_binaria(list_ordenada, key), number=10)
            tiempo_bisect = timeit.timeit(lambda: busqueda_binaria_bisect(list_ordenada, key), number=10)

            print(" \n -------------------------------------------------------------")        
            print(f"Tiempo de ejecución para una cantidad de {n} evebtos es de: ") 
            print(f"El tiempo de ejecucion del metodo de busqueda secuencial:  {tiempo_secuencial:.8f}")
            print(f"El tiempo de ejecucion del metodo de busqueda binaria:  {tiempo_binaria:.8f}")
            print(f"El tiempo de ejecucion del metodo de busqueda bisect:  {tiempo_bisect:.8f}")
            print(" \n -------------------------------------------------------------")        
                        