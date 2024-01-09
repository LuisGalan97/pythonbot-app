import sys
sys.path.insert(1, './DB')
from database import db
sys.path.insert(1, './Models')
from integranteModel import IntegranteModel

class IntegranteService:
    def select(self, id):
        db.start_connection()
        data = db.execute_query("SELECT * FROM integrantes WHERE id = ?", (id,))
        db.close_connection()
        if isinstance(data, list):
            for row in data:
                integrante = IntegranteModel(row[0], row[1], row[2], row[3], row[4])
            return integrante
        else:
            return False

    def selectAll(self):
        db.start_connection()
        data = db.execute_query("SELECT * FROM integrantes")
        db.close_connection()
        if isinstance(data, list):
            integrantes = []
            for row in data:
                integrantes.append(IntegranteModel(row[0], row[1], row[2], row[3], row[4]))
            return integrantes
        else:
            return False

    def insert(self, integrante : IntegranteModel):
        db.start_connection()
        data = db.execute_query("INSERT INTO \
        integrantes (name, rango_id, datecreate) \
        VALUES (?, ?, ?)", 
        (integrante.getName(), integrante.getRangoId(), integrante.getDateCreate(),))
        db.close_connection()
        return(data)

    def update(self, integrante: IntegranteModel):
        db.start_connection()
        data = db.execute_query("UPDATE integrantes \
        SET name = ?, rango_id = ?, dateupdate = ? \
        WHERE id = ?", 
        (integrante.getName(), 
         integrante.getRangoId(), 
         integrante.getDateUpdate(), 
         integrante.getId(),))
        db.close_connection()
        return(data)

    def delete(self, integrante: IntegranteModel):
        db.start_connection()
        data = db.execute_query("DELETE FROM integrantes \
        WHERE id = ?", 
        (integrante.getId(),))
        db.close_connection()
        return(data)