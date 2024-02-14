from DB.database import Database
from Models.assistModel import AssistModel
from Models.eventModel import EventModel
from Models.memberModel import MemberModel
from Services.assistService import AssistService

class AssistController:
    def __init__(self, db : Database):
        self.__service = AssistService(db)

    def getAssists(self, target = None):
        assists = self.__service.select(target)
        if isinstance(assists, list):
            data = []
            for assist in assists:
                data.append(
                    {
                        "id" : assist.getId(),
                        "member_id" : assist.
                                      getMember().
                                      getId(),
                        "member_name" : assist.
                                        getMember().
                                        getName(),
                        "member_range_id" : assist.
                                            getMember().
                                            getRange().
                                            getId(),
                        "member_range_name" : assist.
                                              getMember().
                                              getRange().
                                              getName(),
                        "member_range_control" : assist.
                                                 getMember().
                                                 getRange().
                                                 getControl(),
                        "member_range_description" : assist.
                                                     getMember().
                                                     getRange().
                                                     getDescription(),
                        "member_datecreate" : assist.
                                              getMember().
                                              getDateCreate(),
                        "member_dateupdate" : assist.
                                              getMember().
                                              getDateUpdate(),
                        "event_id" : assist.
                                     getEvent().
                                     getId(),
                        "event_name" : assist.
                                       getEvent().
                                       getName(),
                        "event_points" : assist.
                                         getEvent().
                                         getPoints(),
                        "event_description" : assist.
                                              getEvent().
                                              getDescription(),
                        "date" : assist.getDate()
                    })
            return data
        else:
            return assists

    def createAssist(self, member_id, event_id, date):
        member = MemberModel(member_id, None, None, None, None, None)
        event = EventModel(event_id, None, None, None)
        assist = AssistModel(None, member, event, date)
        result = self.__service.insert(assist)
        return result

    def updateAssist(self, id, member_id, event_id, date):
        member = MemberModel(member_id, None, None, None, None, None)
        event = EventModel(event_id, None, None, None)
        assist = AssistModel(id, member, event, date)
        result = self.__service.update(assist)
        return result

    def deleteAssist(self, id):
        assist = AssistModel(id, None, None, None)
        result = self.__service.delete(assist)
        return result