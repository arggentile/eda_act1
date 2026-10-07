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
        return (f"ID: {self.id_evento}, Timestamp: {self.timestamp}, "
                f"Categoría: {self.categoria}, Nivel Prioridad: {self.prioridad}, Prioridad: {self.__class__.getPrioridades().get(self.prioridad)}, "
                f"Texto: {self.texto}, Origen: {self.origen}, Destino: {self.destino}")

    def __lt__(self, other):
        return self.timestamp < other.timestamp


if __name__ == '__main__':
    evento_prueba1 = Event(743442, "2026-01-01T03:47:01Z",  "EMERGENCIA MEDICA", 3, "Convulsiones en via publica, persona no responde a estimulos", "D", "E")
    evento_prueba2 = Event(869099, "2026-03-04T05:19:49Z",  "ROBO", 5, "Asalto a delivery en la puerta de domicilio particular", "A", "D")
    print(evento_prueba1.info())
    print(evento_prueba2.info())
    print(" \n ----------------  \n")   
    print("\n Prioridades \n")
    prioridades = Event.getPrioridades()
    for i, valor in prioridades.items():
        print(f"Identificador: {i} valor: {valor}")
    print("\n Categorias \n")
    categorias = Event.getCategoriasHabilitadas()
    for i, valor in enumerate(categorias):
        print(f"Identificador: {i} valor: {valor}")    
