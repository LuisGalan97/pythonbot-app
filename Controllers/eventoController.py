import os
dir = os.path.dirname(os.path.abspath(__file__))
dir = os.path.dirname(dir)
import sys
sys.path.insert(1, f'{dir}/Models')
from eventoModel import EventoModel
sys.path.insert(1, f'{dir}/Services')
from eventoService import EventoService
sys.path.insert(1, f'{dir}/DB')
from database import Database

class EventoController:
    def __init__(self, db : Database):
        self.__service = EventoService(db)

    def getEventos(self, target = None):
        eventos = self.__service.select(target)
        if isinstance(eventos, list):
            data = []
            for evento in eventos:
                data.append(
                    {
                        "id" : evento.getId(),
                        "name" : evento.getName(),
                        "points" : evento.getPoints(),
                        "description" : evento.getDescription()
                    })
            return data
        elif eventos:
            return True
        else:
            return False

    def createEvento(self, name, points, description):
        evento = EventoModel(None, name, points, description)
        result = self.__service.insert(evento)
        if result:
            return True
        else:
            return False

    def updateEvento(self, id, name, points, description):
        evento = EventoModel(id, name, points, description)
        result = self.__service.update(evento)
        if result:
            return True
        else:
            return False

    def deleteEvento(self, id):
        evento = EventoModel(id, None, None, None)
        result = self.__service.delete(evento)
        if result:
            return True
        else:
            return False