from datetime import datetime

class Helpers:
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
                                    datas[i] = datetime.strptime(datas[i], "%Y-%m-%d")
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
                        return datas
                    else:
                        return "Datos ingresados invalidos, "\
                        "recuerda que debes ingresar:\n"\
                        f"{alias}."
                else:
                    return "El comando debe mantener la forma:\n"\
                    f"{command} [{alias}]."
            else:
                return "El comando debe mantener la forma:\n"\
                f"{command} [{alias}]."

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