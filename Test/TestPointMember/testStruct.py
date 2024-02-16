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
                                           ["date_1",
                                            "date_2"],
                                            "rtpoints"))
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
                                            "date_1",
                                            "date_2"],
                                            "rtpoints"))
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
                                            "date_1",
                                            "date_2"],
                                            "rtpoints"))
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
                                            "date_1",
                                            "date_2"],
                                            "rtpoints"))
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
                                            "date_1",
                                            "date_2"],
                                            "rtpoints"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listPointMember:event "\
               "[_Evento, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testPointMemberStruct_listPointMemberIdEvent_invalidStruct(capfd):
    commands = ["$listPointMember:id&event",
                "$listPointMember:id&event ",
                "$listPointMember:id&event[",
                "$listPointMember:id&event [",
                "$listPointMember:id&eventFILL[",
                "$listPointMember:id&event]",
                "$listPointMember:id&event ]",
                "$listPointMember:id&eventFILL []",
                "$listPointMember:id&event FILL []",
                "$listPointMember:id&event [FILL",
                "$listPointMember:id&event[FILL",
                "$listPointMember:id&event [ FILL",
                "$listPointMember:id&event FILL]",
                "$listPointMember:id&event FILL ] "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:id&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "rtpoints"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listPointMember:id&event "\
               "[_ID, Evento, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testPointMemberStruct_listPointMemberNameEvent_invalidStruct(capfd):
    commands = ["$listPointMember:name&event",
                "$listPointMember:name&event ",
                "$listPointMember:name&event[",
                "$listPointMember:name&event [",
                "$listPointMember:name&eventFILL[",
                "$listPointMember:name&event]",
                "$listPointMember:name&event ]",
                "$listPointMember:name&eventFILL []",
                "$listPointMember:name&event FILL []",
                "$listPointMember:name&event [FILL",
                "$listPointMember:name&event[FILL",
                "$listPointMember:name&event [ FILL",
                "$listPointMember:name&event FILL]",
                "$listPointMember:name&event FILL ] "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:name&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "rtpoints"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listPointMember:name&event "\
               "[_Nombre, Evento, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testPointMemberStruct_listPointMemberRangeEvent_invalidStruct(capfd):
    commands = ["$listPointMember:range&event",
                "$listPointMember:range&event ",
                "$listPointMember:range&event[",
                "$listPointMember:range&event [",
                "$listPointMember:range&eventFILL[",
                "$listPointMember:range&event]",
                "$listPointMember:range&event ]",
                "$listPointMember:range&eventFILL []",
                "$listPointMember:range&event FILL []",
                "$listPointMember:range&event [FILL",
                "$listPointMember:range&event[FILL",
                "$listPointMember:range&event [ FILL",
                "$listPointMember:range&event FILL]",
                "$listPointMember:range&event FILL ] "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:range&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "rtpoints"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listPointMember:range&event "\
               "[_Rango, Evento, Fecha 1, Fecha 2_]**\n" in out