import sys
import discord
sys.path.insert(1, './DF')
from dataframe import DataFrame

class MessageHandler:
    def __init__(self, message, client):
        self.__message = message
        self.__client = client

    async def inMsg(self):
        if self.__message.author == self.__client.user:
            return

    async def helpMsg(self, command):
        if self.__message.content.startswith(f'${command}'):
            message = (
                "**Lista de comandos:** \n"\
                "- **listAssist:all** -> Genera una excel con todas las _asistencias_ "\
                "registradas en la base de datos.\n"\
                "- **listAssist:id [_ID_]** -> Genera una excel con la _asistencia_ "\
                "registrada en la base de datos, asociada con un identificador unico **_ID_** , "\
                "ingresado como parametro dentro de los corchetes **[ ]**. "\
                "Este parametro **_ID_** debe corresponder a un valor numerico.\n"
                "- **listAssist:idmember [_Integrante ID_]** -> Genera una excel con todas las _asistencias_ "\
                "registradas en la base de datos, asociadas con un identificador unico **_Integrante ID_** "\
                "ingresado como parametro dentro de los corchetes **[ ]**, "\
                "en relacion con el _integrante_ que estuvo presente en la _asistencia_. "\
                "Este parametro **_Integrante ID_** debe corresponder a un valor numerico.\n"


            )
            await self.__message.channel.send(message)

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