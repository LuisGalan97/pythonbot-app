import sys
sys.path.insert(1, './DB')
from database import Database
sys.path.insert(1, './Models')
from asistenciaModel import AsistenciaModel

class AsistenciaService:
    def __init__(self, db : Database):
        self.__db = db

    def select(self, target = None):
        self.__db.start_connection()
        if not target:
            data = self.__db.execute_query("SELECT * FROM asistencias")
        elif "id" in target:
            data = self.__db.execute_query("SELECT * FROM asistencias WHERE id = ?", (target["id"],))
        elif "integrante_id" in target:
            data = self.__db.execute_query("SELECT * FROM asistencias WHERE integrante_id = ?", (target["integrante_id"],))
        elif "evento_id" in target:
            data = self.__db.execute_query("SELECT * FROM asistencias WHERE evento_id = ?", (target["evento_id"],))
        elif "date_1" in target and "date_2" in target:
            data = self.__db.execute_query("SELECT * FROM asistencias WHERE date BETWEEN ? AND ?", (target["date_1"], target["date_2"],))
        else:
            data = None
        self.__db.close_connection()
        if isinstance(data, list):
            asistencias = []
            for row in data:
                asistencias.append(AsistenciaModel(row[0], row[1], row[2], row[3]))
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
        (asistencia.getIntegranteId(), asistencia.getEventoId(), asistencia.getDate(),))
        self.__db.close_connection()
        return data

    def update(self, asistencia: AsistenciaModel):
        self.__db.start_connection()
        data = self.__db.execute_query("UPDATE asistencias "\
        "SET integrante_id = ?, evento_id = ?, date = ? "\
        "WHERE id = ?",
        (asistencia.getIntegranteId(),
        asistencia.getEventoId(),
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