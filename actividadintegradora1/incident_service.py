from event import Event
from event_store import EventStore
from index import Index
from router import Router
from text_analizer import TextAnalyzer


class IncidentService:
    """
    Orquestador del sistema. Coordina EventStore, Index, Router y TextAnalyzer:
    recibe un evento y delega su almacenamiento, indexado, inserción en la red
    de rutas y análisis de texto a cada colaborador.
    """

    def __init__(self):
        self._event_store =  EventStore()
        self._router = Router()
        self._text_analyzer = TextAnalyzer()

        self._indice_id = Index("id")
        self._indice_categoria = Index("categoria")
        self._indice_prioridad = Index("prioridad")
        self._indice_origen = Index("origen")
       
    # ---------- Alta de eventos ----------
    def agregar_evento(self, evento: Event):
        """Alta de un evento: lo almacena, indexa, carga en la red y analiza texto."""
        self._event_store.agregar_evento(evento)
        
        self._indice_categoria.agregar_evento_indice(evento)
        self._indice_prioridad.agregar_evento_indice(evento)
        self._indice_origen.agregar_evento_indice(evento)
        
        self._router.agregar_incidente(evento.origen, evento.destino)
        self._text_analyzer.procesar_texto(evento.id_evento, evento.texto)

    # ---------- Flujo de atención ----------
    def consultar_proxima_atencion(self):
        return self._event_store.consultar_proxima_atencion()

    def procesar_atencion(self):
        """Atiende el próximo evento y lo descuenta de la red de rutas activas."""
        evento = self._event_store.procesar_evento()
        if evento is None:
            print("Cola vacía")
            return None
        self._router.eliminar_incidente(evento.origen, evento.destino)
        return evento

    def procesar_eventos(self, cantidad):
        """ Atiende una determinada cantidad 'N' de eventos  """
        procesados = []
        for _ in range(cantidad):
            evento = self.procesar_atencion()
            if evento is None:
                break
            procesados.append(evento)
        return procesados

    def ultimo_atendido(self):
        """ Devuleve el utimo Evento (Event) atendido d ela pial de átenciones"""
        return self._event_store.ultimo_atendido()

    def cantidad_atenciones(self):
        return self._event_store.cantidad_atenciones()

    # ---------- Consultas por índice ----------
    def buscar_por_id(self, id_evento):
        return self._indice_id["id"].devolver_eventos_x_clave(id_evento)

    def eventos_por_categoria(self, categoria):
        return self._indice_categoria["categoria"].devolver_eventos_x_clave(categoria)

    def eventos_por_prioridad(self, prioridad):
        return self._indice_prioridad["prioridad"].devolver_eventos_x_clave(prioridad)

    def eventos_por_origen(self, origen):
        return self._indice_origen["origen"].devolver_eventos_x_clave(origen)


 
    def camino_menos_saltos(self, origen, destino):
        return self._router.camino_menos_saltos(origen, destino)

    def camino_mas_corto(self, origen, destino):
        # alias para compatibilidad con el menú actual
        return self._router.camino_menos_saltos(origen, destino)

    def mostrar_rutas_incidentes(self):       
        print(f"{self._router.mostrar()}")

    def frecuencia_palabra(self, palabra):
        return self._text_analyzer.mostrar_frecuencia_palabra(palabra)

    def palabras_mas_frecuentes(self, n=10):
        return self._text_analyzer.n_palabras_mas_frecuentes(n)



    def mostrar_info_eventos(self):
        print("Información de los eventos:")
        self._event_store.mostrar_eventos()

    def pasar_a_lista(self):
        return self._event_store.pasar_a_lista()


