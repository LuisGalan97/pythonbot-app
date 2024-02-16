class RangeModel:
    def __init__(self, id = None,
                 name = None,
                 control = None,
                 description = None):
        self.__id = id
        self.__name = name
        self.__control = control
        self.__description = description

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getControl(self):
        return self.__control

    def getDescription(self):
        return self.__description