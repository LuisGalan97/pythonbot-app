from DB.database import Database
from Models.memberModel import MemberModel
from Models.rangeModel import RangeModel
from Services.memberService import MemberService

class MemberController:
    def __init__(self, db : Database):
        self.__service = MemberService(db)

    def getIntegrantes(self, target = None):
        members = self.__service.select(target)
        if isinstance(members, list):
            data = []
            for member in members:
                data.append(
                    {
                        "id" : member.getId(),
                        "name" : member.getName(),
                        "rango_id" : member.getRange().getId(),
                        "rango_name" : member.getRange().getName(),
                        "rango_control" : member.getRange().getControl(),
                        "rango_description" : member.
                                              getRange().
                                              getDescription(),
                        "datecreate" : member.getDateCreate(),
                        "dateupdate" : member.getDateUpdate()
                    })
            return data
        else:
            return members

    def createIntegrante(self, name, range_id, date):
        range = RangeModel(range_id, None, None, None)
        member = MemberModel(None, name, range, date, None)
        result = self.__service.insert(member)
        return result

    def updateIntegrante(self, id, name, range_id, date):
        range = RangeModel(range_id, None, None, None)
        member = MemberModel(id, name, range, None, date)
        result = self.__service.update(member)
        return result

    def deleteIntegrante(self, id):
        member = MemberModel(id, None, None, None, None)
        result = self.__service.delete(member)
        return result