if __name__ == "__main__":
    mis_eventos = []
    mis_eventos.append( Event(743442, "2026-01-01T03:47:01Z",  "EMERGENCIA MEDICA", 3, "Convulsiones en via publica, persona no responde a estimulos", "D", "E"))
    mis_eventos.append( Event(869099, "2026-01-02T10:13:49Z",  "ROBO", 5, "Asalto a delivery en la puerta de domicilio particular", "A", "D"))
    mis_eventos.append( Event(129299, "2026-01-12T05:15:49Z",  "EMERGENCIA MEDICA", 5, "Disturbio en comedor comunitario por reparto de alimentos", "A", "B") )
    mis_eventos.append( Event(280902, "2026-04-11T05:11:11Z",  "ROBO", 3, "Paciente psiquiatrico con crisis, riesgo autolesivo", "E", "A") )
    mis_eventos.append( Event(497282, "2026-02-01T15:10:49Z",  "EMERGENCIA MEDICA", 3, "Disturbio en comedor comunitario por reparto de alimentos", "B", "C") )
    mis_eventos.append( Event(857458, "2026-05-16T22:22:49Z",  "EMERGENCIA MEDICA", 2, "Asalto a delivery en la puerta de domicilio particular", "A", "E") )
    
    mis_eventos.append( Event(953412, "2026-01-01T13:47:01Z",  "Accidente de Tránsito", 3, "Convulsiones en via publica, persona no responde a estimulos", "A", "D"))
    mis_eventos.append( Event(112095, "2026-01-01T14:19:49Z",  "Disturbio", 5, "Asalto a delivery en la puerta de domicilio particular", "A", "D"))
    mis_eventos.append( Event(326589, "2026-01-01T20:17:49Z",  "EMERGENCIA MEDICA", 5, "Disturbio en comedor comunitario por reparto de alimentos", "D", "A") )
    mis_eventos.append( Event(110066, "2026-01-01T22:15:49Z",  "Accidente de Tránsito", 3, "Paciente psiquiatrico con crisis, riesgo autolesivo", "C", "E") )
    mis_eventos.append( Event(151161, "2026-01-01T23:22:49Z",  "EMERGENCIA MEDICA", 3, "Disturbio en comedor comunitario por reparto de alimentos", "E", "B") )
    mis_eventos.append( Event(166998, "2026-01-01T05:19:49Z",  "Disturbio", 2, "Asalto a delivery en la puerta de domicilio particular", "A", "E") )
    
       
    service = IncidentService()
    for evento in mis_eventos:
        service.agregar_evento(evento)
    
    service.mostrar_info_eventos()

    
    print("\n ----------------Analizador de rutas:---------------------------------")   
    print(f"\n Red de rutas: {service.mostrar_rutas_incidentes()} \n")
        
    print(f"\n Camio con menos incidente desde A -> B: {service.camino_menos_saltos('A', 'B')}")
    print(f"\n Camio con menos incidente desde A -> C: {service.camino_menos_saltos('A', 'C')}")
    print(f"\n Camio con menos incidente desde D -> A: {service.camino_menos_saltos('D', 'A')}")

    print(f"\n Cantidad de eventos atendidos: {service.cantidad_atenciones()} ")
    print("\n ----------------Próximo evento a atender:---------------------------------")   
    el_evento = service.consultar_proxima_atencion()
    print(f"{el_evento.info()}")

    service.procesar_atencion()
    print(f"\n Cantidad de eventos atendidos: {service.cantidad_atenciones()}")
    service.procesar_eventos(3)
    print(f"\n Cantidad de eventos atendidos: {service.cantidad_atenciones()}")    
    service.procesar_eventos(3)
    print(f"\n Cantidad de eventos atendidos: {service.cantidad_atenciones()}")

    print("\n ----------------Último atendido:---------------------------------")   
    mi_ultima_atencion =     service.ultimo_atendido()
    print(f"{mi_ultima_atencion.info()}")

    print("\n ----------------Analizador de rutas:---------------------------------")   
    print(f"\n Red de rutas: {service.mostrar_rutas_incidentes()} \n")
        
    print(f"\n Camio con menos incidente desde A -> B: {service.camino_menos_saltos('A', 'B')}")
    print(f"\n Camio con menos incidente desde A -> C: {service.camino_menos_saltos('A', 'C')}")
    print(f"\n Camio con menos incidente desde D -> A: {service.camino_menos_saltos('D', 'A')}")
    
    
    print("------------ Analizando frecuencias de palabras y alertas ------------ ")
    print("\n 15 palabras más frecuentes --------------")
    mas_frecuentes = service.palabras_mas_frecuentes(15)
    for i, p in enumerate(mas_frecuentes):
        print(f"Palabra =  {p[0]} --> frecuencia: {p[1]}")
    
    print(f"\n Cantidda de frecuencias d ela palabra Asalto {service.frecuencia_palabra('Asalto')} --------------")
    print(f"\n Cantidda de frecuencias d ela palabra Asalto {service.frecuencia_palabra('psiquiatrico')} --------------")
    print(f"\n Cantidda de frecuencias d ela palabra Asalto {service.frecuencia_palabra('en')} --------------")
        