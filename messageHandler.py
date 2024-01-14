import sys
sys.path.insert(1, './DF')
from dataframe import DataFrame
import discord

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

    async def dFMsg(self, command, method, struct = None):
        if self.__message.content.startswith(f'${command}'):
            request = self.__message.content.replace(f'${command}', '').strip()
            request = f"${command} {request}"
            result = method(request, struct)
            if isinstance(result, list):
                df = DataFrame(command, result)
                if df.getSuccess():
                    discordFile = discord.File(df.getDirectory())
                    await self.__message.channel.send(file=discordFile)
                    if not df.deleteFrame():
                        await self.__message.channel.send('Error al intentar eliminar el dataframe, por favor informe al administrador.')
                else:
                    await self.__message.channel.send('Error al intentar crear el dataframe, por favor informe al administrador.')
            elif isinstance(result, str):
                await self.__message.channel.send(result)
            else:
                await self.__message.channel.send('Error al consultar la base de datos, por favor informe al administrador.')

    async def contMsg(self, command, method):
        if self.__message.content.startswith(f'${command}'):
            request = self.__message.content.replace(f'${command}', '').strip()
            request = f"${command} {request}"
            result = method(request)
            await self.__message.channel.send(result)