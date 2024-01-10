import sys
sys.path.insert(1, './Models')
from participacionModel import ParticipacionModel
sys.path.insert(1, './Services')
from participacionService import ParticipacionService
sys.path.insert(1, './DB')
from database import Database

class ParticipacionController:
    def __init__(self, db : Database):
        self.service = ParticipacionService(db)
    
    def getParticipaciones(self):
        participaciones = self.service.selectAll()
        if participaciones:
            data = []
            for participacion in participaciones:
                data.append(
                    {
                        "id" : participacion.getId(),
                        "integrante_id" : participacion.getIntegranteId(),
                        "evento_id" : participacion.getEventoId(),
                        "date" : participacion.getDate()
                    })
            return data
        else:
            return False
    
    def getParticipacion(self, id):
        participacion = self.service.select(id)
        if participacion:
            data = {
                "id" : participacion.getId(),
                "integrante_id" : participacion.getIntegranteId(),
                "evento_id" : participacion.getEventoId(),
                "date" : participacion.getDate()
            }
            return data
        else:
            return False

    def createParticipacion(self, integrante_id, evento_id, date):
        participacion = ParticipacionModel(None, integrante_id, evento_id, date)
        result = self.service.insert(participacion)
        if result:
            return True
        else:
            return False
    
    def updateParticipacion(self, id, integrante_id, evento_id, date):
        participacion = ParticipacionModel(id, integrante_id, evento_id, date)
        result = self.service.update(participacion)
        if result:
            return True
        else:
            return False
    
    def deleteParticipacion(self, id):
        result = self.service.delete(id)
        if result:
            return True
        else:
            return False
