from event import Event


class Index:
    """
    Maneja índices secundarios basados en tablas de dispersión (diccionarios).   
    Permite accesos inmediatos O(1) filtrando por atributos clave.
    """
    def __init__(self, atributo):
        # nombre del indice, podemos crear indice por categoria, prioridad; origen, destino, etc
        self.atributo = atributo
        self.eventos_dict = {}

    def agregar_evento_indice(self, evento: Event):  
        clave = getattr(evento, self.atributo)
        if clave not in self.eventos_dict:
            self.eventos_dict[clave] = []    
        self.eventos_dict[clave].append(evento) #ver si no priorizar ordenamineto por id

    def devolver_eventos_x_clave(self, clave):
        if clave not in self.eventos_dict:
            return None       
        return self.eventos_dict[clave]
