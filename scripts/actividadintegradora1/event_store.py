import heapq
from collections import deque
from itertools import islice

from event import Event
from index import Index
from router import Router


class EventStore:
    """
       Almacena y gestiona los eventos. Es la fachada del sistema: coordina
       las estructuras y delega en Index, Router y TextAnalyzer.

        Estructuras usadas y por qué:
        * eventos (deque, Queue): histórico en orden de llegada. append O(1).
        * eventos_prioritarios (heap con heapq): próxima atención por
            severidad y, a igual severidad, el más antiguo. push/pop O(log n), consulta O(1).
            Se guarda -prioridad para simular un max-heap con el min-heap de heapq.
        * pila_atendidos (deque, Stack): atendidos en orden LIFO, permite
            deshacer la última atención. push/pop O(1).
        * índices (dict): consultas O(1) promedio por id, categoría, prioridad y origen.

        Decisión: al atender un evento se lo quita del heap y se descuenta del
        Router (deja de ser un incidente activo), pero se conserva en el histórico
        y en los índices, porque sigue siendo parte del registro de la organización.
    """
    def __init__(self):
        #colas , pilas, heap para almacenar y mantener los eventos
        self.eventos_prioritarios = [] # cola de eventos según severidad/tiempo (heap binario).  Se usa -prioridad para simular un max-heap usando el min-heap de heapq 
        self.eventos = deque() # mantiene el orden de ingreso de eventos, para mostrar en orden de llegada
        self.pila_atendidos = deque() # pila de atendidos
        self.cantidad_tareas_atendidas = 0      

        #indices
        #self.indiceCategoria = Index("categoria")  
        self._indice_id = Index("id")
        self._indice_categoria = Index("categoria")
        self._indice_prioridad = Index("prioridad")
        self._indice_origen = Index("origen")
        
        self._router = Router() # arma la red de rutas de incidentes
            
    def agregar_evento(self, evento: Event):
        """ Agrega un evento a la lista de eventos del historico y a la cola de eventos prioritarios """
        self.eventos.append(evento)
        #implementa un max-heap
        prioridad_max = -1 * evento.prioridad
        evento_prioritario = (prioridad_max, evento.timestamp, evento)        
        heapq.heappush(self.eventos_prioritarios, evento_prioritario)
        self._router.agregar_incidente(evento.origen, evento.destino) # mandamos a la ruta
        
        # actualizamos indices
        self._indice_categoria.agregar_evento_indice(evento)
        self._indice_prioridad.agregar_evento_indice(evento)
        self._indice_origen.agregar_evento_indice(evento)

        #self._analyzer = TextAnalyzer()   # NUEVO

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
        events = self._indice_prioridad.devolver_eventos_x_clave(prioridad)
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
        """ Atiende hasta N 'cantidad' de eventos """ 
        procesados = []
        for _ in range(cantidad):
            evento = self.procesar_pedido()
            if evento is None:
                break
            procesados.append(evento)
        return procesados

    def ultimo_atendido(self):
        """Tope de la pila sin sacarlo. O(1)."""
        if self.pila_atendidos:
            return self.pila_atendidos[-1] 
        else: 
            return None

    # NUEVO
    def buscar_por_id(self, id_evento):
        """Evento con ese id o None. O(1) promedio (hash)."""
        return self._indice_id.devolver_eventos_x_clave(id_evento)

    # NUEVO
    def eventos_por_categoria(self, categoria):
        return self._indice_categoria.devolver_eventos_x_clave(categoria)

    # NUEVO
    def eventos_por_origen(self, origen):
        return self._indice_origen.devolver_eventos_x_clave(origen)
    