from datetime import datetime
import re

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
                structTargets["id"] = {"type" : int, "fk" : False, "alias" : "ID (número)"}
            if "name" in targets:
                structTargets["name"] = {"type" : str, "fk" : False, "alias" : "Nombre (texto)"}
            if "rango" in targets:
                structTargets["rango"] = {"type" : str, "fk" : True, "alias" : "Rango (texto)"}
            if "rango_id" in targets:
                structTargets["rango_id"] = {"type" : int, "fk" : False, "alias" : "Rango ID (número)"}
            if "evento" in targets:
                structTargets["evento"] = {"type" : str, "fk" : True, "alias" : "Evento (texto)"}
            if "evento_id" in targets:
                structTargets["evento_id"] = {"type" : int, "fk" : False, "alias" : "Evento ID (número)"}
            if "integrante" in targets:
                structTargets["integrante"] = {"type" : str, "fk" : True, "alias" : "Integrante (texto)"}
            if "integrante_id" in targets:
                structTargets["integrante_id"] = {"type" : int, "fk" : False, "alias" : "Integrante ID (número)"}
            if "date_1" in targets:
                structTargets["date_1"] = {"type" : datetime, "fk" : False, "alias" : "Fecha 1 (día-mes-año)"}
            if "date_2" in targets:
                structTargets["date_2"] = {"type" : datetime, "fk" : False, "alias" : "Fecha 2 (día-mes-año)"}
        return {"controller" : structCtrl, "targets" : structTargets}

    @staticmethod
    def setStruct(nameCtrl):
        structCtrl = {}
        structTargets = {}
        if nameCtrl == "asistencia":
            structCtrl[nameCtrl] = {"create" : False}
            structTargets["integrante"] = {"type" : str, "fk" : True, "alias" : "Integrante (texto)"}
            structTargets["evento"] = {"type" : str, "fk" : True, "alias" : "Evento (texto)"}
            structTargets["date"] = {"type" : datetime, "fk" : False, "alias" : "Fecha (día-mes-año)"}
        elif nameCtrl == "evento":
            structCtrl[nameCtrl] = {"create" : "name"}
            structTargets["name"] = {"type" : str, "fk" : False, "alias" : "Nombre (texto)"}
            structTargets["points"] = {"type" : float, "fk" : False, "alias" : "Puntos (número)"}
            structTargets["description"] = {"type" : str, "fk" : False, "alias" : "Descripción (texto)"}
        elif nameCtrl == "integrante":
            structCtrl[nameCtrl] = {"create" : "name"}
            structTargets["name"] = {"type" : str, "fk" : False, "alias" : "Nombre (texto)"}
            structTargets["rango"] = {"type" : str, "fk" : True, "alias" : "Rango (texto)"}
            structTargets["date"] = {"type" : datetime, "fk" : False, "alias" : "Fecha (día-mes-año)"}
        elif nameCtrl == "rango":
            structCtrl[nameCtrl] = {"create" : "name"}
            structTargets["name"] = {"type" : str, "fk" : False, "alias" : "Nombre (texto)"}
            structTargets["description"] = {"type" : str, "fk" : False, "alias" : "Descripción (texto)"}
        return {"controller" : structCtrl, "targets" : structTargets}

    @staticmethod
    def updStruct(nameCtrl, update):
        structCtrl = {}
        structTargets = {}
        if nameCtrl == "asistencia":
             if update == "id":
                structCtrl[nameCtrl] = {"update" : update}
                structTargets["id"] = {"type" : int, "fk" : False, "alias" : "ID (número)"}
                structTargets["integrante"] = {"type" : str, "fk" : True, "alias" : "Integrante (texto)"}
                structTargets["evento"] = {"type" : str, "fk" : True, "alias" : "Evento (texto)"}
                structTargets["date"] = {"type" : datetime, "fk" : False, "alias" : "Fecha (día-mes-año)"}
        elif nameCtrl == "evento":
            if update == "name":
                structCtrl[nameCtrl] = {"update" : update}
                structTargets["name"] = {"type" : str, "fk" : False, "alias" : "Nombre (texto)"}
                structTargets["points"] = {"type" : float, "fk" : False, "alias" : "Puntos (número)"}
                structTargets["description"] = {"type" : str, "fk" : False, "alias" : "Descripción (texto)"}
            elif update == "id":
                structCtrl[nameCtrl] = {"update" : update}
                structTargets["id"] = {"type" : int, "fk" : False, "alias" : "ID (número)"}
                structTargets["name"] = {"type" : str, "fk" : False, "alias" : "Nombre (texto)"}
                structTargets["points"] = {"type" : float, "fk" : False, "alias" : "Puntos (número)"}
                structTargets["description"] = {"type" : str, "fk" : False, "alias" : "Descripción (texto)"}
        elif nameCtrl == "integrante":
            if update == "name":
                structCtrl[nameCtrl] = {"update" : update}
                structTargets["name"] = {"type" : str, "fk" : False, "alias" : "Nombre (texto)"}
                structTargets["rango"] = {"type" : str, "fk" : True, "alias" : "Rango (texto)"}
                structTargets["date"] = {"type" : datetime, "fk" : False, "alias" : "Fecha (día-mes-año)"}
            elif update == "id":
                structCtrl[nameCtrl] = {"update" : update}
                structTargets["id"] = {"type" : int, "fk" : False, "alias" : "ID (número)"}
                structTargets["name"] = {"type" : str, "fk" : False, "alias" : "Nombre (texto)"}
                structTargets["rango"] = {"type" : str, "fk" : True, "alias" : "Rango (texto)"}
                structTargets["date"] = {"type" : datetime, "fk" : False, "alias" : "Fecha (día-mes-año)"}
        elif nameCtrl == "rango":
            if update == "name":
                structCtrl[nameCtrl] = {"update" : update}
                structTargets["name"] = {"type" : str, "fk" : False, "alias" : "Nombre (texto)"}
                structTargets["description"] = {"type" : str, "fk" : False, "alias" : "Descripción (texto)"}
            elif update == "id":
                structCtrl[nameCtrl] = {"update" : update}
                structTargets["id"] = {"type" : int, "fk" : False, "alias" : "ID (número)"}
                structTargets["name"] = {"type" : str, "fk" : False, "alias" : "Nombre (texto)"}
                structTargets["description"] = {"type" : str, "fk" : False, "alias" : "Descripción (texto)"}
        return {"controller" : structCtrl, "targets" : structTargets}

    @staticmethod
    def delStruct(nameCtrl, delete):
        structCtrl = {}
        structTargets = {}
        if nameCtrl == "asistencia":
             if delete == "id":
                structCtrl[nameCtrl] = {"delete" : delete}
                structTargets["id"] = {"type" : int, "fk" : False, "alias" : "ID (número)"}
        elif nameCtrl == "evento":
            if delete == "name":
                structCtrl[nameCtrl] = {"delete" : delete}
                structTargets["name"] = {"type" : str, "fk" : False, "alias" : "Nombre (texto)"}
            elif delete == "id":
                structCtrl[nameCtrl] = {"delete" : delete}
                structTargets["id"] = {"type" : int, "fk" : False, "alias" : "ID (número)"}
        elif nameCtrl == "integrante":
            if delete == "name":
                structCtrl[nameCtrl] = {"delete" : delete}
                structTargets["name"] = {"type" : str, "fk" : False, "alias" : "Nombre (Texto)"}
            elif delete == "id":
                structCtrl[nameCtrl] = {"delete" : delete}
                structTargets["id"] = {"type" : int, "fk" : False, "alias" : "ID (número)"}
        elif nameCtrl == "rango":
            if delete == "name":
                structCtrl[nameCtrl] = {"delete" : delete}
                structTargets["name"] = {"type" : str, "fk" : False, "alias" : "Nombre (texto)"}
            elif delete == "id":
                structCtrl[nameCtrl] = {"delete" : delete}
                structTargets["id"] = {"type" : int, "fk" : False, "alias" : "ID (número)"}
        return {"controller" : structCtrl, "targets" : structTargets}

    @staticmethod
    def genMsg(command, controller):
        if command.find('[') != -1:   
            head = command[: command.find(':')]
            upper = [i.isupper() for i in head]
            mode = head[:upper.index(True)]
            target = command[command.find(':')+1 : command.find('[')].strip()
            parameters = command[command.find('[')+1 : command.find(']')]
            parameters = [parameter.strip() for parameter in parameters.split(',')]
        else:
            head = command[: command.find(':')]
            upper = [i.isupper() for i in head]
            mode = head[:upper.index(True)]
            target = command[command.find(':')+1 :].strip()
        if mode == "list":
            if target == "all":
                return (f"- **${head}:{target}**  ->  Lista en una hoja de excel "\
                        f"{'todas las'if controller[0] == 'a' else 'todos los'} "\
                        f"_{controller}s_ registrad{'a' if controller[0] == 'a' else 'o'}s en la base de datos.\n")
            elif target == "id":
                return (f"- **${head}:{target} [_{', '.join(parameters)}_]**  ->  Lista en una hoja de excel "\
                        f"{'la' if controller[0] == 'a' else 'el'} "\
                        f"_{controller}_ registrad{'a' if controller[0] == 'a' else 'o'} en la base de datos, "\
                        f"que se encuentre asociad{'a' if controller[0] == 'a' else 'o'} al identificador **_{parameters[0]}_** "\
                        "ingresado como parametro dentro de los corchetes **[ ]**. "\
                        f"Este parametro **_{parameters[0]}_** debe corresponder a un valor numerico.\n")
            elif target.find("id") != -1:
                return (f"- **${head}:{target} [_{', '.join(parameters)}_]**  ->  Lista en una hoja de excel "\
                        f"{'todas las'if controller[0] == 'a' else 'todos los'} "\
                        f"_{controller}s_ registrad{'a' if controller[0] == 'a' else 'o'}s en la base de datos, "\
                        f"asociad{'a' if controller[0] == 'a' else 'o'}s al identificador **_{parameters[0]}_**, "\
                        "ingresado como parametro dentro de los corchetes **[ ]**, "\
                        f"en relacion al identificador de{' la' if parameters[0][0] == 'a' else 'l'} "\
                        f"_{parameters[0][:parameters[0].find(' ')].lower()}_ presente en "\
                        f"{'la' if controller[0] == 'a' else 'el'} _{controller}_. "  
                        f"Este parametro **_{parameters[0]}_** debe corresponder a un valor numerico.\n")
            elif target == "name":
                return (f"- **${head}:{target} [_{', '.join(parameters)}_]**  ->  Lista en una hoja de excel "\
                        f"{'la' if controller[0] == 'a' else 'el'} "\
                        f"_{controller}_ registrad{'a' if controller[0] == 'a' else 'o'} en la base de datos, "\
                        f"asociad{'a' if controller[0] == 'a' else 'o'} al nombre **_{parameters[0]}_**, "\
                        "ingresado como parametro dentro de los corchetes **[ ]**. "\
                        f"Este parametro **_{parameters[0]}_** debe corresponder a un valor de texto.\n")
            elif target == "date":
                return (f"- **${head}:{target} [_{', '.join(parameters)}_]**  ->  Lista en una hoja de excel "\
                        f"{'todas las'if controller[0] == 'a' else 'todos los'} "\
                        f"_{controller}s_ registrad{'a' if controller[0] == 'a' else 'o'}s en la base de datos, "\
                        f"que lo hayan sido entre las fechas **_{parameters[0]}_** y **_{parameters[1]}_**, "\
                        "ingresadas como parametros dentro de los corchetes **[ ]**. "\
                        f"Estos parametros **_{parameters[0]}_** y **_{parameters[1]}_** "\
                        "deben corresponder a valores de fecha en 'Día-Mes-Año'.\n")
            else:
                return (f"- **${head}:{target} [_{', '.join(parameters)}_]**  ->  Lista en una hoja de excel "\
                        f"{'todas las'if controller[0] == 'a' else 'todos los'} "\
                        f"_{controller}s_ registrad{'a' if controller[0] == 'a' else 'o'}s en la base de datos, "\
                        f"asociad{'a' if controller[0] == 'a' else 'o'}s al nombre **_{parameters[0]}_**, "\
                        "ingresado como parametro dentro de los corchetes **[ ]**, "\
                        f"en relacion al nombre de{' la' if parameters[0][0] == 'a' else 'l'} "\
                        f"_{parameters[0].lower()}_ presente en "\
                        f"{'la' if controller[0] == 'a' else 'el'} _{controller}_. "  
                        f"Este parametro **_{parameters[0]}_** debe corresponder a un valor de texto.\n")
        elif mode == "add":
            value = (f"- **${head}:{target} [_{', '.join(parameters)}_]**  ->  Añade "\
                    f"{'una nueva'if controller[0] == 'a' else 'un nuevo'} "\
                    f"_{controller}_ a la base de datos, ingresando dentro de los corchetes **[ ]** ")
            for i in range(len(parameters)):
                if parameters[i] == "Nombre":
                    value = value + f"un parametro **_{parameters[i]}_** como valor de texto"
                elif parameters[i] == "Puntos":
                    value = value + f"un parametro **_{parameters[i]}_** como valor numerico decimal"
                elif parameters[i] == "Fecha":
                    value = value + f"un parametro **_{parameters[i]}_** como valor de fecha en 'Día-Mes-Año'"
                elif parameters[i] == "Descripción":
                    value = value + f"un parametro **_{parameters[i]}_** como valor de texto"
                else: 
                    value = value + (f"un parametro **_{parameters[i]}_** como valor de texto asociado al nombre "\
                    f"de un _{parameters[i].lower()}_ existente en la base de datos")
                if i == len(parameters) - 1:
                    value = value + ".\n"
                elif i == len(parameters) - 2:
                    value = value + " y "
                else:
                    value = value + ", "
            return value
        elif mode == "upd":
            if target == "id":
                value = (f"- **${head}:{target} [_{', '.join(parameters)}_]**  ->  Actualiza los datos de "\
                        f"{'una 'if controller[0] == 'a' else 'un'} _{controller}_ existente en la base de datos "\
                        f"apuntando a su identificador **_{parameters[0]}_**, ingresando dentro de los corchetes **[ ]** ")
                for i in range(len(parameters)):
                    if parameters[i] == "ID":
                        value = value + f"un parametro **_{parameters[i]}_** como valor numerico"
                    elif parameters[i] == "Nombre":
                        value = value + f"un parametro **_{parameters[i]}_** como valor de texto"
                    elif parameters[i] == "Puntos":
                        value = value + f"un parametro **_{parameters[i]}_** como valor numerico decimal"
                    elif parameters[i] == "Fecha":
                        value = value + f"un parametro **_{parameters[i]}_** como valor de fecha en 'Día-Mes-Año'"
                    elif parameters[i] == "Descripción":
                        value = value + f"un parametro **_{parameters[i]}_** como valor de texto"
                    else: 
                        value = value + (f"un parametro **_{parameters[i]}_** como valor de texto asociado al nombre "\
                        f"de un _{parameters[i].lower()}_ existente en la base de datos")
                    if i == len(parameters) - 1:
                        value = value + ".\n"
                    elif i == len(parameters) - 2:
                        value = value + " y "
                    else:
                        value = value + ", "
                return value
            elif target == "name":
                value = (f"- **${head}:{target} [_{', '.join(parameters)}_]**  ->  Actualiza los datos de "\
                        f"{'una 'if controller[0] == 'a' else 'un'} _{controller}_ existente en la base de datos "\
                        f"apuntando a su nombre **_{parameters[0]}_**, ingresando dentro de los corchetes **[ ]** ")
                for i in range(len(parameters)):
                    if parameters[i] == "Nombre":
                        value = value + f"un parametro **_{parameters[i]}_** como valor de texto"
                    elif parameters[i] == "Puntos":
                        value = value + f"un parametro **_{parameters[i]}_** como valor numerico decimal"
                    elif parameters[i] == "Fecha":
                        value = value + f"un parametro **_{parameters[i]}_** como valor de fecha en 'Día-Mes-Año'"
                    elif parameters[i] == "Descripción":
                        value = value + f"un parametro **_{parameters[i]}_** como valor de texto"
                    else: 
                        value = value + (f"un parametro **_{parameters[i]}_** como valor de texto asociado al nombre "\
                        f"de un _{parameters[i].lower()}_ existente en la base de datos")
                    if i == len(parameters) - 1:
                        value = value + ".\n"
                    elif i == len(parameters) - 2:
                        value = value + " y "
                    else:
                        value = value + ", "
                return value      
        elif mode == "del":
            if target == "id":
                return (f"- **${head}:{target} [_{', '.join(parameters)}_]**  ->  Elimina "\
                        f"{'una 'if controller[0] == 'a' else 'un'} _{controller}_ existente en la base de datos "\
                        f"apuntando a su identificador **_{parameters[0]}_**, ingresando dentro de los corchetes **[ ]** "\
                        f"un parametro **_{parameters[0]}_** como valor numerico.\n")
            elif target == "name":
                return (f"- **${head}:{target} [_{', '.join(parameters)}_]**  ->  Elimina "\
                        f"{'una 'if controller[0] == 'a' else 'un'} _{controller}_ existente en la base de datos "\
                        f"apuntando a su nombre **_{parameters[0]}_**, ingresando dentro de los corchetes **[ ]** "\
                        f"un parametro **_{parameters[0]}_** como valor de texto.\n")               