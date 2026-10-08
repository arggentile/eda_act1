class Vertice:
    def __init__(self, id):
        self.id = id
        self.vecinos = {}

    def agregar_vecino(self, vecino, peso=1):
        self.vecinos[vecino] = peso

    def obtener_vecinos(self):
        return list(self.vecinos.keys())

    def obtener_peso(self, vecino):
        return self.vecinos.get(vecino, None)

class Grafo:
    def __init__(self, dirigido=False):
        self.vertices = {}
        self.dirigido = dirigido

    def agregar_vertice(self, id):
        if id not in self.vertices:
            self.vertices[id] = Vertice(id)
            return True
        return False

    def agregar_arista(self, origen, destino, peso=1):
        if origen not in self.vertices:
            self.agregar_vertice(origen)
        if destino not in self.vertices:
            self.agregar_vertice(destino)
        self.vertices[origen].agregar_vecino(destino, peso)
        if not self.dirigido:
            self.vertices[destino].agregar_vecino(origen, peso)

    def obtener_vecinos(self, id):
        vertice = self.vertices.get(id)
        if vertice:
            return vertice.obtener_vecinos()
        return []

    def bfs(self, inicio):
        if inicio not in self.vertices:
            return []
        visitados = set()
        cola = [inicio]
        visitados.add(inicio)
        resultado = []

        while len(cola) > 0:
            vertice_actual = cola.pop(0)
            resultado.append(vertice_actual)

            for vecino in self.obtener_vecinos(vertice_actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        return resultado

    def camino_mas_corto(self, inicio, destino):
        if inicio not in self.vertices or destino not in self.vertices:
            return None
        if inicio == destino:
            return [inicio]

        visitados = set()
        cola = [inicio]
        visitados.add(inicio)
        padres = {inicio: None}

        while len(cola) > 0:
            vertice_actual = cola.pop(0)
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
        for id_vertice in self.vertices:
            vertice = self.vertices[id_vertice]
            conexiones = [f"{v}(peso:{vertice.obtener_peso(v)})"
            for v in vertice.obtener_vecinos()]
            print(f"{id_vertice} → {'', ''.join(conexiones)}")

if __name__ == "__main__":
    grafo_ciudades = Grafo(dirigido=False)
    grafo_ciudades.agregar_arista("Buenos Aires", "Córdoba", 700)
    grafo_ciudades.agregar_arista("Buenos Aires", "Rosario", 300)
    grafo_ciudades.agregar_arista("Córdoba", "Mendoza", 600)
    grafo_ciudades.agregar_arista("Rosario", "Santa Fe", 150)
    grafo_ciudades.agregar_arista("Córdoba", "Santa Fe", 350)
    print("Estructura del grafo:")
    grafo_ciudades.mostrar()
    print(f"\nVecinos de Córdoba: {grafo_ciudades.obtener_vecinos('Córdoba')}")
    print("\nRecorrido BFS desde Buenos Aires:")
    print(grafo_ciudades.bfs("Buenos Aires"))

    print("\nCamino más corto de Buenos Aires a Mendoza:")
    camino = grafo_ciudades.camino_mas_corto("Buenos Aires", "Mendoza")
    if camino:
        print(" → ".join(camino))