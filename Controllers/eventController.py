from DB.database import Database
from Models.eventModel import EventModel
from Services.eventService import EventService

class EventController:
    def __init__(self, db : Database):
        self.__service = EventService(db)

    def getEvents(self, target, option):
        events = self.__service.select(target, option)
        if isinstance(events, list):
            data = []
            for event in events:
                data.append(
                    {
                        "id" : event.getId(),
                        "name" : event.getName(),
                        "points" : event.getPoints(),
                        "description" : event.getDescription()
                    })
            return data
        else:
            return events

    def createEvent(self, name, points, description):
        event = EventModel(None, name, points, description)
        result = self.__service.insert(event)
        return result

    def updateEvent(self, id, name, points, description):
        event = EventModel(id, name, points, description)
        result = self.__service.update(event)
        return result

    def deleteEvent(self, id):
        event = EventModel(id)
        result = self.__service.delete(event)
        return result