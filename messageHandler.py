import sys
import discord
sys.path.insert(1, './DF')
from dataframe import DataFrame
sys.path.insert(1, './Helpers')
from helpers import Helpers

class MessageHandler:
    def __init__(self, message, client):
        self.__message = message
        self.__client = client

    async def inMsg(self):
        if self.__message.author == self.__client.user:
            return

    async def helpMsg(self, command):
        if self.__message.content.startswith(f'${command}'):
            messages = []
            messages.append("**Lista de comandos**\n")
            messages.append("**_Asistencias:_**\n")
            messages.append("Las asistencias hacen referencia a una serie de registros de todas las participaciones, "\
            "en las cuales los integrantes de ⚜Avalon⚜ han podido hacer parte, "\
            "para actividades o eventos tales como ataques, defensas, AVAs, entre otros. Por tanto una asistencia "\
            "por defecto contiene informacion de un integrante y evento asociado, junto con la fecha del suceso en cuestion\n")
            messages.append(f"{Helpers.genMsg('addAssist:default [Nombre, Integrante, Evento, Fecha]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('updAssist:id [ID, Nombre, Integrante, Evento, Fecha]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('delAssist:id [ID]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:all', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:id [ID]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:idmember [Integrante ID]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:member [Integrante]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:idevent [Evento ID]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:event [Evento]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:date [Fecha 1, Fecha 2]', 'asistencia')}")
            messages.append("**_Eventos:_**\n")
            messages.append("Las eventos corresponden a una lista con informacion de las actividades "\
            "que ⚜Avalon⚜ ha decidido puntuar para poder premiar a sus integrantes, "\
            "por aporte y participacion, involucrando ataques, defensas, AVAs, entre otros.\n")
            messages.append(f"{Helpers.genMsg('addEvent:default [Nombre, Puntos, Descripción]', 'evento')}")
            messages.append(f"{Helpers.genMsg('updEvent:id [ID, Nombre, Puntos, Descripción]', 'evento')}")
            messages.append(f"{Helpers.genMsg('updEvent:name [Nombre, Puntos, Descripción]', 'evento')}")
            messages.append(f"{Helpers.genMsg('delEvent:id [ID]', 'evento')}")
            messages.append(f"{Helpers.genMsg('delEvent:name [Nombre]', 'evento')}")
            messages.append(f"{Helpers.genMsg('listEvent:all', 'evento')}")
            messages.append(f"{Helpers.genMsg('listEvent:id [ID]', 'evento')}")
            messages.append(f"{Helpers.genMsg('listEvent:name [Nombre]', 'evento')}")
            messages.append("**_Integrantes:_**\n")
            messages.append("Los integrantes son una serie de registros en los cuales se encuentran "\
            "listados y referenciados todos los miembros de la alianza ⚜Avalon⚜, junto con informacion "\
            "complementaria tales como un rango asignado y la fecha de ingreso.\n")
            messages.append(f"{Helpers.genMsg('addMember:default [Nombre, Rango, Fecha]', 'integrante')}")
            messages.append(f"{Helpers.genMsg('updMember:id [ID, Nombre, Rango, Fecha]', 'integrante')}")
            messages.append(f"{Helpers.genMsg('updMember:name [Nombre, Rango, Fecha]', 'integrante')}")
            messages.append(f"{Helpers.genMsg('delMember:id [ID]', 'integrante')}")
            messages.append(f"{Helpers.genMsg('delMember:name [Nombre]', 'integrante')}")
            messages.append(f"{Helpers.genMsg('listMember:all', 'integrante')}")
            messages.append(f"{Helpers.genMsg('listMember:id [ID]', 'integrante')}")
            messages.append(f"{Helpers.genMsg('listMember:name [Nombre]', 'integrante')}")
            messages.append(f"{Helpers.genMsg('listMember:idrange [Rango ID]', 'integrante')}")
            messages.append(f"{Helpers.genMsg('listMember:range [Rango]', 'integrante')}")
            messages.append(f"{Helpers.genMsg('listMember:date [Fecha 1, Fecha 2]', 'integrante')}")
            messages.append("**_Rangos:_**\n")
            messages.append("Las rangos disponen registros con informacion de los diferentes "\
            "rangos asignables a los integrante o miembros de la alianza ⚜Avalon⚜.\n")
            messages.append(f"{Helpers.genMsg('addRange:default [Nombre, Descripción]', 'rango')}")
            messages.append(f"{Helpers.genMsg('updRange:id [ID, Nombre, Descripción]', 'rango')}")
            messages.append(f"{Helpers.genMsg('updRange:name [Nombre, Descripción]', 'rango')}")
            messages.append(f"{Helpers.genMsg('delRange:id [ID]', 'rango')}")
            messages.append(f"{Helpers.genMsg('delRange:name [Nombre]', 'rango')}")
            messages.append(f"{Helpers.genMsg('listRange:all', 'rango')}")
            messages.append(f"{Helpers.genMsg('listRange:id [ID]', 'rango')}")
            messages.append(f"{Helpers.genMsg('listRange:name [Nombre]', 'rango')}")
            array = []  
            for i in range(len(messages)):  
                array.append(messages[i])
                if i == 0:
                    await self.__message.channel.send(''.join(array))
                    array = [] 
                if len(array) == 4: 
                    await self.__message.channel.send(''.join(array))
                    array = []
                elif i == len(messages) - 1:
                    await self.__message.channel.send(''.join(array))
                    array = []

    async def dFMsg(self, command, method, struct):
        if self.__message.content.startswith(f'${command}'):
            content = self.__message.content.replace(f'${command}', '').strip()
            request = f"${command} {content}"
            result = method(request, struct)
            if isinstance(result, list):
                strContent = content.strip("[]").split(",")
                strContent = "_".join(data.strip() for data in strContent)
                fileName = f"{command.split(':')[0]}{command.split(':')[1].capitalize()}{strContent}"
                df = DataFrame(fileName, result)
                if df.getSuccess():
                    discordFile = discord.File(df.getDirectory())
                    await self.__message.channel.send(file=discordFile)
                    if not df.deleteFrame():
                        await self.__message.channel.send('Error al intentar eliminar el excel, por favor consulte con el administrador.')
                else:
                    await self.__message.channel.send('Error al intentar crear el excel, por favor consulte con el administrador.')
            elif isinstance(result, str):
                await self.__message.channel.send(result)
            else:
                await self.__message.channel.send('Error en la base de datos, por favor consulte con el administrador.')

    async def contMsg(self, command, method, struct):
        if self.__message.content.startswith(f'${command}'):
            request = self.__message.content.replace(f'${command}', '').strip()
            request = f"${command} {request}"
            result = method(request, struct)
            if result:
                await self.__message.channel.send(result)
            else:
                await self.__message.channel.send('Error en la base de datos, por favor consulte con el administrador.')