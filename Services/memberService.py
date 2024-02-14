from DB.database import Database
from Models.memberModel import MemberModel
from Models.rangeModel import RangeModel

class MemberService:
    def __init__(self, db : Database):
        self.__db = db
        self.__selectQuery = (
        "SELECT "\
            "r.id AS range_id, "\
            "r.nombre AS range_name, "\
            "r.control AS range_control, "\
            "r.descripcion AS range_description, "\
            "i.id, "\
            "i.nombre AS name, "\
            "strftime('%d/%m/%Y', i.fechacreacion) AS datecreate, "\
            "strftime('%d/%m/%Y', i.fechamodificacion) AS dateupdate, "\
            "COALESCE(SUM(e.puntos), 0) AS totalpoints "\
        "FROM integrantes i "\
        "LEFT JOIN rangos r ON r.id = i.rango_id "\
        "LEFT JOIN asistencias a ON a.integrante_id = i.id "\
        "LEFT JOIN eventos e ON e.id = a.evento_id"
        )

    def select(self, target = None):
        self.__db.start_connection()
        if not target:
            data = self.__db.execute_query(f"{self.__selectQuery} "\
                                            "GROUP BY i.id")
        elif ("id" in target and
              "event_id" in target and
              "assist_date_1" in target and
              "assist_date_2" in target):
             data = self.__db.execute_query(f"{self.__selectQuery} "\
                                            "WHERE a.fecha BETWEEN "\
                                            "? AND ? "\
                                            "AND i.id = ? "\
                                            "AND a.evento_id = ? "\
                                            "GROUP BY i.id "\
                                            "ORDER BY totalpoints",
                                           (target["assist_date_1"],
                                            target["assist_date_2"],
                                            target["id"],
                                            target["event_id"],))
        elif ("name" in target and
              "event_id" in target and
              "assist_date_1" in target and
              "assist_date_2" in target):
             data = self.__db.execute_query(f"{self.__selectQuery} "\
                                            "WHERE a.fecha BETWEEN "\
                                            "? AND ? "\
                                            "AND i.nombre = ? "\
                                            "AND a.evento_id = ? "\
                                            "GROUP BY i.id "\
                                            "ORDER BY totalpoints",
                                           (target["assist_date_1"],
                                            target["assist_date_2"],
                                            target["name"],
                                            target["event_id"],))
        elif ("range_id" in target and
              "event_id" in target and
              "assist_date_1" in target and
              "assist_date_2" in target):
             data = self.__db.execute_query(f"{self.__selectQuery} "\
                                            "WHERE a.fecha BETWEEN "\
                                            "? AND ? "\
                                            "AND i.rango_id = ? "\
                                            "AND a.evento_id = ? "\
                                            "GROUP BY i.id "\
                                            "ORDER BY totalpoints",
                                           (target["assist_date_1"],
                                            target["assist_date_2"],
                                            target["range_id"],
                                            target["event_id"],))
        elif ("id" in target and
              "assist_date_1" in target and
              "assist_date_2" in target):
             data = self.__db.execute_query(f"{self.__selectQuery} "\
                                            "WHERE a.fecha BETWEEN "\
                                            "? AND ? "\
                                            "AND i.id = ? "\
                                            "GROUP BY i.id "\
                                            "ORDER BY totalpoints",
                                           (target["assist_date_1"],
                                            target["assist_date_2"],
                                            target["id"],))
        elif ("name" in target and
              "assist_date_1" in target and
              "assist_date_2" in target):
             data = self.__db.execute_query(f"{self.__selectQuery} "\
                                            "WHERE a.fecha BETWEEN "\
                                            "? AND ? "\
                                            "AND i.nombre = ? "\
                                            "GROUP BY i.id "\
                                            "ORDER BY totalpoints",
                                           (target["assist_date_1"],
                                            target["assist_date_2"],
                                            target["name"],))
        elif ("range_id" in target and
              "assist_date_1" in target and
              "assist_date_2" in target):
             data = self.__db.execute_query(f"{self.__selectQuery} "\
                                            "WHERE a.fecha BETWEEN "\
                                            "? AND ? "\
                                            "AND i.rango_id = ? "\
                                            "GROUP BY i.id "\
                                            "ORDER BY totalpoints",
                                           (target["assist_date_1"],
                                            target["assist_date_2"],
                                            target["range_id"],))
        elif ("event_id" in target and
              "assist_date_1" in target and
              "assist_date_2" in target):
             data = self.__db.execute_query(f"{self.__selectQuery} "\
                                            "WHERE a.fecha BETWEEN "\
                                            "? AND ? "\
                                            "AND a.evento_id = ? "\
                                            "GROUP BY i.id "\
                                            "ORDER BY totalpoints",
                                           (target["assist_date_1"],
                                            target["assist_date_2"],
                                            target["event_id"],))
        elif "assist_date_1" in target and "assist_date_2" in target:
             data = self.__db.execute_query(f"{self.__selectQuery} "\
                                            "WHERE a.fecha BETWEEN "\
                                            "? AND ? "\
                                            "GROUP BY i.id "\
                                            "ORDER BY totalpoints",
                                           (target["assist_date_1"],
                                            target["assist_date_2"],))
        elif "id" in target:
            data = self.__db.execute_query(f"{self.__selectQuery} "\
                                            "WHERE i.id = ? "\
                                            "GROUP BY i.id",
                                           (target["id"],))
        elif "name" in target:
            data = self.__db.execute_query(f"{self.__selectQuery} "\
                                            "WHERE i.nombre = ? "\
                                            "GROUP BY i.id",
                                           (target["name"],))
        elif "range_id" in target:
            data = self.__db.execute_query(f"{self.__selectQuery} "\
                                            "WHERE i.rango_id = ? "\
                                            "GROUP BY i.id",
                                           (target["range_id"],))
        elif "date_1" in target and "date_2" in target:
            data = self.__db.execute_query(f"{self.__selectQuery} "\
                                            "WHERE i.fechacreacion BETWEEN "\
                                            "? AND ? "\
                                            "GROUP BY i.id",
                                           (target["date_1"],
                                            target["date_2"],))
        else:
            data = None
        self.__db.close_connection()
        if isinstance(data, list):
            members = []
            for row in data:
                range = RangeModel(row['range_id'],
                                   row['range_name'],
                                   row['range_control'],
                                   row['range_description'])
                member = MemberModel(row['id'],
                                     row['name'],
                                     range,
                                     row['datecreate'],
                                     row['dateupdate'],
                                     row['totalpoints'])
                members.append(member)
            return members
        else:
            return data

    def insert(self, member : MemberModel):
        self.__db.start_connection()
        data = self.__db.execute_query("INSERT INTO "\
        "integrantes (nombre, rango_id, fechacreacion) "\
        "VALUES (?, ?, ?)",
        (member.getName(),
         member.getRange().getId(),
         member.getDateCreate(),))
        if data:
            data = self.__db.execute_query("SELECT last_insert_rowid()")[0][0]
        self.__db.close_connection()
        return data

    def update(self, member: MemberModel):
        self.__db.start_connection()
        data = self.__db.execute_query("UPDATE integrantes "\
        "SET nombre = ?, rango_id = ?, fechamodificacion = ? "\
        "WHERE id = ?",
        (member.getName(),
         member.getRange().getId(),
         member.getDateUpdate(),
         member.getId(),))
        self.__db.close_connection()
        return data

    def delete(self, member: MemberModel):
        self.__db.start_connection()
        data = self.__db.execute_query("DELETE FROM integrantes "\
        "WHERE id = ?",
        (member.getId(),))
        self.__db.close_connection()
        return data