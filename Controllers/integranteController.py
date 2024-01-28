from DB.database import Database
from Models.integranteModel import IntegranteModel
from Models.rangoModel import RangoModel
from Services.integranteService import IntegranteService

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
                        "rango_description" : integrante.
                                              getRango().
                                              getDescription(),
                        "datecreate" : integrante.getDateCreate(),
                        "dateupdate" : integrante.getDateUpdate()
                    })
            return data
        else:
            return integrantes

    def createIntegrante(self, name, rango_id, date):
        rango = RangoModel(rango_id, None, None, None)
        integrante = IntegranteModel(None, name, rango, date, None)
        result = self.__service.insert(integrante)
        return result

    def updateIntegrante(self, id, name, rango_id, date):
        rango = RangoModel(rango_id, None, None, None)
        integrante = IntegranteModel(id, name, rango, None, date)
        result = self.__service.update(integrante)
        return result

    def deleteIntegrante(self, id):
        integrante = IntegranteModel(id, None, None, None, None)
        result = self.__service.delete(integrante)
        return result