from DB.database import Database
from Models.assistModel import AssistModel
from Models.eventModel import EventModel
from Models.memberModel import MemberModel
from Models.rangeModel import RangeModel

class AssistService:
    def __init__(self, db : Database):
        self.__db = db

    def select(self, target, option):
        if not option:
            selectQuery = (
            "SELECT "\
                "r.id AS member_range_id, "\
                "r.nombre AS member_range_name, "\
                "r.control AS member_range_control, "\
                "r.descripcion AS member_range_description, "\
                "i.id AS member_id, "\
                "i.nombre AS member_name, "\
                "strftime('%d/%m/%Y', i.fechacreacion) AS member_datecreate, "\
                "strftime('%d/%m/%Y', i.fechamodificacion) AS "\
                "member_dateupdate, "\
                "e.id AS event_id, "\
                "e.nombre AS event_name, "\
                "e.puntos AS event_points, "\
                "e.descripcion AS event_description, "\
                "a.id, "\
                "strftime('%d/%m/%Y', a.fecha) AS date "\
            "FROM asistencias a "\
            "LEFT JOIN integrantes i ON i.id = a.integrante_id "\
            "LEFT JOIN eventos e ON e.id = a.evento_id "\
            "LEFT JOIN rangos r ON r.id = i.rango_id"
            )
            self.__db.start_connection()
            if not target:
                data = self.__db.execute_query(selectQuery)
            elif target.keys() == {"id"}:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "WHERE a.id = ?",
                        (target["id"],))
            elif target.keys() == {"member_id"}:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "WHERE a.integrante_id = ?",
                        (target["member_id"],))
            elif target.keys() == {"event_id"}:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "WHERE a.evento_id = ?",
                        (target["event_id"],))
            elif target.keys() == {"date_1", "date_2"}:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "WHERE a.fecha BETWEEN ? AND ?",
                        (target["date_1"],
                         target["date_2"],))
            elif target.keys() == {"member_id", "event_id"}:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "WHERE a.integrante_id = ? "\
                        "AND a.evento_id = ?",
                        (target["member_id"],
                         target["event_id"],))
            elif target.keys() == {"member_id", "date_1", "date_2"}:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "WHERE a.fecha BETWEEN ? AND ? "\
                        "AND a.integrante_id = ?",
                        (target["date_1"],
                         target["date_2"],
                         target["member_id"],))
            elif target.keys() == {"event_id", "date_1", "date_2"}:
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "WHERE a.fecha BETWEEN ? AND ? "\
                        "AND a.evento_id = ?",
                        (target["date_1"],
                         target["date_2"],
                         target["event_id"],))
            elif (target.keys() ==
                {"member_id", "event_id", "date_1", "date_2"}):
                data = self.__db.execute_query(
                       f"{selectQuery} "\
                        "WHERE a.fecha BETWEEN ? AND ? "\
                        "AND a.integrante_id = ? AND "\
                        "a.evento_id = ?",
                        (target["date_1"],
                         target["date_2"],
                         target["member_id"],
                         target["event_id"],))
            else:
                print( "-> No fue posible realizar la consulta "\
                       "'ya que se especificó un 'target' no valido: "\
                      f"{target}'.")
                data = False
            self.__db.close_connection()
            if isinstance(data, list):
                assists = []
                for row in data:
                    range = RangeModel(row['member_range_id'],
                                       row['member_range_name'],
                                       row['member_range_control'],
                                       row['member_range_description'])
                    member = MemberModel(row['member_id'],
                                         row['member_name'],
                                         range,
                                         row['member_datecreate'],
                                         row['member_dateupdate'])
                    event = EventModel(row['event_id'],
                                       row['event_name'],
                                       row['event_points'],
                                       row['event_description'])
                    assist = AssistModel(row['id'],
                                         member,
                                         event,
                                         row['date'])
                    assists.append(assist)
                return assists
            else:
                return data
        else:
            print( "-> No fue posible realizar la consulta "\
                   "'ya que se especificó un 'option' no valido: "\
                  f"{option}'.")
            return False

    def insert(self, assist : AssistModel):
        self.__db.start_connection()
        data = self.__db.execute_query("INSERT INTO "\
        "asistencias (integrante_id, evento_id, fecha) "\
        "VALUES (?, ?, ?)",
        (assist.getMember().getId(),
         assist.getEvent().getId(),
         assist.getDate(),))
        if data:
            data = self.__db.execute_query("SELECT last_insert_rowid()")[0][0]
        self.__db.close_connection()
        return data

    def update(self, assist: AssistModel):
        self.__db.start_connection()
        data = self.__db.execute_query("UPDATE asistencias "\
        "SET integrante_id = ?, evento_id = ?, fecha = ? "\
        "WHERE id = ?",
        (assist.getMember().getId(),
         assist.getEvent().getId(),
         assist.getDate(),
         assist.getId(),))
        self.__db.close_connection()
        return data

    def delete(self, assist: AssistModel):
        self.__db.start_connection()
        data = self.__db.execute_query("DELETE FROM asistencias "\
        "WHERE id = ?",
        (assist.getId(),))
        self.__db.close_connection()
        return data