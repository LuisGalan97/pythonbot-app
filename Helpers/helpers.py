from datetime import datetime

class Helpers:
    @staticmethod
    def setTarget(self, request, struct):
        target = {}
        if struct:
            result = Helpers.checkRequest(request, struct)
            if isinstance(result, dict):
                foreignkey = {}
                for key in struct:
                    if struct[key]["fk"]:
                        foreignkey[key] = result[key]
                if foreignkey:
                    foreignid = {}
                    for key, value in foreignkey.items():
                        foreignid[key] = getattr(getattr(self, f"_AppHandler__{key}Controller"), f"get{key.capitalize()}s")({"name" : value})
                        if isinstance(foreignid[key], list):
                            target[f"{key}_id"] = foreignid[key][0]["id"]
                        elif foreignid[key]:
                            return f"El valor '{value}' ingresado en el campo "\
                            f"'{struct[key]['alias']}' no fue encontrado en la base de datos."
                        else:
                            return False
                    for key, value in result.items():
                        if not key in foreignid:
                            target[key] = value
                else:
                    target = {}
                    for key, value in result.items():
                        target[key] = value
            else:
                return result
        return target

    @staticmethod
    def checkRequest(request, struct):
            command = request.split(' ')[0]
            content = request.replace(command, '').strip()
            references = f"{', '.join(map(str, list(struct.keys())))}"
            types = [value["type"] for value in struct.values()]
            alias = f"{', '.join(map(str, [value['alias'] for value in struct.values()]))}"
            if content.startswith('['):
                content = content.replace('[', '')
                if content.find(']') != -1:
                    content = content[: content.find(']')]
                    datas = content.split(',')
                    if len(datas) == len(references.split(',')):
                        for i in range(len(datas)):
                            datas[i] = datas[i].strip()
                            if not datas[i]:
                                return "No fue ingresado ningun dato en el campo "\
                                f"'{alias.split(',')[i].strip()}'."
                            try:
                                if types[i] == datetime:
                                    datas[i] = datetime.strptime(datas[i], "%d-%m-%Y")
                                    datas[i] = datas[i].strftime("%Y-%m-%d")
                                else:
                                    datas[i] = types[i](datas[i])
                            except ValueError:
                                return f"El dato '{datas[i]}' ingresado en el campo "\
                                f"'{alias.split(',')[i].strip()}' es invalido."
                            if types[i] == str:
                                if Helpers.checkTrueChar(datas[i][0]):
                                    return f"El dato '{datas[i]}' ingresado en el campo "\
                                    f"'{alias.split(',')[i].strip()}' no debe comenzar "\
                                    "con valores numericos ni caracteres especiales."
                                try:
                                    int(datas[i][0])
                                    return f"El dato '{datas[i]}' ingresado en el campo "\
                                    f"'{alias.split(',')[i].strip()}' no debe comenzar "\
                                    "con valores numericos ni caracteres especiales."
                                except ValueError:
                                    pass
                                if Helpers.checkChar(datas[i]):
                                    return f"El dato '{datas[i]}' ingresado en el campo "\
                                    f"'{alias.split(',')[i].strip()}' no debe contener "\
                                    "caracteres especiales a excepcion de '-' o '|'."
                                if Helpers.checkRepeatChar(datas[i]):
                                    return f"El dato '{datas[i]}' ingresado en el campo "\
                                    f"'{alias.split(',')[i].strip()}' no debe debe repetir "\
                                    "mas de dos veces los caracteres '-' o '|'."
                        references = list(map(lambda x: x.strip(), references.split(',')))
                        datas = dict(zip(references, datas))
                        return datas
                    else:
                        return "Datos ingresados invalidos, "\
                        "recuerda que debes ingresar:\n"\
                        f"[{alias}]"
                else:
                    return "El comando debe mantener la forma:\n"\
                    f"{command} [{alias}]"
            else:
                return "El comando debe mantener la forma:\n"\
                f"{command} [{alias}]"

    @staticmethod
    def checkChar(strValue):
        spechar = ['/', '\\', '\'', '!', '¡',
        '?', '¿', '"', '´', '{', '}', '[', ']',
        '*', '+', '$', '%', '&', '=', '#', '@',
        '_', '||', '°', '¬', '.', ';', ':', '>',
        '<', '~', '¨', '^', '`', '--']
        for char in spechar:
            if strValue.find(char) != -1:
                return True
        return False

    @staticmethod
    def checkTrueChar(strValue):
        spechar = ['/', '\\', '\'', '!', '¡',
        '?', '¿', '"', '´', '{', '}', '[', ']',
        '*', '+', '$', '%', '&', '=', '#', '@',
        '_', '|', '°', '¬', '.', ';', ':', '>',
        '<', '~', '¨', '^', '`', '-']
        for char in spechar:
            if strValue.find(char) != -1:
                return True
        return False

    @staticmethod
    def checkRepeatChar(strValue):
        repeat = ['-', '|']
        for char in repeat:
            if strValue.count(char) > 2:
                return True
        return False

    @staticmethod
    def checkValue(value):
        if value:
            return value
        else:
            return "Ninguno"

    @staticmethod
    def getStruct(nameCtrl, targets = None):
        structCtrl = {}
        structTargets = {}
        if nameCtrl == "asistencia":
            structCtrl[nameCtrl] = {
                "Id" : "id",
                #"Id Integrante" : "integrante_id",
                "Integrante" : "integrante_name",
                #"Id Rango" : "integrante_rango_id",
                #"Rango" : "integrante_rango_name",
                #"Descripción Rango" : "integrante_rango_description",
                #"Fecha de creación Integrante" : "integrante_datecreate",
                #"Fecha de modificación Integrante" : "integrante_dateupdate",
                #"Id Evento" : "evento_id",
                "Evento" : "evento_name",
                "Puntos" : "evento_points",
                #"Descripción Evento" : "evento_description",
                "Fecha" : "date"
            }
        elif nameCtrl == "evento":
            structCtrl[nameCtrl] = {
                "Id" : "id",
                "Nombre" : "name",
                "Puntos" : "points",
                "Descripción" : "description"
            }
        elif nameCtrl == "integrante":
            structCtrl[nameCtrl] = {
                "Id" : "id",
                "Nombre" : "name",
                #"Id Rango" : "rango_id",
                "Rango" : "rango_name",
                #"Descripción Rango" : "rango_description",
                "Fecha de creación" : "datecreate",
                "Fecha de modificación" : "dateupdate"
            }
        elif nameCtrl == "rango":
            structCtrl[nameCtrl] = {
                "Id" : "id",
                "Nombre" : "name",
                "Descripción" : "description"
            }
        if targets:
            if "id" in targets:
                structTargets["id"] = {"type" : int, "fk" : False, "alias" : "Identificador"}
            if "name" in targets:
                structTargets["name"] = {"type" : str, "fk" : False, "alias" : "Nombre"}
            if "rango" in targets:
                structTargets["rango"] = {"type" : str, "fk" : True, "alias" : "Rango"}
            if "rango_id" in targets:
                structTargets["rango_id"] = {"type" : int, "fk" : False, "alias" : "Id Rango"}
            if "evento" in targets:
                structTargets["evento"] = {"type" : str, "fk" : True, "alias" : "Evento"}
            if "evento_id" in targets:
                structTargets["evento_id"] = {"type" : int, "fk" : False, "alias" : "Id Evento"}
            if "integrante" in targets:
                structTargets["integrante"] = {"type" : str, "fk" : True, "alias" : "Integrante"}
            if "integrante_id" in targets:
                structTargets["integrante_id"] = {"type" : int, "fk" : False, "alias" : "Id Integrante"}
            if "date_1" in targets:
                structTargets["date_1"] = {"type" : datetime, "fk" : False, "alias" : "Fecha 1 (Día-Mes-Año)"}
            if "date_2" in targets:
                structTargets["date_2"] = {"type" : datetime, "fk" : False, "alias" : "Fecha 2 (Día-Mes-Año)"}
        return {"controller" : structCtrl, "targets" : structTargets}

    @staticmethod
    def setStruct(nameCtrl):
        structCtrl = {}
        structTargets = {}
        if nameCtrl == "asistencia":
            structCtrl[nameCtrl] = {"create" : False}
            structTargets["integrante"] = {"type" : str, "fk" : True, "alias" : "Integrante"}
            structTargets["evento"] = {"type" : str, "fk" : True, "alias" : "Evento"}
            structTargets["date"] = {"type" : datetime, "fk" : False, "alias" : "Fecha (Día-Mes-Año)"}
        elif nameCtrl == "evento":
            structCtrl[nameCtrl] = {"create" : "name"}
            structTargets["name"] = {"type" : str, "fk" : False, "alias" : "Nombre"}
            structTargets["points"] = {"type" : float, "fk" : False, "alias" : "Puntos"}
            structTargets["description"] = {"type" : str, "fk" : False, "alias" : "Descripción"}
        elif nameCtrl == "integrante":
            structCtrl[nameCtrl] = {"create" : "name"}
            structTargets["name"] = {"type" : str, "fk" : False, "alias" : "Nombre"}
            structTargets["rango"] = {"type" : str, "fk" : True, "alias" : "Rango"}
            structTargets["date"] = {"type" : datetime, "fk" : False, "alias" : "Fecha (Día-Mes-Año)"}
        elif nameCtrl == "rango":
            structCtrl[nameCtrl] = {"create" : "name"}
            structTargets["name"] = {"type" : str, "fk" : False, "alias" : "Nombre"}
            structTargets["description"] = {"type" : str, "fk" : False, "alias" : "Descripción"}
        return {"controller" : structCtrl, "targets" : structTargets}

    @staticmethod
    def updStruct(nameCtrl, update):
        structCtrl = {}
        structTargets = {}
        if nameCtrl == "asistencia":
             if update == "id":
                structCtrl[nameCtrl] = {"update" : update}
                structTargets["id"] = {"type" : int, "fk" : False, "alias" : "Identificador"}
                structTargets["integrante"] = {"type" : str, "fk" : True, "alias" : "Integrante"}
                structTargets["evento"] = {"type" : str, "fk" : True, "alias" : "Evento"}
                structTargets["date"] = {"type" : datetime, "fk" : False, "alias" : "Fecha (Día-Mes-Año)"}
        elif nameCtrl == "evento":
            if update == "name":
                structCtrl[nameCtrl] = {"update" : update}
                structTargets["name"] = {"type" : str, "fk" : False, "alias" : "Nombre"}
                structTargets["points"] = {"type" : float, "fk" : False, "alias" : "Puntos"}
                structTargets["description"] = {"type" : str, "fk" : False, "alias" : "Descripción"}
            elif update == "id":
                structCtrl[nameCtrl] = {"update" : update}
                structTargets["id"] = {"type" : int, "fk" : False, "alias" : "Identificador"}
                structTargets["name"] = {"type" : str, "fk" : False, "alias" : "Nombre"}
                structTargets["points"] = {"type" : float, "fk" : False, "alias" : "Puntos"}
                structTargets["description"] = {"type" : str, "fk" : False, "alias" : "Descripción"}
        elif nameCtrl == "integrante":
            if update == "name":
                structCtrl[nameCtrl] = {"update" : update}
                structTargets["name"] = {"type" : str, "fk" : False, "alias" : "Nombre"}
                structTargets["rango"] = {"type" : str, "fk" : True, "alias" : "Rango"}
                structTargets["date"] = {"type" : datetime, "fk" : False, "alias" : "Fecha (Día-Mes-Año)"}
            elif update == "id":
                structCtrl[nameCtrl] = {"update" : update}
                structTargets["id"] = {"type" : int, "fk" : False, "alias" : "Identificador"}
                structTargets["name"] = {"type" : str, "fk" : False, "alias" : "Nombre"}
                structTargets["rango"] = {"type" : str, "fk" : True, "alias" : "Rango"}
                structTargets["date"] = {"type" : datetime, "fk" : False, "alias" : "Fecha (Día-Mes-Año)"}
        elif nameCtrl == "rango":
            if update == "name":
                structCtrl[nameCtrl] = {"update" : update}
                structTargets["name"] = {"type" : str, "fk" : False, "alias" : "Nombre"}
                structTargets["description"] = {"type" : str, "fk" : False, "alias" : "Descripción"}
            elif update == "id":
                structCtrl[nameCtrl] = {"update" : update}
                structTargets["id"] = {"type" : int, "fk" : False, "alias" : "Identificador"}
                structTargets["name"] = {"type" : str, "fk" : False, "alias" : "Nombre"}
                structTargets["description"] = {"type" : str, "fk" : False, "alias" : "Descripción"}
        return {"controller" : structCtrl, "targets" : structTargets}

    @staticmethod
    def delStruct(nameCtrl, delete):
        structCtrl = {}
        structTargets = {}
        if nameCtrl == "asistencia":
             if delete == "id":
                structCtrl[nameCtrl] = {"delete" : delete}
                structTargets["id"] = {"type" : int, "fk" : False, "alias" : "Identificador"}
        elif nameCtrl == "evento":
            if delete == "name":
                structCtrl[nameCtrl] = {"delete" : delete}
                structTargets["name"] = {"type" : str, "fk" : False, "alias" : "Nombre"}
            elif delete == "id":
                structCtrl[nameCtrl] = {"delete" : delete}
                structTargets["id"] = {"type" : int, "fk" : False, "alias" : "Identificador"}
        elif nameCtrl == "integrante":
            if delete == "name":
                structCtrl[nameCtrl] = {"delete" : delete}
                structTargets["name"] = {"type" : str, "fk" : False, "alias" : "Nombre"}
            elif delete == "id":
                structCtrl[nameCtrl] = {"delete" : delete}
                structTargets["id"] = {"type" : int, "fk" : False, "alias" : "Identificador"}
        elif nameCtrl == "rango":
            if delete == "name":
                structCtrl[nameCtrl] = {"delete" : delete}
                structTargets["name"] = {"type" : str, "fk" : False, "alias" : "Nombre"}
            elif delete == "id":
                structCtrl[nameCtrl] = {"delete" : delete}
                structTargets["id"] = {"type" : int, "fk" : False, "alias" : "Identificador"}
        return {"controller" : structCtrl, "targets" : structTargets}