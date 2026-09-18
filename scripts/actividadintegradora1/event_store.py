from event import Event
from collections import deque
import heapq
from itertools import islice

class EventStore:
    """ Clase EventStore para almacenar y gestionar eventos """
    def __init__(self):
        #self.eventos = [] # mantiene la lista de historico de eventos, para ordenacion y probar metodos inserccion
        self.eventos_prioritarios = [] # cola de eventos según severidad/tiempo
        self.eventos = deque() # mantiene el orden de ingreso de eventos, para mostrar en orden de llegada
        self.cantidad_tareas_atendidas = 0      
        self.eventos_atendidos = deque() # solo para mostrar implementacoin de pilas, a traves de un retroceso mostramos como fueorn atendidos
        
    def agregar_evento(self, evento: Event):
        """ Agrega un evento a la lista de eventos del historico y a la cola de eventos prioritarios """
        self.eventos.append(evento)
        new_evento = (evento.prioridad, evento.timestamp, evento)        
        heapq.heappush(self.eventos_prioritarios, new_evento)

    def consultar_proxima_atencion(self):
        """Consulta el evento con mayor prioridad sin extraerlo"""
        if not self.eventos_prioritarios:
            print("No existen eventos.")
            return None
        
        prioridad, time, evento = self.eventos_prioritarios[0]
        # Volvemos a invertir la prioridad para mostrar el valor original
        return evento, prioridad, time

    """ Agarra un pedido para ser procesado, solo lo quita de la cola de prioridades"""
    def procesar_pedido(self):           
        if not self.eventos_prioritarios:
            print("Cola vacia")
            return None
        
        self.cantidad_tareas_atendidas+=1        
        prioridad, time, evento = heapq.heappop(self.eventos_prioritarios)
        self.eventos_atendidos.append(evento)
        return evento, prioridad, time
        
    def mostrar_eventos(self):
        """ Muestra la información de todos los eventos almacenados """
        for evento in self.eventos:
            print(evento.info())

    def mostrar_eventos_resumido(self):
        """ Muestra la información de todos los eventos almacenados """
        for evento in self.eventos:
            print(evento.info_resumido())

    def pasar_a_lista(self):
        return list(self.eventos)

    """ Retorna una lista con N cntidad de elementos, iomplementado con el objetivo de medir tiempos de ejecucion y memoria"""
    def primeros_n(self, cantidadElementos):
        return list(islice(self.eventos))
           
            