import sys
sys.path.insert(1, './DF')
from dataframe import DataFrame
import discord

class MessageHandler:
    def __init__(self, message, client):
        self.__message = message
        self.__client = client
    
    async def initialMessage(self):
        if self.__message.author == self.__client.user:
            return
    
    async def textMessage(self, command, message):
        if self.__message.content.startswith(f'${command}'):
            await self.__message.channel.send(message)
    
    async def dataFrameMessage(self, command, method):
        if self.__message.content.startswith(f'${command}'):
            datas = method()
            if datas:
                df = DataFrame(command, datas)
                if df.getSuccess():
                    discordFile = discord.File(df.getDirectory())
                    await self.__message.channel.send(file=discordFile)
                    if not df.deleteFrame():
                        await self.__message.channel.send('Error al intentar eliminar el dataframe, por favor informe al administrador.')
                else:
                    await self.__message.channel.send('Error al intentar crear el dataframe, por favor informe al administrador.')
            else:
                await self.__message.channel.send('Error al consultar la base de datos, por favor informe al administrador.')


    
