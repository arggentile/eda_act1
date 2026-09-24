from collections import deque


class Vertice:
    def __init__(self, id):
        self.id = id
        self.vecinos = {}
    
    def agregar_vecino(self, vecino):
        # agregar vecino al vertice/nodeo o incrementa los incidentes entre esas rutas
        if (vecino in self.vecinos):
            self.vecinos[vecino] +=1
        else:    
            self.vecinos[vecino] = 1

    def eliminar_vecino(self, vecino):
        if vecino not in self.vecinos:
            return False
        self.vecinos[vecino] -= 1
        if self.vecinos[vecino] <= 0:
            del self.vecinos[vecino]
        return True

    def obtener_vecinos(self):
        return list(self.vecinos.keys())

    def obtener_peso(self, vecino):
        return self.vecinos.get(vecino, None)


class Router:
    def __init__(self):
        self.vertices = {}
    
    def _agregar_vertice(self, id):
        if id not in self.vertices:
            self.vertices[id] = Vertice(id)
            return True
        return False
    
   
    def agregar_incidente(self, origen, destino):
        """ Agrega un incidente entre origen y destino, y vceversa para construir un grafo de rutas no dirigido  """
        if origen not in self.vertices:
            self._agregar_vertice(origen)
        if destino not in self.vertices:
            self._agregar_vertice(destino)
        self.vertices[origen].agregar_vecino(destino)
        self.vertices[destino].agregar_vecino(origen)

    def obtener_vecinos(self, id):
        vertice = self.vertices.get(id)
        if vertice:
            return vertice.obtener_vecinos()
        return []
    
    
    def eliminar_incidente(self, origen, destino):
        """ Se resta un incidente entre los los nodos """
        if origen not in self.vertices or destino not in self.vertices:
            return False
        return (self.vertices[origen].eliminar_vecino(destino)) and (self.vertices[destino].eliminar_vecino(origen))

    def bfs(self, inicio):
        if inicio not in self.vertices:
            return []

        cola = deque()
        cola.append(inicio)
        visitados = set()
        visitados.add(inicio)
        resultado = []

        while len(cola) > 0:
            vertice_actual = cola.popleft()
            resultado.append(vertice_actual)

            for vecino in self.obtener_vecinos(vertice_actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        return resultado

    def camino_menos_saltos(self, inicio, destino):
        if inicio not in self.vertices or destino not in self.vertices:
            print("No se encontro origen y/o destino")
            return None
        if inicio == destino:
            return [inicio]

        visitados = set()
        cola =deque()
        cola.append(inicio)
        visitados.add(inicio)
        padres = {inicio: None}

        while len(cola) > 0:
            vertice_actual = cola.popleft()
            if vertice_actual == destino:
                camino = []
                nodo = destino
                while nodo is not None:
                    camino.append(nodo)
                    nodo = padres[nodo]
                return camino[::-1]
            for vecino in self.obtener_vecinos(vertice_actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    padres[vecino] = vertice_actual
                    cola.append(vecino)
        return None        

    def mostrar(self):       
        if not self.vertices:
            return ""
        
        inforRutas=""
        for id_vertice in self.vertices:
            vertice = self.vertices[id_vertice]
            conexiones = [f"{v}(peso:{vertice.obtener_peso(v)})"
            for v in vertice.obtener_vecinos()]
            inforRutas += f"{id_vertice} → {'', ''.join(conexiones)}\n"
        return     inforRutas