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
        self.db = Database("avalon.db", "avalon-lite.sql", "data.sql")
        self.partCtrl = ParticipacionController(self.db)
        self.rangoCtrl = RangoController(self.db)
        self.eventCtrl = EventoController(self.db)
        self.inteCtrl = IntegranteController(self.db)



