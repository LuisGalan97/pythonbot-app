import sys
sys.path.insert(1, './DB')
from database import Database
sys.path.insert(1, './Models')
from rangoModel import RangoModel

class RangoService:
    def __init__(self, db : Database):
        self.__db = db

    def select(self, id):
        self.__db.start_connection()
        data = self.__db.execute_query("SELECT * FROM rangos WHERE id = ?", (id,))
        self.__db.close_connection()
        if isinstance(data, list):
            for row in data:
                rango = RangoModel(row[0], row[1], row[2])
            return rango
        else:
            return False

    def selectAll(self):
        self.__db.start_connection()
        data = self.__db.execute_query("SELECT * FROM rangos")
        self.__db.close_connection()
        if isinstance(data, list):
            rangos = []
            for row in data:
                rangos.append(RangoModel(row[0], row[1], row[2]))
            return rangos
        else:
            return False

    def insert(self, rango : RangoModel):
        self.__db.start_connection()
        data = self.__db.execute_query("INSERT INTO \
        rangos (name, description) \
        VALUES (?, ?)", 
        (rango.getName(), rango.getDescription(),))
        self.__db.close_connection()
        return(data)

    def update(self, rango: RangoModel):
        self.__db.start_connection()
        data = self.__db.execute_query("UPDATE rangos \
        SET name = ?, description = ? \
        WHERE id = ?", 
        (rango.getName(), 
         rango.getDescription(),
         rango.getId(),))
        self.__db.close_connection()
        return(data)

    def delete(self, rango: RangoModel):
        self.__db.start_connection()
        data = self.__db.execute_query("DELETE FROM rangos \
        WHERE id = ?", 
        (rango.getId(),))
        self.__db.close_connection()
        return(data)