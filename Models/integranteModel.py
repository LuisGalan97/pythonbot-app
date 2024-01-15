from rangoModel import RangoModel

class IntegranteModel:
    def __init__(self, id, name, rango : RangoModel, datecreate, dateupdate):
        self.__id = id
        self.__name = name
        self.__rango = rango
        self.__datecreate = datecreate
        self.__dateupdate = dateupdate

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getRango(self):
        return self.__rango

    def getDateCreate(self):
        return self.__datecreate

    def getDateUpdate(self):
        return self.__dateupdate