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

    async def txtMsg(self, command, message):
        if self.__message.content.startswith(f'${command}'):
            await self.__message.channel.send(message)

    async def dFMsg(self, command, method, struct):
        if self.__message.content.startswith(f'${command}'):
            content = self.__message.content.replace(f'${command}', '').strip()
            request = f"${command} {content}"
            result = method(request, struct)
            if isinstance(result, list):
                strContent = content.strip("[]").split(",")
                strContent = "_".join(data.strip() for data in strContent)
                fileName = f"{command.split(':')[0]}{command.split(':')[1].capitalize()}_{strContent}"
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