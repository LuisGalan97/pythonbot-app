import sys
import pdb
sys.path.insert(1, './DB')
from database import Database
sys.path.insert(1, './Controllers')
from database import Database
sys.path.insert(1, './Helpers')
from asistenciaController import AsistenciaController
from rangoController import RangoController
from eventoController import EventoController
from integranteController import IntegranteController
from helpers import Helpers
from datetime import datetime

class AppHandler:
    def __init__(self):
        self.__db = Database("avalon.db", "avalon-lite.sql", "data.sql")
        self.__asistenciaController = AsistenciaController(self.__db)
        self.__rangoController = RangoController(self.__db)
        self.__eventoController = EventoController(self.__db)
        self.__integranteController = IntegranteController(self.__db)

    def getIntegrantes(self, request, struct = None):
        target = Helpers.setTarget(self, request, struct)
        if isinstance(target, dict):
            integrantes = self.__integranteController.getIntegrantes(target)
        else:
            return target
        if isinstance(integrantes, list):
            data = []
            for integrante in integrantes:
                data.append(
                    {   
                        "Id" : Helpers.checkValue(integrante["id"]),
                        "Nombre" : Helpers.checkValue(integrante["name"]),
                        "Rango" : Helpers.checkValue(integrante["rango_name"]),
                        "Fecha de creacion" : Helpers.checkValue(integrante["datecreate"]),
                        "Fecha de modificacion" : Helpers.checkValue(integrante["dateupdate"])
                    }
                )
            return data
        elif integrantes:
            return "No se encontraron integrantes para la consulta realizada."
        else:
            return False

    def getEventos(self, request, struct = None):
        target = Helpers.setTarget(self, request, struct)
        if isinstance(target, dict):
            eventos = self.__eventoController.getEventos(target)
        else:
            return target
        if isinstance(eventos, list):
            data = []
            for evento in eventos:
                data.append(
                    {
                        "Id" : Helpers.checkValue(evento["id"]),
                        "Nombre" : Helpers.checkValue(evento["name"]),
                        "Puntos" : Helpers.checkValue(evento["points"]),
                        "Descripción" : Helpers.checkValue(evento["description"])
                    }
                )
            return data
        elif eventos:
            return True
        else:
            return False

    def getAsistencias(self, request, struct = None):
        target = Helpers.setTarget(self, request, struct)
        if isinstance(target, dict):
            asistencias = self.__asistenciaController.getAsistencias(target)
        else:
            return target
        if isinstance(asistencias, list):
            data = []
            for asistencia in asistencias:
                data.append(
                    {
                        "Id" : Helpers.checkValue(asistencia["id"]),
                        "Integrante" : Helpers.checkValue(asistencia["integrante_name"]),
                        "Evento" : Helpers.checkValue(asistencia["evento_name"]),
                        "Puntos" : Helpers.checkValue(asistencia["evento_points"]),
                        "Fecha" : Helpers.checkValue(asistencia["date"])
                    }
                )
            return data
        elif asistencias:
            return True
        else:
            return False

    def getRangos(self, request, struct = None):
        target = Helpers.setTarget(self, request, struct)
        if isinstance(target, dict):
            rangos = self.__rangoController.getRangos(target)
        else:
            return target
        if isinstance(rangos, list):
            data = []
            for rango in rangos:
                data.append(
                    {
                        "Id" : Helpers.checkValue(rango["id"]),
                        "Nombre" : Helpers.checkValue(rango["name"]),
                        "Descripción" : Helpers.checkValue(rango["description"])
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