from DB.database import Database
from Models.rangeModel import RangeModel

class RangeService:
    def __init__(self, db : Database):
        self.__db = db
        self.__selectQuery = (
        "SELECT "\
            "id, "\
            "nombre AS name, "\
            "control, "\
            "descripcion AS description "\
        "FROM rangos"
        )

    def select(self, target = None):
        self.__db.start_connection()
        if not target:
            data = self.__db.execute_query(f"{self.__selectQuery} "\
                                            "ORDER BY control ASC")
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
            ranges = []
            for row in data:
                range = RangeModel(row['id'],
                                   row['name'],
                                   row['control'],
                                   row['description'])
                ranges.append(range)
            return ranges
        else:
            return data

    def insert(self, range : RangeModel):
        self.__db.start_connection()
        data = self.__db.execute_query("INSERT INTO "\
        "rangos (nombre, control, descripcion) "\
        "VALUES (?, ?, ?)",
        (range.getName(),
         range.getControl(),
         range.getDescription(),))
        if data:
            data = self.__db.execute_query("SELECT last_insert_rowid()")[0][0]
        self.__db.close_connection()
        return data

    def update(self, range: RangeModel):
        self.__db.start_connection()
        data = self.__db.execute_query("UPDATE rangos "\
        "SET nombre = ?, control = ?, descripcion = ? "\
        "WHERE id = ?",
        (range.getName(),
         range.getControl(),
         range.getDescription(),
         range.getId(),))
        self.__db.close_connection()
        return data

    def delete(self, range: RangeModel):
        self.__db.start_connection()
        data = self.__db.execute_query("DELETE FROM rangos "\
        "WHERE id = ?",
        (range.getId(),))
        self.__db.close_connection()
        return data