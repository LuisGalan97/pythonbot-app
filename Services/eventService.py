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
            events = []
            for row in data:
                event = EventModel(row['id'],
                                   row['name'],
                                   row['points'],
                                   row['description'])
                events.append(event)
            return events
        else:
            return data

    def insert(self, event : EventModel):
        self.__db.start_connection()
        data = self.__db.execute_query("INSERT INTO "\
        "eventos (nombre, puntos, descripcion) "\
        "VALUES (?, ?, ?)",
        (event.getName(),
         event.getPoints(),
         event.getDescription(),))
        if data:
            data = self.__db.execute_query("SELECT last_insert_rowid()")[0][0]
        self.__db.close_connection()
        return data

    def update(self, event: EventModel):
        self.__db.start_connection()
        data = self.__db.execute_query("UPDATE eventos "\
        "SET nombre = ?, puntos = ?, descripcion = ? "\
        "WHERE id = ?",
        (event.getName(),
         event.getPoints(),
         event.getDescription(),
         event.getId(),))
        self.__db.close_connection()
        return data

    def delete(self, event: EventModel):
        self.__db.start_connection()
        data = self.__db.execute_query("DELETE FROM eventos "\
        "WHERE id = ?",
        (event.getId(),))
        self.__db.close_connection()
        return data