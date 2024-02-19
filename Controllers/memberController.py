from DB.database import Database
from Models.memberModel import MemberModel
from Models.rangeModel import RangeModel
from Services.memberService import MemberService

class MemberController:
    def __init__(self, db : Database):
        self.__service = MemberService(db)

    def getMembers(self, target = None, option = None):
        members = self.__service.select(target, option)
        if isinstance(members, list):
            data = []
            for member in members:
                data.append(
                    {
                        "id" : member.getId(),
                        "name" : member.getName(),
                        "range_id" : member.getRange().getId(),
                        "range_name" : member.getRange().getName(),
                        "range_control" : member.getRange().getControl(),
                        "range_description" : member.
                                              getRange().
                                              getDescription(),
                        "principal_id" : member.getPrincipal().getId(),
                        "principal_name" : member.getPrincipal().getName(),
                        "datecreate" : member.getDateCreate(),
                        "dateupdate" : member.getDateUpdate(),
                        "totalpoints" : member.getTotalPoints()
                    })
            return data
        else:
            return members

    def createMember(self, name, range_id, date, principal_id = None):
        range = RangeModel(range_id)
        principal = MemberModel(principal_id)
        member = MemberModel(None, name, range, principal, date)
        result = self.__service.insert(member)
        return result

    def updateMember(self, id, name, range_id, date, principal_id = None):
        range = RangeModel(range_id)
        principal = MemberModel(principal_id)
        member = MemberModel(id, name, range, principal, None, date)
        result = self.__service.update(member)
        return result

    def deleteMember(self, id):
        member = MemberModel(id)
        result = self.__service.delete(member)
        return result