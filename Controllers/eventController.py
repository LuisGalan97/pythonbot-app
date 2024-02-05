from DB.database import Database
from Models.eventModel import EventModel
from Services.eventService import EventService

class EventController:
    def __init__(self, db : Database):
        self.__service = EventService(db)

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
        evento = EventModel(None, name, points, description)
        result = self.__service.insert(evento)
        return result

    def updateEvento(self, id, name, points, description):
        evento = EventModel(id, name, points, description)
        result = self.__service.update(evento)
        return result

    def deleteEvento(self, id):
        evento = EventModel(id, None, None, None)
        result = self.__service.delete(evento)
        return result