from DB.database import Database
from Controllers.assistController import AssistController
from Controllers.eventController import EventController
from Controllers.memberController import MemberController
from Controllers.rangeController import RangeController
from Helpers.helpers import Helpers

class AppHandler:
    def __init__(self):
        self.__db = Database("avalon.db", "avalon-lite.sql", "data.sql")
        self.__asistenciaController = AssistController(self.__db)
        self.__rangoController = RangeController(self.__db)
        self.__eventoController = EventController(self.__db)
        self.__integranteController = MemberController(self.__db)

    def getDatas(self, request, struct):
        try:
            target = Helpers.setTarget(self, request, struct["targets"])
            nameCtrl, structRef = dict(struct["controller"]).popitem()
            aliasCtrl = structRef["alias"]
            references = structRef["ref"]
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
                return f"No se encontraron ___{aliasCtrl}s___ "\
                        "para la consulta realizada."
            else:
                return False
        except Exception as ex:
            print(f"-> Ocurrio un error al intentar seleccionar "\
                   "en la base de datos: {str(ex)}.")
            return False

    def setData(self, request, struct):
        try:
            target = Helpers.setTarget(self, request, struct["targets"])
            nameCtrl, references = struct["controller"].popitem()
            aliasCtrl = references["alias"]
            if isinstance(target, dict):
                controller = f"_AppHandler__{nameCtrl}Controller"
                key = references["create"]
                if key:
                    method = f"get{nameCtrl.capitalize()}s"
                    exist = getattr(getattr(self, controller),
                                    method)({key : target[key]})
                    if isinstance(exist, list):
                        return f"{'La' if aliasCtrl[0] == 'a' else 'El'} "\
                               f"___{aliasCtrl}___ "\
                               f"de **_{struct['targets'][key]['alias']}_** "\
                               f"\'{target[key]}\' "\
                                "ya se encuentra en la base de datos."
                    elif exist:
                        method = f"create{nameCtrl.capitalize()}"
                        result = getattr(getattr(self, controller),
                                         method)(**target)
                    else:
                        return False
                else:
                    method = f"create{nameCtrl.capitalize()}"
                    result = getattr(getattr(self, controller),
                                     method)(**target)
                return (f"{'La' if aliasCtrl[0] == 'a' else 'El'} "\
                        f"___{aliasCtrl}___ ha sido "\
                        f"cread{'a' if aliasCtrl[0] == 'a' else 'o'} "\
                        f"con exito sobre el **_ID_** '{result}'."\
                        if result else False)
            else:
                return target
        except Exception as ex:
            print( "-> Ocurrio un error al intentar insertar "\
                  f"en la base de datos: {str(ex)}.")
            return False

    def updateData(self, request, struct):
        try:
            target = Helpers.setTarget(self, request, struct["targets"])
            nameCtrl, references = struct["controller"].popitem()
            aliasCtrl = references["alias"]
            if isinstance(target, dict):
                controller = f"_AppHandler__{nameCtrl}Controller"
                key = references["update"]
                method = f"get{nameCtrl.capitalize()}s"
                existUpd = getattr(getattr(self, controller),
                                method)({key : target[key]})
                if isinstance(existUpd, list):
                    key = references["create"]
                    if key:
                        existSet = getattr(getattr(self, controller),
                                        method)({key : target[key]})
                        if (isinstance(existSet, list) and
                            existSet[0]["id"] != existUpd[0]["id"]):
                            return f"{'La' if aliasCtrl[0] == 'a' else 'El'} "\
                                   f"___{aliasCtrl}___ "\
                                   f"de **_{struct['targets'][key]['alias']}_"\
                                    "** "\
                                   f"\'{target[key]}\' "\
                                    "ya se encuentra en la base de datos."
                        elif existSet:
                            method = f"update{nameCtrl.capitalize()}"
                            target["id"] = existUpd[0]["id"]
                            result = getattr(getattr(self, controller),
                                             method)(**target)
                        else:
                            return False
                    else:
                        method = f"update{nameCtrl.capitalize()}"
                        target["id"] = existUpd[0]["id"]
                        result = getattr(getattr(self, controller),
                                         method)(**target)
                    return (f"{'La' if aliasCtrl[0] == 'a' else 'El'} "\
                            f"___{aliasCtrl}___ ha sido "\
                            f"actualizad{'a' if aliasCtrl[0] == 'a' else 'o'} "\
                            "con exito."\
                            if result else False)
                elif existUpd:
                    return f"{'La' if aliasCtrl[0] == 'a' else 'El'} "\
                           f"___{aliasCtrl}___ "\
                           f"de **_{struct['targets'][key]['alias']}_** "\
                           f"\'{target[key]}\' "\
                            "no se encuentra en la base de datos."
                else:
                    return False
            else:
                return target
        except Exception as ex:
            print( "-> Ocurrio un error al intentar actualizar "\
                  f"en la base de datos: {str(ex)}.")
            return False

    def deleteData(self, request, struct):
        try:
            target = Helpers.setTarget(self, request, struct["targets"])
            nameCtrl, references = struct["controller"].popitem()
            aliasCtrl = references["alias"]
            if isinstance(target, dict):
                controller = f"_AppHandler__{nameCtrl}Controller"
                key = references["delete"]
                method = f"get{nameCtrl.capitalize()}s"
                exist = getattr(getattr(self, controller),
                                method)({key : target[key]})
                if isinstance(exist, list):
                    method = f"delete{nameCtrl.capitalize()}"
                    target.pop(key)
                    target["id"] = exist[0]["id"]
                    result = getattr(getattr(self, controller),
                                     method)(**target)
                elif exist:
                    return f"{'La' if aliasCtrl[0] == 'a' else 'El'} "\
                           f"___{aliasCtrl}___ "\
                           f"de **_{struct['targets'][key]['alias']}_** "\
                           f"\'{target[key]}\' "\
                            "no se encuentra en la base de datos."
                else:
                    return False
                return (f"{'La' if aliasCtrl[0] == 'a' else 'El'} "\
                        f"___{aliasCtrl}___ ha sido "\
                        f"eliminad{'a' if aliasCtrl[0] == 'a' else 'o'} "\
                         "con exito."\
                        if result else False)
            else:
                return target
        except Exception as ex:
            print( "-> Ocurrio un error al intentar eliminar "\
                  f"en la base de datos: {str(ex)}.")
            return False