import copy
import json
from bisect import bisect_left
from itertools import islice

from event import Event


def cargar_dataset_eventos(name_files):
    """Lee el dataset JSON con datos de prueba y devuelve una lista de instancias de Event."""
    with open(name_files, "r", encoding="utf-8") as f:
        datos = json.load(f)
    print("Claves del primer registro:", list(datos[0].keys())) 
    eventos = [
        Event(
            id_evento=item["id_evento"],
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

# metodos de busqueda, buscan una llave ID dentro de una lista de "Eventos"    
def busqueda_secuencial(lista_eventos, llave_id):
    """ 
    Busca un determinado evento mediante una llave en una lista.
    En caso de exito, devuelve la posicion en la lista del evento, caso contrario devuelve None.
    Complejidad: O(n). Mejor caso O(1), peor caso O(n), promedio: O(n/2):
    """
    for posicion, elEvento in enumerate(lista_eventos):
        if elEvento.id_evento == llave_id:
            return posicion
    return None


def busqueda_binaria(lista_eventos, llave_id):
    """ 
    Busca un determinado evento mediante una llave en una lista previamente ordenada.
    En caso de exito, devuelve la posicion en la lista del evento, caso contrario devuelve None.
    Complejidad: O(log n). Mejor caso O(1), pero caso O(log2 n), promedio: O(log n):
    """
    inicio = 0
    fin = len(lista_eventos) - 1

    while inicio <= fin:
        mitad = (inicio + fin) // 2
        if lista_eventos[mitad].id_evento == llave_id:
            return mitad
        elif lista_eventos[mitad].id_evento < llave_id:
            inicio = mitad + 1
        else:
            fin = mitad - 1

    return None        

def busqueda_binaria_bisect(lista_eventos, llave_id):
    """ 
    Busca binaria con bisect. busca un determinado evento mediante una llave en una lista previamente ordenada.
    En caso de exito, devuelve la posicion en la lista del evento, caso contrario devuelve None.
    Complejidad: O(log n). Mejor caso O(1), pero caso O(log2 n), promedio: O(log n)
    """
    posicion = bisect_left(lista_eventos, llave_id, key=lambda e: e.id_evento)
    if posicion < len(lista_eventos) and lista_eventos[posicion].id_evento == llave_id:
        return posicion
    return None


# metodos de ordenamiento, ordenan una lista de "Eventos" mediante su llave id
def select_order(lista_eventos):
    """ Ordena la lista de eventos por id, in-place.
    Complejidad: O(n²) en peor y caso promedio, O(n) en el mejor caso-lista ordenada
    """    
    tamanio_lista = len(lista_eventos)
    for i in range(tamanio_lista - 1):
        min_inx = i
        for j in range(i +1, tamanio_lista):
            if (lista_eventos[j].id_evento < lista_eventos[min_inx].id_evento):
                min_inx = j
        lista_eventos[i], lista_eventos[min_inx] = lista_eventos[min_inx], lista_eventos[i]

def bubble_sort(lista_eventos):
    """
    Ordena la lista de eventos por id, in-place.
    Complejidad: O(n²) en peor y caso promedio, O(n) en el mejor caso-lista ordenada
    """
    tamanio_lista = len(lista_eventos)
    for i in range(tamanio_lista):
        hubo_intercambio = False 
        for j in range(0, tamanio_lista - i -1):
            if (lista_eventos[j].id_evento > lista_eventos[j+1].id_evento):
                mnro =   lista_eventos[j]
                lista_eventos[j] = lista_eventos[j+1]
                lista_eventos[j+1] = mnro
                hubo_intercambio = True
        if not hubo_intercambio:
            break

def ordenar_sorted(lista_eventos):
    """ Ordena una lista de eventos mediante su clave ID con el metodo sorted """
    return sorted(lista_eventos, key=lambda evnt: evnt.id_evento)

def ordenar_listsort(lista_eventos):
    """ Ordena una lista de eventos mediante su clave ID con el metodo sort() """
    lista_eventos.sort(key=lambda evnt: evnt.id_evento)


def primeros_n(lista, cantidadElementos):
    """ Retorna una lista con N cantidad de elementos, implementado con el objetivo de medir tiempos de ejecucion y memoria"""
    return list(islice(lista, cantidadElementos))


if __name__ == "__main__":
    eventos = []
    eventos.append( Event(614827, "2026-03-05T08:22:15Z",  "EMERGENCIA MEDICA", 2, "Adulto mayor con dolor toracico intenso y dificultad respiratoria", "B", "C"))
    eventos.append( Event(738201, "2026-03-07T19:45:33Z",  "ROBO", 4, "Hurto de motocicleta en estacionamiento de supermercado", "C", "E"))
    eventos.append( Event(205544, "2026-03-18T02:08:17Z",  "EMERGENCIA MEDICA", 4, "Intoxicacion alcoholica en joven, inconsciente en la vereda", "E", "A") )
    eventos.append( Event(391877, "2026-06-22T11:33:40Z",  "ROBO", 2, "Entradera a vivienda con moradores presentes, sin heridos", "D", "B") )
    eventos.append( Event(582039, "2026-04-14T17:55:12Z",  "EMERGENCIA MEDICA", 3, "Caida de obrero desde andamio en obra en construccion", "C", "D") )
    eventos.append( Event(946715, "2026-07-30T23:41:08Z",  "EMERGENCIA MEDICA", 1, "Parto en domicilio, madre primeriza con contracciones avanzadas", "B", "A") )
    
    eventos.append( Event(417206, "2026-02-14T09:12:44Z",  "Accidente de Tránsito", 2, "Colision frontal entre dos vehiculos en ruta, heridos graves", "E", "C"))
    eventos.append( Event(853990, "2026-02-14T13:28:19Z",  "Disturbio", 4, "Pelea entre hinchas a la salida del estadio, varios involucrados", "A", "B"))
    eventos.append( Event(672188, "2026-02-14T18:04:55Z",  "EMERGENCIA MEDICA", 4, "Reaccion alergica severa tras ingesta de mariscos en restaurante", "C", "D") )
    eventos.append( Event(239074, "2026-02-14T21:50:31Z",  "Accidente de Tránsito", 2, "Motociclista derrapo en curva, politraumatismos", "B", "E") )
    eventos.append( Event(508623, "2026-02-14T23:17:02Z",  "EMERGENCIA MEDICA", 2, "Incendio en departamento, personas atrapadas con humo", "D", "C") )
    eventos.append( Event(760451, "2026-02-14T04:36:28Z",  "Disturbio", 3, "Ruidos molestos y gritos en vivienda, posible violencia domestica", "E", "B") )
    print("-" * 126)
    print(f"Verificando existencia de la llave 508623 mediante busqueda secuencial: {busqueda_secuencial(eventos, 508623)}") #existe
    print(f"Verificando existencia de la llave 946715 mediante busqueda secuencial: {busqueda_secuencial(eventos, 946715)}")#existe
    print(f"Verificando existencia de la llave 3265 mediante busqueda secuencial: {busqueda_secuencial(eventos, 3265)}") #NO existe
    print("-" * 126)
    lista_ordenada = ordenar_sorted( copy.deepcopy(eventos) )
    print(f"Verificando existencia de la llave 508623 mediante busqueda binaria: {busqueda_binaria(lista_ordenada, 508623)}") #existe
    print(f"Verificando existencia de la llave 946715 mediante busqueda binaria: {busqueda_binaria(lista_ordenada, 946715)}")#existe
    print(f"Verificando existencia de la llave 3265 mediante busqueda binaria: {busqueda_binaria(lista_ordenada, 3265)}") #NO existe
    print("-" * 126)
    print(f"Verificando existencia de la llave 508623 mediante busqueda binaria con bisect: {busqueda_binaria_bisect(lista_ordenada, 508623)}") #existe
    print(f"Verificando existencia de la llave 946715 mediante busqueda binaria con bisect : {busqueda_binaria_bisect(lista_ordenada, 946715)}")#existe
    print(f"Verificando existencia de la llave 3265 mediante busqueda binaria con bisect: {busqueda_binaria_bisect(lista_ordenada, 3265)}") #NO existe
    print("-" * 126)
    print("-" * 126)    
    lista_ordenada_sorted =  eventos.copy()
    ordenar_sorted(  lista_ordenada_sorted )

    list_select_order =  eventos.copy() 
    select_order( list_select_order )

    lista_ordenada_bubble =   eventos.copy()
    bubble_sort( lista_ordenada_bubble )

    lista_listsort =  eventos.copy()
    ordenar_listsort( lista_listsort )

    print("Verificando ordenamiento mediante sorted: ")
    for i in lista_ordenada_sorted:
        print(f"{i.info()}")

    print("Verificando ordenamiento mediante select order: ")
    print("-" * 126)    
    for i in list_select_order:
           print(f"{i.info()}")

    print("Verificando ordenamiento mediante bubble: ")
    print("-" * 126)    
    for i in lista_ordenada_bubble:
           print(f"{i.info()}")

    print("Verificando ordenamiento mediante listsort: ")
    print("-" * 126)    
    for i in lista_listsort:
           print(f"{i.info()}")
                 