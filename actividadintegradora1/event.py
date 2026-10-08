class Event:
    """ Define la estructura de la identidad principal """
    def __init__(self, id_evento, timestamp, categoria, prioridad, texto, origen, destino):
        self.id_evento = id_evento
        self.timestamp = timestamp
        self.categoria = categoria
        self.prioridad = prioridad
        self.texto = texto
        self.origen = origen
        self.destino = destino

    @staticmethod
    def getCategoriasHabilitadas():
        """ Retorna el listado de las categorias habilitadas """
        return ("Error", "Advertencia", "Información", "Depuración", "Robo", "Disturbio", "Emergencia Médica", "Incendio", "Accidente de Tránsito", "Desastre Natural", "Otro")

    @staticmethod
    def getPrioridades():
        """ Retorna las prioridades habilitadas """
        prioridades = {
            0: "Baja",
            1: "Media",
            2: "Alta",
            3: "Urgente/Importante",
            4: "Emergencia"
        }
        return prioridades   
      
    def info(self):
        """ Método para mostrar la información del evento """
        return f"{self.id_evento:<8}{self.timestamp:<22}{self.categoria:<22}{self.prioridad:<6}{self.texto[:58]:<60}{self.origen:<4}{self.destino:<4}"
    
    def __lt__(self, other):
        return self.timestamp < other.timestamp


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

    print(f"{'ID':<8}{'FECHA':<22}{'TIPO':<22}{'PRIO':<6}{'DESCRIPCION':<60}{'O':<4}{'D':<4}")
    print("-" * 126)
    for e in eventos:
        print(f"{e.id_evento:<8}{e.timestamp:<22}{e.categoria:<22}{e.prioridad:<6}{e.texto[:58]:<60}{e.origen:<4}{e.destino:<4}")


    print(" \n ----------------  \n")   
    print("\n Prioridades \n")
    prioridades = Event.getPrioridades()
    for i, valor in prioridades.items():
        print(f"Identificador: {i} valor: {valor}")
    print("\n Categorias \n")
    categorias = Event.getCategoriasHabilitadas()
    for i, valor in enumerate(categorias):
        print(f"Identificador: {i} valor: {valor}")    
