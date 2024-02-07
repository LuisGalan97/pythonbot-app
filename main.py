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
    await hdlr.sendText()
    await hdlr.helpMsg()
    #------------------------------Asistencias---------------------------------
    await hdlr.contMsg("addAssist", app.setData,
                       Helpers.setStruct("assist"))
    await hdlr.contMsg("updAssist:id", app.updateData,
                       Helpers.updStruct("assist", "id"))
    await hdlr.contMsg("delAssist:id", app.deleteData,
                       Helpers.delStruct("assist", "id"))
    await hdlr.dFMsg("listAssist", app.getDatas,
                     Helpers.getStruct("assist"))
    await hdlr.dFMsg("listAssist:id", app.getDatas,
                     Helpers.getStruct("assist", ["id"]))
    await hdlr.dFMsg("listAssist:member", app.getDatas,
                     Helpers.getStruct("assist", ["member"]))
    await hdlr.dFMsg("listAssist:event", app.getDatas,
                     Helpers.getStruct("assist", ["event"]))
    await hdlr.dFMsg("listAssist:date", app.getDatas,
                     Helpers.getStruct("assist", ["date_1", "date_2"]))
    await hdlr.dFMsg("listAssist:member&event", app.getDatas,
                     Helpers.getStruct("assist", ["member", "event"]))
    await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                     Helpers.getStruct("assist",
                                       ["member", "date_1", "date_2"]))
    await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                     Helpers.getStruct("assist",
                                       ["event", "date_1", "date_2"]))
    await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                     Helpers.getStruct("assist",
                                       ["member", "event",
                                        "date_1", "date_2"]))
    await hdlr.scan("scan")
    #--------------------------------Eventos-----------------------------------
    await hdlr.contMsg("addEvent", app.setData,
                       Helpers.setStruct("event"))
    await hdlr.contMsg("updEvent:id", app.updateData,
                       Helpers.updStruct("event", "id"))
    await hdlr.contMsg("updEvent:name", app.updateData,
                       Helpers.updStruct("event", "name"))
    await hdlr.contMsg("delEvent:id", app.deleteData,
                       Helpers.delStruct("event", "id"))
    await hdlr.contMsg("delEvent:name", app.deleteData,
                       Helpers.delStruct("event", "name"))
    await hdlr.dFMsg("listEvent", app.getDatas,
                     Helpers.getStruct("event"))
    await hdlr.dFMsg("listEvent:id", app.getDatas,
                     Helpers.getStruct("event", ["id"]))
    await hdlr.dFMsg("listEvent:name", app.getDatas,
                     Helpers.getStruct("event", ["name"]))
    #-------------------------------Integrantes--------------------------------
    await hdlr.contMsg("addMember", app.setData,
                       Helpers.setStruct("member"))
    await hdlr.contMsg("updMember:id", app.updateData,
                       Helpers.updStruct("member", "id"))
    await hdlr.contMsg("updMember:name", app.updateData,
                       Helpers.updStruct("member", "name"))
    await hdlr.contMsg("delMember:id", app.deleteData,
                       Helpers.delStruct("member", "id"))
    await hdlr.contMsg("delMember:name", app.deleteData,
                       Helpers.delStruct("member", "name"))
    await hdlr.dFMsg("listMember", app.getDatas,
                     Helpers.getStruct("member"))
    await hdlr.dFMsg("listMember:id", app.getDatas,
                     Helpers.getStruct("member", ["id"]))
    await hdlr.dFMsg("listMember:name", app.getDatas,
                     Helpers.getStruct("member", ["name"]))
    await hdlr.dFMsg("listMember:range", app.getDatas,
                     Helpers.getStruct("member", ["range"]))
    await hdlr.dFMsg("listMember:date", app.getDatas,
                     Helpers.getStruct("member", ["date_1", "date_2"]))
    #----------------------------------Rangos----------------------------------
    await hdlr.contMsg("addRange", app.setData,
                       Helpers.setStruct("range"))
    await hdlr.contMsg("updRange:id", app.updateData,
                       Helpers.updStruct("range", "id"))
    await hdlr.contMsg("updRange:name", app.updateData,
                       Helpers.updStruct("range", "name"))
    await hdlr.contMsg("delRange:id", app.deleteData,
                       Helpers.delStruct("range", "id"))
    await hdlr.contMsg("delRange:name", app.deleteData,
                       Helpers.delStruct("range", "name"))
    await hdlr.dFMsg("listRange", app.getDatas,
                     Helpers.getStruct("range"))
    await hdlr.dFMsg("listRange:id", app.getDatas,
                     Helpers.getStruct("range", ["id"]))
    await hdlr.dFMsg("listRange:name", app.getDatas,
                     Helpers.getStruct("range", ["name"]))

client.run(Config.TOKEN)