import sys
sys.path.insert(1, './Config')
from config import Config
sys.path.insert(1, './Helpers')
from appHandler import AppHandler
from helpers import Helpers
from messageHandler import MessageHandler
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
    handler = MessageHandler(message, client)
    await handler.initialMessage()
    await handler.textMessage("comando", "Hola mundo desde el bot de discord.")
    await handler.dataFrameMessage("lista_integrantes", app.getIntegrantes)
    await handler.dataFrameMessage("lista_eventos", app.getEventos)
    await handler.dataFrameMessage("lista_participaciones", app.getParticipaciones)
    await handler.dataFrameMessage("lista_rangos", app.getRangos)
    await handler.dataFrameMessage("buscar_nombre_integrantes", app.getIntegrantes, Helpers.strTemp(["date_1", "date_2"]))
    await handler.dataFrameMessage("buscar_rango_integrantes", app.getIntegrantes, Helpers.strTemp(["rango"]))
    await handler.addContentMessage("add_integrante", app.setIntegrante)

client.run(Config.TOKEN)