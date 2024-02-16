from .rangeModel import RangeModel

class MemberModel:
    def __init__(self,
                 id = None,
                 name = None,
                 range : RangeModel = None,
                 datecreate = None,
                 dateupdate = None,
                 totalpoints = None):
        self.__id = id
        self.__name = name
        self.__range = range
        self.__datecreate = datecreate
        self.__dateupdate = dateupdate
        self.__totalpoints = totalpoints

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getRange(self):
        return self.__range

    def getDateCreate(self):
        return self.__datecreate

    def getDateUpdate(self):
        return self.__dateupdate

    def getTotalPoints(self):
        return self.__totalpoints