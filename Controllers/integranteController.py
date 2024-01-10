import sys
sys.path.insert(1, './Models')
from integranteModel import IntegranteModel
sys.path.insert(1, './Services')
from integranteService import IntegranteService
sys.path.insert(1, './DB')
from database import Database

class IntegranteController:
    def __init__(self, db : Database):
        self.service = IntegranteService(db)