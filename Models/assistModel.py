from .memberModel import MemberModel
from .eventModel import EventModel

class AssistModel:
    def __init__(self, id, member : MemberModel,
                 event : EventModel, date):
        self.__id = id
        self.__member = member
        self.__event = event
        self.__date = date

    def getId(self):
        return self.__id

    def getMember(self):
        return self.__member

    def getEvent(self):
        return self.__event

    def getDate(self):
        return self.__date