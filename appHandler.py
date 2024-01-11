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
                rangoName = self.__rangoController.getRango(integrante["rango_id"])["name"] 
                rangoName = rangoName if rangoName else 'Unknown'
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
    
    def getEventos(self):
        eventos = self.__eventoController.getEventos()
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

    def getParticipaciones(self):
        participaciones = self.__participacionController.getParticipaciones()
        if participaciones:
            data = []
            for participacion in participaciones:
                integranteName = self.__integranteController.getIntegrante(participacion["integrante_id"])["name"] 
                integranteName = integranteName if integranteName else 'Unknown'
                eventoName = self.__eventoController.getEvento(participacion["evento_id"])["name"] 
                eventoName = eventoName if eventoName else 'Unknown'
                eventoPoints = self.__eventoController.getEvento(participacion["evento_id"])["points"] 
                eventoPoints = eventoPoints if eventoPoints else 'Unknown'
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
        
    def getRangos(self):
        rangos = self.__rangoController.getRangos()
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



