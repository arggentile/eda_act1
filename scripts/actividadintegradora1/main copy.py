import json
import sys

from bisect import bisect_left

from event import Event
from event_store import EventStore

#implementacion de las bsquedas
""" Busqueda secuencial: busca un determinado evento en una lista, la busqueda se realiza
 mediante el identificaodr ID del evento.
  Devuelve la posicion en la lista del evento, junto con el evento """
def busqueda_secuenical(lista_eventos, llave_id):
     for posicion, elEvento in enumerate(lista_eventos):
        if elEvento.id == llave_id:
            return posicion, elEvento
        return None


""" 
 Busqueda binaria: busca un determinado evento en una lista previamente ordenada, la busqueda se realiza
   mediante el identificaodr ID del evento.
 Devuelve la posicion en la lista del evento 
"""
def busqueda_binaria(lista_eventos, llave_id):
    inicio = 0
    fin = len(lista_eventos) - 1

    while inicio <= fin:
        mitad = (inicio + fin) // 2
        if lista_eventos[mitad] == llave_id:
            return mitad
        elif lista_eventos[mitad] < llave_id:
            inicio = mitad + 1
        else:
            fin = mitad - 1

    return None        

""" 
 Busqueda binaria: busca un determinado evento en una lista previamente ordenada, la busqueda se realiza
   mediante el identificaodr ID del evento.
 Devuelve la posicion en la lista del evento 
"""
def busqueda_binaria_bistec(lista_eventos, llave_id):
       # obtenemos las id del los eventos 
    llavesIds = [unEvento.id for unEvento in lista_eventos]
    posicion = bisect_left(llavesIds, llave_id) # buscamos l posicion a insertar
    if posicion < len(lista_eventos) and lista_eventos[posicion].id == llave_id:
        return posicion
    return None

   

def cargar_eventos():
    """Lee el dataset JSON y devuelve una lista de instancias de Event."""
    with open('dataset.json', "r", encoding="utf-8") as f:
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

def select_order(lista_eventos):
    tamanio_lista = len(lista_eventos)
    for i in range(tamanio_lista):
        min_inx = i
        for j in range(i +1, tamanio_lista):
            if (lista_eventos[j].id < lista_eventos[min_inx].id):
                min_inx = j
        lista_eventos[i], lista_eventos[min_inx] = lista_eventos[min_inx], lista_eventos[i]
        

def bubble_sort(lista_eventos):
    tamanio_lista = len(lista_eventos)
    for i in range(tamanio_lista):
        for j in range(0, n - i -1):
            if (lista_eventos[j].id > lista_eventos[j+1].id):
                mnro =   lista_eventos[j]
                lista_eventos[j], lista_eventos[j+1]
                lista_eventos[j+1] = mnro

def orden_sorted(lista):
    return sorted()

def cargar_datos_basicos():
    evento1 = Event(1, "2023-10-01 10:00:00", "Error", 1, "Error 1005 envio de mercaderia", "Servidor A", "Administrador")
    evento2 = Event(2, "2023-15-01 10:00:00", "Error", 5, "calle cortada.", "Servidor A", "Administrador")
    evento3 = Event(3, "2023-20-01 10:00:00", "Error", 5, "Atascamiento de papel.", "Servidor A", "Administrador")
    evento4 = Event(4, "2023-15-01 12:00:00", "Error", 3, ".", "Servidor A", "Administrador")
    evento5 = Event(5, "2025-06-01 10:00:00", "Error", 2, "Se ha producido un error en el sistema.", "Servidor A", "Administrador")
    store = EventStore()
    store.agregar_evento(evento2)
    store.agregar_evento(evento3)
    store.agregar_evento(evento4)
    store.agregar_evento(evento5)
    print("proxioma atencion")
    while (store.consultar_proxima_atencion() != None):
        evento_atendido = store.procesar_pedido()
        print(f"{evento_atendido.info()}")



def main():
    eventos  = cargar_eventos()
    #print(f"Lista nde eventos {eventos}")
    store = EventStore()
    
    for i, unEvento in enumerate(eventos):
        store.agregar_evento(unEvento)

    #store.mostrar_eventos()
    evento_atender, priopridad_proximo, time_proximo = store.procesar_pedido()
    print(f" {evento_atender.info()}")



if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(f"Error global no controlado: {error}")
        