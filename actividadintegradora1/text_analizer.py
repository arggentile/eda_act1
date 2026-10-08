from event import Event
from metodos import *

from grafo import Grafo


class TextAnalyzer:
    """
        palabras: dict (hashing) por palabra como indice.  Tiempo O(1). 
      Almacena la cantidad de frecuencias de la palabras

       y un diccionaro de idEvento, para contabilizar las apariciones en dicho evento

    - un GRAFO dirigido y ponderado para las conexiones entre palabras consecutivas
    """
    def __init__(self):
        # Diccionario conteo frecuencia de palabras. Acceso O(1)  -> {"cantidad": int, "eventos":disct -> { id_evento -> cantidad de eventos}
        self.palabras = {}
        
        # Grafo (lista de adyacencia): palabra -> {palabra_siguiente: peso}
        self.grafo = Grafo()
        
   
    def __dividir_palabras(self, texto):
        """ Divide un texto en palabras, convirtiendo a minusculas, y retornando una lista de palabras """
        textoMin = texto.lower().split()
        return [palabra for palabra in textoMin]

    def __agregar_palabra_conteo(self, idEvento, palabra):
        """ 
        Agrega un palabra al diccionario de conteo de palabras
        """ 
        if palabra not in self.palabras:
            self.palabras[palabra] = {"cantidad": 0, "eventos": []}           

        entrada = self.palabras[palabra]
        entrada["cantidad"] += 1
        if idEvento not in entrada["eventos"]:
            entrada["eventos"] = { idEvento: 0}   
        entrada["eventos"][idEvento] +=1 


    def __conectar_palabras(self, palabra_origen, palabra_destino):
        """ Agrega una conexion entre palabras """
        self.grafo.agregar_arista(palabra_origen, palabra_destino)


    def procesar_texto(self, idEvento, texto):
        """ Dado un determinado texto, lo procesa palabra a palabra, y va formando 
            el diccionario de palabras de frecuencias y el grafo de conecion de palabras """
        palabras = self.__dividir_palabras(texto)

        for pos, palabra in enumerate(palabras):
            # armamaos el diccionario de conteo de palabras O(1)  
            self.__agregar_palabra_conteo(idEvento, palabra)

            #armamos el grafo de conexion de palabras, conectando las palbras en si
            if pos + 1 < len(palabras): #conecto la pabra actual con la siguiente
                siguiente = palabras[pos + 1]
                self.__conectar_palabras(palabra, siguiente)

 
    # ---------- Consultas sobre el diccionario ----------
    def mostrar_frecuenias_palabras(self):
        """ Muestra la cantidad de apariciones de cada palabra en el diccionario """
        texto = ''
        if self.palabras:
            for palabra, content in self.palabras.items():
                texto += f"\n Palabra: {palabra} - apariciones = {content["cantidad"]}"
        return texto

    def mostrar_frecuencia_palabra(self, palabra):
        """ Dada una determinada palabra devuelve la cantidad de apariciones de la misma """
        palabraLow = palabra.lower()
        if palabraLow in self.palabras:
            return self.palabras[palabraLow]["cantidad"]
        return 0

    def mostrar_frecuencia_palabra_x_evento(self, palabra):
        """ Dada una determinada palabra devuelve los eventos en donde estuvo presente dicha palabra y la cantidad de veces que fue mencionada"""
        palabraLow = palabra.lower()
        if palabraLow in self.palabras:
            listIdsEventos = self.palabras[palabraLow]["eventos"]            
            return listIdsEventos
        return None    
    
    
    def n_palabras_mas_frecuentes(self, n=10):
        """ retorna ua lista de dupla de palabra -> frecuncia"""
        return sorted(((p, d["cantidad"]) for p, d in self.palabras.items()),
                      key=lambda x: (-x[1], x[0]))[:n]
 
    def total_palabras(self):
        """ Retorna la cantidad de palabras procesadas, cuenta las duplicaciones"""
        return sum(d["cantidad"] for d in self.palabras.values())
 
    # ---------- Consultas sobre el grafo ----------
    def vecinos_de_palabra(self, palabra):
        palabraLow = palabra.lower()
        return self.grafo.obtener_vecinos(palabraLow)
 
    def conexiones_mas_fuertes(self, n=10):
        aristas = [(o, d, w) for o, v in self.grafo.items() for d, w in v.items()]
        return sorted(aristas, key=lambda x: (-x[2], x[0], x[1]))[:n]
 
 
if __name__ == "__main__":
    eventos = []
    eventos.append( Event(743442, "2026-01-01T03:47:01Z",  "EMERGENCIA MEDICA", 3, "Convulsiones en via publica,  persona no responde a estimulos, en via publica. Muchas Convulsiones", "D", "E"))
    eventos.append( Event(869099, "2026-01-01T05:19:49Z",  "ROBO", 5, "Asalto a delivery en la puerta de domicilio particular", "A", "D"))
    eventos.append( Event(129299, "2026-01-01T05:19:49Z",  "EMERGENCIA MEDICA", 5, "Disturbio en cancha de futbol. Se llevaron todos los muebles. El repartidor de pizza recibio un disparo", "A", "B") )
    eventos.append( Event(280902, "2026-01-01T05:19:49Z",  "ROBO", 3, "Paciente psiquiatrico con crisis, riesgo autolesivo, Asalto a Paciente", "E", "A") )
    eventos.append( Event(497282, "2026-01-01T05:19:49Z",  "EMERGENCIA MEDICA", 3, "Disturbio en comedor comunitario por reparto de alimentos . Asalto a mano armado a repartidor", "B", "C") )
    eventos.append( Event(857458, "2026-01-01T05:19:49Z",  "EMERGENCIA MEDICA", 2, "Asalto a delivery en la puerta de domicilio particular", "A", "E") )
    
    textAnalizer = TextAnalyzer()
    for i, event in enumerate(eventos):
        textAnalizer.procesar_texto(event.id_evento, event.texto )

    print("\n Cantidad de frecuenicas de las palabras:")
    print(f"{textAnalizer.mostrar_frecuenias_palabras()}")
     
    print("\n Cantidad de apariciones de la Palabra Asalto:")
    print(f"{textAnalizer.mostrar_frecuencia_palabra('Asalto')}")
    print("\n Cantidad de apariciones de la Palabra alimentos:")
    print(f"{textAnalizer.mostrar_frecuencia_palabra('alimentos')}")
    print("\n Cantidad de apariciones de la Palabra NoExiste :")
    print(f"{textAnalizer.mostrar_frecuencia_palabra('NoExiste')}")

    print("\n Cantidad de frecuenicas de las palabras x Evento:")
    listCantEventos = textAnalizer.mostrar_frecuencia_palabra_x_evento("Disturbio")
    for id, cantfrecuencias in  listCantEventos.items():
        print(f"El id del evento es: {id}, cantidad de frecuenicas {cantfrecuencias} ")

    print("\n Las 5 palabras más frecuentes son:")
    print(f"{textAnalizer.n_palabras_mas_frecuentes(5)}")

    print("\n La cantidad de palabras son ")
    print(f"{textAnalizer.total_palabras()}")



    print("\n Conexiones entre palabras:")
    print(f"{textAnalizer.grafo.mostrar() }")        
    
    print("\n Vecinos de Asalto:")
    print(f"{textAnalizer.vecinos_de_palabra("Asalto")}")
    print("\n Vecinos de  comedor:")
    print(f"{textAnalizer.vecinos_de_palabra("comedor")}")
    