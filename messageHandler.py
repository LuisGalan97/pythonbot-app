import os
dir = os.path.dirname(os.path.abspath(__file__))
import discord
from DF.dataframe import DataFrame
from Helpers.helpers import Helpers
from datetime import datetime

class MessageHandler:
    def __init__(self, message, client, test = False):
        self.__message = message
        self.__client = client
        self.__send = self.defaultFunction if not test else self.testFunction

    async def inMsg(self):
        if self.__message.author == self.__client.user:
            return

    async def sendText(self):
        author = self.__message.author
        nameChannel = self.__message.channel.name
        msg = ""
        if Helpers.checkAccess("hello", author, nameChannel):
            msg = self.__message.content
        if msg.startswith("$hello"):
            await self.__send(message = f"Hola **{author}**!, "\
                                         "soy **Avalon-bot** identificado "\
                                         "bajo la cuenta "\
                                        f"**{self.__client.user}**.\n")

    async def helpMsg(self):
        author = self.__message.author
        nameChannel = self.__message.channel.name
        msg = ""
        if Helpers.checkAccess("help", author, nameChannel):
            msg = self.__message.content
        messages = []
        if msg.startswith("$help:assist"):
        #---------------------------Asistencias--------------------------------
            messages.append("**___Asistencias___**\n")
            messages.append("\n")
            messages.append("Las ___asistencias___ hacen referencia a "\
            "una serie de registros de todas las participaciones, "\
            "en las cuales los integrantes de **⚜Avalon⚜** han podido "\
            "hacer parte, para actividades o eventos tales como ataques, "\
            "defensas, AVAs, entre otros. Una ___asistencia___ "\
            "por defecto contiene informacion de un ___integrante___ y "\
            "___evento___ asociado, junto con la fecha del suceso en "\
            "cuestion. Con lo anterior, se presentan una lista de todos "\
            "los comandos que permiten interactuar con los registros "\
            "de ___asistencias___.\n")
            messages.append("\n")
            messages.append("_Comandos de escaneo:_\n")
            messages.append("- **$checkAssist**   "\
                            "->    Realiza un escaneo de todos los "\
                            "mensajes presentes en el canal donde es "\
                            "invocado el comando. Para todos los mensajes "\
                            "que posean exclusivamente la reaccion ⚜️, "\
                            "se intentarán validar para la creacion de "\
                            "nuevas ___asistencias___. "\
                            "El mensaje deberá contener "\
                            "un ___evento___ y los ___integrantes___ "\
                            "que hicieron parte de este mismo, todos "\
                            "separados "\
                            "por comas: **_Evento_, _Integrante 1_, "\
                            "_Integrante 2_, ... _Integrante N_**. "\
                            "Se pueden añadir imagenes pero no "\
                            "serán revisadas por **Avalon-bot**. "\
                            "Si el mensaje es "\
                            "valido y las creaciones son exitosas, "\
                            "este será marcado con un ✅. "\
                            "Por otro lado si el mensaje es valido pero "\
                            "ocurre un error "\
                            "durante la creacion de las ___asistencias___, "\
                            "este será marcado con un ⚠️. "\
                            "Por ultimo, si el mensaje es invalido "\
                            "sea por sintaxis o por ingresar "\
                            "___integrantes___ o ___eventos___ que no estan "\
                            "presentes en la base de datos, este será "\
                            "marcado con un ❌. Este comando esta pensado "\
                            "para ser utilizado en un canal dedicado donde "\
                            "los ___integrantes___ de la alianza "\
                            "**⚜Avalon⚜** puedan subir sus ___asistencias___"\
                            ", para que posteriormente los moderadores, "\
                            "puedan revisar de forma preliminar las "\
                            "solicitudes y validarlas con un ⚜️, para por "\
                            "ultimo invocar el comando en cuestion.\n")
            messages.append("\n")
            messages.append("_Comandos de modificacion:_\n")
            messages.append(Helpers.genMsg("addAssist [Integrante, "\
                                           "Evento, Fecha]", "asistencia"))
            messages.append(Helpers.genMsg("updAssist:id [ID, Integrante, "\
                                           "Evento, Fecha]", "asistencia"))
            messages.append(Helpers.genMsg("delAssist:id [ID]", "asistencia"))
            messages.append("\n")
            messages.append("_Comandos de consulta:_\n")
            messages.append(Helpers.genMsg("listAssist", "asistencia"))
            messages.append(Helpers.genMsg("listAssist:id [ID]", "asistencia"))
            messages.append(Helpers.genMsg("listAssist:member [Integrante]",
                                           "asistencia"))
            messages.append(Helpers.genMsg("listAssist:event [Evento]",
                                           "asistencia"))
            messages.append(Helpers.genMsg("listAssist:date [Fecha 1, "\
                                           "Fecha 2]", "asistencia"))
            messages.append(Helpers.genMsg("listAssist:member&event "\
                                           "[Integrante, Evento]",
                                           "asistencia"))
            messages.append(Helpers.genMsg("listAssist:member&date "\
                                           "[Integrante, Fecha 1, Fecha 2]",
                                           "asistencia"))
            messages.append(Helpers.genMsg("listAssist:event&date "\
                                           "[Evento, Fecha 1, Fecha 2]",
                                           "asistencia"))
            messages.append(Helpers.genMsg("listAssist:member&event&date "\
                                           "[Integrante, Evento, "\
                                            "Fecha 1, Fecha 2]",
                                            "asistencia"))
            messages.append("\n")
            messages.append("_Comandos de consulta con impresion en excel:_\n")
            messages.append("Por defecto, los comandos de consulta imprimen "\
            "los registros en el canal de discord, "\
            "sin embargo, tambien pueden ser impresos dentro de una "\
            "hoja de excel, si despues del comando "\
            "se especifica el parametro **> e**.\n")
            messages.append(Helpers.genMsg("listAssist > e", "asistencia"))
            messages.append(Helpers.genMsg("listAssist:id [ID] > e",
                                           "asistencia"))
            messages.append(Helpers.genMsg("listAssist:member "\
                                           "[Integrante] > e", "asistencia"))
            messages.append(Helpers.genMsg("listAssist:event "\
                                           "[Evento] > e", "asistencia"))
            messages.append(Helpers.genMsg("listAssist:date "\
                                           "[Fecha 1, Fecha 2] > e",
                                           "asistencia"))
            messages.append(Helpers.genMsg("listAssist:member&event "\
                                           "[Integrante, Evento] > e",
                                           "asistencia"))
            messages.append(Helpers.genMsg("listAssist:member&date "\
                                           "[Integrante, Fecha 1, "\
                                            "Fecha 2] > e", "asistencia"))
            messages.append(Helpers.genMsg("listAssist:event&date "\
                                           "[Evento, Fecha 1, Fecha 2] > e",
                                           "asistencia"))
            messages.append(Helpers.genMsg("listAssist:member&event&date "\
                                           "[Integrante, Evento, "\
                                            "Fecha 1, Fecha 2] > e",
                                            "asistencia"))
        elif msg.startswith("$help:event"):
        #-----------------------------Eventos----------------------------------
            messages.append("**___Eventos___**\n")
            messages.append("\n")
            messages.append("Los ___eventos___ corresponden a una lista "\
            "con informacion de las actividades "\
            "las cuales **⚜Avalon⚜** ha decidido puntuar, "\
            "para poder recompensar a sus integrantes "\
            "por aporte y participacion, involucrando ataques, "\
            "defensas, AVAs, entre otros.\n")
            messages.append("\n")
            messages.append("_Comandos de modificacion:_\n")
            messages.append(Helpers.genMsg("addEvent "\
                                           "[Nombre, Puntos, Descripción]",
                                           "evento"))
            messages.append(Helpers.genMsg("updEvent:id "\
                                           "[ID, Nombre, "\
                                            "Puntos, Descripción]",
                                           "evento"))
            messages.append(Helpers.genMsg("updEvent:name "\
                                           "[Nombre, Puntos, Descripción]",
                                           "evento"))
            messages.append(Helpers.genMsg("delEvent:id [ID]", "evento"))
            messages.append(Helpers.genMsg("delEvent:name [Nombre]", "evento"))
            messages.append("\n")
            messages.append("_Comandos de consulta:_\n")
            messages.append(Helpers.genMsg("listEvent", "evento"))
            messages.append(Helpers.genMsg("listEvent:id [ID]", "evento"))
            messages.append(Helpers.genMsg("listEvent:name [Nombre]",
                                           "evento"))
            messages.append("\n")
            messages.append("_Comandos de consulta con impresion en excel:_\n")
            messages.append("Por defecto, los comandos de consulta "\
            "imprimen los registros en el canal de discord, "\
            "sin embargo, tambien pueden ser impresos dentro "\
            "de una hoja de excel, si despues del comando "\
            "se especifica el parametro **> e**.\n")
            messages.append(Helpers.genMsg("listEvent > e", "evento"))
            messages.append(Helpers.genMsg("listEvent:id [ID] > e", "evento"))
            messages.append(Helpers.genMsg("listEvent:name [Nombre] > e",
                                           "evento"))
        elif msg.startswith("$help:member"):
        #----------------------------Integrantes-------------------------------
            messages.append("**___Integrantes___**\n")
            messages.append("\n")
            messages.append("Los ___integrantes___ son una serie de "\
            "registros en los cuales se encuentran "\
            "listados y referenciados todos los miembros de la alianza "\
            "**⚜Avalon⚜**, junto con informacion "\
            "complementaria tales como el ___rango___ "\
            "asignado y la fecha de ingreso de cada miembro.\n")
            messages.append("\n")
            messages.append("_Comandos de modificacion:_\n")
            messages.append(Helpers.genMsg("addMember [Nombre, Rango, Fecha]",
                                           "integrante"))
            messages.append(Helpers.genMsg("updMember:id "\
                                           "[ID, Nombre, Rango, Fecha]",
                                           "integrante"))
            messages.append(Helpers.genMsg("updMember:name "\
                                           "[Nombre, Rango, Fecha]",
                                           "integrante"))
            messages.append(Helpers.genMsg("delMember:id [ID]", "integrante"))
            messages.append(Helpers.genMsg("delMember:name [Nombre]",
                                           "integrante"))
            messages.append("\n")
            messages.append("_Comandos de consulta:_\n")
            messages.append(Helpers.genMsg("listMember", "integrante"))
            messages.append(Helpers.genMsg("listMember:id [ID]", "integrante"))
            messages.append(Helpers.genMsg("listMember:name [Nombre]",
                                           "integrante"))
            messages.append(Helpers.genMsg("listMember:range [Rango]",
                                           "integrante"))
            messages.append(Helpers.genMsg("listMember:date "\
                                           "[Fecha 1, Fecha 2]",
                                           "integrante"))
            messages.append("\n")
            messages.append("_Comandos de consulta con impresion en excel:_\n")
            messages.append("Por defecto, los comandos de consulta "\
            "imprimen los registros en el canal de discord, "\
            "sin embargo, tambien pueden ser impresos dentro "\
            "de una hoja de excel, si despues del comando "\
            "se especifica el parametro **> e**.\n")
            messages.append(Helpers.genMsg("listMember > e", "integrante"))
            messages.append(Helpers.genMsg("listMember:id [ID] > e",
                                           "integrante"))
            messages.append(Helpers.genMsg("listMember:name [Nombre] > e",
                                           "integrante"))
            messages.append(Helpers.genMsg("listMember:range [Rango] > e",
                                           "integrante"))
            messages.append(Helpers.genMsg("listMember:date "\
                                           "[Fecha 1, Fecha 2] > e",
                                           "integrante"))
        elif msg.startswith("$help:range"):
        #--------------------------------Rangos--------------------------------
            messages.append("**_Rangos_**\n")
            messages.append("\n")
            messages.append("Los ___rangos___ disponen registros con "\
            "informacion de los diferentes "\
            "rangos asignables a los integrante o "\
            "miembros de la alianza **⚜Avalon⚜**.\n")
            messages.append("\n")
            messages.append("_Comandos de modificacion:_\n")
            messages.append(Helpers.genMsg("addRange "\
                                           "[Nombre, Control, Descripción]",
                                           "rango"))
            messages.append(Helpers.genMsg("updRange:id "\
                                           "[ID, Nombre, "\
                                            "Control, Descripción]",
                                            "rango"))
            messages.append(Helpers.genMsg("updRange:name "\
                                           "[Nombre, Control, Descripción]",
                                           "rango"))
            messages.append(Helpers.genMsg("delRange:id [ID]", "rango"))
            messages.append(Helpers.genMsg("delRange:name [Nombre]", "rango"))
            messages.append("\n")
            messages.append("_Comandos de consulta:_\n")
            messages.append(Helpers.genMsg("listRange", "rango"))
            messages.append(Helpers.genMsg("listRange:id [ID]", "rango"))
            messages.append(Helpers.genMsg("listRange:name [Nombre]", "rango"))
            messages.append("\n")
            messages.append("_Comandos de consulta con impresion en excel:_\n")
            messages.append("Por defecto, los comandos de consulta "\
            "imprimen los registros en el canal de discord, "\
            "sin embargo, tambien pueden ser impresos "\
            "dentro de una hoja de excel, si despues del comando "\
            "se especifica el parametro **> e**.\n")
            messages.append(Helpers.genMsg("listRange > e", "rango"))
            messages.append(Helpers.genMsg("listRange:id [ID] > e", "rango"))
            messages.append(Helpers.genMsg("listRange:name [Nombre] > e",
                                           "rango"))
        elif msg.startswith("$help:diagram"):
            await self.__send(message = "**___Diagrama de la estructura "\
                                        "de los datos:___**")
            discordFile = discord.File(f"{dir}/SQL/db_diagram.png")
            await self.__send(file = discordFile)
        elif msg.startswith("$help"):
            messages.append("**___Guia de usuario de Avalon-bot___**\n")
            messages.append("\n")
            messages.append("Bienvenido/a a la guia de usuario del "\
                            "bot de **⚜Avalon⚜** "\
                            "para discord. En esta seccion "\
                            "realizaremos una breve introduccion, "\
                            "de las funciones principales que dispone "\
                            "**_Avalon-bot_**, "\
                            "la estructura de la informacion con la que "\
                            "trabaja, y como podemos "\
                            "utilizarlo para obtener importantes beneficios, "\
                            "en el manejo y gestion de los datos "\
                            "asociados con la alianza.\n")
            messages.append("\n")
            messages.append("**_¿Que es Avalon-bot?_**\n")
            messages.append("**_Avalon-bot_** es una herramienta pensada "\
                            "y diseñada para facilitar al usuario la gestion "\
                            "de los datos asociados con la alianza "\
                            "**⚜Avalon⚜**, mediante la comprension "\
                            "de la estructura de la informacion planteada "\
                            "para este proposito, y la correcta "\
                            "utilizacion de los comandos dispuestos para "\
                            "poder acceder y manipular dicha informacion. "\
                            "Dicho esto, con Avalon-bot podras generar un "\
                            "seguimiento automatizado y estructurado, "\
                            "de datos relacionados con los "\
                            "___integrantes___, las ___asistencias___, "\
                            "los ___rangos___, "\
                            "y los ___eventos___ establecidos en la alianza, "\
                            "en conjunto con la capacidad de generar "\
                            "informes personalizados en excel, gracias "\
                            "a la implementacion de bases de datos SQL.\n")
            messages.append("\n")
            messages.append("**_¿Como se encuentra estructurada la "\
                            "informacion?_**\n")
            messages.append("Para la organizacion, gestion y guardado "\
                            "de la informacion, **_Avalon-bot_** "\
                            "tiene programada "\
                            "la interaccion con una base de "\
                            "datos SQLite en lenguaje python, "\
                            "teniendo acceso a un gestor de "\
                            "base de datos ligero, donde se encuentra "\
                            "cargada una estructura "\
                            "de 4 tablas relacionadas entre si, "\
                            "pensadas para almacenar la informacion "\
                            "de 4 datos principales: "\
                            "___integrantes___, ___asistencias___, "\
                            "___rangos___ y ___eventos___, con "\
                            "el fin de permitir la disposicion "\
                            "de por ejemplo una tabla de ___rangos___ "\
                            "de alianza, que posteriormente "\
                            "podra ser relacionada "\
                            "a un ___integrante___ de la tabla de "\
                            "___integrantes___, conservando la "\
                            "independencia de ambas tablas con "\
                            "sus datos propios y "\
                            "facilitando de esta forma su manipulacion. "\
                            "De forma similar la tabla ___eventos___ "\
                            "e ___integrantes___ "\
                            "pueden relacionarse o asociarse con la "\
                            "tabla de ___asistencias___, con el fin de "\
                            "registrar, que en una ___asistencia___ "\
                            "estuvo presente un ___integrante___ y "\
                            "fue con respecto a un ___evento___ especifico, "\
                            "los cuales tambien se encuentran "\
                            "en sus respectivas tablas.\n\n_Si desea "\
                            "visualizar el diagrama de la estructura de "\
                            "los datos, puede emplear el comando de ayuda:_\n"\
                            "* **$help:diagram**\n")
            messages.append("\n")
            messages.append("**_¿Como puedo empezar a utilizar "\
                            "Avalon-bot?_**\n")
            messages.append("Para poder utilizar **_Avalon-bot_**, debes "\
                            "emplear los comandos dispuestos por este mismo, "\
                            "los cuales varian dependiendo de la tabla con "\
                            "la que deseas interactuar, "\
                            "y el tipo de solicitud "\
                            "que deseas realizar (consulta, "\
                            "creacion, actualizacion o eliminacion). "\
                            "Con lo anterior, dada la extension "\
                            "de los comandos, estos se han especificado "\
                            "y detallado en su propia seccion "\
                            "asociada con cada tabla respectiva, "\
                            "siendo visibles mediante los comandos "\
                            "de ayuda que se presentan a continuacion.\n\n"\
                            "_Comandos de_ ___asistencias___:\n"\
                            "** * $help:assist**\n"\
                            "_Comandos de_ ___eventos___:\n"\
                            "** * $help:event**\n"\
                            "_Comandos de_ ___integrantes___:\n"\
                            "** * $help:member**\n"\
                            "_Comandos de_ ___rangos___:\n"\
                            "** * $help:range**")
        if messages:
            array = []
            length = 0
            for i in range(len(messages)):
                length = length + len(messages[i])
                if length >= 2000:
                    await self.__send(message = ''.join(array))
                    array = []
                    length = len(messages[i])
                    array.append(messages[i])
                    if i == len(messages) - 1:
                        await self.__send(message = ''.join(array))
                elif i == len(messages) - 1:
                    array.append(messages[i])
                    await self.__send(message = ''.join(array))
                else:
                    array.append(messages[i])

    async def dFMsg(self, command, method, struct):
        author = self.__message.author
        nameChannel = self.__message.channel.name
        msg = ""
        if Helpers.checkAccess(command, author, nameChannel):
            msg = self.__message.content
        if Helpers.checkCommand(msg, command):
            content = msg.replace(f'${command}', '').strip()
            request = Helpers.checkContent(command, content, struct["targets"])
            if isinstance(request, list):
                result = method(request, struct)
                if isinstance(result, list):
                    if content.find('>') != -1:
                        excelreq = content.lower()
                        excelreq = excelreq[excelreq.rfind(']')+1:]
                        excelreq = excelreq[:excelreq.find('e')+2]
                        excelreq = excelreq.replace(' ','')
                        if excelreq == ">e":
                            strContent = (content[content.find('[')+1:
                                          content.find(']')]
                                          .split(","))
                            strContent = "_".join(data.strip()
                                                  for data
                                                  in strContent)
                            if command.find(':') != -1:
                                fileName = (command.split(':')[0]) + \
                                           (command.split(':')[1]
                                            .capitalize()) + \
                                           (strContent)
                            else:
                                fileName = f"{command}{strContent}"
                            df = DataFrame(fileName, result)
                            if df.getSuccess():
                                discordFile = discord.File(df.getDirectory())
                                await self.__send(message =
                                                  "**___" + \
                                                  ([value['alias'] for
                                                    value in
                                                    struct['controller']
                                                    .values()][0]
                                                   .capitalize()) + \
                                                  "s___** "\
                                                  "**___encontrad" + \
                                                  ('a'
                                                   if list(struct['controller']
                                                      .keys())[0][0] == 'a'
                                                   else 'o') + \
                                                  "s:___**")
                                await self.__send(file = discordFile)
                                if not df.deleteFrame():
                                    await self.__send(message =
                                                      "Error al intentar "\
                                                      "eliminar el excel, "\
                                                      "por favor consulte "\
                                                      "con el administrador.")
                            else:
                                await self.__send(message =
                                                  "Error al intentar "\
                                                  "crear el excel, "\
                                                  "por favor consulte "\
                                                  "con el administrador.")
                        else:
                            parameters = "**[**" + \
                                         (', '.join([i.strip() for i
                                           in content[content.find('[')+1:
                                           content.rfind(']')]
                                           .split(',')])) + \
                                         "**]** "
                            await self.__send(message =
                                              "Se ha detectado el uso del "\
                                              "operador **>** despues "\
                                              "del comando "\
                                              "inicial, si desea obtener "\
                                              "los datos en un archivo "\
                                              "de excel, "\
                                              "debe completar el comando "\
                                              "ingresadolo de la "\
                                              "siguiente forma:\n"\
                                              f"**${command}** " + \
                                              (parameters
                                               if command.find(':') != -1
                                               else '') + \
                                              "**> e**")
                    else:
                        array = []
                        title = "**___" + \
                                ([value['alias'] for
                                  value in
                                  struct['controller']
                                  .values()][0]
                                  .capitalize())  + \
                                "s___** "\
                                "**___encontrad" + \
                                ('a'
                                 if [value['alias'] for
                                     value in
                                     struct['controller']
                                     .values()][0][0] == 'a'
                                 else 'o') + \
                                "s:___**"
                        length = len(title)
                        array.append(title)
                        for i in range(len(result)):
                            tempdict = "* " + \
                                       (', '.join([f'**_{key}_** : _{value}_'
                                        for key, value in result[i].items()]))
                            length = length + len(tempdict) + 1
                            if length >= 2000:
                                await self.__send(message = '\n'.join(array))
                                array = []
                                length = len(tempdict) + 1
                                array.append(tempdict)
                                if i == len(result) - 1:
                                    await self.__send(message =
                                                      '\n'.join(array))
                            elif i == len(result) - 1:
                                array.append(tempdict)
                                await self.__send(message = '\n'.join(array))
                            else:
                                array.append(tempdict)
                elif isinstance(result, str):
                    await self.__send(message = result)
                else:
                    await self.__send(message = "Error en la base de datos, "\
                                                "por favor consulte con el "\
                                                "administrador.")
            else:
                await self.__send(message = request)

    async def contMsg(self, command, method, struct):
        author = self.__message.author
        nameChannel = self.__message.channel.name
        msg = ""
        if Helpers.checkAccess(command, author, nameChannel):
            msg = self.__message.content
        if Helpers.checkCommand(msg, command):
            content = msg.replace(f'${command}', '').strip()
            request = Helpers.checkContent(command, content, struct["targets"])
            if isinstance(request, list):
                result = method(request, struct)
                if result:
                    await self.__send(message = result)
                else:
                    await self.__send(message = "Error en la base de datos, "\
                                                "por favor consulte con el "\
                                                "administrador.")
            else:
                await self.__send(message = request)

    async def checkAssist(self, command, app):
        author = self.__message.author
        channel = self.__message.channel
        permissions = channel.permissions_for(channel.guild.me)
        nameChannel = channel.name
        msg = ""
        if Helpers.checkAccess(command, author, nameChannel):
            msg = self.__message.content
        if msg.startswith(f"${command}"):
            if (permissions.send_messages and
                permissions.manage_messages and
                permissions.add_reactions):
                async for message in channel.history(limit=None):
                    if (len(message.reactions) == 1 and
                        str(message.reactions[0]) == '⚜️'):
                        targets = message.content.split(',')
                        targets = [target.strip() for
                                   target in
                                   targets]
                        if len(targets) > 1:
                            event = targets[0].split()
                            members = targets[1:]
                            members = [member.capitalize() for
                                       member in members]
                            date = datetime.now()
                            date = date.strftime('%d/%m/%Y')
                            notfound = False
                            result = app.getDatas(event,
                                     Helpers.getStruct("event",
                                                       ["name"]))
                            if not isinstance(result, list):
                                notfound = True
                            for member in members:
                                member = member.split()
                                result = app.getDatas(member,
                                         Helpers.getStruct("member",
                                                           ["name"]))
                                if not isinstance(result, list):
                                    notfound = True
                            if not notfound:
                                success = True
                                for member in members:
                                    assist = [member, event[0], date]
                                    result = app.setData(assist,
                                             Helpers.setStruct("assist"))
                                    if not "exito" in result:
                                        success = False
                                if success:
                                    await channel.send("* La solicitud "\
                                          f"**_{message.content}_** "\
                                           "fue registrada con exito. "\
                                           "Un ✅ ha sido añadido a la "\
                                            "solicitud en cuestion.\n")
                                    await message.clear_reactions()
                                    await message.add_reaction('✅')
                                else:
                                    await channel.send("* Ocurrio "\
                                          "un error al intentar "\
                                          "registrar la solicitud "\
                                         f"**_{message.content}_**, "\
                                          "por lo que puede que no se "\
                                          "no se hayan realizado todos "\
                                          "los registros, por favor "\
                                          "informe al administrador. "\
                                          "Una ⚠️ ha sido añadida a la "\
                                          "solicitud en cuestion.\n")
                                    await message.clear_reactions()
                                    await message.add_reaction('⚠️')
                            else:
                                await channel.send("* No se realizó "\
                                      "el registro de la solicitud "\
                                     f"**_{message.content}_**, "\
                                      "ya que existen errores "\
                                      "en los valores ingresados. "\
                                      "Una ❌ ha sido añadida a la "\
                                      "solicitud en cuestion.\n")
                                await message.clear_reactions()
                                await message.add_reaction('❌')
                        else:
                            await channel.send("* No se realizó "\
                                      "el registro de la solicitud "\
                                     f"**_{message.content}_**, "\
                                      "ya que existen errores "\
                                      "en los valores ingresados. "\
                                      "Una ❌ ha sido añadida a la "\
                                      "solicitud en cuestion.\n")
                            await message.clear_reactions()
                            await message.add_reaction('❌')
            else:
                if permissions.send_messages:
                    await channel.send("**Avalon-bot** no dispone de "\
                    "los permisos necesarios para eliminar o reaccionar "\
                   f"a mensajes por el canal **{channel.name}**. "\
                    "Por favor activelos "\
                    "para acceder a todas las funcionalidades.\n")
                else:
                    print( "-> Avalon-bot no dispone de los permisos "\
                           "necesarios para enviar mensajes "\
                          f"por el canal '{channel.name}'. Por favor "\
                           "activelos para acceder a todas "\
                           "las funcionalidades.\n")

    async def defaultFunction(self, message = None, file = None):
        channel = self.__message.channel
        permissions = channel.permissions_for(channel.guild.me)
        if permissions.send_messages:
            if message:
                await channel.send(message)
            elif file:
                if permissions.attach_files:
                    await channel.send(file=file)
                else:
                    await channel.send( "**Avalon-bot** no dispone "\
                                        "de permisos para enviar "\
                                        "archivos por el canal "\
                                       f"**{channel.name}**.")
        else:
            print( "-> Avalon-bot no dispone de permisos para "\
                  f"enviar mensajes por el canal '{channel.name}'.")

    async def testFunction(self, message = None, file = None):
        if message:
            print(f"Enviando mensaje a Discord: {message}")
        elif file:
            print(f"Enviando archivo a Discord: {file}")