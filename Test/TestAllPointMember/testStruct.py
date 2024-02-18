import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Certs.certificates import Certificates
from Helpers.helpers import Helpers
from collections import namedtuple

Message = namedtuple('Message', ['author', 'content', 'channel'])
Channel = namedtuple('Channel', ['name'])
Client = namedtuple('Client', ['user'])
name = 'test'
author = "test"
user = "test"
app = AppHandler()
permissions = Certificates()

@pytest.mark.asyncio
async def testAllPointMemberStruct_listAllPointMember_invalidStruct(capfd):
    commands = ["$listAllPointMember", "$listAllPointMember ",
                "$listAllPointMember[", "$listAllPointMember [",
                "$listAllPointMemberFILL[", "$listAllPointMember]",
                "$listAllPointMember ]", "$listAllPointMemberFILL []",
                "$listAllPointMember FILL []", "$listAllPointMember [FILL",
                "$listAllPointMember[FILL", "$listAllPointMember [ FILL",
                "$listAllPointMember FILL]", "$listAllPointMember FILL ] "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember", app.getDatas,
                         Helpers.getStruct("member",
                                           ["date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listAllPointMember [_Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberStruct_listAllPointMemberId_invalidStruct(capfd):
    commands = ["$listAllPointMember:id",
                "$listAllPointMember:id ",
                "$listAllPointMember:id[",
                "$listAllPointMember:id [",
                "$listAllPointMember:idFILL[",
                "$listAllPointMember:id]",
                "$listAllPointMember:id ]",
                "$listAllPointMember:idFILL []",
                "$listAllPointMember:id FILL []",
                "$listAllPointMember:id [FILL",
                "$listAllPointMember:id[FILL",
                "$listAllPointMember:id [ FILL",
                "$listAllPointMember:id FILL]",
                "$listAllPointMember:id FILL ] "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:id", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listAllPointMember:id [_ID, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberStruct_listAllPointMemberName_invalidStruct(capfd):
    commands = ["$listAllPointMember:name",
                "$listAllPointMember:name ",
                "$listAllPointMember:name[",
                "$listAllPointMember:name [",
                "$listAllPointMember:nameFILL[",
                "$listAllPointMember:name]",
                "$listAllPointMember:name ]",
                "$listAllPointMember:nameFILL []",
                "$listAllPointMember:name FILL []",
                "$listAllPointMember:name [FILL",
                "$listAllPointMember:name[FILL",
                "$listAllPointMember:name [ FILL",
                "$listAllPointMember:name FILL]",
                "$listAllPointMember:name FILL ] "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:name", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listAllPointMember:name "\
               "[_Nombre, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberStruct_listAllPointMemberRange_invalidStruct(
    capfd):
    commands = ["$listAllPointMember:range",
                "$listAllPointMember:range ",
                "$listAllPointMember:range[",
                "$listAllPointMember:range [",
                "$listAllPointMember:rangeFILL[",
                "$listAllPointMember:range]",
                "$listAllPointMember:range ]",
                "$listAllPointMember:rangeFILL []",
                "$listAllPointMember:range FILL []",
                "$listAllPointMember:range [FILL",
                "$listAllPointMember:range[FILL",
                "$listAllPointMember:range [ FILL",
                "$listAllPointMember:range FILL]",
                "$listAllPointMember:range FILL ] "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:range", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listAllPointMember:range "\
               "[_Rango, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberStruct_listAllPointMemberEvent_invalidStruct(
    capfd):
    commands = ["$listAllPointMember:event",
                "$listAllPointMember:event ",
                "$listAllPointMember:event[",
                "$listAllPointMember:event [",
                "$listAllPointMember:eventFILL[",
                "$listAllPointMember:event]",
                "$listAllPointMember:event ]",
                "$listAllPointMember:eventFILL []",
                "$listAllPointMember:event FILL []",
                "$listAllPointMember:event [FILL",
                "$listAllPointMember:event[FILL",
                "$listAllPointMember:event [ FILL",
                "$listAllPointMember:event FILL]",
                "$listAllPointMember:event FILL ] "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listAllPointMember:event "\
               "[_Evento, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberStruct_listAllPointMemberIdEvent_invalidStruct(
    capfd):
    commands = ["$listAllPointMember:id&event",
                "$listAllPointMember:id&event ",
                "$listAllPointMember:id&event[",
                "$listAllPointMember:id&event [",
                "$listAllPointMember:id&eventFILL[",
                "$listAllPointMember:id&event]",
                "$listAllPointMember:id&event ]",
                "$listAllPointMember:id&eventFILL []",
                "$listAllPointMember:id&event FILL []",
                "$listAllPointMember:id&event [FILL",
                "$listAllPointMember:id&event[FILL",
                "$listAllPointMember:id&event [ FILL",
                "$listAllPointMember:id&event FILL]",
                "$listAllPointMember:id&event FILL ] "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:id&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listAllPointMember:id&event "\
               "[_ID, Evento, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberStruct_listAllPointMemberNameEvent_invalidStruct(
    capfd):
    commands = ["$listAllPointMember:name&event",
                "$listAllPointMember:name&event ",
                "$listAllPointMember:name&event[",
                "$listAllPointMember:name&event [",
                "$listAllPointMember:name&eventFILL[",
                "$listAllPointMember:name&event]",
                "$listAllPointMember:name&event ]",
                "$listAllPointMember:name&eventFILL []",
                "$listAllPointMember:name&event FILL []",
                "$listAllPointMember:name&event [FILL",
                "$listAllPointMember:name&event[FILL",
                "$listAllPointMember:name&event [ FILL",
                "$listAllPointMember:name&event FILL]",
                "$listAllPointMember:name&event FILL ] "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:name&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listAllPointMember:name&event "\
               "[_Nombre, Evento, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberStruct_listAllPointMemberRangeEvent_invalidStruct(
    capfd):
    commands = ["$listAllPointMember:range&event",
                "$listAllPointMember:range&event ",
                "$listAllPointMember:range&event[",
                "$listAllPointMember:range&event [",
                "$listAllPointMember:range&eventFILL[",
                "$listAllPointMember:range&event]",
                "$listAllPointMember:range&event ]",
                "$listAllPointMember:range&eventFILL []",
                "$listAllPointMember:range&event FILL []",
                "$listAllPointMember:range&event [FILL",
                "$listAllPointMember:range&event[FILL",
                "$listAllPointMember:range&event [ FILL",
                "$listAllPointMember:range&event FILL]",
                "$listAllPointMember:range&event FILL ] "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:range&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listAllPointMember:range&event "\
               "[_Rango, Evento, Fecha 1, Fecha 2_]**\n" in out