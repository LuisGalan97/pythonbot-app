class ParticipacionModel:
    def __init__(self, id, integrante_id, evento_id, date):
        self.__id = id
        self.__integrante_id = integrante_id
        self.__evento_id = evento_id
        self.__date = date

    def getId(self):
        return self.__id

    def getIntegranteId(self):
        return self.__integrante_id

    def getEventoId(self):
        return self.__evento_id

    def getDate(self):
        return self.__date
