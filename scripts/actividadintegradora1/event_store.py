import heapq
from collections import deque
from itertools import islice

from event import Event
from index import Index
from router import Router


class EventStore:
    """ Clase EventStore para almacena eventos y gestionar eventos.
        Defien una estructura de datos deque la cual almacena el historico de todos los eventos, implementa una cola para 
        mantener el orden en el que llegaron.
          
        Define una estructura eventos_prioritarios, con   heap binario, para priorizar evebntos según severidad/tiempo """
    def __init__(self):
        self.eventos_prioritarios = [] # cola de eventos según severidad/tiempo (heap binario).  Se usa -prioridad para simular un max-heap usando el min-heap de heapq 
        self.eventos = deque() # mantiene el orden de ingreso de eventos, para mostrar en orden de llegada
        self.pila_atendidos = deque() # pila de atendidos
        self.cantidad_tareas_atendidas = 0      
       
        #self.indiceCategoria = Index("categoria")  
        self._indicePrioridad = Index("prioridad")  
        
        self._router = Router() # arma la red de rutas de incidentes
            
    def agregar_evento(self, evento: Event):
        """ Agrega un evento a la lista de eventos del historico y a la cola de eventos prioritarios """
        self.eventos.append(evento)
        #implementa un max-heap
        prioridad_max = -1 * evento.prioridad
        evento_prioritario = (prioridad_max, evento.timestamp, evento)        
        heapq.heappush(self.eventos_prioritarios, evento_prioritario)
        self._router.agregar_incidente(evento.origen, evento.destino) # mandamos a la ruta
        self._indicePrioridad.agregar_evento_indice(evento) # actualizamos indices
        
    def consultar_proxima_atencion(self):
        """Consulta el evento con mayor prioridad sin extraerlo"""
        if not self.eventos_prioritarios:
            print("No existen eventos.")
            return None
        
        prioridad, time, evento = self.eventos_prioritarios[0]
        return evento

   
    def procesar_pedido(self):           
        """ Agarra un pedido para ser procesado, solo lo quita de la cola de prioridades"""
        """ Analizar s en un futuro no deberiamos eliminarlo de los indices"""
        if not self.eventos_prioritarios:
            print("Cola vacia")
            return None
        
        self.cantidad_tareas_atendidas+=1        
        prioridad, time, evento = heapq.heappop(self.eventos_prioritarios)       
        self.pila_atendidos.append(evento) 
        self._router.eliminar_incidente(evento.origen, evento.destino)
        return evento
    
        
    def mostrar_eventos(self):
        """ Muestra la información de todos los eventos almacenados """
        for evento in self.eventos:
            print(evento.info())


    def mostrar_rutas_incidentes(self):
        """ Muestra info de las rutas """
        print("Red Rutas de Incidentes: ")
        print(f"{self._router.mostrar()}")

    def camino_menos_saltos(self, origen, destino):
        # muestra el camino más corto entre Orgien y Destino
        return self._router.camino_menos_saltos(origen, destino)    

    def mostrar_info_eventos(self):
        """ Muestra la información de todos los eventos almacenados """
        print("información delos eventos: ")
        for evento in self.eventos:
            print(f"{evento.info()}\n")

    def eventos_por_prioridad(self, prioridad):
        print(f"Eventos prioridad {Event.getDescripcionPrioridad(prioridad)}")
        events = self._indicePrioridad.devolver_eventos_x_clave(prioridad)
        print(f"{events}")
        if(events is not None):
            for i, event in enumerate(events):
                print(f"{event.info()}")
        
    def pasar_a_lista(self):
        return list(self.eventos)

    def camino_mas_corto(self, origen, destino):
        """Camino con menos saltos."""
        return self._router.camino_menos_saltos(origen, destino)

    def procesar_eventos(self, cantidad):
        """Atiende hasta 'cantidad' eventos por prioridad y los devuelve en una lista."""
        procesados = []
        for _ in range(cantidad):
            evento = self.procesar_pedido()
            if evento is None:
                break
            procesados.append(evento)
        return procesados
    def primeros_n(self, cantidadElementos):
        """ Retorna una lista con N cantidad de elementos, implementado con el objetivo de medir tiempos de ejecucion y memoria"""
        return list(islice(self.eventos, cantidadElementos))