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