import sys
import pdb
sys.path.insert(1, './DB')
from database import Database
sys.path.insert(1, './Controllers')
from database import Database
sys.path.insert(1, './Helpers')
from asistenciaController import AsistenciaController
from rangoController import RangoController
from eventoController import EventoController
from integranteController import IntegranteController
from helpers import Helpers
from datetime import datetime

class AppHandler:
    def __init__(self):
        self.__db = Database("avalon.db", "avalon-lite.sql", "data.sql")
        self.__asistenciaController = AsistenciaController(self.__db)
        self.__rangoController = RangoController(self.__db)
        self.__eventoController = EventoController(self.__db)
        self.__integranteController = IntegranteController(self.__db)

    def getDatas(self, request, struct):
        try:
            target = Helpers.setTarget(self, request, struct["targets"])
            nameCtrl, references = struct["controller"].popitem()
            if isinstance(target, dict):
                controller = f"_AppHandler__{nameCtrl}Controller"
                method = f"get{nameCtrl.capitalize()}s"
                items = getattr(getattr(self, controller), method)(target)
            else:
                return target
            if isinstance(items, list):
                datas = []
                for item in items:
                    data = {}
                    for key, value in references.items():
                        data[key] = Helpers.checkValue(item[value])
                    datas.append(data)
                return datas
            elif items:
                return f"No se encontraron {nameCtrl}s para la consulta realizada."
            else:
                return False
        except Exception as ex:
            return False

    def setData(self, request, struct):
        try:
            target = Helpers.setTarget(self, request, struct["targets"])
            nameCtrl, references = struct["controller"].popitem()
            if isinstance(target, dict):
                controller = f"_AppHandler__{nameCtrl}Controller"
                if references["update"]:
                    method = f"get{nameCtrl.capitalize()}s"
                    exist = getattr(getattr(self, controller), method)({"name" : target["name"]})
                    if isinstance(exist, list):
                        return f"El {nameCtrl} \'{target['name']}\' ya existe en la base de datos."
                    elif exist:
                        method = f"create{nameCtrl.capitalize()}"
                        result = getattr(getattr(self, controller), method)(**target)
                    else:
                        return False
                else:
                    method = f"create{nameCtrl.capitalize()}"
                    result = getattr(getattr(self, controller), method)(**target)
                return "Creado con exito." if result else "Ocurrio un error."
            else:
                return target
        except Exception as ex:
            return False
    
    def updateData(self, request, struct):
        try:
            target = Helpers.setTarget(self, request, struct["targets"])
            nameCtrl, references = struct["controller"].popitem()
            if isinstance(target, dict):
                controller = f"_AppHandler__{nameCtrl}Controller"
                if references["update"]:
                    method = f"get{nameCtrl.capitalize()}s"
                    exist = getattr(getattr(self, controller), method)({"name" : target["name"]})
                    if isinstance(exist, list):
                        method = f"update{nameCtrl.capitalize()}"
                        target["id"] = exist[0]["id"]
                        result = getattr(getattr(self, controller), method)(**target)
                    elif exist:
                        return f"El {nameCtrl} \'{target['name']}\' no existe en la base de datos."
                    else:
                        return False
                else:
                    return False
                return "Actualizado con exito." if result else "Ocurrio un error."
            else:
                return target
        except Exception as ex:
            print(str(ex))
            return False