class RangoModel:
    def __init__(self, id, name, order, description):
        self.__id = id
        self.__name = name
        self.__order = order
        self.__description = description

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getOrder(self):
        return self.__order

    def getDescription(self):
        return self.__description