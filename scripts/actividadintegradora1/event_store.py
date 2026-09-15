from event import Event
from collections import deque
import heapq

class EventStore:
    """ Clase EventStore para almacenar y gestionar eventos """
    def __init__(self):
        #self.eventos = [] # mantiene la lista de historico de eventos, para ordenacion y probar metodos inserccion
        self.eventos_prioritarios = [] # cola de eventos según severidad/tiempo
        self.eventos = deque() # mantiene el orden de ingreso de eventos, para mostrar en orden de llegada
        self.cantidad_tareas_atendidas = 0      

    def agregar_evento(self, evento):
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
        return prioridad, time, evento

    """ Agarra un pedido para ser procesado, solo lo quita de la cola de prioridades"""
    def procesar_pedido(self):           
        if not self.eventos_prioritarios:
            return None
        self.cantidad_tareas_atendidas+=1
        prioridad, time, evento = heapq.heappop(self.eventos_prioritarios)
        return evento
        
    def mostrar_eventos(self):
        """ Muestra la información de todos los eventos almacenados """
        for evento in self.eventos:
            print(evento.info())