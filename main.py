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
    await hdlr.helpMsg("help")
    await hdlr.dFMsg("listAssist:all", app.getDatas, Helpers.getStruct("asistencia"))
    await hdlr.dFMsg("listAssist:id", app.getDatas, Helpers.getStruct("asistencia", ["id"]))
    await hdlr.dFMsg("listAssist:idmember", app.getDatas, Helpers.getStruct("asistencia", ["integrante_id"]))
    await hdlr.dFMsg("listAssist:member", app.getDatas, Helpers.getStruct("asistencia", ["integrante"]))
    await hdlr.dFMsg("listAssist:idevent", app.getDatas, Helpers.getStruct("asistencia", ["evento_id"]))
    await hdlr.dFMsg("listAssist:event", app.getDatas, Helpers.getStruct("asistencia", ["evento"]))
    await hdlr.dFMsg("listAssist:date", app.getDatas, Helpers.getStruct("asistencia", ["date_1", "date_2"]))
    #await hdlr.dFMsg("listEventos:all", app.getDatas, Helpers.getStruct("evento"))
    #await hdlr.dFMsg("listIntegrantes:all", app.getDatas, Helpers.getStruct("integrante"))
    #await hdlr.dFMsg("listRangos:all", app.getDatas, Helpers.getStruct("rango"))
    
    #await hdlr.dFMsg("listEventos:name]", app.getDatas, Helpers.getStruct("evento", ["name"]))
    #await hdlr.dFMsg("listIntegrantes:name]", app.getDatas, Helpers.getStruct("integrante", ["name"]))
    #await hdlr.dFMsg("listRangos:name]", app.getDatas, Helpers.getStruct("integrante", ["name"]))

    #await hdlr.dFMsg("buscar_rango_integrantes", app.getDatas, Helpers.getStruct("integrante", ["rango"]))
    #await hdlr.contMsg("add_integrante", app.setData, Helpers.setStruct("integrante"))
    #await hdlr.contMsg("add_asistencia", app.setData, Helpers.setStruct("asistencia"))
    #await hdlr.contMsg("add_evento", app.setData, Helpers.setStruct("evento"))
    #await hdlr.contMsg("add_rango", app.setData, Helpers.setStruct("rango"))
    #await hdlr.contMsg("update_integrante", app.updateData, Helpers.updStruct("integrante", "name"))
    #await hdlr.contMsg("update_asistencia", app.updateData, Helpers.updStruct("asistencia", "id"))
    #await hdlr.contMsg("update_evento", app.updateData, Helpers.updStruct("evento", "name"))
    #await hdlr.contMsg("update_rango", app.updateData, Helpers.updStruct("rango", "name"))
    #await hdlr.contMsg("del_integrante", app.deleteData, Helpers.deleteStruct("integrante", "name"))
    #await hdlr.contMsg("del_asistencia", app.deleteData, Helpers.delStruct("asistencia", "id"))
    #await hdlr.contMsg("del_evento", app.deleteData, Helpers.delStruct("evento", "name"))
    #await hdlr.contMsg("del_rango", app.deleteData, Helpers.delStruct("rango", "name"))

client.run(Config.TOKEN)