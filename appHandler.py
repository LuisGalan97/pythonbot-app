import sys
import pdb
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
        #pdb.set_trace()
        if struct is None:
            integrantes = self.__integranteController.getIntegrantes()
        else:
            result = Helpers.checkRequest(request, struct)
            if isinstance(result, dict):
                foreignkey = {}
                for key in struct:
                    if struct[key]["fk"]:
                        foreignkey[key] = result[key]
                if foreignkey:
                    foreignid = {}
                    target = {}
                    for key, value in foreignkey.items(): 
                        foreignid[key] = getattr(getattr(self, f"__{key}Controller"), f"get{key.capitalize()}s")({"name" : value})
                        if isinstance(foreignid[key], list):
                            target[f"{key}__id"] = foreignid[key][0]["id"]
                        elif foreignid[key]:
                            return True
                        else: 
                            return False
                    for key, value in result.items():
                        if key in foreignid:
                            pass
                        else:
                            target[key] = value
                else:
                    target = {}
                    for index, key in enumerate(struct.keys()):
                        target[key] = result[index]
                    integrantes = self.__integranteController.getIntegrantes(target)               
            else:
                return result
        if isinstance(integrantes, list):
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
        elif integrantes:
            return True
        else: 
            return False
    
    def getEventos(self, request, struct = None):
        if struct is None:
            eventos = self.__eventoController.getEventos()
        else:
            result = Helpers.checkRequest(request, struct)
            if isinstance(result, list):
                target = {}
                for index, key in enumerate(struct.keys()):
                    target[key] = result[index]
                eventos = self.__eventoController.getEventos(target)
            else:
                return result
        if isinstance(eventos, list):
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
        elif eventos:
            return True
        else: 
            return False

    def getParticipaciones(self, request, struct = None):
        if struct is None:
            participaciones = self.__participacionController.getParticipaciones()
        else:
            result = Helpers.checkRequest(request, struct)
            if isinstance(result, list):
                target = {}
                for index, key in enumerate(struct.keys()):
                    target[key] = result[index]
                participaciones = self.__participacionController.getParticipaciones(target)
            else:
                return result  
        if isinstance(participaciones, list):
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
        elif participaciones:
            return True
        else: 
            return False
        
    def getRangos(self, request, struct = None):
        if struct is None:
            rangos = self.__rangoController.getRangos()
        else:
            result = Helpers.checkRequest(request, struct)
            if isinstance(result, list):
                target = {}
                for index, key in enumerate(struct.keys()):
                    target[key] = result[index]
                rangos = self.__rangoController.getRangos(target)
            else:
                return result  
        if isinstance(rangos, list):
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
        elif rangos:
            return True
        else: 
            return False

    def setIntegrante(self, request):
        struct = {"name" : {"type" : str, "alias" : "Nombre", "fk" : False}, 
                 "rango" : {"type" : str, "alias" : "Rango", "fk" : True}, 
                  "date" : {"type" : datetime, "alias" : "Fecha (AA-MM-DD)", "fk" : False}}
        data = Helpers.checkRequest(request, struct)
        if type(data) == list:
            data = self.__integranteController.createIntegrante(data[0], data[1], data[2])
            return data
        else:
            return data
        
        
        
        
        



