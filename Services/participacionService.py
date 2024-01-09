import sys
sys.path.insert(1, './DB')
from database import db
sys.path.insert(1, './Models')
from participacionModel import ParticipacionModel

class ParticipacionService:
    def select(self, id):
        db.start_connection()
        data = db.execute_query("SELECT * FROM participaciones WHERE id = ?", (id,))
        db.close_connection()
        if isinstance(data, list):
            for row in data:
                participacion = ParticipacionModel(row[0], row[1], row[2], row[3])
            return participacion
        else:
            return False

    def selectAll(self):
        db.start_connection()
        data = db.execute_query("SELECT * FROM participaciones")
        db.close_connection()
        if isinstance(data, list):
            participaciones = []
            for row in data:
                participaciones.append(ParticipacionModel(row[0], row[1], row[2], row[3]))
            return participaciones
        else:
            return False

    def insert(self, participacion : ParticipacionModel):
        db.start_connection()
        data = db.execute_query("INSERT INTO \
        participaciones (integrante_id, evento_id, date) \
        VALUES (?, ?, ?)", 
        (participacion.getIntegranteId(), participacion.getEventoId(), participacion.getDate(),))
        db.close_connection()
        return(data)

    def update(self, participacion: ParticipacionModel):
        db.start_connection()
        data = db.execute_query("UPDATE participaciones \
        SET integrante_id = ?, evento_id = ?, date = ? \
        WHERE id = ?", 
        (participacion.getIntegranteId(), 
         participacion.getEventoId(), 
         participacion.getDate(), 
         participacion.getId(),))
        db.close_connection()
        return(data)

    def delete(self, participacion: ParticipacionModel):
        db.start_connection()
        data = db.execute_query("DELETE FROM participaciones \
        WHERE id = ?", 
        (participacion.getId(),))
        db.close_connection()
        return(data)