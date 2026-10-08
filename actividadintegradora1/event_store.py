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
        print(f"{'ID':<8}{'FECHA':<22}{'TIPO':<22}{'PRIO':<6}{'DESCRIPCION':<60}{'O':<4}{'D':<4}")
        print("-" * 126)
        for e in self.eventos:
            print(f"{e.info()}")
        

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

    event_store = EventStore()
    for evento in eventos:
        event_store.agregar_evento(evento)

    event_store.mostrar_eventos()
    print("-" * 126)

    print(f"\n Cantidad de eventos atendidos: {event_store.cantidad_atenciones()}")

    print("\n ------------Próximo evento a atender:----------------------------------")
    el_evento = event_store.consultar_proxima_atencion()
    print(f"{el_evento.info()}")
    event_store.procesar_evento()
    print(f"\n Cantidad de eventos atendidos: {event_store.cantidad_atenciones()}")

    print(event_store.cantidad_atenciones())
    print("\n ------------Próximo evento a atender:----------------------------------")
    el_evento = event_store.consultar_proxima_atencion()
    print(f"{el_evento.info()}")    
    event_store.procesar_evento()
    print("\n Cantidad de eventos atendidos: ")
    print(event_store.cantidad_atenciones())

    print("\n --------------- Ultimo Atendido ---------------------")
    ultima_atencion = event_store.ultimo_atendido()
    print(f"{ultima_atencion.info()}")
        
