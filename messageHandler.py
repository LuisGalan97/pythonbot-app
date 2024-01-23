import os
dir = os.path.dirname(os.path.abspath(__file__))
import sys
import discord
sys.path.insert(1, f'{dir}/DF')
from dataframe import DataFrame
sys.path.insert(1, f'{dir}/Helpers')
from helpers import Helpers

class MessageHandler:
    def __init__(self, message, client):
        self.__message = message
        self.__client = client

    async def inMsg(self):
        if self.__message.author == self.__client.user:
            return

    async def helpMsg(self):
        msg = self.__message.content
        messages = []
        #messages.append("**Lista de comandos**\n")
        if msg.startswith("$help:assist"):
         #---------------------------------Asistencias----------------------------------------
            messages.append("**___Asistencias___**\n")
            messages.append("\n")
            messages.append("Las ___asistencias___ hacen referencia a una serie de registros de todas las participaciones, "\
            "en las cuales los integrantes de **⚜Avalon⚜** han podido hacer parte, "\
            "para actividades o eventos tales como ataques, defensas, AVAs, entre otros. Una ___asistencia___ "\
            "por defecto contiene informacion de un ___integrante___ y ___evento___ asociado, junto con la fecha del suceso en cuestion. "\
            "Con lo anterior, se presentan una lista de todos los comandos que permiten interactuar con los registros de ___asistencias___.\n")
            messages.append("\n")
            messages.append("_Comandos de modificacion:_\n")
            messages.append(f"{Helpers.genMsg('addAssist [Integrante, Evento, Fecha]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('updAssist:id [ID, Integrante, Evento, Fecha]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('delAssist:id [ID]', 'asistencia')}")
            messages.append("\n")
            messages.append("_Comandos de consulta:_\n")
            messages.append(f"{Helpers.genMsg('listAssist', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:id [ID]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:member [Integrante]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:event [Evento]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:date [Fecha 1, Fecha 2]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:member&event [Integrante, Evento]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:member&date [Integrante, Fecha 1, Fecha 2]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:event&date [Evento, Fecha 1, Fecha 2]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:member&event&date [Integrante, Evento, Fecha 1, Fecha 2]', 'asistencia')}")
            messages.append("\n")
            messages.append("_Comandos de consulta con impresion en excel:_\n")
            messages.append("Por defecto, los comandos de consulta imprimen los registros en el canal de discord, "\
            "sin embargo, tambien pueden ser impresos dentro de una hoja de excel, si despues del comando "\
            "se especifica el parametro **> e**.\n")
            messages.append(f"{Helpers.genMsg('listAssist > e', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:id [ID] > e', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:member [Integrante] > e', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:event [Evento] > e', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:date [Fecha 1, Fecha 2] > e', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:member&event [Integrante, Evento] > e', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:member&date [Integrante, Fecha 1, Fecha 2] > e', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:event&date [Evento, Fecha 1, Fecha 2] > e', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:member&event&date [Integrante, Evento, Fecha 1, Fecha 2] > e', 'asistencia')}")
        elif msg.startswith("$help:event"):
             #-----------------------------------Eventos----------------------------------------
            messages.append("**___Eventos___**\n")
            messages.append("\n")
            messages.append("Los ___eventos___ corresponden a una lista con informacion de las actividades "\
            "las cuales **⚜Avalon⚜** ha decidido puntuar, para poder recompensar a sus integrantes "\
            "por aporte y participacion, involucrando ataques, defensas, AVAs, entre otros.\n")
            messages.append("\n")
            messages.append("_Comandos de modificacion:_\n")
            messages.append(f"{Helpers.genMsg('addEvent [Nombre, Puntos, Descripción]', 'evento')}")
            messages.append(f"{Helpers.genMsg('updEvent:id [ID, Nombre, Puntos, Descripción]', 'evento')}")
            messages.append(f"{Helpers.genMsg('updEvent:name [Nombre, Puntos, Descripción]', 'evento')}")
            messages.append(f"{Helpers.genMsg('delEvent:id [ID]', 'evento')}")
            messages.append(f"{Helpers.genMsg('delEvent:name [Nombre]', 'evento')}")
            messages.append("\n")
            messages.append("_Comandos de consulta:_\n")
            messages.append(f"{Helpers.genMsg('listEvent', 'evento')}")
            messages.append(f"{Helpers.genMsg('listEvent:id [ID]', 'evento')}")
            messages.append(f"{Helpers.genMsg('listEvent:name [Nombre]', 'evento')}")
            messages.append("\n")
            messages.append("_Comandos de consulta con impresion en excel:_\n")
            messages.append("Por defecto, los comandos de consulta imprimen los registros en el canal de discord, "\
            "sin embargo, tambien pueden ser impresos dentro de una hoja de excel, si despues del comando "\
            "se especifica el parametro **> e**.\n")
            messages.append(f"{Helpers.genMsg('listEvent > e', 'evento')}")
            messages.append(f"{Helpers.genMsg('listEvent:id [ID] > e', 'evento')}")
            messages.append(f"{Helpers.genMsg('listEvent:name [Nombre] > e', 'evento')}")
        elif msg.startswith("$help:member"):
            #----------------------------------Integrantes----------------------------------------
            messages.append("**___Integrantes___**\n")
            messages.append("\n")
            messages.append("Los ___integrantes___ son una serie de registros en los cuales se encuentran "\
            "listados y referenciados todos los miembros de la alianza **⚜Avalon⚜**, junto con informacion "\
            "complementaria tales como el ___rango___ asignado y la fecha de ingreso de cada miembro.\n")
            messages.append("\n")
            messages.append("_Comandos de modificacion:_\n")
            messages.append(f"{Helpers.genMsg('addMember [Nombre, Rango, Fecha]', 'integrante')}")
            messages.append(f"{Helpers.genMsg('updMember:id [ID, Nombre, Rango, Fecha]', 'integrante')}")
            messages.append(f"{Helpers.genMsg('updMember:name [Nombre, Rango, Fecha]', 'integrante')}")
            messages.append(f"{Helpers.genMsg('delMember:id [ID]', 'integrante')}")
            messages.append(f"{Helpers.genMsg('delMember:name [Nombre]', 'integrante')}")
            messages.append("\n")
            messages.append("_Comandos de consulta:_\n")
            messages.append(f"{Helpers.genMsg('listMember', 'integrante')}")
            messages.append(f"{Helpers.genMsg('listMember:id [ID]', 'integrante')}")
            messages.append(f"{Helpers.genMsg('listMember:name [Nombre]', 'integrante')}")
            messages.append(f"{Helpers.genMsg('listMember:range [Rango]', 'integrante')}")
            messages.append(f"{Helpers.genMsg('listMember:date [Fecha 1, Fecha 2]', 'integrante')}")
            messages.append("\n")
            messages.append("_Comandos de consulta con impresion en excel:_\n")
            messages.append("Por defecto, los comandos de consulta imprimen los registros en el canal de discord, "\
            "sin embargo, tambien pueden ser impresos dentro de una hoja de excel, si despues del comando "\
            "se especifica el parametro **> e**.\n")
            messages.append(f"{Helpers.genMsg('listMember > e', 'integrante')}")
            messages.append(f"{Helpers.genMsg('listMember:id [ID] > e', 'integrante')}")
            messages.append(f"{Helpers.genMsg('listMember:name [Nombre] > e', 'integrante')}")
            messages.append(f"{Helpers.genMsg('listMember:range [Rango] > e', 'integrante')}")
            messages.append(f"{Helpers.genMsg('listMember:date [Fecha 1, Fecha 2] > e', 'integrante')}")
        elif msg.startswith("$help:range"):
            #-------------------------------------Rangos----------------------------------------
            messages.append("**_Rangos_**\n")
            messages.append("\n")
            messages.append("Las ___rangos___ disponen registros con informacion de los diferentes "\
            "rangos asignables a los integrante o miembros de la alianza **⚜Avalon⚜**.\n")
            messages.append("\n")
            messages.append("_Comandos de modificacion:_\n")
            messages.append(f"{Helpers.genMsg('addRange [Nombre, Control, Descripción]', 'rango')}")
            messages.append(f"{Helpers.genMsg('updRange:id [ID, Nombre, Control, Descripción]', 'rango')}")
            messages.append(f"{Helpers.genMsg('updRange:name [Nombre, Control, Descripción]', 'rango')}")
            messages.append(f"{Helpers.genMsg('delRange:id [ID]', 'rango')}")
            messages.append(f"{Helpers.genMsg('delRange:name [Nombre]', 'rango')}")
            messages.append("\n")
            messages.append("_Comandos de consulta:_\n")
            messages.append(f"{Helpers.genMsg('listRange', 'rango')}")
            messages.append(f"{Helpers.genMsg('listRange:id [ID]', 'rango')}")
            messages.append(f"{Helpers.genMsg('listRange:name [Nombre]', 'rango')}")
            messages.append("\n")
            messages.append("_Comandos de consulta con impresion en excel:_\n")
            messages.append("Por defecto, los comandos de consulta imprimen los registros en el canal de discord, "\
            "sin embargo, tambien pueden ser impresos dentro de una hoja de excel, si despues del comando "\
            "se especifica el parametro **> e**.\n")
            messages.append(f"{Helpers.genMsg('listRange > e', 'rango')}")
            messages.append(f"{Helpers.genMsg('listRange:id [ID] > e', 'rango')}")
            messages.append(f"{Helpers.genMsg('listRange:name [Nombre] > e', 'rango')}")
        elif msg.startswith("$help:diagram"):
            await self.__message.channel.send(f"**___Diagrama de la estructura de los datos:___**")
            discordFile = discord.File("./SQL/db_diagram.png")
            await self.__message.channel.send(file = discordFile)
        elif msg.startswith("$help"):
            messages.append("**___Guia de usuario de Avalon-bot___**\n")
            messages.append("\n")
            messages.append("Bienvenido/a a la guia de usuario del bot de **⚜Avalon⚜** "\
                            "para discord. En esta seccion realizaremos una breve introduccion, "\
                            "de las funciones principales que dispone **_Avalon-bot_**, "\
                            "la estructura de la informacion con la que trabaja, y como podemos "\
                            "utilizarlo para obtener importantes beneficios, "\
                            "en el manejo y gestion de los datos asociados con la alianza.\n")
            messages.append("\n")
            messages.append("**_¿Que es Avalon-bot?_**\n")
            messages.append("**_Avalon-bot_** es una herramienta pensada y diseñada para facilitar al usuario la gestion "\
                            "de los datos asociados con la alianza **⚜Avalon⚜**, mediante la comprension "\
                            "de la estructura de la informacion planteada para este proposito, y la correcta "\
                            "utilizacion de los comandos dispuestos para poder acceder y manipular dicha informacion. "\
                            "Dicho esto, con Avalon-bot podras generar un seguimiento automatizado y estructurado, "\
                            "de datos relacionados con los ___integrantes___, las ___asistencias___, los ___rangos___, "\
                            "y los ___eventos___ establecidos en la alianza, en conjunto con la capacidad de generar "\
                            "informes personalizados en excel, gracias a la implementacion de bases de datos SQL.\n")
            messages.append("\n")
            messages.append("**_¿Como se encuentra estructurada la informacion?_**\n")
            messages.append("Para la organizacion, gestion y guardado de la informacion, **_Avalon-bot_** tiene programada "\
                            "la interaccion con una base de datos SQLite en lenguaje python, "\
                            "teniendo acceso a un gestor de base de datos ligero, donde se encuentra cargada una estructura "\
                            "de 4 tablas relacionadas entre si, pensadas para almacenar la informacion de 4 datos principales: "\
                            "___integrantes___, ___asistencias___, ___rangos___ y ___eventos___, con el fin de permitir la disposicion "\
                            "de por ejemplo una tabla de ___rangos___ de alianza, que posteriormente podra ser relacionada "\
                            "a un ___integrante___ de la tabla de ___integrantes___, conservando la independencia de ambas tablas con sus datos propios y "\
                            "facilitando de esta forma su manipulacion. De forma similar la tabla ___eventos___ e ___integrantes___ "\
                            "pueden relacionarse o asociarse con la tabla asistencias, con el fin de registrar, que en una ___asistencia___ "\
                            "estuvo presente un ___integrante___ y fue con respecto a un ___evento___ especifico, registrado en su tabla de forma "\
                            "independiente.\n\n_Si desea visualizar el diagrama de la estructura de los datos, puede emplear el comando de ayuda:_\n"\
                            "* **$help:diagram**\n")
            messages.append("\n")
            messages.append("**_¿Como puedo empezar a utilizar Avalon-bot?_**\n")
            messages.append("Para poder utilizar **_Avalon-bot_**, debes emplear los comandos dispuestos por este mismo, "\
                            "los cuales varian dependiendo de la tabla con la que deseas interactuar, y el tipo de solicitud "\
                            "que deseas realizar (consulta, creacion, actualizacion o eliminacion). "\
                            "Con lo anterior, dada la extension de los comandos, estos se han especificado y detallado en su propia seccion "\
                            "asociada con cada tabla respectiva, siendo visibles mediante los comandos de ayuda que se presentan a continuacion.\n\n"\
                            "_Comandos de_ ___asistencias___:\n"\
                            "** * $help:assist**\n"\
                            "_Comandos de_ ___eventos___: \n"\
                            "** * $help:event**\n"\
                            "_Comandos de_ ___integrantes___: \n"\
                            "** * $help:member**\n"\
                            "_Comandos de_ ___rangos___: \n"\
                            "** * $help:range**")
        if messages:
            array = []
            length = 0
            for i in range(len(messages)):
                length = length + len(messages[i])
                if length >= 2000:
                    await self.__message.channel.send(''.join(array))
                    array = []
                    length = len(messages[i])
                    array.append(messages[i])
                    if i == len(messages) - 1:
                        await self.__message.channel.send(''.join(array))
                elif i == len(messages) - 1:
                    array.append(messages[i])
                    await self.__message.channel.send(''.join(array))
                else:
                    array.append(messages[i])

    async def dFMsg(self, command, method, struct):
        msg = self.__message.content
        if msg.find(':') != -1 and command.find(':') != -1 and msg.startswith(f"${command}"):
            if msg.find('&') != -1 and command.find('&') != -1 and msg.startswith(f"${command}"):
                msgpos = msg.find('&') + 1
                cmdpos = command.find('&') + 1
                if msg.find('&', msgpos) != -1 and command.find('&', cmdpos) != -1 and msg.startswith(f"${command}"):
                    msg = True
                elif not msg.startswith(f"${command}&") and command.find('&', cmdpos) == -1 and msg.startswith(f"${command}"):
                    msg = True
                else:
                    msg = False
            elif not msg.startswith(f"${command}&") and command.find('&') == -1 and msg.startswith(f"${command}"):
                msg = True
            else:
                msg = False
        elif not msg.startswith(f"${command}:") and command.find(':') == -1 and msg.startswith(f"${command}"):
            msg = True
        else:
            msg = False
        if msg:
            content = self.__message.content.replace(f'${command}', '').strip()
            request = f"${command} {content}"
            result = method(request, struct)
            if isinstance(result, list):
                if request.find('>') != -1:
                    excelreq = content.lower()
                    excelreq = excelreq[excelreq.find(']')+1:]
                    excelreq = excelreq[:excelreq.find('e')+2].replace(' ','')
                    if excelreq == ">e":
                        strContent = content[content.find('[')+1:content.find(']')].split(",")
                        strContent = "_".join(data.strip() for data in strContent)
                        if command.find(':') != -1:
                            fileName = f"{command.split(':')[0]}{command.split(':')[1].capitalize()}{strContent}"
                        else:
                            fileName = f"{command}{strContent}"
                        df = DataFrame(fileName, result)
                        if df.getSuccess():
                            discordFile = discord.File(df.getDirectory())
                            await self.__message.channel.send(f"**___{list(struct['controller'].keys())[0].capitalize()}s___** "\
                                                              f"**___encontrad{'a' if list(struct['controller'].keys())[0][0] == 'a' else 'o'}s:___**")
                            await self.__message.channel.send(file=discordFile)
                            if not df.deleteFrame():
                                await self.__message.channel.send("Error al intentar eliminar el excel, "\
                                                                  "por favor consulte con el administrador.")
                        else:
                            await self.__message.channel.send("Error al intentar crear el excel, "\
                                                              "por favor consulte con el administrador.")
                    else:
                        parameters = f"**[**{content[content.find('[')+1:content.find(']')]}**]** "
                        await self.__message.channel.send("Se ha detectado el uso del operador **>** despues del comando "\
                                                          "inicial, si desea obtener los datos en un archivo de excel, "\
                                                          "debe completar el comando ingresadolo de la siguiente forma:\n"\
                                                         f"$**{command}** {parameters if command.find(':') != -1 else ''} **> e**")
                else:
                    array = []
                    title = f"**___{list(struct['controller'].keys())[0].capitalize()}s___** "\
                            f"**___encontrad{'a' if list(struct['controller'].keys())[0][0] == 'a' else 'o'}s:___**"
                    length = len(title)
                    array.append(title)
                    for i in range(len(result)):
                        tempdict = f"* {', '.join([f'**_{key}_** : _{value}_' for key, value in result[i].items()])}"
                        length = length + len(tempdict) + 1
                        if length >= 2000:
                            await self.__message.channel.send('\n'.join(array))
                            array = []
                            length = len(tempdict) + 1
                            array.append(tempdict)
                            if i == len(result) - 1:
                                await self.__message.channel.send('\n'.join(array))
                        elif i == len(result) - 1:
                            array.append(tempdict)
                            await self.__message.channel.send('\n'.join(array))
                        else:
                            array.append(tempdict)

            elif isinstance(result, str):
                await self.__message.channel.send(result)
            else:
                await self.__message.channel.send("Error en la base de datos, "\
                                                  "por favor consulte con el administrador.")

    async def contMsg(self, command, method, struct):
        msg = self.__message.content
        if msg.find(':') != -1 and command.find(':') != -1 and msg.startswith(f"${command}"):
            msg = True
        elif not msg.startswith(f"${command}:") and command.find(':') == -1 and msg.startswith(f"${command}"):
            msg = True
        else:
            msg = False
        if msg:
            request = self.__message.content.replace(f'${command}', '').strip()
            request = f"${command} {request}"
            result = method(request, struct)
            if result:
                await self.__message.channel.send(result)
            else:
                await self.__message.channel.send("Error en la base de datos, "\
                                                  "por favor consulte con el administrador.")