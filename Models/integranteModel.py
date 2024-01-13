class IntegranteModel:
    def __init__(self, id, name, rango_id, datecreate, dateupdate):
        self.__id = id
        self.__name = name
        self.__rango_id = rango_id
        self.__datecreate = datecreate
        self.__dateupdate = dateupdate

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getRangoId(self):
        return self.__rango_id

    def getDateCreate(self):
        return self.__datecreate

    def getDateUpdate(self):
        return self.__dateupdate