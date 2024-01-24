import os
dir = os.path.dirname(os.path.abspath(__file__))
dir = os.path.dirname(dir)
import sys
sys.path.insert(1, f'{dir}/Models')
from rangoModel import RangoModel
sys.path.insert(1, f'{dir}/Services')
from rangoService import RangoService
sys.path.insert(1, f'{dir}/DB')
from database import Database

class RangoController:
    def __init__(self, db : Database):
        self.__service = RangoService(db)

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
        elif rangos:
            return True
        else:
            return False

    def createRango(self, name, control, description):
        rango = RangoModel(None, name, control, description)
        result = self.__service.insert(rango)
        if result:
            return True
        else:
            return False

    def updateRango(self, id, name, control, description):
        rango = RangoModel(id, name, control, description)
        result = self.__service.update(rango)
        if result:
            return True
        else:
            return False

    def deleteRango(self, id):
        rango = RangoModel(id, None, None, None)
        result = self.__service.delete(rango)
        if result:
            return True
        else:
            return False