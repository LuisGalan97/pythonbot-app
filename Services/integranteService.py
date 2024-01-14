import sys
sys.path.insert(1, './DB')
from database import Database
sys.path.insert(1, './Models')
from integranteModel import IntegranteModel

class IntegranteService:
    def __init__(self, db : Database):
        self.__db = db

    def select(self, target = None):
        self.__db.start_connection()
        if not target:
            data = self.__db.execute_query("SELECT * FROM integrantes")
        elif "id" in target:
            data = self.__db.execute_query("SELECT * FROM integrantes WHERE id = ?", (target["id"],))
        elif "name" in target:
            data = self.__db.execute_query("SELECT * FROM integrantes WHERE name = ?", (target["name"],))
        elif "rango_id" in target:
            data = self.__db.execute_query("SELECT * FROM integrantes WHERE rango_id = ?", (target["rango_id"],))
        elif "date_1" in target and "date_2" in target:
            data = self.__db.execute_query("SELECT * FROM integrantes WHERE datecreate BETWEEN ? AND ?", (target["date_1"], target["date_2"],))
        else:
            data = None
        self.__db.close_connection()
        if isinstance(data, list):
            integrantes = []
            for row in data:
                integrantes.append(IntegranteModel(row[0], row[1], row[2], row[3], row[4]))
            return integrantes
        elif data:
            return True
        else:
            return False

    def insert(self, integrante : IntegranteModel):
        self.__db.start_connection()
        data = self.__db.execute_query("INSERT INTO "\
        "integrantes (name, rango_id, datecreate) "\
        "VALUES (?, ?, ?)",
        (integrante.getName(), integrante.getRangoId(), integrante.getDateCreate(),))
        self.__db.close_connection()
        return data

    def update(self, integrante: IntegranteModel):
        self.__db.start_connection()
        data = self.__db.execute_query("UPDATE integrantes "\
        "SET name = ?, rango_id = ?, dateupdate = ? "\
        "WHERE id = ?",
        (integrante.getName(),
        integrante.getRangoId(),
        integrante.getDateUpdate(),
        integrante.getId(),))
        self.__db.close_connection()
        return data

    def delete(self, integrante: IntegranteModel):
        self.__db.start_connection()
        data = self.__db.execute_query("DELETE FROM integrantes "\
        "WHERE id = ?",
        (integrante.getId(),))
        self.__db.close_connection()
        return data