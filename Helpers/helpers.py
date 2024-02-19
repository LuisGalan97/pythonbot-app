from datetime import datetime

class Helpers:
    @staticmethod
    def checkCommand(request, command):
        if (request.find(':') != -1 and
            command.find(':') != -1 and
            request.startswith(f"${command}")):
            if (request.find('&') != -1 and
                command.find('&') != -1 and
                request.startswith(f"${command}")):
                requestpos = request.find('&') + 1
                cmdpos = command.find('&') + 1
                if (request.find('&', requestpos) != -1 and
                    command.find('&', cmdpos) != -1 and
                    request.startswith(f"${command}")):
                    return True
                elif (not request.startswith(f"${command}&") and
                      command.find('&', cmdpos) == -1 and
                      request.startswith(f"${command}")):
                    return True
                else:
                    return False
            elif (not request.startswith(f"${command}&") and
                  command.find('&') == -1 and
                  request.startswith(f"${command}")):
                return True
            else:
                return False
        elif (not request.startswith(f"${command}:") and
              command.find(':') == -1 and
              request.startswith(f"${command}")):
            return True
        else:
            return False

    @staticmethod
    def checkContent(command, content, reftarget):
        if reftarget:
            opts = [value.get("opt", False) for value in reftarget.values()]
            alias = [value['alias'] for value in reftarget.values()]
            alias = [name + "​_**_(____Opcional____)_**_​"
                     if opt else name
                     for opt, name
                     in zip(opts, alias)]
            alias = ', '.join(map(str, alias))
            if content.find('[') == 0 and content.rfind(']') != -1:
                request = content.replace('[', '', 1)
                request = request[: request.rfind(']')]
                request = request.split(',')
                return request
            else:
                return "El comando debe mantener la forma:\n"\
                      f"**${command} [_{alias}_]**"
        else:
            return []

    @staticmethod
    def setTarget(self, request, struct):
        target = {}
        nameCtrl = next(iter(struct["controller"].keys()))
        struct = struct["targets"]
        if struct:
            result = Helpers.checkRequest(request, struct)
            if isinstance(result, dict):
                checktarget = {}
                foreignkey = {}
                for key in struct:
                    if "ct" in struct[key]:
                        if key in result:
                            checktarget[key] = result[key]
                    elif "fk" in struct[key]:
                        foreignkey[key] = result[key]
                if checktarget:
                    checkid = {}
                    for key, value in checktarget.items():
                        checkid[key] = getattr(getattr(self,
                                       f"_AppHandler__{nameCtrl}Controller"),
                                       f"get{nameCtrl.capitalize()}s")(
                                       {f"{struct[key]['ct']}" : value})
                        if isinstance(checkid[key], list):
                            if key == struct[key]['ct']:
                                target[key] = value
                            else:
                                if "update" in struct["controlller"]:
                                    update = struct["controlller"]["update"]
                                    if (result[update]  ==
                                        checkid[key][0][update]):
                                        return f"El valor '{value}' "\
                                        "ingresado en el "\
                                       f"campo **_{struct[key]['alias']}_** "\
                                        "no puede hacer referencia al mismo "\
                                       f"___{nameCtrl}___ que desea "\
                                        "actualizar."
                                target[f"{key}_id"] = checkid[key][0]["id"]
                        elif checkid[key]:
                            return f"El valor '{value}' ingresado en el "\
                                   f"campo **_{struct[key]['alias']}_** "\
                                    "no fue encontrado en la base de datos."
                        else:
                            return False
                if foreignkey:
                    foreignid = {}
                    for key, value in foreignkey.items():
                        fkCtrl = struct[key]['fk']
                        foreignid[key] = getattr(getattr(self,
                                         f"_AppHandler__{fkCtrl}Controller"),
                                         f"get{fkCtrl.capitalize()}s")(
                                         {"name" : value})
                        if isinstance(foreignid[key], list):
                            target[f"{key}_id"] = foreignid[key][0]["id"]
                        elif foreignid[key]:
                            return f"El valor '{value}' ingresado en el "\
                                   f"campo **_{struct[key]['alias']}_** "\
                                    "no fue encontrado en la base de datos."
                        else:
                            return False
                for key, value in result.items():
                    if (not key in foreignkey and
                        not key in checktarget):
                        target[key] = value
            else:
                return result
        return target

    @staticmethod
    def checkRequest(request, reftarget):
        opts = [value.get("opt", False) for value in reftarget.values()]
        partOpts = [item for item, value in zip(opts, opts) if not value]
        references = ', '.join(map(str, list(reftarget.keys())))
        references = list(map(lambda x: x.strip(),
                          references.split(',')))
        types = [value["type"] for value in reftarget.values()]
        alias = [value['alias'] for value in reftarget.values()]
        datas = request
        if (isinstance(datas, list) and
            len(datas) == len(partOpts)):
            references = [ref for opt, ref
                          in zip(opts, references)
                          if not opt]
            types = [typ for opt, typ
                     in zip(opts, types)
                     if not opt]
            alias = [name for opt, name
                     in zip(opts, alias)
                     if not opt]
        elif (isinstance(datas, list) and
              len(datas) == len(opts)):
            pass
        else:
            alias = [name + "​_**_(____Opcional____)_**_​"
                     if opt else name
                     for opt, name
                     in zip(opts, alias)]
            alias = ', '.join(map(str, alias))
            return "Datos ingresados invalidos, "\
                   "recuerda que debes ingresar:\n"\
                  f"**[_{alias}_]**"
        alias = ', '.join(map(str, alias))
        for i in range(len(datas)):
            datas[i] = datas[i].strip()
            if not datas[i]:
                return "No fue ingresado ningun dato en el campo "\
                      f"**_{alias.split(',')[i].strip()}_**"
            try:
                if types[i] == datetime:
                    datas[i] = datetime.strptime(datas[i], "%d/%m/%Y")
                    datas[i] = datas[i].strftime("%Y-%m-%d")
                else:
                    datas[i] = types[i](datas[i])
            except ValueError:
                return f"El dato '{datas[i]}' ingresado en el campo "\
                       f"**_{alias.split(',')[i].strip()}_** "\
                        "es invalido."
            if types[i] == str:
                if len(datas[i]) > 50:
                    return f"El dato '{datas[i]}' ingresado "\
                            "en el campo "\
                           f"**_{alias.split(',')[i].strip()}_** "\
                            "no debe exceder los 50 caracteres."
                if Helpers.checkTrueChar(datas[i][0]):
                    return f"El dato '{datas[i]}' ingresado "\
                            "en el campo "\
                           f"**_{alias.split(',')[i].strip()}_** "\
                            "no debe comenzar con valores numericos "\
                            "ni caracteres especiales."
                try:
                    int(datas[i][0])
                    return f"El dato '{datas[i]}' ingresado "\
                            "en el campo "\
                           f"**_{alias.split(',')[i].strip()}_** "\
                            "no debe comenzar con valores numericos "\
                            "ni caracteres especiales."
                except ValueError:
                    pass
                if Helpers.checkChar(datas[i]):
                    return f"El dato '{datas[i]}' ingresado "\
                            "en el campo "\
                           f"**_{alias.split(',')[i].strip()}_** "\
                            "no debe contener caracteres especiales "\
                            "a excepcion de **-** o **|**."
                if Helpers.checkRepeatChar(datas[i]):
                    return f"El dato '{datas[i]}' ingresado "\
                            "en el campo "\
                           f"**_{alias.split(',')[i].strip()}_** "\
                            "no debe repetir mas de dos veces los "\
                            "caracteres **-** **|**, o mas de una "\
                            "vez los caracteres **[** **]**."
        datas = dict(zip(references, datas))
        return datas

    @staticmethod
    def checkChar(strValue):
        spechar = ['/', '\\', '\'', '!', '¡',
        '?', '¿', '"', '´', '{', '}',
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
        repeat = ['-', '|','[', ']']
        for char in repeat:
            if char == '[' or char == ']':
                if strValue.count(char) > 1:
                    return True
            else:
                if strValue.count(char) > 2:
                    return True
        return False

    @staticmethod
    def checkValue(value):
        if value is not None:
            return value
        else:
            return "Ninguno"

    @staticmethod
    def getStruct(nameCtrl, targets = None, option = None):
        structCtrl = {}
        structTargets = {}
        if nameCtrl == "assist":
            if not option:
                reference = {
                    "ID" : "id",
                    #"Integrante ID" : "member_id",
                    "Integrante" : "member_name",
                    #"Rango ID" : "member_range_id",
                    #"Rango" : "member_range_name",
                    #"Control" : "member_range_control",
                    #"Descripción Rango" : "member_range_description",
                    #"Fecha de creación Integrante" : "member_datecreate",
                    #"Fecha de modificación Integrante" : "member_dateupdate",
                    #"Evento ID" : "event_id",
                    "Evento" : "event_name",
                    "Puntos" : "event_points",
                    #"Descripción Evento" : "event_description",
                    "Fecha" : "date"
                }
            structCtrl[nameCtrl] = {
                "alias" : "asistencia",
                "ref" : reference
            }
        elif nameCtrl == "event":
            if not option:
                reference = {
                    "ID" : "id",
                    "Nombre" : "name",
                    "Puntos" : "points",
                    "Descripción" : "description"
                }
            structCtrl[nameCtrl] = {
                "alias" : "evento",
                "ref" : reference
            }
        elif nameCtrl == "member":
            if not option:
                reference = {
                    "ID" : "id",
                    "Nombre" : "name",
                    #"Rango ID" : "range_id",
                    "Rango" : "range_name",
                    #"Principal ID" : "principal_id",
                    "Principal" : "principal_name",
                    #"Control Rango" : "range_control",
                    #"Descripción Rango" : "range_description",
                    "Fecha de creación" : "datecreate",
                    "Fecha de modificación" : "dateupdate"
                }
            elif option in ["rtpoints", "atpoints"]:
                reference = {
                    "ID" : "id",
                    "Nombre" : "name",
                    #"Rango ID" : "range_id",
                    "Rango" : "range_name",
                    #"Principal ID" : "principal_id",
                    #"Principal" : "principal_name",
                    #"Control Rango" : "range_control",
                    #"Descripción Rango" : "range_description",
                    #"Fecha de creación" : "datecreate",
                    #"Fecha de modificación" : "dateupdate",
                    "Puntos acumulados" : "totalpoints"
                }
            structCtrl[nameCtrl] = {
                "alias" : "integrante",
                "ref" : reference
            }
        elif nameCtrl == "range":
            if not option:
                reference = {
                    "ID" : "id",
                    "Nombre" : "name",
                    "Control" : "control",
                    "Descripción" : "description"
                }
            structCtrl[nameCtrl] = {
                "alias" : "rango",
                "ref" : reference
            }
        if targets:
            if "id" in targets:
                structTargets["id"] = {
                    "type" : int,
                    "ct" : "id",
                    "alias" : "ID"
                }
            if "name" in targets:
                structTargets["name"] = {
                    "type" : str,
                    "ct" : "name",
                    "alias" : "Nombre"
                }
            if "range" in targets:
                structTargets["range"] = {
                    "type" : str,
                    "fk" : "range",
                    "alias" : "Rango"
                }
            if "range_id" in targets:
                structTargets["range_id"] = {
                    "type" : int,
                    "alias" : "Rango ID"
                }
            if "member" in targets:
                structTargets["member"] = {
                    "type" : str,
                    "fk" : "member",
                    "alias" : "Integrante"
                }
            if "member_id" in targets:
                structTargets["member_id"] = {
                    "type" : int,
                    "alias" : "Integrante ID"
                }
            if "event" in targets:
                structTargets["event"] = {
                    "type" : str,
                    "fk" : "event",
                    "alias" : "Evento"
                }
            if "event_id" in targets:
                structTargets["event_id"] = {
                    "type" : int,
                    "alias" : "Event ID"
                }
            if "date_1" in targets:
                structTargets["date_1"] = {
                    "type" : datetime,
                    "alias" : "Fecha 1"
                }
            if "date_2" in targets:
                structTargets["date_2"] = {
                    "type" : datetime,
                    "alias" : "Fecha 2"
                }
        return {"controller" : structCtrl,
                "targets" : structTargets,
                "option" : option}

    @staticmethod
    def setStruct(nameCtrl):
        structCtrl = {}
        structTargets = {}
        if nameCtrl == "assist":
            structCtrl[nameCtrl] = {
                "create" : False,
                "alias" : "asistencia"
            }
            structTargets["member"] = {
                "type" : str,
                "fk" : "member",
                "alias" : "Integrante"
            }
            structTargets["event"] = {
                "type" : str,
                "fk" : "event",
                "alias" : "Evento"
            }
            structTargets["date"] = {
                "type" : datetime,
                "alias" : "Fecha"
            }
        elif nameCtrl == "event":
            structCtrl[nameCtrl] = {
                "create" : "name",
                "alias" : "evento"
            }
            structTargets["name"] = {
                "type" : str,
                "alias" : "Nombre"
            }
            structTargets["points"] = {
                "type" : float,
                "alias" : "Puntos"
            }
            structTargets["description"] = {
                "type" : str,
                "alias" : "Descripción"
            }
        elif nameCtrl == "member":
            structCtrl[nameCtrl] = {
                "create" : "name",
                "alias" : "integrante"
            }
            structTargets["name"] = {
                "type" : str,
                "alias" : "Nombre"
            }
            structTargets["range"] = {
                "type" : str,
                "fk" : "range",
                "alias" : "Rango"
            }
            structTargets["principal"] = {
                "type" : str,
                "ct" : "name",
                "opt" : True,
                "alias" : "Principal"
            }
            structTargets["date"] = {
                "type" : datetime,
                "alias" : "Fecha"
            }
        elif nameCtrl == "range":
            structCtrl[nameCtrl] = {
                "create" : "name",
                "alias" : "rango"
            }
            structTargets["name"] = {
                "type" : str,
                "alias" : "Nombre"
            }
            structTargets["control"] = {
                "type" : int,
                "alias" : "Control"
            }
            structTargets["description"] = {
                "type" : str,
                "alias" : "Descripción"
            }
        return {"controller" : structCtrl, "targets" : structTargets}

    @staticmethod
    def updStruct(nameCtrl, update):
        structCtrl = {}
        structTargets = {}
        if nameCtrl == "assist":
             if update == "id":
                structCtrl[nameCtrl] = {
                    "update" : update,
                    "create" : False,
                    "alias" : "asistencia"
                }
                structTargets["id"] = {
                    "type" : int,
                    "ct" : "id",
                    "alias" : "ID"
                }
                structTargets["member"] = {
                    "type" : str,
                    "fk" : "member",
                    "alias" : "Integrante"
                }
                structTargets["event"] = {
                    "type" : str,
                    "fk" : "event",
                    "alias" : "Evento"
                }
                structTargets["date"] = {
                    "type" : datetime,
                    "alias" : "Fecha"
                }
        elif nameCtrl == "event":
            if update == "name":
                structCtrl[nameCtrl] = {
                    "update" : update,
                    "create" : False,
                    "alias" : "evento"
                }
                structTargets["name"] = {
                    "type" : str,
                    "ct" : "name",
                    "alias" : "Nombre"
                }
                structTargets["points"] = {
                    "type" : float,
                    "alias" : "Puntos"
                }
                structTargets["description"] = {
                    "type" : str,
                    "alias" : "Descripción"
                }
            elif update == "id":
                structCtrl[nameCtrl] = {
                    "update" : update,
                    "create" : "name",
                    "alias" : "evento"
                }
                structTargets["id"] = {
                    "type" : int,
                    "ct" : "id",
                    "alias" : "ID"
                }
                structTargets["name"] = {
                    "type" : str,
                    "alias" : "Nombre"
                }
                structTargets["points"] = {
                    "type" : float,
                    "alias" : "Puntos"
                }
                structTargets["description"] = {
                    "type" : str,
                    "alias" : "Descripción"
                }
        elif nameCtrl == "member":
            if update == "name":
                structCtrl[nameCtrl] = {
                    "update" : update,
                    "create" : False,
                    "alias" : "integrante"
                }
                structTargets["name"] = {
                    "type" : str,
                    "ct" : "name",
                    "alias" : "Nombre"
                }
                structTargets["range"] = {
                    "type" : str,
                    "fk" : "range",
                    "alias" : "Rango"
                }
                structTargets["principal"] = {
                    "type" : str,
                    "ct" : "name",
                    "opt" : True,
                    "alias" : "Principal"
                }
                structTargets["date"] = {
                    "type" : datetime,
                    "alias" : "Fecha"
                }
            elif update == "id":
                structCtrl[nameCtrl] = {
                    "update" : update,
                    "create" : "name",
                    "alias" : "integrante"
                }
                structTargets["id"] = {
                    "type" : int,
                    "ct" : "id",
                    "alias" : "ID"
                }
                structTargets["name"] = {
                    "type" : str,
                    "alias" : "Nombre"
                }
                structTargets["range"] = {
                    "type" : str,
                    "fk" : "range",
                    "alias" : "Rango"
                }
                structTargets["principal"] = {
                    "type" : str,
                    "ct" : "name",
                    "opt" : True,
                    "alias" : "Principal"
                }
                structTargets["date"] = {
                    "type" : datetime,
                    "alias" : "Fecha"
                }
        elif nameCtrl == "range":
            if update == "name":
                structCtrl[nameCtrl] = {
                    "update" : update,
                    "create" : False,
                    "alias" : "rango"
                }
                structTargets["name"] = {
                    "type" : str,
                    "ct" : "name",
                    "alias" : "Nombre"
                }
                structTargets["control"] = {
                    "type" : int,
                    "alias" : "Control"
                }
                structTargets["description"] = {
                    "type" : str,
                    "alias" : "Descripción"
                }
            elif update == "id":
                structCtrl[nameCtrl] = {
                    "update" : update,
                    "create" : "name",
                    "alias" : "rango"
                }
                structTargets["id"] = {
                    "type" : int,
                    "ct" : "id",
                    "alias" : "ID"
                }
                structTargets["name"] = {
                    "type" : str,
                    "alias" : "Nombre"
                }
                structTargets["control"] = {
                    "type" : int,
                    "alias" : "Control"
                }
                structTargets["description"] = {
                    "type" : str,
                    "alias" : "Descripción"
                }
        return {"controller" : structCtrl, "targets" : structTargets}

    @staticmethod
    def delStruct(nameCtrl, delete):
        structCtrl = {}
        structTargets = {}
        if nameCtrl == "assist":
             if delete == "id":
                structCtrl[nameCtrl] = {
                    "delete" : delete,
                    "alias" : "asistencia"
                }
                structTargets["id"] = {
                    "type" : int,
                    "ct" : "id",
                    "alias" : "ID"
                }
        elif nameCtrl == "event":
            if delete == "name":
                structCtrl[nameCtrl] = {
                    "delete" : delete,
                    "alias" : "evento"
                }
                structTargets["name"] = {
                    "type" : str,
                    "ct" : "name",
                    "alias" : "Nombre"
                }
            elif delete == "id":
                structCtrl[nameCtrl] = {
                    "delete" : delete,
                    "alias" : "evento"
                }
                structTargets["id"] = {
                    "type" : int,
                    "ct" : "id",
                    "alias" : "ID"
                }
        elif nameCtrl == "member":
            if delete == "name":
                structCtrl[nameCtrl] = {
                    "delete" : delete,
                    "alias" : "integrante"
                }
                structTargets["name"] = {
                    "type" : str,
                    "ct" : "name",
                    "alias" : "Nombre"
                }
            elif delete == "id":
                structCtrl[nameCtrl] = {
                    "delete" : delete,
                    "alias" : "integrante"
                }
                structTargets["id"] = {
                    "type" : int,
                    "ct" : "id",
                    "alias" : "ID"
                }
        elif nameCtrl == "range":
            if delete == "name":
                structCtrl[nameCtrl] = {
                    "delete" : delete,
                    "alias" : "rango"
                }
                structTargets["name"] = {
                    "type" : str,
                    "ct" : "name",
                    "alias" : "Nombre"
                }
            elif delete == "id":
                structCtrl[nameCtrl] = {
                    "delete" : delete,
                    "alias" : "rango"
                }
                structTargets["id"] = {
                    "type" : int,
                    "ct" : "id",
                    "alias" : "ID"
                }
        return {"controller" : structCtrl, "targets" : structTargets}

    @staticmethod
    def genMsg(command, controller):
        if command.find('[') != -1:
            head = (command[: command.find(':')]
                    if command.find(':') != -1
                    else command[: command.find('[')].strip())
            upper = [i.isupper() for i in head]
            mode = head[:upper.index(True)]
            target = (command[command.find(':')+1 : command.find('[')].strip()
                      if command.find(':') != -1
                      else "")
            parameters = command[command.find('[')+1 : command.find(']')]
            parameters = [parameter.strip()
                          for parameter
                          in parameters.split(',')]
            excelrequest = True if command.find('>') != -1 else False
        else:
            head = (command[: command.find(':')]
                    if command.find(':') != -1
                    else command.strip())
            upper = [i.isupper() for i in head]
            mode = head[:upper.index(True)]
            target = (command[command.find(':')+1 :].strip()
                      if command.find(':') != -1
                      else "")
            parameters = []
            excelrequest = True if command.find('>') != -1 else False
        if mode == "list":
            if not target and not parameters:
                return f"- **${head}**   ->   " + \
                       ('Lista en una hoja de excel '
                         if excelrequest
                         else 'Lista ') + \
                       ('todas las '
                         if controller[0] == 'a'
                         else 'todos los ') + \
                       f"___{controller}s___.\n"
            elif not target and len(parameters) == 2:
                if head == "listPointMember":
                    return f"- **${head} "\
                           f"[_{', '.join(parameters)}_]** " + \
                           ('**> e**   ->   Lista en una hoja de excel '
                            if excelrequest
                            else '   ->   Lista ') + \
                           ('todas las '
                            if controller[0] == 'a'
                            else 'todos los ') + \
                           f"___{controller}s___ "\
                            "que posean ___asistencias___ registradas "\
                           f"entre las fechas **_{parameters[0]}_** "\
                           f"y **_{parameters[1]}_**, "\
                            "ingresadas como parametros dentro de los "\
                            "corchetes **[ ]**, "\
                            "mostrando de mayor a menor el total de "\
                            "puntos de las ___asistencias___ "\
                           f"en cuestion para cada ___{controller}___. "\
                           f"Los parametros **_{parameters[0]}_** "\
                           f"y **_{parameters[1]}_** "\
                            "deberán corresponder a valores de fecha "\
                            "en 'Día/Mes/Año'.\n"
                elif head == "listAllPointMember":
                    return f"- **${head} "\
                           f"[_{', '.join(parameters)}_]** " + \
                           ('**> e**   ->   Lista en una hoja de excel '
                            if excelrequest
                            else '   ->   Lista ') + \
                           ('todas las '
                            if controller[0] == 'a'
                            else 'todos los ') + \
                           f"___{controller}s___, "\
                            "mostrando para cada uno "\
                            "de mayor a  menor el total de "\
                            "puntos de sus ___asistencias___ registradas "\
                           f"entre las fechas **_{parameters[0]}_** "\
                           f"y **_{parameters[1]}_**, "\
                            "ingresadas como parametros dentro de los "\
                            "corchetes **[ ]**. "\
                           f"Los parametros **_{parameters[0]}_** "\
                           f"y **_{parameters[1]}_** "\
                            "deberán corresponder a valores de fecha "\
                            "en 'Día/Mes/Año'.\n"
            elif target == "id" and len(parameters) == 1:
                return f"- **${head}:{target} "\
                       f"[_{', '.join(parameters)}_]** " + \
                       ('**> e**   ->   Lista en una hoja de excel '
                        if excelrequest
                        else '   ->   Lista ') + \
                       ('la '
                        if controller[0] == 'a'
                        else 'el ') + \
                       f"___{controller}___ "\
                        "asociad" + \
                       ('a ' if controller[0] == 'a' else 'o ') + \
                       f"al parametro **_{parameters[0]}_** "\
                        "ingresado dentro de los corchetes **[ ]**. "\
                       f"Este parametro **_{parameters[0]}_** deberá "\
                        "corresponder a un valor numerico.\n"
            elif target == "id" and len(parameters) == 3:
                if head == "listPointMember":
                    return f"- **${head}:{target} "\
                           f"[_{', '.join(parameters)}_]** " + \
                           ('**> e**   ->   Lista en una hoja de excel '
                            if excelrequest
                            else '   ->   Lista ') + \
                           ('la '
                            if controller[0] == 'a'
                            else 'el ') + \
                           f"___{controller}___ "\
                           "asociad" + \
                           ('a ' if controller[0] == 'a' else 'o ') + \
                           f"al parametro **_{parameters[0]}_**, "\
                            "que posea ___asistencias___ registradas "\
                           f"entre las fechas **_{parameters[1]}_** "\
                           f"y **_{parameters[2]}_**, "\
                            "todos ingresados como parametros dentro de los "\
                            "corchetes **[ ]**, "\
                            "mostrando el total de "\
                            "puntos de las ___asistencias___ "\
                           f"en cuestion para el ___{controller}___. "\
                           f"El parametro **_{parameters[0]}_** deberá "\
                            "corresponder a un valor numerico y "\
                           f"los parametros **_{parameters[1]}_** "\
                           f"y **_{parameters[2]}_** "\
                            "deberán corresponder a valores de fecha "\
                            "en 'Día/Mes/Año'.\n"
                elif head == "listAllPointMember":
                    return f"- **${head}:{target} "\
                           f"[_{', '.join(parameters)}_]** " + \
                           ('**> e**   ->   Lista en una hoja de excel '
                            if excelrequest
                            else '   ->   Lista ') + \
                           ('la '
                            if controller[0] == 'a'
                            else 'el ') + \
                           f"___{controller}___ "\
                            "asociad" + \
                           ('a ' if controller[0] == 'a' else 'o ') + \
                           f"al parametro **_{parameters[0]}_**, "\
                            "mostrando "\
                           f"el total de "\
                            "puntos de sus ___asistencias___ "\
                            "registradas entre las fechas "\
                           f"**_{parameters[1]}_** "\
                           f"y **_{parameters[2]}_**, "\
                            "todos ingresados como parametros dentro de los "\
                            "corchetes **[ ]**. "\
                           f"El parametro **_{parameters[0]}_** deberá "\
                            "corresponder a un valor numerico y "\
                           f"los parametros **_{parameters[1]}_** "\
                           f"y **_{parameters[2]}_** "\
                            "deberán corresponder a valores de fecha "\
                            "en 'Día/Mes/Año'.\n"
            elif target == "name" and len(parameters) == 1:
                return f"- **${head}:{target} "\
                       f"[_{', '.join(parameters)}_]** " + \
                       ('**> e**   ->   Lista en una hoja de excel '
                        if excelrequest
                        else '   ->   Lista ') + \
                       ('la '
                        if controller[0] == 'a'
                        else 'el ') + \
                       f"___{controller}___ "\
                        "asociad" + \
                       ('a '
                        if controller[0] == 'a '
                        else 'o ') + \
                       f"al parametro **_{parameters[0]}_** "\
                        "ingresado dentro de los corchetes **[ ]**. "\
                       f"Este parametro **_{parameters[0]}_** deberá "\
                        "corresponder a un valor de texto.\n"
            elif target == "name" and len(parameters) == 3:
                if head == "listPointMember":
                    return f"- **${head}:{target} "\
                           f"[_{', '.join(parameters)}_]** " + \
                           ('**> e**   ->   Lista en una hoja de excel '
                            if excelrequest
                            else '   ->   Lista ') + \
                           ('la '
                            if controller[0] == 'a'
                            else 'el ') + \
                           f"___{controller}___ "\
                           "asociad" + \
                           ('a ' if controller[0] == 'a' else 'o ') + \
                           f"al parametro **_{parameters[0]}_**, "\
                            "que posea ___asistencias___ registradas "\
                           f"entre las fechas **_{parameters[1]}_** "\
                           f"y **_{parameters[2]}_**, "\
                            "todos ingresados como parametros dentro de los "\
                            "corchetes **[ ]**, "\
                            "mostrando el total de "\
                            "puntos de las ___asistencias___ "\
                           f"en cuestion para el ___{controller}___. "\
                           f"El parametro **_{parameters[0]}_** deberá "\
                            "corresponder a un valor de texto y "\
                           f"los parametros **_{parameters[1]}_** "\
                           f"y **_{parameters[2]}_** "\
                            "deberán corresponder a valores de fecha "\
                            "en 'Día/Mes/Año'.\n"
                elif head == "listAllPointMember":
                    return f"- **${head}:{target} "\
                           f"[_{', '.join(parameters)}_]** " + \
                           ('**> e**   ->   Lista en una hoja de excel '
                            if excelrequest
                            else '   ->   Lista ') + \
                           ('la '
                            if controller[0] == 'a'
                            else 'el ') + \
                           f"___{controller}___ "\
                            "asociad" + \
                           ('a ' if controller[0] == 'a' else 'o ') + \
                           f"al parametro **_{parameters[0]}_**, "\
                            "mostrando "\
                            "el total de "\
                            "puntos de sus ___asistencias___ "\
                            "registradas entre las fechas "\
                           f"**_{parameters[1]}_** "\
                           f"y **_{parameters[2]}_**, "\
                            "todos ingresados como parametros dentro de los "\
                            "corchetes **[ ]**. "\
                           f"El parametro **_{parameters[0]}_** deberá "\
                            "corresponder a un valor de texto y "\
                           f"los parametros **_{parameters[1]}_** "\
                           f"y **_{parameters[2]}_** "\
                            "deberán corresponder a valores de fecha "\
                            "en 'Día/Mes/Año'.\n"
            elif target == "date" and len(parameters) == 2:
                return f"- **${head}:{target} "\
                       f"[_{', '.join(parameters)}_]** " + \
                       ('**> e**   ->   Lista en una hoja de excel '
                        if excelrequest
                        else '   ->   Lista ') + \
                       ('todas las '
                        if controller[0] == 'a'
                        else 'todos los ') + \
                       f"___{controller}s___ "\
                        "registrad" + \
                       ('a'
                        if controller[0] == 'a'
                        else 'o') + "s "\
                       f"entre las fechas **_{parameters[0]}_** "\
                       f"y **_{parameters[1]}_**, "\
                        "ingresadas como parametros dentro de los "\
                        "corchetes **[ ]**. "\
                       f"Estos parametros **_{parameters[0]}_** "\
                       f"y **_{parameters[1]}_** "\
                        "deberán corresponder a valores de fecha "\
                        "en 'Día/Mes/Año'.\n"
            elif target == "id&event" and len(parameters) == 4:
                if head == "listPointMember":
                    return f"- **${head}:{target} "\
                           f"[_{', '.join(parameters)}_]** " + \
                           ('**> e**   ->   Lista en una hoja de excel '
                            if excelrequest
                            else '   ->   Lista ') + \
                           ('la '
                            if controller[0] == 'a'
                            else 'el ') + \
                           f"___{controller}___ "\
                           "asociad" + \
                           ('a ' if controller[0] == 'a' else 'o ') + \
                           f"al parametro **_{parameters[0]}_**, "\
                           "que posea ___asistencias___ vinculadas "\
                           f"al parametro **_{parameters[1]}_**, "\
                           "en relacion al nombre de" + \
                           (' la '
                            if parameters[1][0] == 'a'
                            else 'l ') + \
                           f"___{parameters[1].lower()}___ presente en "\
                           f"cada ___asistencia___, "\
                            "y registradas "\
                           f"entre las fechas **_{parameters[2]}_** "\
                           f"y **_{parameters[3]}_**, "\
                            "todos ingresados como parametros dentro de los "\
                            "corchetes **[ ]**, "\
                            "mostrando el total de "\
                            "puntos de las ___asistencias___ "\
                           f"en cuestion para el ___{controller}___. "\
                           f"El parametro **_{parameters[0]}_** deberá "\
                            "corresponder a un valor numerico, "\
                           f"el parametro **_{parameters[1]}_** deberá "\
                            "corresponder a un valor de texto y "\
                           f"los parametros **_{parameters[2]}_** "\
                           f"y **_{parameters[3]}_** "\
                            "deberán corresponder a valores de fecha "\
                            "en 'Día/Mes/Año'.\n"
                elif head == "listAllPointMember":
                    return f"- **${head}:{target} "\
                           f"[_{', '.join(parameters)}_]** " + \
                           ('**> e**   ->   Lista en una hoja de excel '
                            if excelrequest
                            else '   ->   Lista ') + \
                           ('la '
                            if controller[0] == 'a'
                            else 'el ') + \
                           f"___{controller}___ "\
                            "asociad" + \
                            ('a ' if controller[0] == 'a' else 'o ') + \
                           f"al parametro **_{parameters[0]}_**, "\
                            "mostrando "\
                            "el total de "\
                            "puntos de sus ___asistencias___ "\
                            "vinculadas al parametro "\
                           f"**_{parameters[1]}_**, "\
                            "en relacion al nombre de" + \
                           (' la '
                            if parameters[1][0] == 'a'
                            else 'l ') + \
                           f"___{parameters[1].lower()}___ presente en "\
                           f"cada ___asistencia___, "\
                            "y registradas entre las fechas "\
                           f"**_{parameters[2]}_** "\
                           f"y **_{parameters[3]}_**, "\
                            "todos ingresados como parametros dentro de los "\
                            "corchetes **[ ]**. "\
                           f"El parametro **_{parameters[0]}_** deberá "\
                            "corresponder a un valor numerico, "\
                           f"el parametro **_{parameters[1]}_** deberá "\
                            "corresponder a un valor de texto y "\
                           f"los parametros **_{parameters[2]}_** "\
                           f"y **_{parameters[3]}_** "\
                            "deberán corresponder a valores de fecha "\
                            "en 'Día/Mes/Año'.\n"
            elif target == "name&event" and len(parameters) == 4:
                if head == "listPointMember":
                    return f"- **${head}:{target} "\
                           f"[_{', '.join(parameters)}_]** " + \
                           ('**> e**   ->   Lista en una hoja de excel '
                            if excelrequest
                            else '   ->   Lista ') + \
                           ('la '
                            if controller[0] == 'a'
                            else 'el ') + \
                           f"___{controller}___ "\
                           "asociad" + \
                           ('a ' if controller[0] == 'a' else 'o ') + \
                           f"al parametro **_{parameters[0]}_**, "\
                           "que posea ___asistencias___ vinculadas "\
                           f"al parametro **_{parameters[1]}_**, "\
                           "en relacion al nombre de" + \
                           (' la '
                            if parameters[1][0] == 'a'
                            else 'l ') + \
                           f"___{parameters[1].lower()}___ presente en "\
                           f"cada ___asistencia___, "\
                            "y registradas "\
                           f"entre las fechas **_{parameters[2]}_** "\
                           f"y **_{parameters[3]}_**, "\
                            "todos ingresados como parametros dentro de los "\
                            "corchetes **[ ]**, "\
                            "mostrando el total de "\
                            "puntos de las ___asistencias___ "\
                           f"en cuestion para el ___{controller}___. "\
                           f"El parametro **_{parameters[0]}_** y "\
                           f"**_{parameters[1]}_** deberán "\
                            "corresponder a valores de texto y "\
                           f"los parametros **_{parameters[2]}_** "\
                           f"y **_{parameters[3]}_** "\
                            "deberán corresponder a valores de fecha "\
                            "en 'Día/Mes/Año'.\n"
                elif head == "listAllPointMember":
                    return f"- **${head}:{target} "\
                           f"[_{', '.join(parameters)}_]** " + \
                           ('**> e**   ->   Lista en una hoja de excel '
                            if excelrequest
                            else '   ->   Lista ') + \
                           ('la '
                            if controller[0] == 'a'
                            else 'el ') + \
                           f"___{controller}___ "\
                            "asociad" + \
                            ('a ' if controller[0] == 'a' else 'o ') + \
                           f"al parametro **_{parameters[0]}_**, "\
                            "mostrando "\
                            "el total de "\
                            "puntos de sus ___asistencias___ "\
                            "vinculadas al parametro "\
                           f"**_{parameters[1]}_**, "\
                            "en relacion al nombre de" + \
                           (' la '
                            if parameters[1][0] == 'a'
                            else 'l ') + \
                           f"___{parameters[1].lower()}___ presente en "\
                           f"cada ___asistencia___, "\
                            "y registradas entre las fechas "\
                           f"**_{parameters[2]}_** "\
                           f"y **_{parameters[3]}_**, "\
                            "todos ingresados como parametros dentro de los "\
                            "corchetes **[ ]**. "\
                           f"El parametro **_{parameters[0]}_** y "\
                           f"**_{parameters[1]}_** deberán "\
                            "corresponder a valores de texto y "\
                           f"los parametros **_{parameters[2]}_** "\
                           f"y **_{parameters[3]}_** "\
                            "deberán corresponder a valores de fecha "\
                            "en 'Día/Mes/Año'.\n"
            elif target == "range&event" and len(parameters) == 4:
                if head == "listPointMember":
                    return f"- **${head}:{target} "\
                           f"[_{', '.join(parameters)}_]** " + \
                           ('**> e**   ->   Lista en una hoja de excel '
                            if excelrequest
                            else '   ->   Lista ') + \
                           ('todas las '
                            if controller[0] == 'a'
                            else 'todos los ') + \
                           f"___{controller}s___ "\
                           "asociad" + \
                           ('a ' if controller[0] == 'a' else 'o ') + \
                           f"al parametro **_{parameters[0]}_**, "\
                           "en relacion al nombre de" + \
                           (' la '
                            if parameters[0][0] == 'a'
                            else 'l ') + \
                           f"___{parameters[0].lower()}___ presente en " + \
                           f"cada ___{controller}___, "\
                           "que posea ___asistencias___ vinculadas "\
                           f"al parametro **_{parameters[1]}_**, "\
                           "en relacion al nombre de" + \
                           (' la '
                            if parameters[1][0] == 'a'
                            else 'l ') + \
                           f"___{parameters[1].lower()}___ presente en "\
                           f"cada ___asistencia___, "\
                            "y registradas "\
                           f"entre las fechas **_{parameters[2]}_** "\
                           f"y **_{parameters[3]}_**, "\
                            "todos ingresados como parametros dentro de los "\
                            "corchetes **[ ]**, "\
                            "mostrando de mayor a menor el total de "\
                            "puntos de las ___asistencias___ "\
                           f"en cuestion para cada ___{controller}___. "\
                           f"El parametro **_{parameters[0]}_** y "\
                           f"**_{parameters[1]}_** deberán "\
                            "corresponder a valores de texto y "\
                           f"los parametros **_{parameters[2]}_** "\
                           f"y **_{parameters[3]}_** "\
                            "deberán corresponder a valores de fecha "\
                            "en 'Día/Mes/Año'.\n"
                elif head == "listAllPointMember":
                    return f"- **${head}:{target} "\
                           f"[_{', '.join(parameters)}_]** " + \
                           ('**> e**   ->   Lista en una hoja de excel '
                            if excelrequest
                            else '   ->   Lista ') + \
                           ('todas las '
                            if controller[0] == 'a'
                            else 'todos los ') + \
                           f"___{controller}s___ "\
                            "asociad" + \
                            ('a ' if controller[0] == 'a' else 'o ') + \
                           f"al parametro **_{parameters[0]}_**, "\
                           "en relacion al nombre de" + \
                           (' la '
                            if parameters[0][0] == 'a'
                            else 'l ') + \
                           f"___{parameters[0].lower()}___ presente en " + \
                           f"cada ___{controller}___, "\
                            "mostrando de mayor a menor "\
                            "el total de "\
                            "puntos de sus ___asistencias___ "\
                            "vinculadas al parametro "\
                           f"**_{parameters[1]}_**, "\
                            "en relacion al nombre de" + \
                           (' la '
                            if parameters[1][0] == 'a'
                            else 'l ') + \
                           f"___{parameters[1].lower()}___ presente en "\
                           f"cada ___asistencia___, "\
                            "y registradas entre las fechas "\
                           f"**_{parameters[2]}_** "\
                           f"y **_{parameters[3]}_**, "\
                            "todos ingresados como parametros dentro de los "\
                            "corchetes **[ ]**. "\
                           f"El parametro **_{parameters[0]}_** y "\
                           f"**_{parameters[1]}_** deberán "\
                            "corresponder a valores de texto y "\
                           f"los parametros **_{parameters[2]}_** "\
                           f"y **_{parameters[3]}_** "\
                            "deberán corresponder a valores de fecha "\
                            "en 'Día/Mes/Año'.\n"
            elif target == "member&event" and len(parameters) == 2:
                return f"- **${head}:{target} "\
                       f"[_{', '.join(parameters)}_]** " + \
                       ('**> e**   ->   Lista en una hoja de excel '
                        if excelrequest
                        else '   ->   Lista ') + \
                       ('todas las '
                        if controller[0] == 'a'
                        else 'todos los ') + \
                       f"___{controller}s___ "\
                        "asociad" + \
                       ('a'
                        if controller[0] == 'a'
                        else 'o') + "s "\
                       f"a los parametros **_{parameters[0]}_** "\
                       f"y **_{parameters[1]}_** "\
                        "ingresados dentro de los corchetes **[ ]**, "\
                        "en relacion al nombre de" + \
                       (' la '
                        if parameters[0][0] == 'a'
                        else 'l ') + \
                       f"___{parameters[0].lower()}___ "\
                        "y al nombre de" + \
                       (' la '
                        if parameters[1][0] == 'a'
                        else 'l ') + \
                       f"___{parameters[1].lower()}___ presentes en "\
                       f"cada ___{controller}___. "\
                       f"Ambos parametros **_{parameters[0]}_** "\
                       f"y **_{parameters[1]}_** "\
                        "deberán corresponder a valores de texto.\n"
            elif target == "member&date" and len(parameters) == 3:
                return f"- **${head}:{target} "\
                       f"[_{', '.join(parameters)}_]** " + \
                       ('**> e**   ->   Lista en una hoja de excel '
                        if excelrequest
                        else '   ->   Lista ') + \
                       ('todas las '
                        if controller[0] == 'a'
                        else 'todos los ') + \
                       f"___{controller}s___ "\
                        "asociad" + \
                       ('a'
                        if controller[0] == 'a'
                        else 'o') + \
                       f"s al parametro **_{parameters[0]}_** "\
                        "en relacion al nombre de" + \
                       (' la '
                        if parameters[0][0] == 'a'
                        else 'l ') + \
                       f"___{parameters[0].lower()}___ presente en "\
                       f"cada ___{controller}___, "\
                        "y registrad" + \
                       ('a'if
                        controller[0] == 'a'
                        else 'o') + \
                        "s "\
                       f"entre las fechas **_{parameters[1]}_** "\
                       f"y **_{parameters[2]}_**, "\
                        "todos ingresados como parametros "\
                        "dentro de los corchetes **[ ]**. "\
                       f"El parametro **_{parameters[0]}_** deberá "\
                        "corresponder a un valor de texto "\
                       f"y los parametros **_{parameters[1]}_** "\
                       f"y **_{parameters[2]}_** "\
                        "deberán corresponder a valores de "\
                        "fecha en 'Día/Mes/Año'.\n"
            elif target == "event&date" and len(parameters) == 3:
                return f"- **${head}:{target} "\
                       f"[_{', '.join(parameters)}_]** " + \
                       ('**> e**   ->   Lista en una hoja de excel '
                        if excelrequest
                        else '   ->   Lista ') + \
                       ('todas las '
                        if controller[0] == 'a'
                        else 'todos los ') + \
                       f"___{controller}s___ "\
                        "asociad" + \
                       ('a'
                        if controller[0] == 'a'
                        else 'o') + \
                       f"s al parametro **_{parameters[0]}_** "\
                        "en relacion al nombre de" + \
                       (' la '
                        if parameters[0][0] == 'a'
                        else 'l ') + \
                       f"___{parameters[0].lower()}___ presente en "\
                       f"cada ___{controller}___, "\
                        "y registrad" + \
                       ('a'
                        if controller[0] == 'a'
                        else 'o') + "s "\
                       f"entre las fechas **_{parameters[1]}_** "\
                       f"y **_{parameters[2]}_**, "\
                        "todos ingresados como parametros "\
                        "dentro de los corchetes **[ ]**. "\
                       f"El parametro **_{parameters[0]}_** deberá "\
                        "corresponder a un valor de texto "\
                       f"y los parametros **_{parameters[1]}_** "\
                       f"y **_{parameters[2]}_** "\
                        "deberán corresponder a valores de fecha "\
                        "en 'Día/Mes/Año'.\n"
            elif target == "member&event&date" and len(parameters) == 4:
                return f"- **${head}:{target} "\
                       f"[_{', '.join(parameters)}_]** " + \
                       ('**> e**   ->   Lista en una hoja de excel '
                        if excelrequest
                        else '   ->   Lista ') + \
                       ('todas las '
                        if controller[0] == 'a'
                        else 'todos los ') + \
                       f"___{controller}s___ "\
                        "asociad" + \
                       ('a'
                        if controller[0] == 'a'
                        else 'o') + \
                       f"s a los parametros **_{parameters[0]}_** "\
                       f"y **_{parameters[1]}_**, "\
                        "en relacion al nombre de" + \
                       (' la '
                        if parameters[0][0] == 'a'
                        else 'l ') + \
                       f"___{parameters[0].lower()}___ "\
                        "y al nombre de" + \
                       (' la '
                        if parameters[1][0] == 'a'
                        else 'l ') + \
                       f"___{parameters[1].lower()}___ presentes en "\
                       f"cada ___{controller}___, "\
                        "y registrad" + \
                       ('a'
                        if controller[0] == 'a'
                        else 'o') + "s "\
                       f"entre las fechas **_{parameters[2]}_** "\
                       f"y **_{parameters[3]}_**, "\
                        "todos ingresados como parametros dentro "\
                        "de los corchetes **[ ]**. "\
                       f"Los parametros **_{parameters[0]}_** "\
                       f"y **_{parameters[1]}_** "\
                        "deberán corresponder a valores de texto, "\
                       f"y los parametros **_{parameters[2]}_** "\
                       f"y **_{parameters[3]}_** "\
                        "deberán corresponder a valores de fecha "\
                        "en 'Día/Mes/Año'.\n"
            elif target == "range" and len(parameters) == 3:
                if head == "listPointMember":
                    return f"- **${head}:{target} "\
                           f"[_{', '.join(parameters)}_]** " + \
                           ('**> e**   ->   Lista en una hoja de excel '
                            if excelrequest
                            else '   ->   Lista ') + \
                           ('todas las '
                            if controller[0] == 'a'
                            else 'todos los ') + \
                           f"___{controller}s___ "\
                           "asociad" + \
                           ('as ' if controller[0] == 'a' else 'os ') + \
                           f"al parametro **_{parameters[0]}_**, "\
                           "en relacion al nombre de" + \
                           (' la '
                            if parameters[0][0] == 'a'
                            else 'l ') + \
                           f"___{parameters[0].lower()}___ presente en " + \
                           f"cada ___{controller}___, "\
                            "que posean ___asistencias___ registradas "\
                           f"entre las fechas **_{parameters[1]}_** "\
                           f"y **_{parameters[2]}_**, "\
                            "todos ingresados como parametros dentro de los "\
                            "corchetes **[ ]**, "\
                            "mostrando de mayor a menor el total de "\
                            "puntos de las ___asistencias___ "\
                           f"en cuestion para cada ___{controller}___. "\
                           f"El parametro **_{parameters[0]}_** deberá "\
                            "corresponder a un valor de texto y "\
                           f"los parametros **_{parameters[1]}_** "\
                           f"y **_{parameters[2]}_** "\
                            "deberán corresponder a valores de fecha "\
                            "en 'Día/Mes/Año'.\n"
                elif head == "listAllPointMember":
                    return f"- **${head}:{target} "\
                           f"[_{', '.join(parameters)}_]** " + \
                           ('**> e**   ->   Lista en una hoja de excel '
                            if excelrequest
                            else '   ->   Lista ') + \
                           ('todas las '
                            if controller[0] == 'a'
                            else 'todos los ') + \
                           f"___{controller}s___, "\
                            "asociad" + \
                           ('as ' if controller[0] == 'a' else 'os ') + \
                           f"al parametro **_{parameters[0]}_**, "\
                           "en relacion al nombre de" + \
                           (' la '
                            if parameters[0][0] == 'a'
                            else 'l ') + \
                           f"___{parameters[0].lower()}___ presente en "\
                           f"cada ___{controller}___, "\
                            "mostrando para cada uno "\
                            "de mayor a menor el total de "\
                            "puntos de sus ___asistencias___ "\
                            "registradas entre las fechas "\
                           f"**_{parameters[1]}_** "\
                           f"y **_{parameters[2]}_**, "\
                            "todos ingresados como parametros dentro de los "\
                            "corchetes **[ ]**. "\
                           f"El parametro **_{parameters[0]}_** deberá "\
                            "corresponder a un valor de texto y "\
                           f"los parametros **_{parameters[1]}_** "\
                           f"y **_{parameters[2]}_** "\
                            "deberán corresponder a valores de fecha "\
                            "en 'Día/Mes/Año'.\n"
            elif target == "event" and len(parameters) == 3:
                if head == "listPointMember":
                    return f"- **${head}:{target} "\
                           f"[_{', '.join(parameters)}_]** " + \
                           ('**> e**   ->   Lista en una hoja de excel '
                            if excelrequest
                            else '   ->   Lista ') + \
                           ('todas las '
                            if controller[0] == 'a'
                            else 'todos los ') + \
                           f"___{controller}s___ "\
                           "que posean ___asistencias___ vinculadas "\
                           f"al parametro **_{parameters[0]}_**, "\
                           "en relacion al nombre de" + \
                           (' la '
                            if parameters[0][0] == 'a'
                            else 'l ') + \
                           f"___{parameters[0].lower()}___ presente en "\
                           f"cada ___asistencia___, "\
                            "y registradas "\
                           f"entre las fechas **_{parameters[1]}_** "\
                           f"y **_{parameters[2]}_**, "\
                            "todos ingresados como parametros dentro de los "\
                            "corchetes **[ ]**, "\
                            "mostrando de mayor a menor el total de "\
                            "puntos de las ___asistencias___ "\
                           f"en cuestion para cada ___{controller}___. "\
                           f"El parametro **_{parameters[0]}_** deberá "\
                            "corresponder a un valor de texto y "\
                           f"los parametros **_{parameters[1]}_** "\
                           f"y **_{parameters[2]}_** "\
                            "deberán corresponder a valores de fecha "\
                            "en 'Día/Mes/Año'.\n"
                elif head == "listAllPointMember":
                    return f"- **${head}:{target} "\
                           f"[_{', '.join(parameters)}_]** " + \
                           ('**> e**   ->   Lista en una hoja de excel '
                            if excelrequest
                            else '   ->   Lista ') + \
                           ('todas las '
                            if controller[0] == 'a'
                            else 'todos los ') + \
                           f"___{controller}s___, "\
                            "mostrando para cada uno "\
                            "de mayor a menor el total de "\
                            "puntos de sus ___asistencias___ "\
                            "vinculadas al parametro "\
                           f"**_{parameters[0]}_**, "\
                            "en relacion al nombre de" + \
                           (' la '
                            if parameters[0][0] == 'a'
                            else 'l ') + \
                           f"___{parameters[0].lower()}___ presente en "\
                           f"cada ___asistencia___, "\
                            "y registradas entre las fechas "\
                           f"**_{parameters[1]}_** "\
                           f"y **_{parameters[2]}_**, "\
                            "todos ingresados como parametros dentro de los "\
                            "corchetes **[ ]**. "\
                           f"El parametro **_{parameters[0]}_** deberá "\
                            "corresponder a un valor de texto y "\
                           f"los parametros **_{parameters[1]}_** "\
                           f"y **_{parameters[2]}_** "\
                            "deberán corresponder a valores de fecha "\
                            "en 'Día/Mes/Año'.\n"
            else:
                return f"- **${head}:{target} "\
                       f"[_{', '.join(parameters)}_]** " + \
                       ('**> e**   ->   Lista en una hoja de excel '
                        if excelrequest
                        else '   ->   Lista ') + \
                       ('todas las '
                        if controller[0] == 'a'
                        else 'todos los ') + \
                       f"___{controller}s___ "\
                        "asociad" + \
                       ('a'
                        if controller[0] == 'a'
                        else 'o') + \
                       f"s al parametro **_{parameters[0]}_** "\
                        "ingresado dentro de los corchetes **[ ]**, "\
                        "en relacion al nombre de" + \
                       (' la '
                        if parameters[0][0] == 'a'
                        else 'l ') + \
                       f"___{parameters[0].lower()}___ presente en "\
                       f"cada ___{controller}___. "\
                       f"Este parametro **_{parameters[0]}_** "\
                        "deberá corresponder a un valor de texto.\n"
        elif mode == "add":
            value = f"- **${head} [_{', '.join(parameters)}_]**   ->   "\
                     "Añade " + \
                    ('una nueva '
                     if controller[0] == 'a'
                     else 'un nuevo ') + \
                    f"___{controller}___, ingresando "\
                     "dentro de los corchetes **[ ]** "
            for i in range(len(parameters)):
                if parameters[i] == "Nombre":
                    value = value + "un parametro "\
                            f"**_{parameters[i]}_** "\
                            "como valor de texto"
                elif parameters[i] == "Puntos":
                    value = value + "un parametro "\
                            f"**_{parameters[i]}_** "\
                            "como valor numerico decimal"
                elif parameters[i] == "Fecha":
                    value = value + "un parametro "\
                            f"**_{parameters[i]}_** "\
                            "como valor de fecha en 'Día/Mes/Año'"
                elif parameters[i] == "Control":
                        value = value + "un parametro "\
                                f"**_{parameters[i]}_** "\
                                "como valor numerico"
                elif parameters[i] == "Descripción":
                    value = value + f"un parametro "\
                            f"**_{parameters[i]}_** "\
                            "como valor de texto"
                else:
                    value = value + "un parametro "\
                            f"**_{parameters[i]}_** "\
                            "como valor de texto asociado al nombre "\
                            f"de un ___{parameters[i].lower()}___"
                if i == len(parameters) - 1:
                    value = value + ".\n"
                elif i == len(parameters) - 2:
                    value = value + " y "
                else:
                    value = value + ", "
            return value
        elif mode == "upd":
            if target == "id":
                value = f"- **${head}:{target} "\
                        f"[_{', '.join(parameters)}_]**   ->   "\
                         "Actualiza los datos de " + \
                        ('una '
                         if controller[0] == 'a'
                         else 'un ') + \
                        f"___{controller}___ "\
                         "apuntando a su identificador, "\
                         "ingresando dentro de los corchetes **[ ]** "
                for i in range(len(parameters)):
                    if parameters[i] == "ID":
                        value = value + "un parametro "\
                                f"**_{parameters[i]}_** "\
                                "como valor numerico"
                    elif parameters[i] == "Nombre":
                        value = value + "un parametro "\
                                f"**_{parameters[i]}_** "\
                                "como valor de texto"
                    elif parameters[i] == "Puntos":
                        value = value + "un parametro "\
                                f"**_{parameters[i]}_** "\
                                "como valor numerico decimal"
                    elif parameters[i] == "Fecha":
                        value = value + "un parametro "\
                                f"**_{parameters[i]}_** "\
                                "como valor de fecha en 'Día/Mes/Año'"
                    elif parameters[i] == "Control":
                        value = value + "un parametro "\
                                f"**_{parameters[i]}_** "\
                                "como valor numerico"
                    elif parameters[i] == "Descripción":
                        value = value + "un parametro "\
                                f"**_{parameters[i]}_** "\
                                "como valor de texto"
                    else:
                        value = value + "un parametro "\
                                f"**_{parameters[i]}_** "\
                                 "como valor de texto asociado al nombre "\
                                f"de un ___{parameters[i].lower()}___"
                    if i == len(parameters) - 1:
                        value = value + ".\n"
                    elif i == len(parameters) - 2:
                        value = value + " y "
                    else:
                        value = value + ", "
                return value
            elif target == "name":
                value = f"- **${head}:{target} "\
                        f"[_{', '.join(parameters)}_]**   ->   "\
                         "Actualiza los datos de " + \
                        ('una '
                         if controller[0] == 'a'
                         else 'un ') + \
                        f"___{controller}___ "\
                        f"apuntando a su nombre, "\
                         "ingresando dentro de los corchetes **[ ]** "
                for i in range(len(parameters)):
                    if parameters[i] == "Nombre":
                        value = value + "un parametro "\
                                f"**_{parameters[i]}_** "\
                                "como valor de texto"
                    elif parameters[i] == "Puntos":
                        value = value + "un parametro "\
                                f"**_{parameters[i]}_** "\
                                "como valor numerico decimal"
                    elif parameters[i] == "Fecha":
                        value = value + "un parametro "\
                                f"**_{parameters[i]}_** "\
                                "como valor de fecha en 'Día/Mes/Año'"
                    elif parameters[i] == "Control":
                        value = value + "un parametro "\
                                f"**_{parameters[i]}_** "\
                                "como valor numerico"
                    elif parameters[i] == "Descripción":
                        value = value + "un parametro "\
                                f"**_{parameters[i]}_** "\
                                "como valor de texto"
                    else:
                        value = value + "un parametro "\
                                f"**_{parameters[i]}_** "\
                                "como valor de texto asociado al nombre "\
                                f"de un ___{parameters[i].lower()}___"
                    if i == len(parameters) - 1:
                        value = value + ".\n"
                    elif i == len(parameters) - 2:
                        value = value + " y "
                    else:
                        value = value + ", "
                return value
        elif mode == "del":
            if target == "id":
                return f"- **${head}:{target} "\
                       f"[_{', '.join(parameters)}_]**   ->   "\
                        "Elimina " + \
                       ('una '
                        if controller[0] == 'a'
                        else 'un ') + \
                       f"___{controller}___ "\
                        "apuntando a su identificador, ingresando "\
                        "dentro de los corchetes **[ ]** "\
                       f"un parametro **_{parameters[0]}_** "\
                        "como valor numerico.\n"
            elif target == "name":
                return f"- **${head}:{target} "\
                       f"[_{', '.join(parameters)}_]**   ->   "\
                        "Elimina " + \
                       ('una '
                        if controller[0] == 'a'
                        else 'un ') + \
                       f"___{controller}___ "\
                        "apuntando a su nombre, ingresando "\
                        "dentro de los corchetes **[ ]** "\
                       f"un parametro **_{parameters[0]}_** "\
                        "como valor de texto.\n"