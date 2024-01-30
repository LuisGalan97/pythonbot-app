import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Helpers.helpers import Helpers
from collections import namedtuple

Message = namedtuple('Message', ['author', 'content'])
Client = namedtuple('Client', ['user'])
app = AppHandler()

@pytest.mark.asyncio
async def test_addEvent_invalidStruct(capfd):
    commands = ["$addEvent", "$addEvent ",
                "$addEvent[", "$addEvent [",
                "$addEventFILL[", "$addEvent]",
                "$addEvent ]", "$addEventFILL []",
                "$addEvent FILL []", "$addEvent [FILL",
                "$addEvent[FILL", "$addEvent [ FILL",
                "$addEvent FILL]", "$addEvent FILL ] "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addEvent", app.setData,
                           Helpers.setStruct("evento"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:" in out
        assert "**$addEvent [_Nombre, Puntos, Descripción_]**" in out

@pytest.mark.asyncio
async def test_updEventId_invalidStruct(capfd):
    commands = ["$updEvent:id", "$updEvent:id ",
                "$updEvent:id[", "$updEvent:id [",
                "$updEvent:idFILL[", "$updEvent:id]",
                "$updEvent:id ]", "$updEvent:idFILL []",
                "$updEvent:id FILL []", "$updEvent:id [FILL",
                "$updEvent:id[FILL", "$updEvent:id [ FILL",
                "$updEvent:id FILL]", "$updEvent:id FILL ] "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updEvent:id", app.updateData,
                           Helpers.updStruct("evento", "id"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:" in out
        assert "**$updEvent:id [_ID, Nombre, Puntos, Descripción_]**" in out

@pytest.mark.asyncio
async def test_updEventName_invalidStruct(capfd):
    commands = ["$updEvent:name", "$updEvent:name ",
                "$updEvent:name[", "$updEvent:name [",
                "$updEvent:nameFILL[", "$updEvent:name]",
                "$updEvent:name ]", "$updEvent:nameFILL []",
                "$updEvent:name FILL []", "$updEvent:name [FILL",
                "$updEvent:name[FILL", "$updEvent:name [ FILL",
                "$updEvent:name FILL]", "$updEvent:name FILL ] "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updEvent:name", app.updateData,
                           Helpers.updStruct("evento", "name"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:" in out
        assert "**$updEvent:name [_Nombre, Puntos, Descripción_]**" in out

@pytest.mark.asyncio
async def test_delEventId_invalidStruct(capfd):
    commands = ["$delEvent:id", "$delEvent:id ",
                "$delEvent:id[", "$delEvent:id [",
                "$delEvent:idFILL[", "$delEvent:id]",
                "$delEvent:id ]", "$delEvent:idFILL []",
                "$delEvent:id FILL []", "$delEvent:id [FILL",
                "$delEvent:id[FILL", "$delEvent:id [ FILL",
                "$delEvent:id FILL]", "$delEvent:id FILL ] "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delEvent:id", app.deleteData,
                           Helpers.delStruct("evento", "id"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:" in out
        assert "**$delEvent:id [_ID_]**" in out

@pytest.mark.asyncio
async def test_delEventName_invalidStruct(capfd):
    commands = ["$delEvent:name", "$delEvent:name ",
                "$delEvent:name[", "$delEvent:name [",
                "$delEvent:nameFILL[", "$delEvent:name]",
                "$delEvent:name ]", "$delEvent:nameFILL []",
                "$delEvent:name FILL []", "$delEvent:name [FILL",
                "$delEvent:name[FILL", "$delEvent:name [ FILL",
                "$delEvent:name FILL]", "$delEvent:name FILL ] "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delEvent:name", app.deleteData,
                           Helpers.delStruct("evento", "name"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:" in out
        assert "**$delEvent:name [_Nombre_]**" in out

@pytest.mark.asyncio
async def test_listEventId_invalidStruct(capfd):
    commands = ["$listEvent:id", "$listEvent:id ",
                "$listEvent:id[", "$listEvent:id [",
                "$listEvent:idFILL[", "$listEvent:id]",
                "$listEvent:id ]", "$listEvent:idFILL []",
                "$listEvent:id FILL []", "$listEvent:id [FILL",
                "$listEvent:id[FILL", "$listEvent:id [ FILL",
                "$listEvent:id FILL]", "$listEvent:id FILL ] "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listEvent:id", app.getDatas,
                         Helpers.getStruct("evento", ["id"]))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:" in out
        assert "**$listEvent:id [_ID_]**" in out

@pytest.mark.asyncio
async def test_listEventName_invalidStruct(capfd):
    commands = ["$listEvent:name", "$listEvent:name ",
                "$listEvent:name[", "$listEvent:name [",
                "$listEvent:nameFILL[", "$listEvent:name]",
                "$listEvent:name ]", "$listEvent:nameFILL []",
                "$listEvent:name FILL []", "$listEvent:name [FILL",
                "$listEvent:name[FILL", "$listEvent:name [ FILL",
                "$listEvent:name FILL]", "$listEvent:name FILL ] "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listEvent:name", app.getDatas,
                         Helpers.getStruct("evento", ["name"]))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:" in out
        assert "**$listEvent:name [_Nombre_]**" in out