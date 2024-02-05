from DB.database import Database
from Models.assistModel import AssistModel
from Models.eventModel import EventModel
from Models.memberModel import MemberModel
from Services.assistService import AssistService

class AssistController:
    def __init__(self, db : Database):
        self.__service = AssistService(db)

    def getAsistencias(self, target = None):
        assists = self.__service.select(target)
        if isinstance(assists, list):
            data = []
            for assist in assists:
                data.append(
                    {
                        "id" : assist.getId(),
                        "integrante_id" : assist.
                                          getMember().
                                          getId(),
                        "integrante_name" : assist.
                                            getMember().
                                            getName(),
                        "integrante_rango_id" : assist.
                                                getMember().
                                                getRange().
                                                getId(),
                        "integrante_rango_name" : assist.
                                                  getMember().
                                                  getRange().
                                                  getName(),
                        "integrante_rango_control" : assist.
                                                     getMember().
                                                     getRange().
                                                     getControl(),
                        "integrante_rango_description" : assist.
                                                         getMember().
                                                         getRange().
                                                         getDescription(),
                        "integrante_datecreate" : assist.
                                                  getMember().
                                                  getDateCreate(),
                        "integrante_dateupdate" : assist.
                                                  getMember().
                                                  getDateUpdate(),
                        "evento_id" : assist.
                                      getEvent().
                                      getId(),
                        "evento_name" : assist.
                                        getEvent().
                                        getName(),
                        "evento_points" : assist.
                                          getEvent().
                                          getPoints(),
                        "evento_description" : assist.
                                               getEvent().
                                               getDescription(),
                        "date" : assist.getDate()
                    })
            return data
        else:
            return assists

    def createAsistencia(self, integrante_id, evento_id, date):
        member = MemberModel(integrante_id, None, None, None, None)
        event = EventModel(evento_id, None, None, None)
        assist = AssistModel(None, member, event, date)
        result = self.__service.insert(assist)
        return result

    def updateAsistencia(self, id, integrante_id, evento_id, date):
        member = MemberModel(integrante_id, None, None, None, None)
        event = EventModel(evento_id, None, None, None)
        assist = AssistModel(id, member, event, date)
        result = self.__service.update(assist)
        return result

    def deleteAsistencia(self, id):
        assist = AssistModel(id, None, None, None)
        result = self.__service.delete(assist)
        return result