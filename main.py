import sys
import discord
sys.path.insert(1, './Config')
from config import Config
from appHandler import AppHandler
from messageHandler import MessageHandler
sys.path.insert(1, './Helpers')
from helpers import Helpers

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
    await hdlr.dFMsg("lista_integrantes", app.getDatas, Helpers.getStruct("integrante"))
    await hdlr.dFMsg("lista_eventos", app.getDatas, Helpers.getStruct("evento"))
    await hdlr.dFMsg("lista_asistencias", app.getDatas, Helpers.getStruct("asistencia"))
    await hdlr.dFMsg("lista_rangos", app.getDatas, Helpers.getStruct("rango"))
    await hdlr.dFMsg("buscar_nombre_integrantes", app.getDatas, Helpers.getStruct("integrante", ["name"]))
    await hdlr.dFMsg("buscar_rango_integrantes", app.getDatas, Helpers.getStruct("integrante", ["rango"]))
    await hdlr.contMsg("add_integrante", app.setData, Helpers.setStruct("integrante"))
    await hdlr.contMsg("add_asistencia", app.setData, Helpers.setStruct("asistencia"))
    await hdlr.contMsg("add_evento", app.setData, Helpers.setStruct("evento"))
    await hdlr.contMsg("add_rango", app.setData, Helpers.setStruct("rango"))
    await hdlr.contMsg("update_integrante", app.updateData, Helpers.updStruct("integrante", "name"))
    await hdlr.contMsg("update_asistencia", app.updateData, Helpers.updStruct("asistencia", "id"))
    await hdlr.contMsg("update_evento", app.updateData, Helpers.updStruct("evento", "name"))
    await hdlr.contMsg("update_rango", app.updateData, Helpers.updStruct("rango", "name"))
    await hdlr.contMsg("del_integrante", app.deleteData, Helpers.deleteStruct("integrante", "name"))
    await hdlr.contMsg("del_asistencia", app.deleteData, Helpers.delStruct("asistencia", "id"))
    await hdlr.contMsg("del_evento", app.deleteData, Helpers.delStruct("evento", "name"))
    await hdlr.contMsg("del_rango", app.deleteData, Helpers.delStruct("rango", "name"))

client.run(Config.TOKEN)