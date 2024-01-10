import sys
sys.path.insert(1, './Models')
from rangoModel import RangoModel
sys.path.insert(1, './Services')
from rangoService import RangoService
sys.path.insert(1, './DB')
from database import Database

class RangoController:
    def __init__(self, db : Database):
        self.service = RangoService(db)
    
    def getRangos(self):
        rangos = self.service.selectAll()
        if rangos:
            data = []
            for rango in rangos:
                data.append(
                    {
                        "id" : rango.getId(),
                        "name" : rango.getName(),
                        "description" : rango.getDescription(),
                    })
            return data
        else:
            return False
    
    def getRango(self, id):
        rango = self.service.select(id)
        if rango:
            data = {
                "id" : rango.getId(),
                "name" : rango.getName(),
                "description" : rango.getDescription(),
            }
            return data
        else:
            return False

    def createRango(self, name, description):
        rango = RangoModel(None, name, description)
        result = self.service.insert(rango)
        if result:
            return True
        else:
            return False
    
    def updateRango(self, id, name, description):
        rango = RangoModel(id, name, description)
        result = self.service.update(rango)
        if result:
            return True
        else:
            return False
    
    def deleteRango(self, id):
        result = self.service.delete(id)
        if result:
            return True
        else:
            return False