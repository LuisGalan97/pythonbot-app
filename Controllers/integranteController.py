import os
dir = os.path.dirname(os.path.abspath(__file__))
import sys
sys.path.insert(1, f'{dir}/Models')
from integranteModel import IntegranteModel
from rangoModel import RangoModel
sys.path.insert(1, f'{dir}/Services')
from integranteService import IntegranteService
sys.path.insert(1, f'{dir}/DB')
from database import Database

class IntegranteController:
    def __init__(self, db : Database):
        self.__service = IntegranteService(db)

    def getIntegrantes(self, target = None):
        integrantes = self.__service.select(target)
        if isinstance(integrantes, list):
            data = []
            for integrante in integrantes:
                data.append(
                    {
                        "id" : integrante.getId(),
                        "name" : integrante.getName(),
                        "rango_id" : integrante.getRango().getId(),
                        "rango_name" : integrante.getRango().getName(),
                        "rango_control" : integrante.getRango().getControl(),
                        "rango_description" : integrante.getRango().getDescription(),
                        "datecreate" : integrante.getDateCreate(),
                        "dateupdate" : integrante.getDateUpdate()
                    })
            return data
        elif integrantes:
            return True
        else:
            return False

    def createIntegrante(self, name, rango_id, date):
        rango = RangoModel(rango_id, None, None, None)
        integrante = IntegranteModel(None, name, rango, date, None)
        result = self.__service.insert(integrante)
        if result:
            return True
        else:
            return False

    def updateIntegrante(self, id, name, rango_id, date):
        rango = RangoModel(rango_id, None, None, None)
        integrante = IntegranteModel(id, name, rango, None, date)
        result = self.__service.update(integrante)
        if result:
            return True
        else:
            return False

    def deleteIntegrante(self, id):
        integrante = IntegranteModel(id, None, None, None, None)
        result = self.__service.delete(integrante)
        if result:
            return True
        else:
            return False