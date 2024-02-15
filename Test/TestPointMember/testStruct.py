import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Helpers.helpers import Helpers
from collections import namedtuple

Message = namedtuple('Message', ['author', 'content', 'channel'])
Channel = namedtuple('Channel', ['name'])
Client = namedtuple('Client', ['user'])
name = 'test'
author = "test"
user = "test"
app = AppHandler()

@pytest.mark.asyncio
async def testPointMemberStruct_listPointMember_invalidStruct(capfd):
    commands = ["$listPointMember", "$listPointMember ",
                "$listPointMember[", "$listPointMember [",
                "$listPointMemberFILL[", "$listPointMember]",
                "$listPointMember ]", "$listPointMemberFILL []",
                "$listPointMember FILL []", "$listPointMember [FILL",
                "$listPointMember[FILL", "$listPointMember [ FILL",
                "$listPointMember FILL]", "$listPointMember FILL ] "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember", app.getDatas,
                         Helpers.getStruct("member",
                                           ["assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listPointMember [_Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testPointMemberStruct_listPointMemberId_invalidStruct(capfd):
    commands = ["$listPointMember:id", "$listPointMember:id ",
                "$listPointMember:id[", "$listPointMember:id [",
                "$listPointMember:idFILL[", "$listPointMember:id]",
                "$listPointMember:id ]", "$listPointMember:idFILL []",
                "$listPointMember:id FILL []", "$listPointMember:id [FILL",
                "$listPointMember:id[FILL", "$listPointMember:id [ FILL",
                "$listPointMember:id FILL]", "$listPointMember:id FILL ] "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:id", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listPointMember:id [_ID, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testPointMemberStruct_listPointMemberName_invalidStruct(capfd):
    commands = ["$listPointMember:name", "$listPointMember:name ",
                "$listPointMember:name[", "$listPointMember:name [",
                "$listPointMember:nameFILL[", "$listPointMember:name]",
                "$listPointMember:name ]", "$listPointMember:nameFILL []",
                "$listPointMember:name FILL []", "$listPointMember:name [FILL",
                "$listPointMember:name[FILL", "$listPointMember:name [ FILL",
                "$listPointMember:name FILL]", "$listPointMember:name FILL ] "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:name", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listPointMember:name "\
               "[_Nombre, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testPointMemberStruct_listPointMemberRange_invalidStruct(capfd):
    commands = ["$listPointMember:range",
                "$listPointMember:range ",
                "$listPointMember:range[",
                "$listPointMember:range [",
                "$listPointMember:rangeFILL[",
                "$listPointMember:range]",
                "$listPointMember:range ]",
                "$listPointMember:rangeFILL []",
                "$listPointMember:range FILL []",
                "$listPointMember:range [FILL",
                "$listPointMember:range[FILL",
                "$listPointMember:range [ FILL",
                "$listPointMember:range FILL]",
                "$listPointMember:range FILL ] "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:range", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listPointMember:range "\
               "[_Rango, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testPointMemberStruct_listPointMemberEvent_invalidStruct(capfd):
    commands = ["$listPointMember:event",
                "$listPointMember:event ",
                "$listPointMember:event[",
                "$listPointMember:event [",
                "$listPointMember:eventFILL[",
                "$listPointMember:event]",
                "$listPointMember:event ]",
                "$listPointMember:eventFILL []",
                "$listPointMember:event FILL []",
                "$listPointMember:event [FILL",
                "$listPointMember:event[FILL",
                "$listPointMember:event [ FILL",
                "$listPointMember:event FILL]",
                "$listPointMember:event FILL ] "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["event",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listPointMember:event "\
               "[_Evento, Fecha 1, Fecha 2_]**\n" in out

'''
@pytest.mark.asyncio
async def testMemberStruct_listPointMemberName_invalidStruct(capfd):
    commands = ["$listPointMember:name", "$listPointMember:name ",
                "$listPointMember:name[", "$listPointMember:name [",
                "$listPointMember:nameFILL[", "$listPointMember:name]",
                "$listPointMember:name ]", "$listPointMember:nameFILL []",
                "$listPointMember:name FILL []", "$listPointMember:name [FILL",
                "$listPointMember:name[FILL", "$listPointMember:name [ FILL",
                "$listPointMember:name FILL]", "$listPointMember:name FILL ] "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:name", app.getDatas,
                         Helpers.getStruct("member", ["name"]))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listPointMember:name [_Nombre_]**\n" in out

@pytest.mark.asyncio
async def testMemberStruct_listPointMemberRange_invalidStruct(capfd):
    commands = ["$listPointMember:range", "$listPointMember:range ",
                "$listPointMember:range[", "$listPointMember:range [",
                "$listPointMember:rangeFILL[", "$listPointMember:range]",
                "$listPointMember:range ]", "$listPointMember:rangeFILL []",
                "$listPointMember:range FILL []", "$listPointMember:range [FILL",
                "$listPointMember:range[FILL", "$listPointMember:range [ FILL",
                "$listPointMember:range FILL]", "$listPointMember:range FILL ] "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:range", app.getDatas,
                         Helpers.getStruct("member", ["range"]))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listPointMember:range [_Rango_]**\n" in out

@pytest.mark.asyncio
async def testMemberStruct_listPointMemberDate_invalidStruct(capfd):
    commands = ["$listPointMember:date", "$listPointMember:date ",
                "$listPointMember:date[", "$listPointMember:date [",
                "$listPointMember:dateFILL[", "$listPointMember:date]",
                "$listPointMember:date ]", "$listPointMember:dateFILL []",
                "$listPointMember:date FILL []", "$listPointMember:date [FILL",
                "$listPointMember:date[FILL", "$listPointMember:date [ FILL",
                "$listPointMember:date FILL]", "$listPointMember:date FILL ] "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:date", app.getDatas,
                         Helpers.getStruct("member", ["date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listPointMember:date [_Fecha 1, Fecha 2_]**\n" in out
'''