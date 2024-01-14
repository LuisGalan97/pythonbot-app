import sys
sys.path.insert(1, './Models')
from participacionModel import ParticipacionModel
sys.path.insert(1, './Services')
from participacionService import ParticipacionService
sys.path.insert(1, './DB')
from database import Database

class ParticipacionController:
    def __init__(self, db : Database):
        self.__service = ParticipacionService(db)
    
    def getParticipaciones(self, target = None):  
        participaciones = self.__service.select(target)
        if isinstance(participaciones, list):
            data = []
            for participacion in participaciones:
                data.append(
                    {
                        "id" : participacion.getId() if participacion.getId() else 'None',
                        "integrante_id" : participacion.getIntegranteId() if participacion.getIntegranteId() else 'None',
                        "evento_id" : participacion.getEventoId() if participacion.getEventoId() else 'None',
                        "date" : participacion.getDate() if participacion.getDate() else 'None'
                    })
            return data
        elif participaciones:
            return True
        else:
            return False

    def createParticipacion(self, integrante_id, evento_id, date):
        participacion = ParticipacionModel(None, integrante_id, evento_id, date)
        result = self.__service.insert(participacion)
        if result:
            return True
        else:
            return False
    
    def updateParticipacion(self, id, integrante_id, evento_id, date):
        participacion = ParticipacionModel(id, integrante_id, evento_id, date)
        result = self.__service.update(participacion)
        if result:
            return True
        else:
            return False
    
    def deleteParticipacion(self, id):
        result = self.__service.delete(id)
        if result:
            return True
        else:
            return False
