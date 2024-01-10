import sys
sys.path.insert(1, './Models')
from rangoModel import RangoModel
sys.path.insert(1, './Services')
from rangoService import RangoService
sys.path.insert(1, './DB')
from database import Database

class RangoController:
    def __init__(self, db : Database):
        self.service = RangoService(db)
