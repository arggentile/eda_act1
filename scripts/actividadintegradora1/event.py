class Event:
    """ Clase Event para definir la estructura de la identidad principal"""
    def __init__(self, id, timestamp, categoria, prioridad, texto, origen, destino):
        self.id = id
        self.timestamp = timestamp
        self.categoria = categoria
        self.prioridad = prioridad
        self.texto = texto
        self.origen = origen
        self.destino = destino

    @staticmethod
    def getCategoriasHabilitadas():
        """ Retorna el listado de las categorias habilitadas """
        return ("Error", "Advertencia", "Información", "Depuración")

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

    @staticmethod
    def getDescripcionPrioridad(prioridad):
        """ Retorna la descripción de la prioridad """
        prioridades = {
            0: "Baja",
            1: "Media",
            2: "Alta",
            3: "Urgente/Importante",
            4: "Emergencia"
        }
        return prioridades.get(prioridad)   # <-- ver nota abajo
      
    def info(self):
        """ Método para mostrar la información del evento """
        return (f"ID: {self.id}, Timestamp: {self.timestamp}, "
                f"Categoría: {self.categoria}, Nivel Prioridad: {self.prioridad}, Prioridad: {self.__class__.getDescripcionPrioridad(self.prioridad)}, "
                f"Texto: {self.texto}, Origen: {self.origen}, Destino: {self.destino}")

    def __lt__(self, other):
        return self.timestamp < other.timestamp