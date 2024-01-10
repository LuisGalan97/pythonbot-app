import sys
sys.path.insert(1, './DB')
from database import Database
sys.path.insert(1, './Controllers')
from participacionController import ParticipacionController
from rangoController import RangoController
from eventoController import EventoController
from integranteController import IntegranteController
import json

class AppHandler:
    def __init__(self):
        self.__db = Database("avalon.db", "avalon-lite.sql", "data.sql")
        self.__participacionController = ParticipacionController(self.__db)
        self.__rangoController = RangoController(self.__db)
        self.__eventoController = EventoController(self.__db)
        self.__integranteController = IntegranteController(self.__db)
    
    def getIntegrantes(self):
        integrantes = self.__integranteController.getIntegrantes()

        if integrantes:
            data = []
            for integrante in integrantes:
                rango = self.__rangoController.getRango(integrante["rango_id"])["name"] 
                rango = rango if rango else 'Unknown'
                data.append(
                    {
                        "Nombre" : integrante["name"],
                        "Rango" : rango,
                        "Fecha de creacion" : integrante["datecreate"],
                        "Fecha de modificacion" : integrante["dateupdate"],
                    }
                )
            return data
        else: 
            return False



