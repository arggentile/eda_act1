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
    
        
    indiceCategoria = Index("categoria")
    indicePrioridad = Index("prioridad")        
    for i, event in enumerate(eventos):    
        indiceCategoria.agregar_evento_indice(event)
        indicePrioridad.agregar_evento_indice(event)


    print(f" \n ----------------- Eventos x Categeria ----------------------- \n")
    for i, events in indiceCategoria.eventos_dict.items():
        print(f"\n Clave: {i}:")                
        for i, event in enumerate(events):
            print(f"{event.info()}")

    print(f" \n ----------------------------Eventos x Prioridad----------------- \n")        
    for i, events in indicePrioridad.eventos_dict.items():
        print(f"\n Clave: {i}:")                
        for i, event in enumerate(events):
            print(f"{event.info()}")
        