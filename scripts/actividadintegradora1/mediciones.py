""" Archivo sencillo para medir tiempos de ejecucion se metodos de busqueda y ordenamiento,
se puede mejorar visualmente, pero a,os fines de medicion e implementacoin se deja asi."""
import timeit
import copy

from event import Event
from event_store import EventStore
from metodos import bubble_sort, select_order, ordenar_sorted, ordenar_listsort, primeros_n

def motrar_mediciones(lista_eventos):
    for n in [50, 100, 250, 500, 1000]:
        lista_origen = primeros_n(lista_eventos, n)
        lista_sorted = copy.deepcopy(lista_origen)
        lista_sort = copy.deepcopy(lista_origen)
        lista_buble = copy.deepcopy(lista_origen)
        
        tiempo_sorted = timeit.timeit( lambda: ordenar_sorted(lista_sorted) , globals=globals(), number=10)
        tiempo_sort = timeit.timeit(lambda:ordenar_sorted(lista_sort) , globals=globals(),number=10)
        tiempo_bubble = timeit.timeit(lambda: bubble_sort(lista_buble) , globals=globals(),number=10)

        print(" \n -------------------------------------------------------------")        
        print(f"Tiempo de ejecución para una cantidad de {n} evebtos es de: ") 
        print(f"El tiempo de ejecucion del metodo de ordenamiento sorted:  {tiempo_sorted:.8f}")
        print(f"El tiempo de ejecucion del metodo de ordenamiento sort():  {tiempo_sort:.8f}")
        print(f"El tiempo de ejecucion del metodo de ordenamiento bubble:  {tiempo_bubble:.8f}")
        print(f"El tiempo de ejecucion del metodo de ordenamiento bubble:  {tiempo_bubble:.8f}")