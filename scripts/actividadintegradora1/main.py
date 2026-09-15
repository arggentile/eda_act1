from event import Event

evento1 = Event(1, "2023-06-01 10:00:00", "Error", 1, "Se ha producido un error en el sistema.", "Servidor A", "Administrador")
evento2 = Event(1, "2023-06-01 10:00:00", "Error", 0, "Se ha producido un error en el sistema.", "Servidor A", "Administrador")
evento3 = Event(1, "2023-06-01 10:00:00", "Error", 0, "Se ha producido un error en el sistema.", "Servidor A", "Administrador")
evento4 = Event(1, "2023-06-01 10:00:00", "Error", 0, "Se ha producido un error en el sistema.", "Servidor A", "Administrador")
evento5 = Event(1, "2023-06-01 10:00:00", "Error", 0, "Se ha producido un error en el sistema.", "Servidor A", "Administrador")

print(f"Evento 2: {evento1.info()}")
print(f"Evento 2: {evento2.info()}")
print(f"Evento 3: {evento3.info()}")
print(f"Evento 4: {evento4.info()}")
print(f"Evento 5: {evento5.info()}")
