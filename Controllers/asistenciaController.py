import sys
sys.path.insert(1, './Models')
from asistenciaModel import AsistenciaModel
from eventoModel import EventoModel
from integranteModel import IntegranteModel
sys.path.insert(1, './Services')
from asistenciaService import AsistenciaService
sys.path.insert(1, './DB')
from database import Database

class AsistenciaController:
    def __init__(self, db : Database):
        self.__service = AsistenciaService(db)

    def getAsistencias(self, target = None):
        asistencias = self.__service.select(target)
        if isinstance(asistencias, list):
            data = []
            for asistencia in asistencias:
                data.append(
                    {
                        "id" : asistencia.getId(),
                        "integrante_id" : asistencia.getIntegrante().getId(),
                        "integrante_name" : asistencia.getIntegrante().getName(),
                        "integrante_rango_id" : asistencia.getIntegrante().getRango().getId(),
                        "integrante_rango_name" : asistencia.getIntegrante().getRango().getName(),
                        "integrante_rango_control" : asistencia.getIntegrante().getRango().getControl(),
                        "integrante_rango_description" : asistencia.getIntegrante().getRango().getDescription(),
                        "integrante_datecreate" : asistencia.getIntegrante().getDateCreate(),
                        "integrante_dateupdate" : asistencia.getIntegrante().getDateUpdate(),
                        "evento_id" : asistencia.getEvento().getId(),
                        "evento_name" : asistencia.getEvento().getName(),
                        "evento_points" : asistencia.getEvento().getPoints(),
                        "evento_description" : asistencia.getEvento().getDescription(),
                        "date" : asistencia.getDate()
                    })
            return data
        elif asistencias:
            return True
        else:
            return False

    def createAsistencia(self, integrante_id, evento_id, date):
        integrante = IntegranteModel(integrante_id, None, None, None, None)
        evento = EventoModel(evento_id, None, None, None)
        asistencia = AsistenciaModel(None, integrante, evento, date)
        result = self.__service.insert(asistencia)
        if result:
            return True
        else:
            return False

    def updateAsistencia(self, id, integrante_id, evento_id, date):
        integrante = IntegranteModel(integrante_id, None, None, None, None)
        evento = EventoModel(evento_id, None, None, None)
        asistencia = AsistenciaModel(id, integrante, evento, date)
        result = self.__service.update(asistencia)
        if result:
            return True
        else:
            return False

    def deleteAsistencia(self, id):
        asistencia = AsistenciaModel(id, None, None, None)
        result = self.__service.delete(asistencia)
        if result:
            return True
        else:
            return False