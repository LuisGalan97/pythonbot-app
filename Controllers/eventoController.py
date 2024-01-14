import sys
sys.path.insert(1, './Models')
from eventoModel import EventoModel
sys.path.insert(1, './Services')
from eventoService import EventoService
sys.path.insert(1, './DB')
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
                        "id" : evento.getId() if evento.getId() else 'None',
                        "name" : evento.getName() if evento.getName() else 'None',
                        "points" : evento.getPoints() if evento.getPoints() else 'None',
                        "description" : evento.getDescription() if evento.getDescription() else 'None'
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
        result = self.__service.delete(id)
        if result:
            return True
        else:
            return False