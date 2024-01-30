import discord
from appHandler import AppHandler
from Config.config import Config
from Helpers.helpers import Helpers
from messageHandler import MessageHandler

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
    await hdlr.helpMsg()
    #------------------------------Asistencias---------------------------------
    await hdlr.contMsg("addAssist", app.setData,
                       Helpers.setStruct("asistencia"))
    await hdlr.contMsg("updAssist:id", app.updateData,
                       Helpers.updStruct("asistencia", "id"))
    await hdlr.contMsg("delAssist:id", app.deleteData,
                       Helpers.delStruct("asistencia", "id"))
    await hdlr.dFMsg("listAssist", app.getDatas,
                     Helpers.getStruct("asistencia"))
    await hdlr.dFMsg("listAssist:id", app.getDatas,
                     Helpers.getStruct("asistencia", ["id"]))
    await hdlr.dFMsg("listAssist:member", app.getDatas,
                     Helpers.getStruct("asistencia", ["integrante"]))
    await hdlr.dFMsg("listAssist:event", app.getDatas,
                     Helpers.getStruct("asistencia", ["evento"]))
    await hdlr.dFMsg("listAssist:date", app.getDatas,
                     Helpers.getStruct("asistencia", ["date_1", "date_2"]))
    await hdlr.dFMsg("listAssist:member&event", app.getDatas,
                     Helpers.getStruct("asistencia", ["integrante", "evento"]))
    await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                     Helpers.getStruct("asistencia",
                                       ["integrante", "date_1", "date_2"]))
    await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                     Helpers.getStruct("asistencia",
                                       ["evento", "date_1", "date_2"]))
    await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                     Helpers.getStruct("asistencia",
                                       ["integrante", "evento",
                                        "date_1", "date_2"]))
    #--------------------------------Eventos-----------------------------------
    await hdlr.contMsg("addEvent", app.setData,
                       Helpers.setStruct("evento"))
    await hdlr.contMsg("updEvent:id", app.updateData,
                       Helpers.updStruct("evento", "id"))
    await hdlr.contMsg("updEvent:name", app.updateData,
                       Helpers.updStruct("evento", "name"))
    await hdlr.contMsg("delEvent:id", app.deleteData,
                       Helpers.delStruct("evento", "id"))
    await hdlr.contMsg("delEvent:name", app.deleteData,
                       Helpers.delStruct("evento", "name"))
    await hdlr.dFMsg("listEvent", app.getDatas,
                     Helpers.getStruct("evento"))
    await hdlr.dFMsg("listEvent:id", app.getDatas,
                     Helpers.getStruct("evento", ["id"]))
    await hdlr.dFMsg("listEvent:name", app.getDatas,
                     Helpers.getStruct("evento", ["name"]))
    #-------------------------------Integrantes--------------------------------
    await hdlr.contMsg("addMember", app.setData,
                       Helpers.setStruct("integrante"))
    await hdlr.contMsg("updMember:id", app.updateData,
                       Helpers.updStruct("integrante", "id"))
    await hdlr.contMsg("updMember:name", app.updateData,
                       Helpers.updStruct("integrante", "name"))
    await hdlr.contMsg("delMember:id", app.deleteData,
                       Helpers.delStruct("integrante", "id"))
    await hdlr.contMsg("delMember:name", app.deleteData,
                       Helpers.delStruct("integrante", "name"))
    await hdlr.dFMsg("listMember", app.getDatas,
                     Helpers.getStruct("integrante"))
    await hdlr.dFMsg("listMember:id", app.getDatas,
                     Helpers.getStruct("integrante", ["id"]))
    await hdlr.dFMsg("listMember:name", app.getDatas,
                     Helpers.getStruct("integrante", ["name"]))
    await hdlr.dFMsg("listMember:range", app.getDatas,
                     Helpers.getStruct("integrante", ["rango"]))
    await hdlr.dFMsg("listMember:date", app.getDatas,
                     Helpers.getStruct("integrante", ["date_1", "date_2"]))
    #----------------------------------Rangos----------------------------------
    await hdlr.contMsg("addRange", app.setData,
                       Helpers.setStruct("rango"))
    await hdlr.contMsg("updRange:id", app.updateData,
                       Helpers.updStruct("rango", "id"))
    await hdlr.contMsg("updRange:name", app.updateData,
                       Helpers.updStruct("rango", "name"))
    await hdlr.contMsg("delRange:id", app.deleteData,
                       Helpers.delStruct("rango", "id"))
    await hdlr.contMsg("delRange:name", app.deleteData,
                       Helpers.delStruct("rango", "name"))
    await hdlr.dFMsg("listRange", app.getDatas,
                     Helpers.getStruct("rango"))
    await hdlr.dFMsg("listRange:id", app.getDatas,
                     Helpers.getStruct("rango", ["id"]))
    await hdlr.dFMsg("listRange:name", app.getDatas,
                     Helpers.getStruct("rango", ["name"]))

client.run(Config.TOKEN)