from DB.database import Database
from Models.rangeModel import RangeModel
from Services.rangeService import RangeService

class RangeController:
    def __init__(self, db : Database):
        self.__service = RangeService(db)

    def getRanges(self, target = None, option = None):
        ranges = self.__service.select(target, option)
        if isinstance(ranges, list):
            data = []
            for range in ranges:
                data.append(
                    {
                        "id" : range.getId(),
                        "name" : range.getName(),
                        "control" : range.getControl(),
                        "description" : range.getDescription()
                    })
            return data
        else:
            return ranges

    def createRange(self, name, control, description):
        range = RangeModel(None, name, control, description)
        result = self.__service.insert(range)
        return result

    def updateRange(self, id, name, control, description):
        range = RangeModel(id, name, control, description)
        result = self.__service.update(range)
        return result

    def deleteRange(self, id):
        range = RangeModel(id)
        result = self.__service.delete(range)
        return result