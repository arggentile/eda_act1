from collections import deque


class Vertice:
    def __init__(self, id_vertice):
        self.id_vertice = id_vertice
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
    
    def _agregar_vertice(self, id_vertice):
        if id_vertice not in self.vertices:
            self.vertices[id_vertice] = Vertice(id_vertice)
            return True
        return False
    
   
    def agregar_incidente(self, origen, destino):
        """ Agrega un incidente entre origen y destino, y construye un grafo de rutas no dirigido  """
        self._agregar_vertice(origen)
        self._agregar_vertice(destino)
        self.vertices[origen].agregar_vecino(destino)
        self.vertices[destino].agregar_vecino(origen)

    def obtener_vecinos(self, id_vertice):
        vertice = self.vertices.get(id_vertice)
        if vertice:
            return vertice.obtener_vecinos()
        return []
    
    
    def eliminar_incidente(self, origen, destino):
        """ Se resta un incidente entre los los nodos """
        if origen not in self.vertices or destino not in self.vertices:
            return False
        
        eliminar_origen =  self.vertices[origen].eliminar_vecino(destino)
        eliminar_destino =  self.vertices[destino].eliminar_vecino(origen)                
        return eliminar_origen and eliminar_destino

    def bfs(self, inicio):
        """ deveulve una lista de los vertices visitados en orden de recorrido BFS desde el vertice inicio """
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
        """ devuelve el camino con menos peso (incidentes) entre el origen y el destino, si no hay camino devuelve None """
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
        
        info_rutas=""
        for id_vertice in self.vertices:
            vertice = self.vertices[id_vertice]
            conexiones = [f"{v}(peso:{vertice.obtener_peso(v)})"
            for v in vertice.obtener_vecinos()]
            info_rutas += f"{id_vertice} → {';'.join(conexiones)}\n"
        return     info_rutas

if __name__ == "__main__":
    rutas = Router()
    rutas.agregar_incidente("A", "C")
    rutas.agregar_incidente("B", "C")
    rutas.agregar_incidente("C", "D")
    rutas.agregar_incidente("E", "F")
    rutas.agregar_incidente("F", "A")
    rutas.agregar_incidente("F", "A")
    rutas.agregar_incidente("A", "C")
    rutas.agregar_incidente("B", "C")
    rutas.agregar_incidente("C", "A")
    rutas.agregar_incidente("B", "C")
    rutas.agregar_incidente("B", "E")   
    rutas.agregar_incidente("E", "D")  
    
    print(f"\n Rutas: {rutas.mostrar()}")
    print(f"\n Rutas: {rutas.camino_menos_saltos('A', 'B')}")
    print(f"\n Rutas: {rutas.camino_menos_saltos('A', 'C')}")
    print(f"\n Rutas: {rutas.camino_menos_saltos('A', 'D')}")
    print(f"\n Rutas: {rutas.camino_menos_saltos('A', 'E')}")
    print(f"\n Rutas: {rutas.camino_menos_saltos('A', 'F')}")
    print(f"\n Rutas: {rutas.camino_menos_saltos('E', 'C')}")
    print(f"\n Rutas: {rutas.camino_menos_saltos('F', 'C')}")
    print(f"\n Rutas: {rutas.camino_menos_saltos('E', 'A')}")

    print(f"\n Ruta de caminos desde A: {rutas.bfs("A")}")
    print(f"\n Ruta de caminos desde D: {rutas.bfs("D")}")

        
        
                        
