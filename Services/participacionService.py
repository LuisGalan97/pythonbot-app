import sys
sys.path.insert(1, './DB')
from database import Database
sys.path.insert(1, './Models')
from participacionModel import ParticipacionModel

class ParticipacionService:
    def __init__(self, db : Database):
        self.__db = db

    def select(self, id):
        self.__db.start_connection()
        data = self.__db.execute_query("SELECT * FROM participaciones WHERE id = ?", (id,))
        self.__db.close_connection()
        if isinstance(data, list):
            for row in data:
                participacion = ParticipacionModel(row[0], row[1], row[2], row[3])
            return participacion
        else:
            return False

    def selectAll(self):
        self.__db.start_connection()
        data = self.__db.execute_query("SELECT * FROM participaciones")
        self.__db.close_connection()
        if isinstance(data, list):
            participaciones = []
            for row in data:
                participaciones.append(ParticipacionModel(row[0], row[1], row[2], row[3]))
            return participaciones
        else:
            return False

    def insert(self, participacion : ParticipacionModel):
        self.__db.start_connection()
        data = self.__db.execute_query("INSERT INTO \
        participaciones (integrante_id, evento_id, date) \
        VALUES (?, ?, ?)", 
        (participacion.getIntegranteId(), participacion.getEventoId(), participacion.getDate(),))
        self.__db.close_connection()
        return(data)

    def update(self, participacion: ParticipacionModel):
        self.__db.start_connection()
        data = self.__db.execute_query("UPDATE participaciones \
        SET integrante_id = ?, evento_id = ?, date = ? \
        WHERE id = ?", 
        (participacion.getIntegranteId(), 
         participacion.getEventoId(), 
         participacion.getDate(), 
         participacion.getId(),))
        self.__db.close_connection()
        return(data)

    def delete(self, participacion: ParticipacionModel):
        self.__db.start_connection()
        data = self.__db.execute_query("DELETE FROM participaciones \
        WHERE id = ?", 
        (participacion.getId(),))
        self.__db.close_connection()
        return(data)