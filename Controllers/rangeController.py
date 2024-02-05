from DB.database import Database
from Models.rangeModel import RangeModel
from Services.rangeService import RangeService

class RangoController:
    def __init__(self, db : Database):
        self.__service = RangeService(db)

    def getRangos(self, target = None):
        rangos = self.__service.select(target)
        if isinstance(rangos, list):
            data = []
            for rango in rangos:
                data.append(
                    {
                        "id" : rango.getId(),
                        "name" : rango.getName(),
                        "control" : rango.getControl(),
                        "description" : rango.getDescription()
                    })
            return data
        else:
            return rangos

    def createRango(self, name, control, description):
        rango = RangeModel(None, name, control, description)
        result = self.__service.insert(rango)
        return result

    def updateRango(self, id, name, control, description):
        rango = RangeModel(id, name, control, description)
        result = self.__service.update(rango)
        return result

    def deleteRango(self, id):
        rango = RangeModel(id, None, None, None)
        result = self.__service.delete(rango)
        return result