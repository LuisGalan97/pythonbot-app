import sys
sys.path.insert(1, './Models')
from rangoModel import RangoModel
sys.path.insert(1, './Services')
from rangoService import RangoService
sys.path.insert(1, './DB')
from database import Database

class RangoController:
    def __init__(self, db : Database):
        self.__service = RangoService(db)
    
    def getRangos(self):
        rangos = self.__service.selectAll()
        if rangos:
            data = []
            for rango in rangos:
                data.append(
                    {
                        "id" : rango.getId() if rango.getId() else 'None',
                        "name" : rango.getName() if rango.getName() else 'None',
                        "description" : rango.getDescription() if rango.getDescription() else 'None'
                    })
            return data
        else:
            return False
    
    def getRango(self, id):
        rango = self.__service.select(id)
        if rango:
            data = {
                "id" : rango.getId() if rango.getId() else 'None',
                "name" : rango.getName() if rango.getName() else 'None',
                "description" : rango.getDescription() if rango.getDescription() else 'None'
            }
            return data
        else:
            return False

    def createRango(self, name, description):
        rango = RangoModel(None, name, description)
        result = self.__service.insert(rango)
        if result:
            return True
        else:
            return False
    
    def updateRango(self, id, name, description):
        rango = RangoModel(id, name, description)
        result = self.__service.update(rango)
        if result:
            return True
        else:
            return False
    
    def deleteRango(self, id):
        result = self.__service.delete(id)
        if result:
            return True
        else:
            return False