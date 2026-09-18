import json
from event import Event
from event_store import EventStore

def cargar_dataset_eventos():
    """Lee el dataset JSON con datos de prueba y devuelve una lista de instancias de Event."""
    with open('dataset.json', "r", encoding="utf-8") as f:
        datos = json.load(f)

    eventos = [
        Event(
            id=item["id"],
            timestamp=item["timestamp"],
            categoria=item["categoria"],  
            prioridad=item["prioridad"],
            texto=item["texto"],
            origen=item["origen"],
            destino=item["destino"],
        )
        for item in datos
    ]
    return eventos

def main():
    eventos  = cargar_dataset_eventos() # dataset inicials
    store = EventStore() 
    for i, unEvento in enumerate(eventos): # empezamos a encolar, 
        store.agregar_evento(unEvento)

    #tomamos los primeros 100 eventos
    



    #lista_copia = store.pasar_a_lista()    
    #cpr_orden_lista = ordenar_sorted(lista_copia)
    #for i, elEvento in enumerate(cpr_orden_lista):
    #    print(elEvento.info())


    #lista_copia = store.pasar_a_lista()    
    #ordenar_listsort(lista_copia)
    #for i, elEvento in enumerate(lista_copia):
    #    print(elEvento.info())
        
    #nueva_lista = ordenar_sorted(store.eventos)
    #for i in nueva_lista:
    #    i.info()
    
    #store.mostrar_eventos_resumido()
    #bubble_sort(store.eventos)
    #store.mostrar_eventos_resumido()

    #store.mostrar_eventos_resumido()
    #bubble_sort(store.eventos)
    #store.mostrar_eventos_resumido()

            
    #evento_atender, priopridad_proximo, time_proximo = store.procesar_pedido()
    #print(f" {evento_atender.info()}")



if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(f"Error global no controlado: {error}")
        