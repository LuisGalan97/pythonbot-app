import sys
sys.path.insert(1, './Models')
from eventoModel import EventoModel
sys.path.insert(1, './Services')
from eventoService import EventoService
sys.path.insert(1, './DB')
from database import Database

class EventoController:
    def __init__(self, db : Database):
        self.service = EventoService(db)
    