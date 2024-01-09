class EventoModel:
    def __init__(self, id, name, points, description):
        self.__id = id
        self.__name = name
        self.__points = points
        self.__description = description

    def getId(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def getPoints(self):
        return self.__points

    def getDescription(self):
        return self.__description