import os
dir = os.path.dirname(os.path.abspath(__file__))
dir = os.path.dirname(dir)
import sys
sys.path.insert(1, f'{dir}/DB')
from database import Database
sys.path.insert(1, f'{dir}/Models')
from asistenciaModel import AsistenciaModel
from eventoModel import EventoModel
from integranteModel import IntegranteModel
from rangoModel import RangoModel

class AsistenciaService:
    def __init__(self, db : Database):
        self.__db = db
        self.__selectQuery = (
        "SELECT "\
            "r.id AS integrante_rango_id, "\
            "r.name AS integrante_rango_name, "\
            "r.control AS integrante_rango_control, "\
            "r.description AS integrante_rango_description, "\
            "i.id as integrante_id, "\
            "i.name AS integrante_name, "\
            "strftime('%d/%m/%Y', i.datecreate) AS integrante_datecreate, "\
            "strftime('%d/%m/%Y', i.dateupdate) AS integrante_dateupdate, "\
            "e.id AS evento_id, "\
            "e.name AS evento_name, "\
            "e.points AS evento_points, "\
            "e.description AS evento_description, "\
            "a.id, "\
            "strftime('%d/%m/%Y', a.date) AS date "\
        "FROM asistencias a "\
        "LEFT JOIN integrantes i ON i.id = a.integrante_id "\
        "LEFT JOIN eventos e ON e.id = a.evento_id "\
        "LEFT JOIN rangos r ON r.id = i.rango_id"
        )

    def select(self, target = None):
        self.__db.start_connection()
        if not target:
            data = self.__db.execute_query(self.__selectQuery)
        elif "id" in target:
            data = self.__db.execute_query(f"{self.__selectQuery} WHERE a.id = ?", (target["id"],))
        elif "integrante_id" in target and "evento_id" in target and "date_1" in target and "date_2" in target:
            data = self.__db.execute_query(f"{self.__selectQuery} WHERE a.date BETWEEN ? AND ? AND a.integrante_id = ? AND a.evento_id = ?",
                  (target["date_1"], target["date_2"], target["integrante_id"], target["evento_id"],))
        elif "integrante_id" in target and "evento_id" in target:
            data = self.__db.execute_query(f"{self.__selectQuery} WHERE a.integrante_id = ? AND a.evento_id = ?",
                  (target["integrante_id"], target["evento_id"],))
        elif "integrante_id" in target and "date_1" in target and "date_2" in target:
            data = self.__db.execute_query(f"{self.__selectQuery} WHERE a.date BETWEEN ? AND ? AND a.integrante_id = ?",
                  (target["date_1"], target["date_2"], target["integrante_id"],))
        elif "integrante_id" in target:
            data = self.__db.execute_query(f"{self.__selectQuery} WHERE a.integrante_id = ?", (target["integrante_id"],))
        elif "evento_id" in target and "date_1" in target and "date_2" in target:
            data = self.__db.execute_query(f"{self.__selectQuery} WHERE a.date BETWEEN ? AND ? AND a.evento_id = ?",
                  (target["date_1"], target["date_2"], target["evento_id"],))
        elif "evento_id" in target:
            data = self.__db.execute_query(f"{self.__selectQuery} WHERE a.evento_id = ?", (target["evento_id"],))
        elif "date_1" in target and "date_2" in target:
            data = self.__db.execute_query(f"{self.__selectQuery} WHERE a.date BETWEEN ? AND ?", (target["date_1"], target["date_2"],))
        else:
            data = None
        self.__db.close_connection()
        if isinstance(data, list):
            asistencias = []
            for row in data:
                rango = RangoModel(row[0], row[1], row[2], row[3])
                integrante = IntegranteModel(row[4], row[5], rango, row[6], row[7])
                evento = EventoModel(row[8], row[9], row[10], row[11])
                asistencia = AsistenciaModel(row[12], integrante, evento, row[13])
                asistencias.append(asistencia)
            return asistencias
        elif data:
            return True
        else:
            return False

    def insert(self, asistencia : AsistenciaModel):
        self.__db.start_connection()
        data = self.__db.execute_query("INSERT INTO "\
        "asistencias (integrante_id, evento_id, date) "\
        "VALUES (?, ?, ?)",
        (asistencia.getIntegrante().getId(),
        asistencia.getEvento().getId(),
        asistencia.getDate(),))
        self.__db.close_connection()
        return data

    def update(self, asistencia: AsistenciaModel):
        self.__db.start_connection()
        data = self.__db.execute_query("UPDATE asistencias "\
        "SET integrante_id = ?, evento_id = ?, date = ? "\
        "WHERE id = ?",
        (asistencia.getIntegrante().getId(),
        asistencia.getEvento().getId(),
        asistencia.getDate(),
        asistencia.getId(),))
        self.__db.close_connection()
        return data

    def delete(self, asistencia: AsistenciaModel):
        self.__db.start_connection()
        data = self.__db.execute_query("DELETE FROM asistencias "\
        "WHERE id = ?",
        (asistencia.getId(),))
        self.__db.close_connection()
        return data