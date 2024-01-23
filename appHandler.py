import os
dir = os.path.dirname(os.path.abspath(__file__))
import sys
sys.path.insert(1, f'{dir}/DB')
from database import Database
sys.path.insert(1, f'{dir}/Controllers')
from asistenciaController import AsistenciaController
from eventoController import EventoController
from integranteController import IntegranteController
from rangoController import RangoController
sys.path.insert(1, f'{dir}/Helpers')
from helpers import Helpers

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
            nameCtrl, references = dict(struct["controller"]).popitem()
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
                return f"No se encontraron ___{nameCtrl}s___ para la consulta realizada."
            else:
                return False
        except Exception as ex:
            print(f"-> Ocurrio un error al intentar seleccionar en la base de datos: {str(ex)}.")
            return False

    def setData(self, request, struct):
        try:
            target = Helpers.setTarget(self, request, struct["targets"])
            nameCtrl, references = struct["controller"].popitem()
            if isinstance(target, dict):
                controller = f"_AppHandler__{nameCtrl}Controller"
                key = references["create"]
                if references["create"]:
                    method = f"get{nameCtrl.capitalize()}s"
                    exist = getattr(getattr(self, controller), method)({key : target[key]})
                    if isinstance(exist, list):
                        return f"{'La' if nameCtrl[0] == 'a' else 'El'} ___{nameCtrl}___ "\
                           f"de **_{struct['targets'][key]['alias']}_** \'{target[key]}\' "\
                            "ya se encuentra en la base de datos."
                    elif exist:
                        method = f"create{nameCtrl.capitalize()}"
                        result = getattr(getattr(self, controller), method)(**target)
                    else:
                        return False
                else:
                    method = f"create{nameCtrl.capitalize()}"
                    result = getattr(getattr(self, controller), method)(**target)
                return (f"{'La' if nameCtrl[0] == 'a' else 'El'} ___{nameCtrl}___ ha sido "\
                        f"cread{'a' if nameCtrl[0] == 'a' else 'o'} con exito." if result else False)
            else:
                return target
        except Exception as ex:
            print(f"-> Ocurrio un error al intentar insertar en la base de datos: {str(ex)}.")
            return False

    def updateData(self, request, struct):
        try:
            target = Helpers.setTarget(self, request, struct["targets"])
            nameCtrl, references = struct["controller"].popitem()
            if isinstance(target, dict):
                controller = f"_AppHandler__{nameCtrl}Controller"
                key = references["update"]
                method = f"get{nameCtrl.capitalize()}s"
                exist = getattr(getattr(self, controller), method)({key : target[key]})
                if isinstance(exist, list):
                    method = f"update{nameCtrl.capitalize()}"
                    target["id"] = exist[0]["id"]
                    result = getattr(getattr(self, controller), method)(**target)
                elif exist:
                    return f"{'La' if nameCtrl[0] == 'a' else 'El'} ___{nameCtrl}___ "\
                           f"de **_{struct['targets'][key]['alias']}_** \'{target[key]}\' "\
                            "no se encuentra en la base de datos."
                else:
                    return False
                return (f"{'La' if nameCtrl[0] == 'a' else 'El'} ___{nameCtrl}___ ha sido "\
                        f"actualizad{'a' if nameCtrl[0] == 'a' else 'o'} con exito." if result else False)
            else:
                return target
        except Exception as ex:
            print(f"-> Ocurrio un error al intentar actualizar en la base de datos: {str(ex)}.")
            return False

    def deleteData(self, request, struct):
        try:
            target = Helpers.setTarget(self, request, struct["targets"])
            nameCtrl, references = struct["controller"].popitem()
            if isinstance(target, dict):
                controller = f"_AppHandler__{nameCtrl}Controller"
                key = references["delete"]
                method = f"get{nameCtrl.capitalize()}s"
                exist = getattr(getattr(self, controller), method)({key : target[key]})
                if isinstance(exist, list):
                    method = f"delete{nameCtrl.capitalize()}"
                    target.pop(key)
                    target["id"] = exist[0]["id"]
                    result = getattr(getattr(self, controller), method)(**target)
                elif exist:
                    return f"{'La' if nameCtrl[0] == 'a' else 'El'} ___{nameCtrl}___ "\
                           f"de **_{struct['targets'][key]['alias']}_** \'{target[key]}\' "\
                            "no se encuentra en la base de datos."
                else:
                    return False
                return (f"{'La' if nameCtrl[0] == 'a' else 'El'} ___{nameCtrl}___ ha sido "\
                        f"eliminad{'a' if nameCtrl[0] == 'a' else 'o'} con exito." if result else False)
            else:
                return target
        except Exception as ex:
            print(f"-> Ocurrio un error al intentar eliminar en la base de datos: {str(ex)}.")
            return False