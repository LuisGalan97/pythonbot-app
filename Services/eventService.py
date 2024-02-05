from DB.database import Database
from Models.eventModel import EventModel

class EventService:
    def __init__(self, db : Database):
        self.__db = db
        self.__selectQuery = (
        "SELECT "\
            "id, "\
            "nombre AS name, "\
            "puntos AS points, "\
            "descripcion AS description "\
        "FROM eventos"\
        )

    def select(self, target = None):
        self.__db.start_connection()
        if not target:
            data = self.__db.execute_query(f"{self.__selectQuery} "\
                                            "ORDER BY puntos DESC")
        elif "id" in target:
            data = self.__db.execute_query(f"{self.__selectQuery} "\
                                            "WHERE id = ?",
                                           (target["id"],))
        elif "name" in target:
            data = self.__db.execute_query(f"{self.__selectQuery} "\
                                            "WHERE nombre = ?",
                                           (target["name"],))
        else:
            data = None
        self.__db.close_connection()
        if isinstance(data, list):
            eventos = []
            for row in data:
                evento = EventModel(row[0], row[1], row[2], row[3])
                eventos.append(evento)
            return eventos
        else:
            return data

    def insert(self, evento : EventModel):
        self.__db.start_connection()
        data = self.__db.execute_query("INSERT INTO "\
        "eventos (nombre, puntos, descripcion) "\
        "VALUES (?, ?, ?)",
        (evento.getName(),
        evento.getPoints(),
        evento.getDescription(),))
        if data:
            data = self.__db.execute_query("SELECT last_insert_rowid()")[0][0]
        self.__db.close_connection()
        return data

    def update(self, evento: EventModel):
        self.__db.start_connection()
        data = self.__db.execute_query("UPDATE eventos "\
        "SET nombre = ?, puntos = ?, descripcion = ? "\
        "WHERE id = ?",
        (evento.getName(),
        evento.getPoints(),
        evento.getDescription(),
        evento.getId(),))
        self.__db.close_connection()
        return data

    def delete(self, evento: EventModel):
        self.__db.start_connection()
        data = self.__db.execute_query("DELETE FROM eventos "\
        "WHERE id = ?",
        (evento.getId(),))
        self.__db.close_connection()
        return data