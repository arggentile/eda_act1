from event import Event
from event_store import EventStore

evento1 = Event(1, "2023-10-01 10:00:00", "Error", 1, "Error 1005 envio de mercaderia", "Servidor A", "Administrador")
evento2 = Event(2, "2023-15-01 10:00:00", "Error", 5, "calle cortada.", "Servidor A", "Administrador")
evento3 = Event(3, "2023-20-01 10:00:00", "Error", 5, "Atascamiento de papel.", "Servidor A", "Administrador")
evento4 = Event(4, "2023-15-01 12:00:00", "Error", 3, ".", "Servidor A", "Administrador")
evento5 = Event(5, "2025-06-01 10:00:00", "Error", 2, "Se ha producido un error en el sistema.", "Servidor A", "Administrador")

store = EventStore()
store.agregar_evento(evento1)
store.agregar_evento(evento2)
store.agregar_evento(evento3)
store.agregar_evento(evento4)
store.agregar_evento(evento5)
#store.mostrar_eventos()
print("proxioma atencion")
while (store.consultar_proxima_atencion() != None):
    evento_atendido = store.procesar_pedido()
    print(f"{evento_atendido.info()}")