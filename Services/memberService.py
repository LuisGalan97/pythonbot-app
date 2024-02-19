from DB.database import Database
from Models.memberModel import MemberModel
from Models.rangeModel import RangeModel

class MemberService:
    def __init__(self, db : Database):
        self.__db = db

    def select(self, target, option):
        if not option:
            selectQuery = (
            "SELECT "\
                "r.id AS range_id, "\
                "r.nombre AS range_name, "\
                "r.control AS range_control, "\
                "r.descripcion AS range_description, "\
                "pi.id AS principal_id, "\
                "pi.nombre AS principal_name, "\
                "i.id, "\
                "i.nombre AS name, "\
                "strftime('%d/%m/%Y', i.fechacreacion) AS datecreate, "\
                "strftime('%d/%m/%Y', i.fechamodificacion) AS dateupdate "\
            "FROM integrantes i "\
            "LEFT JOIN rangos r ON r.id = i.rango_id "\
            "LEFT JOIN integrantes AS pi ON pi.id = i.principal_id"
            )
            self.__db.start_connection()
            if not target:
                data = self.__db.execute_query(selectQuery)
            elif target.keys() == {"id"}:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "WHERE i.id = ?",
                        (target["id"],))
            elif target.keys() == {"name"}:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "WHERE i.nombre = ?",
                        (target["name"],))
            elif target.keys() == {"range_id"}:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "WHERE i.rango_id = ?",
                        (target["range_id"],))
            elif target.keys() == {"date_1", "date_2"}:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "WHERE i.fechacreacion BETWEEN "\
                        "? AND ?",
                        (target["date_1"],
                         target["date_2"],))
            else:
                print( "-> No fue posible realizar la consulta "\
                       "'ya que se especificó un 'target' no valido: "\
                      f"{target}'.")
                data = False
            self.__db.close_connection()
            if isinstance(data, list):
                members = []
                for row in data:
                    range = RangeModel(row['range_id'],
                                       row['range_name'],
                                       row['range_control'],
                                       row['range_description'])
                    principal = MemberModel(row['principal_id'],
                                            row['principal_name'])
                    member = MemberModel(row['id'],
                                         row['name'],
                                         range,
                                         principal,
                                         row['datecreate'],
                                         row['dateupdate'])
                    members.append(member)
                return members
            else:
                return data
        elif option == "rtpoints":
            selectQuery = (
            "SELECT "\
                "r.id AS range_id, "\
                "r.nombre AS range_name, "\
                "r.control AS range_control, "\
                "r.descripcion AS range_description, "\
                "pi.id AS principal_id, "\
                "pi.nombre AS principal_name, "\
                "i.id, "\
                "i.nombre AS name, "\
                "strftime('%d/%m/%Y', i.fechacreacion) AS datecreate, "\
                "strftime('%d/%m/%Y', i.fechamodificacion) AS dateupdate, "\
                "COALESCE(SUM(e.puntos), 0) AS totalpoints "\
            "FROM integrantes i "\
            "LEFT JOIN rangos r ON r.id = i.rango_id "\
            "LEFT JOIN integrantes AS pi ON pi.id = i.principal_id "\
            "LEFT JOIN asistencias a ON a.integrante_id = i.id "\
            "LEFT JOIN eventos e ON e.id = a.evento_id"
            )
            self.__db.start_connection()
            if target.keys() == {"date_1", "date_2"}:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "WHERE a.fecha BETWEEN "\
                        "? AND ? "\
                        "GROUP BY i.id "\
                        "ORDER BY totalpoints DESC",
                        (target["date_1"],
                         target["date_2"],))
            elif target.keys() == {"id", "date_1", "date_2"}:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "WHERE a.fecha BETWEEN "\
                        "? AND ? "\
                        "AND i.id = ? "\
                        "GROUP BY i.id "\
                        "ORDER BY totalpoints DESC",
                        (target["date_1"],
                         target["date_2"],
                         target["id"],))
            elif target.keys() == {"name", "date_1", "date_2"}:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "WHERE a.fecha BETWEEN "\
                        "? AND ? "\
                        "AND i.nombre = ? "\
                        "GROUP BY i.id "\
                        "ORDER BY totalpoints DESC",
                        (target["date_1"],
                         target["date_2"],
                         target["name"],))
            elif target.keys() == {"range_id", "date_1", "date_2"}:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "WHERE a.fecha BETWEEN "\
                        "? AND ? "\
                        "AND i.rango_id = ? "\
                        "GROUP BY i.id "\
                        "ORDER BY totalpoints DESC",
                        (target["date_1"],
                         target["date_2"],
                         target["range_id"],))
            elif target.keys() == {"event_id", "date_1", "date_2"}:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "WHERE a.fecha BETWEEN "\
                        "? AND ? "\
                        "AND a.evento_id = ? "\
                        "GROUP BY i.id "\
                        "ORDER BY totalpoints DESC",
                        (target["date_1"],
                         target["date_2"],
                         target["event_id"],))
            elif target.keys() == {"id", "event_id", "date_1", "date_2"}:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "WHERE a.fecha BETWEEN "\
                        "? AND ? "\
                        "AND i.id = ? "\
                        "AND a.evento_id = ? "\
                        "GROUP BY i.id "\
                        "ORDER BY totalpoints DESC",
                        (target["date_1"],
                         target["date_2"],
                         target["id"],
                         target["event_id"],))
            elif target.keys() == {"name", "event_id", "date_1", "date_2"}:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "WHERE a.fecha BETWEEN "\
                        "? AND ? "\
                        "AND i.nombre = ? "\
                        "AND a.evento_id = ? "\
                        "GROUP BY i.id "\
                        "ORDER BY totalpoints DESC",
                        (target["date_1"],
                         target["date_2"],
                         target["name"],
                         target["event_id"],))
            elif target.keys() == {"range_id", "event_id", "date_1", "date_2"}:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "WHERE a.fecha BETWEEN "\
                        "? AND ? "\
                        "AND i.rango_id = ? "\
                        "AND a.evento_id = ? "\
                        "GROUP BY i.id "\
                        "ORDER BY totalpoints DESC",
                        (target["date_1"],
                         target["date_2"],
                         target["range_id"],
                         target["event_id"],))
            else:
                print( "-> No fue posible realizar la consulta "\
                       "'ya que se especificó un 'target' no valido: "\
                      f"{target}'.")
                data = False
            self.__db.close_connection()
            if isinstance(data, list):
                members = []
                for row in data:
                    range = RangeModel(row['range_id'],
                                       row['range_name'],
                                       row['range_control'],
                                       row['range_description'])
                    principal = MemberModel(row['principal_id'],
                                            row['principal_name'])
                    member = MemberModel(row['id'],
                                         row['name'],
                                         range,
                                         principal,
                                         row['datecreate'],
                                         row['dateupdate'],
                                         row['totalpoints'])
                    members.append(member)
                return members
            else:
                return data
        elif option == "atpoints":
            selectQuery = (
            "SELECT "\
                "r.id AS range_id, "\
                "r.nombre AS range_name, "\
                "r.control AS range_control, "\
                "r.descripcion AS range_description, "\
                "pi.id AS principal_id, "\
                "pi.nombre AS principal_name, "\
                "i.id, "\
                "i.nombre AS name, "\
                "strftime('%d/%m/%Y', i.fechacreacion) AS datecreate, "\
                "strftime('%d/%m/%Y', i.fechamodificacion) AS dateupdate, "\
                "COALESCE(SUM(e.puntos), 0) AS totalpoints "\
            "FROM integrantes i "\
            "LEFT JOIN rangos r ON r.id = i.rango_id "\
            "LEFT JOIN integrantes AS pi ON pi.id = i.principal_id "\
            "LEFT JOIN asistencias a ON a.integrante_id = i.id"\
            )
            self.__db.start_connection()
            if target.keys() == {"date_1", "date_2"}:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "AND a.fecha BETWEEN "\
                        "? AND ? "\
                        "LEFT JOIN eventos e ON e.id = a.evento_id "\
                        "GROUP BY i.id "\
                        "ORDER BY totalpoints DESC",
                        (target["date_1"],
                         target["date_2"],))
            elif target.keys() == {"id", "date_1", "date_2"}:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "AND a.fecha BETWEEN "\
                        "? AND ? "\
                        "LEFT JOIN eventos e ON e.id = a.evento_id "\
                        "WHERE i.id = ? "\
                        "GROUP BY i.id "\
                        "ORDER BY totalpoints DESC",
                        (target["date_1"],
                         target["date_2"],
                         target["id"],))
            elif target.keys() == {"name", "date_1", "date_2"}:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "AND a.fecha BETWEEN "\
                        "? AND ? "\
                        "LEFT JOIN eventos e ON e.id = a.evento_id "\
                        "WHERE i.nombre = ? "\
                        "GROUP BY i.id "\
                        "ORDER BY totalpoints DESC",
                        (target["date_1"],
                         target["date_2"],
                         target["name"],))
            elif target.keys() == {"range_id", "date_1", "date_2"}:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "AND a.fecha BETWEEN "\
                        "? AND ? "\
                        "LEFT JOIN eventos e ON e.id = a.evento_id "\
                        "WHERE i.rango_id = ? "\
                        "GROUP BY i.id "\
                        "ORDER BY totalpoints DESC",
                        (target["date_1"],
                         target["date_2"],
                         target["range_id"],))
            elif target.keys() == {"event_id", "date_1", "date_2"}:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "AND a.fecha BETWEEN "\
                        "? AND ? "\
                        "LEFT JOIN eventos e ON e.id = a.evento_id "\
                        "AND a.evento_id = ? "\
                        "GROUP BY i.id "\
                        "ORDER BY totalpoints DESC",
                        (target["date_1"],
                         target["date_2"],
                         target["event_id"],))
            elif target.keys() == {"id", "event_id", "date_1", "date_2"}:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "AND a.fecha BETWEEN "\
                        "? AND ? "\
                        "LEFT JOIN eventos e ON e.id = a.evento_id "\
                        "AND a.evento_id = ? "\
                        "WHERE i.id = ? "\
                        "GROUP BY i.id "\
                        "ORDER BY totalpoints DESC",
                        (target["date_1"],
                         target["date_2"],
                         target["event_id"],
                         target["id"],))
            elif target.keys() == {"name", "event_id", "date_1", "date_2"}:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "AND a.fecha BETWEEN "\
                        "? AND ? "\
                        "LEFT JOIN eventos e ON e.id = a.evento_id "\
                        "AND a.evento_id = ? "\
                        "AND i.nombre = ? "\
                        "GROUP BY i.id "\
                        "ORDER BY totalpoints DESC",
                        (target["date_1"],
                         target["date_2"],
                         target["event_id"],
                         target["name"],))
            elif target.keys() == {"range_id", "event_id", "date_1", "date_2"}:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "AND a.fecha BETWEEN "\
                        "? AND ? "\
                        "LEFT JOIN eventos e ON e.id = a.evento_id "\
                        "AND a.evento_id = ? "\
                        "WHERE i.rango_id = ? "\
                        "GROUP BY i.id "\
                        "ORDER BY totalpoints DESC",
                        (target["date_1"],
                         target["date_2"],
                         target["event_id"],
                         target["range_id"],))
            else:
                print( "-> No fue posible realizar la consulta "\
                       "'ya que se especificó un 'target' no valido: "\
                      f"{target}'.")
                data = False
            self.__db.close_connection()
            if isinstance(data, list):
                members = []
                for row in data:
                    range = RangeModel(row['range_id'],
                                       row['range_name'],
                                       row['range_control'],
                                       row['range_description'])
                    principal = MemberModel(row['principal_id'],
                                            row['principal_name'])
                    member = MemberModel(row['id'],
                                         row['name'],
                                         range,
                                         principal,
                                         row['datecreate'],
                                         row['dateupdate'],
                                         row['totalpoints'])
                    members.append(member)
                return members
            else:
                return data
        else:
            print( "-> No fue posible realizar la consulta "\
                   "'ya que se especificó un 'option' no valido: "\
                  f"{option}'.")
            return False

    def insert(self, member : MemberModel):
        self.__db.start_connection()
        data = self.__db.execute_query("INSERT INTO "\
        "integrantes (nombre, rango_id, principal_id, fechacreacion) "\
        "VALUES (?, ?, ?, ?)",
        (member.getName(),
         member.getRange().getId(),
         member.getPrincipal().getId(),
         member.getDateCreate(),))
        if data:
            data = self.__db.execute_query("SELECT last_insert_rowid()")[0][0]
        self.__db.close_connection()
        return data

    def update(self, member: MemberModel):
        self.__db.start_connection()
        data = self.__db.execute_query("UPDATE integrantes "\
        "SET nombre = ?, rango_id = ?, principal_id = ?, "\
        "fechamodificacion = ? "\
        "WHERE id = ?",
        (member.getName(),
         member.getRange().getId(),
         member.getPrincipal().getId(),
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