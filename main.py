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
    hdlr = MessageHandler(message, client)
    await hdlr.inMsg()
    await hdlr.txtMsg("comando", "Hola mundo desde el bot de discord.")
    await hdlr.dFMsg("lista_integrantes", app.getIntegrantes)
    await hdlr.dFMsg("lista_eventos", app.getEventos)
    await hdlr.dFMsg("lista_participaciones", app.getParticipaciones)
    await hdlr.dFMsg("lista_rangos", app.getRangos)
    await hdlr.dFMsg("buscar_nombre_integrantes", app.getIntegrantes, Helpers.strTemp(["date_1", "date_2"]))
    await hdlr.dFMsg("buscar_rango_integrantes", app.getIntegrantes, Helpers.strTemp(["rango"]))
    await hdlr.contMsg("add_integrante", app.setIntegrante)

client.run(Config.TOKEN)