import sys
sys.path.insert(1, './DB')
from database import db
sys.path.insert(1, './Models')
from rangoModel import RangoModel

class RangoService:
    def select(self, id):
        db.start_connection()
        data = db.execute_query("SELECT * FROM rangos WHERE id = ?", (id,))
        db.close_connection()
        if isinstance(data, list):
            for row in data:
                rango = RangoModel(row[0], row[1], row[2])
            return rango
        else:
            return False

    def selectAll(self):
        db.start_connection()
        data = db.execute_query("SELECT * FROM rangos")
        db.close_connection()
        if isinstance(data, list):
            rangos = []
            for row in data:
                rangos.append(RangoModel(row[0], row[1], row[2]))
            return rangos
        else:
            return False

    def insert(self, rango : RangoModel):
        db.start_connection()
        data = db.execute_query("INSERT INTO \
        rangos (name, description) \
        VALUES (?, ?)", 
        (rango.getName(), rango.getDescription(),))
        db.close_connection()
        return(data)

    def update(self, rango: RangoModel):
        db.start_connection()
        data = db.execute_query("UPDATE rangos \
        SET name = ?, description = ? \
        WHERE id = ?", 
        (rango.getName(), 
         rango.getDescription(),
         rango.getId(),))
        db.close_connection()
        return(data)

    def delete(self, rango: RangoModel):
        db.start_connection()
        data = db.execute_query("DELETE FROM rangos \
        WHERE id = ?", 
        (rango.getId(),))
        db.close_connection()
        return(data)