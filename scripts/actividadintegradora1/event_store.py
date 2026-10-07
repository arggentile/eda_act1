import heapq
from collections import deque

from event import Event


class EventStore:
    """
    Almacena y gestiona los eventos, cola priridad para atencion prioritaria, historico de eventos y pila de atendidos.
       
    eventos: (deque, Queue): histórico en orden de llegada. append O(1).
    eventos_prioritarios: (heap con heapq): próxima atención por severidad y, a igual severidad, el más antiguo. push/pop O(log n), consulta O(1).
                        Se guarda -prioridad para simular un max-heap con el min-heap de heapq.
    pila_atendidos: (deque, Stack): atendidos en orden LIFO, permite deshacer la última atención. push/pop O(1).
    """
    def __init__(self):
        #colas , pilas, heap para almacenar y mantener los eventos
        self.eventos_prioritarios = [] # cola de eventos según severidad/tiempo (heap binario).  Se usa -prioridad para simular un max-heap usando el min-heap de heapq 
        self.eventos = deque() # mantiene el orden de ingreso de eventos, para mostrar en orden de llegada
        self.pila_atendidos = deque() # pila de atendidos
        self.__cantidad_atenciones = 0         
            
    def agregar_evento(self, evento: Event):
        """ Agrega un evento a la lista de eventos del historico y a la cola de eventos prioritarios """
        self.eventos.append(evento)
        #implementa un max-heap
        prioridad_max = -1 * evento.prioridad
        evento_prioritario = (prioridad_max, evento.timestamp, evento)        
        heapq.heappush(self.eventos_prioritarios, evento_prioritario)
        

    def consultar_proxima_atencion(self):
        """Consulta el evento con mayor prioridad sin extraerlo"""
        if not self.eventos_prioritarios:
            print("No existen eventos.")
            return None

        print(self.eventos_prioritarios[0])
        evento = self.eventos_prioritarios[0][2]  # Extrae el evento del heap
        return evento

   
    def procesar_evento(self):           
        """ Agarra un pedido para ser procesado, solo lo quita de la cola de prioridades"""
        if not self.eventos_prioritarios:
            print("Cola vacia")
            return None
        
        self.__cantidad_atenciones+=1        
        prioridad, time, evento = heapq.heappop(self.eventos_prioritarios)       
        self.pila_atendidos.append(evento) 
        return evento
    
        
    def mostrar_eventos(self):
        """ Muestra la información de todos los eventos almacenados. Recorre total O(n) """
        for evento in self.eventos:
            print(evento.info())

    def cantidad_atenciones(self):
        return self.__cantidad_atenciones          
        

    def ultimo_atendido(self):
        """Tope de la pila sin sacarlo. O(1)."""
        if self.pila_atendidos:
            return self.pila_atendidos[-1] 
        else: 
            return None

    def pasar_a_lista(self):
        return list(self.eventos)


if __name__ == "__main__":
    eventos = []
    eventos.append( Event(743442, "2026-01-01T03:47:01Z",  "EMERGENCIA MEDICA", 3, "Convulsiones en via publica, persona no responde a estimulos", "D", "E"))
    eventos.append( Event(869099, "2026-01-02T10:13:49Z",  "ROBO", 5, "Asalto a delivery en la puerta de domicilio particular", "A", "D"))
    eventos.append( Event(129299, "2026-01-12T05:15:49Z",  "EMERGENCIA MEDICA", 5, "Disturbio en comedor comunitario por reparto de alimentos", "A", "B") )
    eventos.append( Event(280902, "2026-04-11T05:11:11Z",  "ROBO", 3, "Paciente psiquiatrico con crisis, riesgo autolesivo", "E", "A") )
    eventos.append( Event(497282, "2026-02-01T15:10:49Z",  "EMERGENCIA MEDICA", 3, "Disturbio en comedor comunitario por reparto de alimentos", "B", "C") )
    eventos.append( Event(857458, "2026-05-16T22:22:49Z",  "EMERGENCIA MEDICA", 2, "Asalto a delivery en la puerta de domicilio particular", "A", "E") )
    
    eventos.append( Event(953412, "2026-01-01T13:47:01Z",  "Accidente de Tránsito", 3, "Convulsiones en via publica, persona no responde a estimulos", "A", "D"))
    eventos.append( Event(112095, "2026-01-01T14:19:49Z",  "Disturbio", 5, "Asalto a delivery en la puerta de domicilio particular", "A", "D"))
    eventos.append( Event(326589, "2026-01-01T20:17:49Z",  "EMERGENCIA MEDICA", 5, "Disturbio en comedor comunitario por reparto de alimentos", "D", "A") )
    eventos.append( Event(110066, "2026-01-01T22:15:49Z",  "Accidente de Tránsito", 3, "Paciente psiquiatrico con crisis, riesgo autolesivo", "C", "E") )
    eventos.append( Event(151161, "2026-01-01T23:22:49Z",  "EMERGENCIA MEDICA", 3, "Disturbio en comedor comunitario por reparto de alimentos", "E", "B") )
    eventos.append( Event(166998, "2026-01-01T05:19:49Z",  "Disturbio", 2, "Asalto a delivery en la puerta de domicilio particular", "A", "E") )
    
       
    event_store = EventStore()
    for evento in eventos:
        event_store.agregar_evento(evento)
    
    event_store.mostrar_eventos()

    print("\n Cantidad de eventos atendidos: ")
    print(event_store.cantidad_atenciones())

    print("\n -------------------------------------------------------------")
    print("\n Próximo evento a atender: ")
    el_evento = event_store.consultar_proxima_atencion()
    print(el_evento.info())
    
    event_store.procesar_evento()
    print("\n Cantidad de eventos atendidos: ")
    print(event_store.cantidad_atenciones())

    print("\n -------------------------------------------------------------")
    print("\n Próximo evento a atender: ")
    el_evento = event_store.consultar_proxima_atencion()
    print(el_evento.info())
    
    event_store.procesar_evento()
    print("\n Cantidad de eventos atendidos: ")
    print(event_store.cantidad_atenciones())

    print("\n -------------------------------------------------------------")
    print("\n Próximo evento a atender: ")
    el_evento = event_store.consultar_proxima_atencion()
    print(el_evento.info())
    
    event_store.procesar_evento()
    print("\n Cantidad de eventos atendidos: ")
    print(event_store.cantidad_atenciones())    

    print("\n --------------- Ultimo Atendido ---------------------")
    ultima_atencion = event_store.ultimo_atendido()
    print(ultima_atencion.info())
        
    
