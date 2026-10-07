from event import Event


class Index:
    """
    Maneja índices secundarios basados en tablas de dispersión (diccionarios).   
    Permite accesos inmediatos O(1) filtrando por atributos clave.
    """
    def __init__(self, clave_llave):
        # nombre del indice, podemos crear indice por categoria, prioridad; origen, destino, etc
        self.clave_llave = clave_llave
        self.eventos_dict = {}

    def agregar_evento_indice(self, evento: Event):  
        clave = getattr(evento, self.clave_llave)
        if clave not in self.eventos_dict:
            self.eventos_dict[clave] = []    
        self.eventos_dict[clave].append(evento) #ver si no priorizar ordenamineto por id

    def devolver_eventos_x_clave(self, clave):
        if clave not in self.eventos_dict:
            return None       
        return self.eventos_dict[clave]



if __name__ == '__main__':
    eventos = []
    """
    evento_prueba1 = Event(743442, "2026-01-01T03:47:01Z",  "EMERGENCIA MEDICA", 3, "Convulsiones en via publica, persona no responde a estimulos", "D", "E")
    evento_prueba2 = Event(869099, "2026-01-01T05:19:49Z",  "ROBO", 5, "Asalto a delivery en la puerta de domicilio particular", "A", "D")
    evento_prueba3 = Event(129299, "2026-01-01T05:19:49Z",  "EMERGENCIA MEDICA", 5, "Disturbio en comedor comunitario por reparto de alimentos", "A", "B")
    evento_prueba4 = Event(280902, "2026-01-01T05:19:49Z",  "ROBO", 3, "Paciente psiquiatrico con crisis, riesgo autolesivo", "E", "A")
    evento_prueba5 = Event(497282, "2026-01-01T05:19:49Z",  "EMERGENCIA MEDICA", 3, "Disturbio en comedor comunitario por reparto de alimentos", "B", "C")
    evento_prueba6 = Event(857458, "2026-01-01T05:19:49Z",  "EMERGENCIA MEDICA", 2, "Asalto a delivery en la puerta de domicilio particular", "A", "E")
    """

    eventos.append( Event(743442, "2026-01-01T03:47:01Z",  "EMERGENCIA MEDICA", 3, "Convulsiones en via publica, persona no responde a estimulos", "D", "E"))
    eventos.append( Event(869099, "2026-01-01T05:19:49Z",  "ROBO", 5, "Asalto a delivery en la puerta de domicilio particular", "A", "D"))
    eventos.append( Event(129299, "2026-01-01T05:19:49Z",  "EMERGENCIA MEDICA", 5, "Disturbio en comedor comunitario por reparto de alimentos", "A", "B") )
    eventos.append( Event(280902, "2026-01-01T05:19:49Z",  "ROBO", 3, "Paciente psiquiatrico con crisis, riesgo autolesivo", "E", "A") )
    eventos.append( Event(497282, "2026-01-01T05:19:49Z",  "EMERGENCIA MEDICA", 3, "Disturbio en comedor comunitario por reparto de alimentos", "B", "C") )
    eventos.append(Event(857458, "2026-01-01T05:19:49Z",  "EMERGENCIA MEDICA", 2, "Asalto a delivery en la puerta de domicilio particular", "A", "E") )

        
    indiceCategoria = Index("categoria")
    indicePrioridad = Index("prioridad")        
    for i, event in enumerate(eventos):    
        indiceCategoria.agregar_evento_indice(event)
        indicePrioridad.agregar_evento_indice(event)

    print(f" \n Eventos de Categoeria \n")
    for i, events in indiceCategoria.eventos_dict.items():
        print(f" clave es {i} elementos son:")                
        for i, event in enumerate(events):
            print(f"{event.info()}")

    print(f" \n Eventos de Prioridad \n")        
    for i, events in indicePrioridad.eventos_dict.items():
        print(f" clave es {i} elementos son:")                
        for i, event in enumerate(events):
            print(f"{event.info()}")
        