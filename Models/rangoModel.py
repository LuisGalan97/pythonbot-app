class RangoModel:
    def __init__(self, id, name, description):
        self.__id = id
        self.__name = name
        self.__description = description

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getDescription(self):
        return self.__description