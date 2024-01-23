import sys
sys.path.insert(1, './DB')
from database import Database
sys.path.insert(1, './Models')
from rangoModel import RangoModel

class RangoService:
    def __init__(self, db : Database):
        self.__db = db
        self.__selectQuery = "SELECT * FROM rangos ORDER BY control ASC"

    def select(self, target = None):
        self.__db.start_connection()
        if not target:
            data = self.__db.execute_query(self.__selectQuery)
        elif "id" in target:
            data = self.__db.execute_query(f"{self.__selectQuery} WHERE id = ?", (target["id"],))
        elif "name" in target:
            data = self.__db.execute_query(f"{self.__selectQuery} WHERE name = ?", (target["name"],))
        else:
            data = None
        self.__db.close_connection()
        if isinstance(data, list):
            rangos = []
            for row in data:
                rango = RangoModel(row[0], row[1], row[2], row[3])
                rangos.append(rango)
            return rangos
        elif data:
            return True
        else:
            return False

    def insert(self, rango : RangoModel):
        self.__db.start_connection()
        data = self.__db.execute_query("INSERT INTO "\
        "rangos (name, control, description) "\
        "VALUES (?, ?, ?)",
        (rango.getName(),
        rango.getControl(),
        rango.getDescription(),))
        self.__db.close_connection()
        return data

    def update(self, rango: RangoModel):
        self.__db.start_connection()
        data = self.__db.execute_query("UPDATE rangos "\
        "SET name = ?, control = ?, description = ? "\
        "WHERE id = ?",
        (rango.getName(),
        rango.getControl(),
        rango.getDescription(),
        rango.getId(),))
        self.__db.close_connection()
        return data

    def delete(self, rango: RangoModel):
        self.__db.start_connection()
        data = self.__db.execute_query("DELETE FROM rangos "\
        "WHERE id = ?",
        (rango.getId(),))
        self.__db.close_connection()
        return data