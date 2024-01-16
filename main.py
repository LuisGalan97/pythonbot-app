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
    await hdlr.dFMsg("lista_integrantes", app.getDatas, Helpers.setStruct("integrante"))
    await hdlr.dFMsg("lista_eventos", app.getDatas, Helpers.setStruct("evento"))
    await hdlr.dFMsg("lista_asistencias", app.getDatas, Helpers.setStruct("asistencia"))
    await hdlr.dFMsg("lista_rangos", app.getDatas, Helpers.setStruct("rango"))
    await hdlr.dFMsg("buscar_nombre_integrantes", app.getDatas, Helpers.setStruct("integrante", ["name"]))
    await hdlr.dFMsg("buscar_rango_integrantes", app.getDatas, Helpers.setStruct("integrante", ["rango"]))
    await hdlr.contMsg("add_integrante", app.setData, Helpers.getStruct("integrante"))
    await hdlr.contMsg("add_asistencia", app.setData, Helpers.getStruct("asistencia"))
    await hdlr.contMsg("add_evento", app.setData, Helpers.getStruct("evento"))
    await hdlr.contMsg("add_rango", app.setData, Helpers.getStruct("rango"))
    await hdlr.contMsg("update_integrante", app.updateData, Helpers.getStruct("integrante"))
    await hdlr.contMsg("update_asistencia", app.updateData, Helpers.getStruct("asistencia"))
    await hdlr.contMsg("update_evento", app.updateData, Helpers.getStruct("evento"))
    await hdlr.contMsg("update_rango", app.updateData, Helpers.getStruct("rango"))
    

client.run(Config.TOKEN)