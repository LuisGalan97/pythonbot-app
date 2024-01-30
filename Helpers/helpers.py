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
            alias = ', '.join(map(str,\
                    [value['alias'] for value in reftarget.values()]))
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
                        foreignid[key] = getattr(getattr(self,
                                         f"_AppHandler__{key}Controller"),
                                         f"get{key.capitalize()}s")(
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
    def checkRequest(request, reftarget):
            references = ', '.join(map(str, list(reftarget.keys())))
            types = [value["type"] for value in reftarget.values()]
            alias = ', '.join(map(str,
                    [value['alias'] for value in reftarget.values()]))
            datas = request
            if (isinstance(datas, list) and
                len(datas) == len(references.split(','))):
                for i in range(len(datas)):
                    datas[i] = datas[i].strip()
                    if not datas[i]:
                        return "No fue ingresado ningun dato en el campo "\
                              f"**_{alias.split(',')[i].strip()}_**"
                    try:
                        if types[i] == datetime:
                            datas[i] = datetime.strptime(datas[i], "%d-%m-%Y")
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
                references = list(map(lambda x: x.strip(),
                             references.split(',')))
                datas = dict(zip(references, datas))
                return datas
            else:
                return "Datos ingresados invalidos, "\
                       "recuerda que debes ingresar:\n"\
                      f"**[_{alias}_]**"

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
                "ID" : "id",
                #"Integrante ID" : "integrante_id",
                "Integrante" : "integrante_name",
                #"Rango ID" : "integrante_rango_id",
                #"Rango" : "integrante_rango_name",
                #"Control" : "integrante_rango_control",
                #"Descripción Rango" : "integrante_rango_description",
                #"Fecha de creación Integrante" : "integrante_datecreate",
                #"Fecha de modificación Integrante" : "integrante_dateupdate",
                #"Evento ID" : "evento_id",
                "Evento" : "evento_name",
                "Puntos" : "evento_points",
                #"Descripción Evento" : "evento_description",
                "Fecha" : "date"
            }
        elif nameCtrl == "evento":
            structCtrl[nameCtrl] = {
                "ID" : "id",
                "Nombre" : "name",
                "Puntos" : "points",
                "Descripción" : "description"
            }
        elif nameCtrl == "integrante":
            structCtrl[nameCtrl] = {
                "ID" : "id",
                "Nombre" : "name",
                #"Rango ID" : "rango_id",
                "Rango" : "rango_name",
                #"Control Rango" : "rango_control",
                #"Descripción Rango" : "rango_description",
                "Fecha de creación" : "datecreate",
                "Fecha de modificación" : "dateupdate"
            }
        elif nameCtrl == "rango":
            structCtrl[nameCtrl] = {
                "ID" : "id",
                "Nombre" : "name",
                "Control" : "control",
                "Descripción" : "description"
            }
        if targets:
            if "id" in targets:
                structTargets["id"] = {
                    "type" : int,
                    "fk" : False,
                    "alias" : "ID"
                }
            if "name" in targets:
                structTargets["name"] = {
                    "type" : str,
                    "fk" : False,
                    "alias" : "Nombre"
                }
            if "rango" in targets:
                structTargets["rango"] = {
                    "type" : str,
                    "fk" : True,
                    "alias" : "Rango"
                }
            if "rango_id" in targets:
                structTargets["rango_id"] = {
                    "type" : int,
                    "fk" : False,
                    "alias" : "Rango ID"
                }
            if "integrante" in targets:
                structTargets["integrante"] = {
                    "type" : str,
                    "fk" : True,
                    "alias" : "Integrante"
                }
            if "integrante_id" in targets:
                structTargets["integrante_id"] = {
                    "type" : int,
                    "fk" : False,
                    "alias" : "Integrante ID"
                }
            if "evento" in targets:
                structTargets["evento"] = {
                    "type" : str,
                    "fk" : True,
                    "alias" : "Evento"
                }
            if "evento_id" in targets:
                structTargets["evento_id"] = {
                    "type" : int,
                    "fk" : False,
                    "alias" : "Evento ID"
                }
            if "date_1" in targets:
                structTargets["date_1"] = {
                    "type" : datetime,
                    "fk" : False,
                    "alias" : "Fecha 1"
                }
            if "date_2" in targets:
                structTargets["date_2"] = {
                    "type" : datetime,
                    "fk" : False,
                    "alias" : "Fecha 2"
                }
        return {"controller" : structCtrl, "targets" : structTargets}

    @staticmethod
    def setStruct(nameCtrl):
        structCtrl = {}
        structTargets = {}
        if nameCtrl == "asistencia":
            structCtrl[nameCtrl] = {"create" : False}
            structTargets["integrante"] = {
                "type" : str,
                "fk" : True,
                "alias" : "Integrante"
            }
            structTargets["evento"] = {
                "type" : str,
                "fk" : True,
                "alias" : "Evento"
            }
            structTargets["date"] = {
                "type" : datetime,
                "fk" : False,
                "alias" : "Fecha"
            }
        elif nameCtrl == "evento":
            structCtrl[nameCtrl] = {"create" : "name"}
            structTargets["name"] = {
                "type" : str,
                "fk" : False,
                "alias" : "Nombre"
            }
            structTargets["points"] = {
                "type" : float,
                "fk" : False,
                "alias" : "Puntos"
            }
            structTargets["description"] = {
                "type" : str,
                "fk" : False,
                "alias" : "Descripción"
            }
        elif nameCtrl == "integrante":
            structCtrl[nameCtrl] = {"create" : "name"}
            structTargets["name"] = {
                "type" : str,
                "fk" : False,
                "alias" : "Nombre"
            }
            structTargets["rango"] = {
                "type" : str,
                "fk" : True,
                "alias" : "Rango"
            }
            structTargets["date"] = {
                "type" : datetime,
                "fk" : False,
                "alias" : "Fecha"
            }
        elif nameCtrl == "rango":
            structCtrl[nameCtrl] = {"create" : "name"}
            structTargets["name"] = {
                "type" : str,
                "fk" : False,
                "alias" : "Nombre"
            }
            structTargets["control"] = {
                "type" : int,
                "fk" : False,
                "alias" : "Control"
            }
            structTargets["description"] = {
                "type" : str,
                "fk" : False,
                "alias" :
                "Descripción"
            }
        return {"controller" : structCtrl, "targets" : structTargets}

    @staticmethod
    def updStruct(nameCtrl, update):
        structCtrl = {}
        structTargets = {}
        if nameCtrl == "asistencia":
             if update == "id":
                structCtrl[nameCtrl] = {"update" : update}
                structTargets["id"] = {
                    "type" : int,
                    "fk" : False,
                    "alias" : "ID"
                }
                structTargets["integrante"] = {
                    "type" : str,
                    "fk" : True,
                    "alias" : "Integrante"
                }
                structTargets["evento"] = {
                    "type" : str,
                    "fk" : True,
                    "alias" : "Evento"
                }
                structTargets["date"] = {
                    "type" : datetime,
                    "fk" : False,
                    "alias" : "Fecha"
                }
        elif nameCtrl == "evento":
            if update == "name":
                structCtrl[nameCtrl] = {"update" : update}
                structTargets["name"] = {
                    "type" : str,
                    "fk" : False,
                    "alias" : "Nombre"
                }
                structTargets["points"] = {
                    "type" : float,
                    "fk" : False,
                    "alias" : "Puntos"
                }
                structTargets["description"] = {
                    "type" : str,
                    "fk" : False,
                    "alias" : "Descripción"
                }
            elif update == "id":
                structCtrl[nameCtrl] = {"update" : update}
                structTargets["id"] = {
                    "type" : int,
                    "fk" : False,
                    "alias" : "ID"
                }
                structTargets["name"] = {
                    "type" : str,
                    "fk" : False,
                    "alias" : "Nombre"
                }
                structTargets["points"] = {
                    "type" : float,
                    "fk" : False,
                    "alias" : "Puntos"
                }
                structTargets["description"] = {
                    "type" : str,
                    "fk" : False,
                    "alias" : "Descripción"
                }
        elif nameCtrl == "integrante":
            if update == "name":
                structCtrl[nameCtrl] = {"update" : update}
                structTargets["name"] = {
                    "type" : str,
                    "fk" : False,
                    "alias" : "Nombre"
                }
                structTargets["rango"] = {
                    "type" : str,
                    "fk" : True,
                    "alias" : "Rango"
                }
                structTargets["date"] = {
                    "type" : datetime,
                    "fk" : False,
                    "alias" : "Fecha"
                }
            elif update == "id":
                structCtrl[nameCtrl] = {"update" : update}
                structTargets["id"] = {
                    "type" : int,
                    "fk" : False,
                    "alias" : "ID"
                }
                structTargets["name"] = {
                    "type" : str,
                    "fk" : False,
                    "alias" : "Nombre"
                }
                structTargets["rango"] = {
                    "type" : str,
                    "fk" : True,
                    "alias" : "Rango"
                }
                structTargets["date"] = {
                    "type" : datetime,
                    "fk" : False,
                    "alias" : "Fecha"
                }
        elif nameCtrl == "rango":
            if update == "name":
                structCtrl[nameCtrl] = {"update" : update}
                structTargets["name"] = {
                    "type" : str,
                    "fk" : False,
                    "alias" : "Nombre"
                }
                structTargets["control"] = {
                    "type" : int,
                    "fk" : False,
                    "alias" : "Control"
                }
                structTargets["description"] = {
                    "type" : str,
                    "fk" : False,
                    "alias" : "Descripción"
                }
            elif update == "id":
                structCtrl[nameCtrl] = {"update" : update}
                structTargets["id"] = {
                    "type" : int,
                    "fk" : False,
                    "alias" : "ID"
                }
                structTargets["name"] = {
                    "type" : str,
                    "fk" : False,
                    "alias" : "Nombre"
                }
                structTargets["control"] = {
                    "type" : int,
                    "fk" : False,
                    "alias" : "Control"
                }
                structTargets["description"] = {
                    "type" : str,
                    "fk" : False,
                    "alias" : "Descripción"
                }
        return {"controller" : structCtrl, "targets" : structTargets}

    @staticmethod
    def delStruct(nameCtrl, delete):
        structCtrl = {}
        structTargets = {}
        if nameCtrl == "asistencia":
             if delete == "id":
                structCtrl[nameCtrl] = {"delete" : delete}
                structTargets["id"] = {
                    "type" : int,
                    "fk" : False,
                    "alias" : "ID"
                }
        elif nameCtrl == "evento":
            if delete == "name":
                structCtrl[nameCtrl] = {"delete" : delete}
                structTargets["name"] = {
                    "type" : str,
                    "fk" : False,
                    "alias" : "Nombre"
                }
            elif delete == "id":
                structCtrl[nameCtrl] = {"delete" : delete}
                structTargets["id"] = {
                    "type" : int,
                    "fk" : False,
                    "alias" : "ID"
                }
        elif nameCtrl == "integrante":
            if delete == "name":
                structCtrl[nameCtrl] = {"delete" : delete}
                structTargets["name"] = {
                    "type" : str,
                    "fk" : False,
                    "alias" : "Nombre"
                }
            elif delete == "id":
                structCtrl[nameCtrl] = {"delete" : delete}
                structTargets["id"] = {
                    "type" : int,
                    "fk" : False,
                    "alias" : "ID"
                }
        elif nameCtrl == "rango":
            if delete == "name":
                structCtrl[nameCtrl] = {"delete" : delete}
                structTargets["name"] = {
                    "type" : str,
                    "fk" : False,
                    "alias" : "Nombre"
                }
            elif delete == "id":
                structCtrl[nameCtrl] = {"delete" : delete}
                structTargets["id"] = {
                    "type" : int,
                    "fk" : False,
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
            excelrequest = True if command.find('>') != -1 else False
        if mode == "list":
            if not target:
                return f"- **${head}**   ->   " + \
                        ('Lista en una hoja de excel '
                         if excelrequest
                         else 'Lista ') + \
                        ('todas las '
                         if controller[0] == 'a'
                         else 'todos los ') + \
                        f"___{controller}s___.\n"
            elif target == "id":
                return f"- **${head}:{target} "\
                       f"[_{', '.join(parameters)}_]** " + \
                       ('**> e**   ->   Lista en una hoja de excel '
                        if excelrequest
                        else '   ->   Lista ') + \
                       ('la '
                        if controller[0] == 'a'
                        else 'el ') + \
                       f"___{controller}___ "\
                       f"asociad" + \
                       ('a ' if controller[0] == 'a' else 'o ') + \
                       f"al parametro **_{parameters[0]}_** "\
                       f"ingresado dentro de los corchetes **[ ]**. "\
                       f"Este parametro **_{parameters[0]}_** deberá "\
                        "corresponder a un valor numerico.\n"
            elif target == "name":
                return f"- **${head}:{target} "\
                       f"[_{', '.join(parameters)}_]** " + \
                       ('**> e**   ->   Lista en una hoja de excel '
                        if excelrequest
                        else '   ->   Lista ') + \
                       ('la '
                        if controller[0] == 'a'
                        else 'el ') + \
                       f"___{controller}___ "\
                       f"asociad" + \
                       ('a '
                        if controller[0] == 'a '
                        else 'o ') + \
                       f"al parametro **_{parameters[0]}_** "\
                        "ingresado dentro de los corchetes **[ ]**. "\
                       f"Este parametro **_{parameters[0]}_** deberá "\
                        "corresponder a un valor de texto.\n"
            elif target == "date":
                return f"- **${head}:{target} "\
                       f"[_{', '.join(parameters)}_]** " + \
                       ('**> e**   ->   Lista en una hoja de excel '
                        if excelrequest
                        else '   ->   Lista ') + \
                       ('todas las '
                        if controller[0] == 'a'
                        else 'todos los ') + \
                        f"___{controller}s___ "\
                        f"registrad" + \
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
                        "en 'Día-Mes-Año'.\n"
            elif target == "member&event":
                return f"- **${head}:{target} "\
                       f"[_{', '.join(parameters)}_]** " + \
                       ('**> e**   ->   Lista en una hoja de excel '
                        if excelrequest
                        else '   ->   Lista ') + \
                       ('todas las '
                        if controller[0] == 'a'
                        else 'todos los ') + \
                       f"___{controller}s___ "\
                       f"asociad" + \
                       ('a'
                        if controller[0] == 'a'
                        else 'o') + "s "\
                       f"a los parametros **_{parameters[0]}_** "\
                       f"y **_{parameters[1]}_** "\
                        "ingresados dentro de los corchetes **[ ]**, "\
                       f"en relacion al nombre de" + \
                       (' la '
                        if parameters[0][0] == 'a'
                        else 'l ') + \
                       f"___{parameters[0].lower()}___ "\
                       f"y al nombre de" + \
                       (' la '
                        if parameters[1][0] == 'a'
                        else 'l ') + \
                       f"___{parameters[1].lower()}___ presentes en " + \
                       ('la '
                        if controller[0] == 'a'
                        else 'el ') + \
                       f"___{controller}___. "\
                       f"Ambos parametros **_{parameters[0]}_** "\
                       f"y **_{parameters[1]}_** "\
                        "deberán corresponder a valores de texto.\n"
            elif target == "member&date":
                return f"- **${head}:{target} "\
                       f"[_{', '.join(parameters)}_]** " + \
                        ('**> e**   ->   Lista en una hoja de excel '
                         if excelrequest
                         else '   ->   Lista ') + \
                        ('todas las '
                         if controller[0] == 'a'
                         else 'todos los ') + \
                        f"___{controller}s___ "\
                        f"asociad" + \
                        ('a'
                         if controller[0] == 'a'
                         else 'o') + \
                        f"s al parametro **_{parameters[0]}_** "\
                        f"en relacion al nombre de" + \
                        (' la '
                         if parameters[0][0] == 'a'
                         else 'l ') + \
                        f"___{parameters[0].lower()}___ presente en " + \
                        ('la '
                         if controller[0] == 'a'
                         else 'el ') + \
                        f"___{controller}___, "\
                        f"y registrad" + \
                        ('a'if
                         controller[0] == 'a'
                         else 'o') + \
                        f"s "\
                        f"entre las fechas **_{parameters[1]}_** "\
                        f"y **_{parameters[2]}_**, "\
                        "todos ingresados como parametros "\
                        "dentro de los corchetes **[ ]**. "\
                        f"El parametro **_{parameters[0]}_** deberá "\
                        f"corresponder a un valor de texto "\
                        f"y los parametros **_{parameters[1]}_** "\
                        f"y **_{parameters[2]}_** "\
                        "deberán corresponder a valores de "\
                        "fecha en 'Día-Mes-Año'.\n"
            elif target == "event&date":
                return  f"- **${head}:{target} "\
                        f"[_{', '.join(parameters)}_]** "\
                        ('**> e**   ->   Lista en una hoja de excel ' 
                         if excelrequest 
                         else '   ->   Lista ') + \
                        ('todas las '
                         if controller[0] == 'a' 
                         else 'todos los ') + \
                        f"___{controller}s___ "\
                        f"asociad" + \
                        ('a' 
                         if controller[0] == 'a' 
                         else 'o') + \
                        f"s al parametro **_{parameters[0]}_** "\
                        f"en relacion al nombre de " + \
                        (' la ' 
                         if parameters[0][0] == 'a' 
                         else 'l ') + \
                        f"___{parameters[0].lower()}___ presente en " + \
                        ('la ' 
                         if controller[0] == 'a' 
                         else 'el ') + \
                        f"___{controller}___, "\
                        f"y registrad" + \
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
                        "en 'Día-Mes-Año'.\n"
            elif target == "member&event&date":
                return (f"- **${head}:{target} [_{', '.join(parameters)}_]** "\
                        f"{'**> e**   ->   Lista en una hoja de excel' if excelrequest else '   ->   Lista'} "\
                        f"{'todas las'if controller[0] == 'a' else 'todos los'} "\
                        f"___{controller}s___ "\
                        f"asociad{'a' if controller[0] == 'a' else 'o'}s a los parametros **_{parameters[0]}_** "\
                        f"y **_{parameters[1]}_**, "\
                        f"en relacion al nombre de{' la' if parameters[0][0] == 'a' else 'l'} "\
                        f"___{parameters[0].lower()}___ "
                        f"y al nombre de{' la' if parameters[1][0] == 'a' else 'l'} "\
                        f"___{parameters[1].lower()}___ presentes en "\
                        f"{'la' if controller[0] == 'a' else 'el'} ___{controller}___, "
                        f"y registrad{'a'if controller[0] == 'a' else 'o'}s "\
                        f"entre las fechas **_{parameters[2]}_** y **_{parameters[3]}_**, "\
                        "todos ingresados como parametros dentro de los corchetes **[ ]**. "\
                        f"Los parametros **_{parameters[0]}_** y **_{parameters[1]}_** "\
                         "deberán corresponder a valores de texto, "\
                        f"y los parametros **_{parameters[2]}_** y **_{parameters[3]}_** "\
                        "deberán corresponder a valores de fecha en 'Día-Mes-Año'.\n")
            else:
                return (f"- **${head}:{target} [_{', '.join(parameters)}_]** "\
                        f"{'**> e**   ->   Lista en una hoja de excel' if excelrequest else '   ->   Lista'} "\
                        f"{'todas las'if controller[0] == 'a' else 'todos los'} "\
                        f"___{controller}s___ "\
                        f"asociad{'a' if controller[0] == 'a' else 'o'}s al parametro **_{parameters[0]}_** "\
                        "ingresado dentro de los corchetes **[ ]**, "\
                        f"en relacion al nombre de{' la' if parameters[0][0] == 'a' else 'l'} "\
                        f"___{parameters[0].lower()}___ presente en "\
                        f"{'la' if controller[0] == 'a' else 'el'} ___{controller}___. "
                        f"Este parametro **_{parameters[0]}_** deberá corresponder a un valor de texto.\n")
        elif mode == "add":
            value = (f"- **${head} [_{', '.join(parameters)}_]**   ->   Añade "\
                    f"{'una nueva'if controller[0] == 'a' else 'un nuevo'} "\
                    f"___{controller}___, ingresando dentro de los corchetes **[ ]** ")
            for i in range(len(parameters)):
                if parameters[i] == "Nombre":
                    value = value + f"un parametro **_{parameters[i]}_** como valor de texto"
                elif parameters[i] == "Puntos":
                    value = value + f"un parametro **_{parameters[i]}_** como valor numerico decimal"
                elif parameters[i] == "Fecha":
                    value = value + f"un parametro **_{parameters[i]}_** como valor de fecha en 'Día-Mes-Año'"
                elif parameters[i] == "Control":
                        value = value + f"un parametro **_{parameters[i]}_** como valor numerico"
                elif parameters[i] == "Descripción":
                    value = value + f"un parametro **_{parameters[i]}_** como valor de texto"
                else:
                    value = value + (f"un parametro **_{parameters[i]}_** como valor de texto asociado al nombre "\
                    f"de un ___{parameters[i].lower()}___")
                if i == len(parameters) - 1:
                    value = value + ".\n"
                elif i == len(parameters) - 2:
                    value = value + " y "
                else:
                    value = value + ", "
            return value
        elif mode == "upd":
            if target == "id":
                value = (f"- **${head}:{target} [_{', '.join(parameters)}_]**   ->   Actualiza los datos de "\
                        f"{'una'if controller[0] == 'a' else 'un'} ___{controller}___ "\
                        f"apuntando a su identificador, ingresando dentro de los corchetes **[ ]** ")
                for i in range(len(parameters)):
                    if parameters[i] == "ID":
                        value = value + f"un parametro **_{parameters[i]}_** como valor numerico"
                    elif parameters[i] == "Nombre":
                        value = value + f"un parametro **_{parameters[i]}_** como valor de texto"
                    elif parameters[i] == "Puntos":
                        value = value + f"un parametro **_{parameters[i]}_** como valor numerico decimal"
                    elif parameters[i] == "Fecha":
                        value = value + f"un parametro **_{parameters[i]}_** como valor de fecha en 'Día-Mes-Año'"
                    elif parameters[i] == "Control":
                        value = value + f"un parametro **_{parameters[i]}_** como valor numerico"
                    elif parameters[i] == "Descripción":
                        value = value + f"un parametro **_{parameters[i]}_** como valor de texto"
                    else:
                        value = value + (f"un parametro **_{parameters[i]}_** como valor de texto asociado al nombre "\
                        f"de un ___{parameters[i].lower()}___")
                    if i == len(parameters) - 1:
                        value = value + ".\n"
                    elif i == len(parameters) - 2:
                        value = value + " y "
                    else:
                        value = value + ", "
                return value
            elif target == "name":
                value = (f"- **${head}:{target} [_{', '.join(parameters)}_]**   ->   Actualiza los datos de "\
                        f"{'una 'if controller[0] == 'a' else 'un'} ___{controller}___ "\
                        f"apuntando a su nombre, ingresando dentro de los corchetes **[ ]** ")
                for i in range(len(parameters)):
                    if parameters[i] == "Nombre":
                        value = value + f"un parametro **_{parameters[i]}_** como valor de texto"
                    elif parameters[i] == "Puntos":
                        value = value + f"un parametro **_{parameters[i]}_** como valor numerico decimal"
                    elif parameters[i] == "Fecha":
                        value = value + f"un parametro **_{parameters[i]}_** como valor de fecha en 'Día-Mes-Año'"
                    elif parameters[i] == "Control":
                        value = value + f"un parametro **_{parameters[i]}_** como valor numerico"
                    elif parameters[i] == "Descripción":
                        value = value + f"un parametro **_{parameters[i]}_** como valor de texto"
                    else:
                        value = value + (f"un parametro **_{parameters[i]}_** como valor de texto asociado al nombre "\
                        f"de un ___{parameters[i].lower()}___")
                    if i == len(parameters) - 1:
                        value = value + ".\n"
                    elif i == len(parameters) - 2:
                        value = value + " y "
                    else:
                        value = value + ", "
                return value
        elif mode == "del":
            if target == "id":
                return (f"- **${head}:{target} [_{', '.join(parameters)}_]**   ->   Elimina "\
                        f"{'una'if controller[0] == 'a' else 'un'} ___{controller}___ "\
                        f"apuntando a su identificador, ingresando dentro de los corchetes **[ ]** "\
                        f"un parametro **_{parameters[0]}_** como valor numerico.\n")
            elif target == "name":
                return (f"- **${head}:{target} [_{', '.join(parameters)}_]**   ->   Elimina "\
                        f"{'una 'if controller[0] == 'a' else 'un'} ___{controller}___ "\
                        f"apuntando a su nombre, ingresando dentro de los corchetes **[ ]** "\
                        f"un parametro **_{parameters[0]}_** como valor de texto.\n")