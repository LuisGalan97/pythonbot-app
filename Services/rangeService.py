from DB.database import Database
from Models.rangeModel import RangeModel

class RangeService:
    def __init__(self, db : Database):
        self.__db = db

    def select(self, target, option):
        if not option:
            selectQuery = (
            "SELECT "\
                "id, "\
                "nombre AS name, "\
                "control, "\
                "descripcion AS description "\
            "FROM rangos"
            )
            self.__db.start_connection()
            if not target:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "ORDER BY control ASC")
            elif target.keys() == {"id"}:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "WHERE id = ?",
                        (target["id"],))
            elif target.keys() == {"name"}:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "WHERE LOWER(nombre) = LOWER(?)",
                        (target["name"],))
            else:
                print( "-> No fue posible realizar la consulta "\
                       "'ya que se especificó un 'target' no valido: "\
                      f"{target}'.")
                data = False
            self.__db.close_connection()
            if isinstance(data, list):
                ranges = []
                for row in data:
                    range = RangeModel(row['id'],
                                       row['name'],
                                       row['control'],
                                       row['description'])
                    ranges.append(range)
                return ranges
            else:
                return data
        else:
            print( "-> No fue posible realizar la consulta "\
                   "'ya que se especificó un 'option' no valido: "\
                  f"{option}'.")
            return False

    def insert(self, range : RangeModel):
        self.__db.start_connection()
        data = self.__db.execute_query("INSERT INTO "\
        "rangos (nombre, control, descripcion) "\
        "VALUES (?, ?, ?)",
        (range.getName(),
         range.getControl(),
         range.getDescription(),))
        if data:
            data = self.__db.execute_query("SELECT last_insert_rowid()")[0][0]
        self.__db.close_connection()
        return data

    def update(self, range: RangeModel):
        self.__db.start_connection()
        data = self.__db.execute_query("UPDATE rangos "\
        "SET nombre = ?, control = ?, descripcion = ? "\
        "WHERE id = ?",
        (range.getName(),
         range.getControl(),
         range.getDescription(),
         range.getId(),))
        self.__db.close_connection()
        return data

    def delete(self, range: RangeModel):
        self.__db.start_connection()
        data = self.__db.execute_query("DELETE FROM rangos "\
        "WHERE id = ?",
        (range.getId(),))
        self.__db.close_connection()
        return data