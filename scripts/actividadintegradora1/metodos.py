import json
from bisect import bisect_left
from itertools import islice

from event import Event


def cargar_dataset_eventos(name_files):
    """Lee el dataset JSON con datos de prueba y devuelve una lista de instancias de Event."""
    with open(name_files, "r", encoding="utf-8") as f:
        datos = json.load(f)

    eventos = [
        Event(
            id=item["id"],
            timestamp=item["timestamp"],
            categoria=item["categoria"],  
            prioridad=item["prioridad"],
            texto=item["texto"],
            origen=item["origen"],
            destino=item["destino"],
        )
        for item in datos
    ]
    return eventos
    
def busqueda_secuenical(lista_eventos, llave_id):
    """ Busqueda secuencial: busca un determinado evento en una lista, la busqueda se realiza
    mediante el identificaodr ID del evento.
    Devuelve la posicion en la lista del evento, junto con el evento """
    for posicion, elEvento in enumerate(lista_eventos):
        if elEvento.id == llave_id:
            return posicion, elEvento
    return None


def busqueda_binaria(lista_eventos, llave_id):
    """ 
    Busqueda binaria: busca un determinado evento en una lista previamente ordenada, la busqueda se realiza
    mediante el identificaodr ID del evento.
    Devuelve la posicion en la lista del evento 
    """
    inicio = 0
    fin = len(lista_eventos) - 1

    while inicio <= fin:
        mitad = (inicio + fin) // 2
        if lista_eventos[mitad].id == llave_id:
            return mitad
        elif lista_eventos[mitad].id < llave_id:
            inicio = mitad + 1
        else:
            fin = mitad - 1

    return None        

def busqueda_binaria_bisect(lista_eventos, llave_id):
    """
    Búsqueda binaria con bisect sobre una lista ORDENADA por id.
    Complejidad: O(log n), no crea listas auxiliares.
    Devuelve la posición del evento o None si no existe.
    """
    posicion = bisect_left(lista_eventos, llave_id, key=lambda e: e.id)
    if posicion < len(lista_eventos) and lista_eventos[posicion].id == llave_id:
        return posicion
    return None

def select_order(lista_eventos):
    tamanio_lista = len(lista_eventos)
    for i in range(tamanio_lista):
        min_inx = i
        for j in range(i +1, tamanio_lista):
            if (lista_eventos[j].id < lista_eventos[min_inx].id):
                min_inx = j
        lista_eventos[i], lista_eventos[min_inx] = lista_eventos[min_inx], lista_eventos[i]

def bubble_sort(lista_eventos):
    """
    Ordena la lista de eventos por id, in-place.
    Complejidad: O(n²) en peor y caso promedio, O(n) en el mejor caso-lista ordenada
    """
    tamanio_lista = len(lista_eventos)
    for i in range(tamanio_lista):
        for j in range(0, tamanio_lista - i -1):
            if (lista_eventos[j].id > lista_eventos[j+1].id):
                mnro =   lista_eventos[j]
                lista_eventos[j] = lista_eventos[j+1]
                lista_eventos[j+1] = mnro
                #lista_eventos[j], lista_eventos[j + 1] = lista_eventos[j + 1], lista_eventos[j]


def ordenar_sorted(lista_eventos):
    """ Ordena una lista de eventos mediante su clave ID con el metodo sorted """
    return sorted(lista_eventos, key=lambda evnt: evnt.id)

def ordenar_listsort(lista_eventos):
    """ Ordena una lista de eventos mediante su clave ID con el metodo sort() """
    lista_eventos.sort(key=lambda evnt: evnt.id)


def primeros_n(lista, cantidadElementos):
    """ Retorna una lista con N cantidad de elementos, implementado con el objetivo de medir tiempos de ejecucion y memoria"""
    return list(islice(lista, cantidadElementos))