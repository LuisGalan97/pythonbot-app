import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Helpers.helpers import Helpers
from collections import namedtuple

Message = namedtuple('Message', ['author', 'content'])
Client = namedtuple('Client', ['user'])
author = "test"
user = "test"
app = AppHandler()

@pytest.mark.asyncio
async def testRangeStruct_addRange_invalidStruct(capfd):
    commands = ["$addRange", "$addRange ",
                "$addRange[", "$addRange [",
                "$addRangeFILL[", "$addRange]",
                "$addRange ]", "$addRangeFILL []",
                "$addRange FILL []", "$addRange [FILL",
                "$addRange[FILL", "$addRange [ FILL",
                "$addRange FILL]", "$addRange FILL ] "]
    for command in commands:
        message = Message(author=author, content=command)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addRange", app.setData,
                           Helpers.setStruct("range"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$addRange [_Nombre, Control, Descripción_]**\n" in out

@pytest.mark.asyncio
async def testRangeStruct_updRangeId_invalidStruct(capfd):
    commands = ["$updRange:id", "$updRange:id ",
                "$updRange:id[", "$updRange:id [",
                "$updRange:idFILL[", "$updRange:id]",
                "$updRange:id ]", "$updRange:idFILL []",
                "$updRange:id FILL []", "$updRange:id [FILL",
                "$updRange:id[FILL", "$updRange:id [ FILL",
                "$updRange:id FILL]", "$updRange:id FILL ] "]
    for command in commands:
        message = Message(author=author, content=command)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updRange:id", app.updateData,
                           Helpers.updStruct("range", "id"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$updRange:id [_ID, Nombre, Control, Descripción_]**\n" in out

@pytest.mark.asyncio
async def testRangeStruct_updRangeName_invalidStruct(capfd):
    commands = ["$updRange:name", "$updRange:name ",
                "$updRange:name[", "$updRange:name [",
                "$updRange:nameFILL[", "$updRange:name]",
                "$updRange:name ]", "$updRange:nameFILL []",
                "$updRange:name FILL []", "$updRange:name [FILL",
                "$updRange:name[FILL", "$updRange:name [ FILL",
                "$updRange:name FILL]", "$updRange:name FILL ] "]
    for command in commands:
        message = Message(author=author, content=command)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updRange:name", app.updateData,
                           Helpers.updStruct("range", "name"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$updRange:name [_Nombre, Control, Descripción_]**\n" in out

@pytest.mark.asyncio
async def testRangeStruct_delRangeId_invalidStruct(capfd):
    commands = ["$delRange:id", "$delRange:id ",
                "$delRange:id[", "$delRange:id [",
                "$delRange:idFILL[", "$delRange:id]",
                "$delRange:id ]", "$delRange:idFILL []",
                "$delRange:id FILL []", "$delRange:id [FILL",
                "$delRange:id[FILL", "$delRange:id [ FILL",
                "$delRange:id FILL]", "$delRange:id FILL ] "]
    for command in commands:
        message = Message(author=author, content=command)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delRange:id", app.deleteData,
                           Helpers.delStruct("range", "id"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$delRange:id [_ID_]**\n" in out

@pytest.mark.asyncio
async def testRangeStruct_delRangeName_invalidStruct(capfd):
    commands = ["$delRange:name", "$delRange:name ",
                "$delRange:name[", "$delRange:name [",
                "$delRange:nameFILL[", "$delRange:name]",
                "$delRange:name ]", "$delRange:nameFILL []",
                "$delRange:name FILL []", "$delRange:name [FILL",
                "$delRange:name[FILL", "$delRange:name [ FILL",
                "$delRange:name FILL]", "$delRange:name FILL ] "]
    for command in commands:
        message = Message(author=author, content=command)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delRange:name", app.deleteData,
                           Helpers.delStruct("range", "name"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$delRange:name [_Nombre_]**\n" in out

@pytest.mark.asyncio
async def testRangeStruct_listRangeId_invalidStruct(capfd):
    commands = ["$listRange:id", "$listRange:id ",
                "$listRange:id[", "$listRange:id [",
                "$listRange:idFILL[", "$listRange:id]",
                "$listRange:id ]", "$listRange:idFILL []",
                "$listRange:id FILL []", "$listRange:id [FILL",
                "$listRange:id[FILL", "$listRange:id [ FILL",
                "$listRange:id FILL]", "$listRange:id FILL ] "]
    for command in commands:
        message = Message(author=author, content=command)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listRange:id", app.getDatas,
                         Helpers.getStruct("range", ["id"]))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listRange:id [_ID_]**\n" in out

@pytest.mark.asyncio
async def testRangeStruct_listRangeName_invalidStruct(capfd):
    commands = ["$listRange:name", "$listRange:name ",
                "$listRange:name[", "$listRange:name [",
                "$listRange:nameFILL[", "$listRange:name]",
                "$listRange:name ]", "$listRange:nameFILL []",
                "$listRange:name FILL []", "$listRange:name [FILL",
                "$listRange:name[FILL", "$listRange:name [ FILL",
                "$listRange:name FILL]", "$listRange:name FILL ] "]
    for command in commands:
        message = Message(author=author, content=command)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listRange:name", app.getDatas,
                         Helpers.getStruct("range", ["name"]))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listRange:name [_Nombre_]**\n" in out