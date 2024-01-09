import sys
sys.path.insert(1, './DB')
from database import db
sys.path.insert(1, './Models')
from eventoModel import EventoModel

class EventoService:
    def select(self, id):
        db.start_connection()
        data = db.execute_query("SELECT * FROM eventos WHERE id = ?", (id,))
        db.close_connection()
        if isinstance(data, list):
            for row in data:
                evento = EventoModel(row[0], row[1], row[2], row[3])
            return evento
        else:
            return False

    def selectAll(self):
        db.start_connection()
        data = db.execute_query("SELECT * FROM eventos")
        db.close_connection()
        if isinstance(data, list):
            eventos = []
            for row in data:
                eventos.append(EventoModel(row[0], row[1], row[2], row[3]))
            return eventos
        else:
            return False

    def insert(self, evento : EventoModel):
        db.start_connection()
        data = db.execute_query("INSERT INTO \
        eventos (name, points, description) \
        VALUES (?, ?, ?)", 
        (evento.getName(), evento.getPoints(), evento.getDescription(),))
        db.close_connection()
        return(data)

    def update(self, evento: EventoModel):
        db.start_connection()
        data = db.execute_query("UPDATE eventos \
        SET name = ?, points = ?, description = ? \
        WHERE id = ?", 
        (evento.getName(), 
         evento.getPoints(), 
         evento.getDescription(), 
         evento.getId(),))
        db.close_connection()
        return(data)

    def delete(self, evento: EventoModel):
        db.start_connection()
        data = db.execute_query("DELETE FROM eventos \
        WHERE id = ?", 
        (evento.getId(),))
        db.close_connection()
        return(data)
