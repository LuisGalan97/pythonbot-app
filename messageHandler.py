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
            messages.append("**_Tabla de Asistencias:_**\n")
            messages.append(f"{Helpers.genMsg('listAssist:all', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:id [ID]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:idmember [Integrante ID]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:member [Integrante]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:idevent [Evento ID]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:event [Evento]', 'asistencia')}")
            messages.append(f"{Helpers.genMsg('listAssist:date [Fecha 1, Fecha 2]', 'asistencia')}")
            messages.append("**_Tabla de Eventos:_**\n")
            messages.append(f"{Helpers.genMsg('listEvent:all', 'evento')}")
            messages.append(f"{Helpers.genMsg('listEvent:id [ID]', 'evento')}")
            messages.append(f"{Helpers.genMsg('listEvent:name [Nombre]', 'evento')}")
            messages.append("**_Tabla de Integrantes:_**\n")
            messages.append(f"{Helpers.genMsg('listMember:all', 'integrante')}")
            messages.append(f"{Helpers.genMsg('listMember:id [ID]', 'integrante')}")
            messages.append(f"{Helpers.genMsg('listMember:name [Nombre]', 'integrante')}")
            messages.append(f"{Helpers.genMsg('listMember:idrange [Rango ID]', 'integrante')}")
            messages.append(f"{Helpers.genMsg('listMember:range [Rango]', 'integrante')}")
            messages.append(f"{Helpers.genMsg('listMember:date [Fecha 1, Fecha 2]', 'integrante')}")
            messages.append("**_Tabla de Rangos:_**\n")
            messages.append(f"{Helpers.genMsg('listRange:all', 'rango')}")
            messages.append(f"{Helpers.genMsg('listRange:id [ID]', 'rango')}")
            messages.append(f"{Helpers.genMsg('listRange:name [Nombre]', 'rango')}")
            array = []  
            for i in range(len(messages)):  
                array.append(messages[i])
                if i == 0:
                    await self.__message.channel.send(''.join(array))
                    array = [] 
                if len(array) == 6: 
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