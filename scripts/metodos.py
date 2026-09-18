from bisect import bisect_left

#implementacion de las bsquedas
""" Busqueda secuencial: busca un determinado evento en una lista, la busqueda se realiza
    mediante el identificaodr ID del evento.
  Devuelve la posicion en la lista del evento, junto con el evento """
def busqueda_secuenical(lista_eventos, llave_id):
     for posicion, elEvento in enumerate(lista_eventos):
        if elEvento.id == llave_id:
            return posicion, elEvento
        return None


""" 
 Busqueda binaria: busca un determinado evento en una lista previamente ordenada, la busqueda se realiza
   mediante el identificaodr ID del evento.
 Devuelve la posicion en la lista del evento 
"""
def busqueda_binaria(lista_eventos, llave_id):
    inicio = 0
    fin = len(lista_eventos) - 1

    while inicio <= fin:
        mitad = (inicio + fin) // 2
        if lista_eventos[mitad] == llave_id:
            return mitad
        elif lista_eventos[mitad] < llave_id:
            inicio = mitad + 1
        else:
            fin = mitad - 1

    return None        

""" 
 Busqueda binaria: busca un determinado evento en una lista previamente ordenada, la busqueda se realiza
   mediante el identificaodr ID del evento.
 Devuelve la posicion en la lista del evento 
"""
def busqueda_binaria_bistec(lista_eventos, llave_id):
       # obtenemos las id del los eventos 
    llavesIds = [unEvento.id for unEvento in lista_eventos]
    posicion = bisect_left(llavesIds, llave_id) # buscamos l posicion a insertar
    if posicion < len(lista_eventos) and lista_eventos[posicion].id == llave_id:
        return posicion
    return None

def select_order(lista_eventos):
    tamanio_lista = len(lista_eventos)
    for i in range(tamanio_lista):
        min_inx = i
        for j in range(i +1, tamanio_lista):
            if (lista_eventos[j].id < lista_eventos[min_inx].id):
                min_inx = j
        lista_eventos[i], lista_eventos[min_inx] = lista_eventos[min_inx], lista_eventos[i]

def bubble_sort(lista_eventos):
    tamanio_lista = len(lista_eventos)
    for i in range(tamanio_lista):
        for j in range(0, tamanio_lista - i -1):
            if (lista_eventos[j].id > lista_eventos[j+1].id):
                mnro =   lista_eventos[j]
                lista_eventos[j], lista_eventos[j+1]
                lista_eventos[j+1] = mnro

def ordenar_sorted(lista_eventos):
    return sorted(lista_eventos, key=lambda evnt: evnt.id)

def ordenar_listsort(lista_eventos):
    lista_eventos.sort(key=lambda evnt: evnt.id)


