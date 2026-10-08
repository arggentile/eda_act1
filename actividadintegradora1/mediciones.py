import copy
import random
import timeit

from event import Event
from event_store import EventStore
from metodos import *


def medir_ordenamientos(lista_eventos):
    # medicion de lso emtodos de ordenamiento
    for n in [50, 100, 250, 500, 1000]:
        lista_acortada = primeros_n(lista_eventos, n)       

        tiempo_sorted = timeit.timeit(
            stmt="ordenar_sorted(en_orden)",
            setup="en_orden = list(lista_acortada)",
            globals={"ordenar_sorted": ordenar_sorted, "lista_acortada": lista_acortada},
            number=100
        )
        tiempo_sort = timeit.timeit(
            stmt="ordenar_listsort(en_orden)",
            setup="en_orden = list(lista_acortada)",
            globals={"ordenar_listsort": ordenar_listsort, "lista_acortada": lista_acortada},
            number=100
        )
        tiempo_bubble = timeit.timeit(
            stmt="bubble_sort(en_orden)",
            setup="en_orden = list(lista_acortada)",
            globals={"bubble_sort": bubble_sort, "lista_acortada": lista_acortada},
            number=100
        )
        tiempo_select = timeit.timeit(
            stmt="select_order(en_orden)",
            setup="en_orden = list(lista_acortada)",
            globals={"select_order": select_order, "lista_acortada": lista_acortada},
            number=100
        )


        print("\n" + "-" * 65)
        print(f"Tiempo de ejecución para {n} eventos (100 iteraciones c/u):")
        print(f"  sorted()        : {tiempo_sorted:.8f} s")
        print(f"  list.sort()     : {tiempo_sort:.8f} s")
        print(f"  bubble_sort     : {tiempo_bubble:.8f} s")
        print(f"  select_order    : {tiempo_select:.8f} s")

def medir_busquedas(lista_eventos):
    """Mide los tiempos de ejecución de los métodos de búsqueda."""
    for n in [50, 100, 250, 500, 1000]:
        lista_desordenada = primeros_n(lista_eventos, n)
        lista_ordenada = ordenar_sorted(lista_desordenada)

        # 10 ids que sí existen + 1 que no existe (peor caso)
        ids_existentes = [random.choice(lista_ordenada).id_evento for _ in range(10)]
        ids_a_buscar = ids_existentes + [-1]

        total_secuencial = 0.0
        total_binaria = 0.0
        total_bisect = 0.0

        for key in ids_a_buscar:
            total_secuencial += timeit.timeit(
                lambda: busqueda_secuencial(lista_desordenada, key),
                number=100
            )
            total_binaria += timeit.timeit(
                lambda: busqueda_binaria(lista_ordenada, key),
                number=100
            )
            total_bisect += timeit.timeit(
                lambda: busqueda_binaria_bisect(lista_ordenada, key),
                number=100
            )

        cantidad = len(ids_a_buscar)
        print("\n" + "-" * 65)
        print(f"Tiempo promedio de búsqueda para {n} eventos")
        print(f"(promedio sobre {cantidad} claves, 100 iteraciones c/u):")
        print(f"  busqueda_secuencial     : {total_secuencial / cantidad:.8f} s")
        print(f"  busqueda_binaria        : {total_binaria / cantidad:.8f} s")
        print(f"  busqueda_binaria_bisect : {total_bisect / cantidad:.8f} s")


if __name__ == '__main__':
    eventos = cargar_dataset_eventos("dataset.json")  # dataset inicial con 100 muestras aleatorias
    medir_busquedas(eventos)
    medir_ordenamientos(eventos)