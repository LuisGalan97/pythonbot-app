from .integranteModel import IntegranteModel
from .eventoModel import EventoModel

class AsistenciaModel:
    def __init__(self, id, integrante : IntegranteModel, 
                 evento : EventoModel, date):
        self.__id = id
        self.__integrante = integrante
        self.__evento = evento
        self.__date = date

    def getId(self):
        return self.__id

    def getIntegrante(self):
        return self.__integrante

    def getEvento(self):
        return self.__evento

    def getDate(self):
        return self.__date