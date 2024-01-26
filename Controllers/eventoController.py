from DB.database import Database
from Models.eventoModel import EventoModel
from Services.eventoService import EventoService

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
        else:
            return eventos

    def createEvento(self, name, points, description):
        evento = EventoModel(None, name, points, description)
        result = self.__service.insert(evento)
        return result

    def updateEvento(self, id, name, points, description):
        evento = EventoModel(id, name, points, description)
        result = self.__service.update(evento)
        return result

    def deleteEvento(self, id):
        evento = EventoModel(id, None, None, None)
        result = self.__service.delete(evento)
        return result