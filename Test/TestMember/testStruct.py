import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Helpers.helpers import Helpers
from collections import namedtuple

Message = namedtuple('Message', ['author', 'content'])
Client = namedtuple('Client', ['user'])
app = AppHandler()

@pytest.mark.asyncio
async def testMemberStruct_addMember_invalidStruct(capfd):
    commands = ["$addMember", "$addMember ",
                "$addMember[", "$addMember [",
                "$addMemberFILL[", "$addMember]",
                "$addMember ]", "$addMemberFILL []",
                "$addMember FILL []", "$addMember [FILL",
                "$addMember[FILL", "$addMember [ FILL",
                "$addMember FILL]", "$addMember FILL ] "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addMember", app.setData,
                           Helpers.setStruct("member"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$addMember [_Nombre, Rango, Fecha_]**\n" in out

@pytest.mark.asyncio
async def testMemberStruct_updMemberId_invalidStruct(capfd):
    commands = ["$updMember:id", "$updMember:id ",
                "$updMember:id[", "$updMember:id [",
                "$updMember:idFILL[", "$updMember:id]",
                "$updMember:id ]", "$updMember:idFILL []",
                "$updMember:id FILL []", "$updMember:id [FILL",
                "$updMember:id[FILL", "$updMember:id [ FILL",
                "$updMember:id FILL]", "$updMember:id FILL ] "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:id", app.updateData,
                           Helpers.updStruct("member", "id"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$updMember:id [_ID, Nombre, Rango, Fecha_]**\n" in out

@pytest.mark.asyncio
async def testMemberStruct_updMemberName_invalidStruct(capfd):
    commands = ["$updMember:name", "$updMember:name ",
                "$updMember:name[", "$updMember:name [",
                "$updMember:nameFILL[", "$updMember:name]",
                "$updMember:name ]", "$updMember:nameFILL []",
                "$updMember:name FILL []", "$updMember:name [FILL",
                "$updMember:name[FILL", "$updMember:name [ FILL",
                "$updMember:name FILL]", "$updMember:name FILL ] "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:name", app.updateData,
                           Helpers.updStruct("member", "name"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$updMember:name [_Nombre, Rango, Fecha_]**\n" in out

@pytest.mark.asyncio
async def testMemberStruct_delMemberId_invalidStruct(capfd):
    commands = ["$delMember:id", "$delMember:id ",
                "$delMember:id[", "$delMember:id [",
                "$delMember:idFILL[", "$delMember:id]",
                "$delMember:id ]", "$delMember:idFILL []",
                "$delMember:id FILL []", "$delMember:id [FILL",
                "$delMember:id[FILL", "$delMember:id [ FILL",
                "$delMember:id FILL]", "$delMember:id FILL ] "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delMember:id", app.deleteData,
                           Helpers.delStruct("member", "id"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$delMember:id [_ID_]**\n" in out

@pytest.mark.asyncio
async def testMemberStruct_delMemberName_invalidStruct(capfd):
    commands = ["$delMember:name", "$delMember:name ",
                "$delMember:name[", "$delMember:name [",
                "$delMember:nameFILL[", "$delMember:name]",
                "$delMember:name ]", "$delMember:nameFILL []",
                "$delMember:name FILL []", "$delMember:name [FILL",
                "$delMember:name[FILL", "$delMember:name [ FILL",
                "$delMember:name FILL]", "$delMember:name FILL ] "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delMember:name", app.deleteData,
                           Helpers.delStruct("member", "name"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$delMember:name [_Nombre_]**\n" in out

@pytest.mark.asyncio
async def testMemberStruct_listMemberId_invalidStruct(capfd):
    commands = ["$listMember:id", "$listMember:id ",
                "$listMember:id[", "$listMember:id [",
                "$listMember:idFILL[", "$listMember:id]",
                "$listMember:id ]", "$listMember:idFILL []",
                "$listMember:id FILL []", "$listMember:id [FILL",
                "$listMember:id[FILL", "$listMember:id [ FILL",
                "$listMember:id FILL]", "$listMember:id FILL ] "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:id", app.getDatas,
                         Helpers.getStruct("member", ["id"]))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listMember:id [_ID_]**\n" in out

@pytest.mark.asyncio
async def testMemberStruct_listMemberName_invalidStruct(capfd):
    commands = ["$listMember:name", "$listMember:name ",
                "$listMember:name[", "$listMember:name [",
                "$listMember:nameFILL[", "$listMember:name]",
                "$listMember:name ]", "$listMember:nameFILL []",
                "$listMember:name FILL []", "$listMember:name [FILL",
                "$listMember:name[FILL", "$listMember:name [ FILL",
                "$listMember:name FILL]", "$listMember:name FILL ] "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:name", app.getDatas,
                         Helpers.getStruct("member", ["name"]))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listMember:name [_Nombre_]**\n" in out

@pytest.mark.asyncio
async def testMemberStruct_listMemberRange_invalidStruct(capfd):
    commands = ["$listMember:range", "$listMember:range ",
                "$listMember:range[", "$listMember:range [",
                "$listMember:rangeFILL[", "$listMember:range]",
                "$listMember:range ]", "$listMember:rangeFILL []",
                "$listMember:range FILL []", "$listMember:range [FILL",
                "$listMember:range[FILL", "$listMember:range [ FILL",
                "$listMember:range FILL]", "$listMember:range FILL ] "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:range", app.getDatas,
                         Helpers.getStruct("member", ["range"]))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listMember:range [_Rango_]**\n" in out

@pytest.mark.asyncio
async def testMemberStruct_listMemberDate_invalidStruct(capfd):
    commands = ["$listMember:date", "$listMember:date ",
                "$listMember:date[", "$listMember:date [",
                "$listMember:dateFILL[", "$listMember:date]",
                "$listMember:date ]", "$listMember:dateFILL []",
                "$listMember:date FILL []", "$listMember:date [FILL",
                "$listMember:date[FILL", "$listMember:date [ FILL",
                "$listMember:date FILL]", "$listMember:date FILL ] "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:date", app.getDatas,
                         Helpers.getStruct("member", ["date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listMember:date [_Fecha 1, Fecha 2_]**\n" in out