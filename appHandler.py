import sys
sys.path.insert(1, './DB')
from database import Database
sys.path.insert(1, './Controllers')
from database import Database
sys.path.insert(1, './Helpers')
from participacionController import ParticipacionController
from rangoController import RangoController
from eventoController import EventoController
from integranteController import IntegranteController
from helpers import Helpers
from datetime import datetime

class AppHandler:
    def __init__(self):
        self.__db = Database("avalon.db", "avalon-lite.sql", "data.sql")
        self.__participacionController = ParticipacionController(self.__db)
        self.__rangoController = RangoController(self.__db)
        self.__eventoController = EventoController(self.__db)
        self.__integranteController = IntegranteController(self.__db)
    
    def getIntegrantes(self, request, struct = None):
        if struct is None:
            integrantes = self.__integranteController.getIntegrantes()
        else:
            data = Helpers.checkRequest(request, struct)
            if type(data) == list:
                target = {}
                for index, key in enumerate(struct.keys()):
                    target[key] = data[index]
                integrantes = self.__integranteController.getIntegrantes(target)
            else:
                return data
        if integrantes:
            data = []
            for integrante in integrantes:
                rangoName = self.__rangoController.getRangos({"id" : integrante["rango_id"]})
                if rangoName:
                    rangoName = rangoName[0]["name"] 
                else:
                    rangoName = 'Unknown'   
                data.append(
                    {   "Id" : integrante["id"],
                        "Nombre" : integrante["name"],
                        "Rango" : rangoName,
                        "Fecha de creacion" : integrante["datecreate"],
                        "Fecha de modificacion" : integrante["dateupdate"]
                    }
                )
            return data
        else: 
            return False
    
    def getEventos(self, target = None):
        eventos = self.__eventoController.getEventos(target)
        if eventos:
            data = []
            for evento in eventos:
                data.append(
                    {
                        "Id" : evento["id"],
                        "Nombre" : evento["name"],
                        "Puntos" : evento["points"],
                        "Descripción" : evento["description"]
                    }
                )
            return data
        else: 
            return False

    def getParticipaciones(self, target = None):
        participaciones = self.__participacionController.getParticipaciones(target)
        if participaciones:
            data = []
            for participacion in participaciones:
                integranteName = self.__integranteController.getIntegrantes({"id" : participacion["integrante_id"]})
                if integranteName:
                    integranteName = integranteName[0]["name"]
                else:
                    integranteName = 'Unknown'
                eventoName = self.__eventoController.getEventos({"id" : participacion["evento_id"]})
                if eventoName:
                    eventoName = eventoName[0]["name"]
                else: 
                    eventoName = 'Unknown'
                eventoPoints = self.__eventoController.getEventos({"id" : participacion["evento_id"]}) 
                if eventoPoints: 
                    eventoPoints = eventoPoints[0]["points"]
                else:
                    eventoPoints = 'Unknown'
                data.append(
                    {
                        "Id" : participacion["id"],
                        "Integrante" : integranteName,
                        "Evento" : eventoName,
                        "Puntos" : eventoPoints,
                        "Fecha" : participacion["date"]
                    }
                )
            return data
        else: 
            return False
        
    def getRangos(self, target = None):
        rangos = self.__rangoController.getRangos(target)
        if rangos:
            data = []
            for rango in rangos:
                data.append(
                    {
                        "Id" : rango["id"],
                        "Nombre" : rango["name"],
                        "Descripción" : rango["description"]
                    }
                )
            return data
        else: 
            return False

    def setIntegrante(self, request):
        struct = {
            "Nombre" : str,
            "Rango" : str,
            "Fecha (AA-MM-DD)" : datetime
        }
        data = Helpers.checkRequest(request, struct)
        if type(data) == list:
            data = self.__integranteController.createIntegrante(data[0], data[1], data[2])
            return data
        else:
            return data
        
        
        
        
        



