# This example requires the 'message_content' intent.
import sys
import os
sys.path.insert(1, './Config')
from config import Config
sys.path.insert(1, './DF')
from dataframe import DataFrame
from appHandler import AppHandler
import discord

app = AppHandler()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$integrantes'):
        integrantes = app.getIntegrantes()
        if integrantes:
            df = DataFrame('Lista de integrantes', integrantes)
            if df.getSuccess():
                discordFile = discord.File(df.getDirectory())
                await message.channel.send(file=discordFile)
                if not df.deleteFrame():
                    await message.channel.send('Error al intentar eliminar el dataframe, por favor informe al administrador.')
            else:
                await message.channel.send('Error al intentar crear el dataframe, por favor informe al administrador.')
        else:
            await message.channel.send('Error al consultar la base de datos, por favor informe al administrador.')

    if message.content.startswith('$eventos'):
        eventos = app.getEventos()
        if eventos:
            df = DataFrame('Lista de eventos', eventos)
            if df.getSuccess():
                discordFile = discord.File(df.getDirectory())
                await message.channel.send(file=discordFile)
                if not df.deleteFrame():
                    await message.channel.send('Error al intentar eliminar el dataframe, por favor informe al administrador.')
            else:
                await message.channel.send('Error al intentar crear el dataframe, por favor informe al administrador.')
        else:
            await message.channel.send('Error al consultar la base de datos, por favor informe al administrador.')

    if message.content.startswith('$participaciones'):
        participaciones = app.getParticipaciones()
        if participaciones:
            df = DataFrame('Lista de participaciones', participaciones)
            if df.getSuccess():
                discordFile = discord.File(df.getDirectory())
                await message.channel.send(file=discordFile)
                if not df.deleteFrame():
                    await message.channel.send('Error al intentar eliminar el dataframe, por favor informe al administrador.')
            else:
                await message.channel.send('Error al intentar crear el dataframe, por favor informe al administrador.')
        else:
            await message.channel.send('Error al consultar la base de datos, por favor informe al administrador.')

    if message.content.startswith('$comando'):
        await message.channel.send('Respuesta del bot en discord')

client.run(Config.TOKEN)
#Este token es valido unicamente para el servidor Omega-xis