import json

from metodos import *
from mediciones import *

from event import Event
from event_store import EventStore


def volcar_data_store(eventos, store):
    # procesamos los eventos para encolarlo y guardarlos en el store
    for i, elEvento in enumerate(eventos):  
        store.agregar_evento(elEvento)


def pedir_origen_destino():
    """Pide origen y destino por teclado."""
    origen = input("Origen: ").strip()
    destino = input("Destino: ").strip()
    return origen, destino
 
 
def mostrar_camino_menos_saltos(store):
    opciones_validas = ["A", "B", "C", "D", "E", "F", "G", "H"]
    while True:
        origen = input("Ingrese la estación de origen (A-E): ").upper()
        destino = input("Ingrese la estación de destino (A-E): ").upper()

        if origen in opciones_validas and destino in opciones_validas:
            print("¡Opciones válidas guardadas con éxito!")
            break  # Rompe el bucle y continúa con el programa
        else:
            print(
                "Error: El origen y el destino deben estar estrictamente entre A y E. Inténtelo de nuevo.\n"
            )

    camino = store.camino_mas_corto(origen, destino)
    if camino is None:
        print(f"No existe camino entre {origen} y {destino}.")
    else:
        print(f"Camino con menos saltos: {' -> '.join(camino)} ({len(camino) - 1} saltos)")
                 
def procesar_n_eventos(store):
    cantidad = input("¿Cuántos eventos desea procesar, se permite un maximo de 10 simultaneamente? ").strip()
    if not cantidad.isdigit() or int(cantidad) == 0:
        print("Ingrese un número entero mayor a 0.")
        return
    cantidad = int(cantidad)
    if cantidad<0 or cantidad>10: 
        print("Ingrese un número entero 0 y 10.")
        return
        
    procesados = store.procesar_eventos(cantidad)
    if not procesados:
        print("No quedan eventos por procesar.")
        return
    for evento in procesados:
        print(evento.info())
    if len(procesados) < int(cantidad):
        print(f"Solo había {len(procesados)} eventos pendientes.")

def mostrar_estadisticas():
    """ carga el dataset de pruebas pára medicoin con 1000 entradas y llama al mnetodo para mostrar estaditicas de medion de tiempo"""   
    eventos  = cargar_dataset_eventos("dataset.json") # dataset inicial con 100 muestras aleatorias
    motrar_mediciones(eventos)

def main():
    eventos = cargar_dataset_eventos("dataset.json")  # dataset inicial con 100 muestras aleatorias
    store = EventStore()
    volcar_data_store(eventos, store)
    #MENU
    while True:
        print("\n--- MENU ---")
        print("1. Mostrar Eventos")
        print("2. Mostrar Rutas/Indicentes")
        print("3. Mostrar Caminos menos saltos entre origen / destino")        
        print("4. Mostrar Caminos más cortos (menos indicente) entre origen / destino") #iplementar en un futuro algortimo Dkjestra
        print("5. Procesar N cantidad de eventos: mostrar su info")
        print("6. Metricas")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            store.mostrar_info_eventos() 
        elif opcion == "2":
            store.mostrar_rutas_incidentes()
        elif opcion == "3":
            mostrar_camino_menos_saltos(store)
        elif opcion== "4":
            print("Implementar a futuro")
        elif opcion == "5":
            procesar_n_eventos(store)    
        elif opcion == "6":
            motrar_mediciones(eventos)
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente de nuevo.") 
    
     
    

    #   
    #mostramos los caminos con menos incidentes de un origen a destino
    #print( f"Camino más corto (con menos incidentes) de A a B {store.camino_menos_saltos('A', 'B')}")
    #print( f"Camino más corto (con menos incidentes) de B a F {store.camino_menos_saltos('B', 'F')}")

    #mostramos los incidents por categoria
    #prioridades = Event.getPrioridades()
    #for indPrioridad, descPrioridad in prioridades.items():
     #   store.eventos_por_prioridad(indPrioridad)

    #mostrar_info_ordenamiento(store)

            
    
if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(f"Error global no controlado: {error}")
        