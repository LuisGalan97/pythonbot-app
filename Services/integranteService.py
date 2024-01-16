import sys
sys.path.insert(1, './DB')
from database import Database
sys.path.insert(1, './Models')
from integranteModel import IntegranteModel
from rangoModel import RangoModel

class IntegranteService:
    def __init__(self, db : Database):
        self.__db = db
        self.__selectQuery = (
        "SELECT "\
            "r.id AS rango_id, "\
            "r.name AS rango_name, "\
            "r.description AS rango_description, "\
            "i.id, "\
            "i.name, "\
            "strftime('%d/%m/%Y', i.datecreate) AS datecreate, "\
            "strftime('%d/%m/%Y', i.dateupdate) AS dateupdate "\
        "FROM integrantes i "\
        "LEFT JOIN rangos r ON r.id = i.rango_id"
        )

    def select(self, target = None):
        self.__db.start_connection()
        if not target:
            data = self.__db.execute_query(self.__selectQuery)
        elif "id" in target:
            data = self.__db.execute_query(f"{self.__selectQuery} WHERE i.id = ?", (target["id"],))
        elif "name" in target:
            data = self.__db.execute_query(f"{self.__selectQuery} WHERE i.name = ?", (target["name"],))
        elif "rango_id" in target:
            data = self.__db.execute_query(f"{self.__selectQuery} WHERE i.rango_id = ?", (target["rango_id"],))
        elif "date_1" in target and "date_2" in target:
            data = self.__db.execute_query(f"{self.__selectQuery} WHERE i.datecreate BETWEEN ? AND ?", (target["date_1"], target["date_2"],))
        else:
            data = None
        self.__db.close_connection()
        if isinstance(data, list):
            integrantes = []
            for row in data:
                rango = RangoModel(row[0], row[1], row[2])
                integrante = IntegranteModel(row[3], row[4], rango, row[5], row[6])
                integrantes.append(integrante)
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
        (integrante.getName(), 
        integrante.getRango().getId(), 
        integrante.getDateCreate(),))
        self.__db.close_connection()
        return data

    def update(self, integrante: IntegranteModel):
        self.__db.start_connection()
        data = self.__db.execute_query("UPDATE integrantes "\
        "SET name = ?, rango_id = ?, dateupdate = ? "\
        "WHERE id = ?",
        (integrante.getName(),
        integrante.getRango().getId(),
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