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
async def testAllPointMemberParams_listAllPointMember_invalidParams(capfd):
    commands = ["$listAllPointMember[]",
                "$listAllPointMember []",
                "$listAllPointMember[,,,,]",
                "$listAllPointMember [,,,,]",
                "$listAllPointMember[,,,,]FILL",
                "$listAllPointMember[,,,,] FILL",
                "$listAllPointMember[,,,,]]FILL",
                "$listAllPointMember [,,,,]] FILL",
                "$listAllPointMember[[,,,,]FILL",
                "$listAllPointMember [[,,,,] FILL",
                "$listAllPointMember[[,,,,]]FILL",
                "$listAllPointMember [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember", app.getDatas,
                         Helpers.getStruct("member",
                                           ["date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberParams_listAllPointMemberId_invalidParams(capfd):
    commands = ["$listAllPointMember:id[]",
                "$listAllPointMember:id []",
                "$listAllPointMember:id[,,,,]",
                "$listAllPointMember:id [,,,,]",
                "$listAllPointMember:id[,,,,]FILL",
                "$listAllPointMember:id[,,,,] FILL",
                "$listAllPointMember:id[,,,,]]FILL",
                "$listAllPointMember:id [,,,,]] FILL",
                "$listAllPointMember:id[[,,,,]FILL",
                "$listAllPointMember:id [[,,,,] FILL",
                "$listAllPointMember:id[[,,,,]]FILL",
                "$listAllPointMember:id [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:id", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_ID, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberParams_listAllPointMemberName_invalidParams(capfd):
    commands = ["$listAllPointMember:name[]",
                "$listAllPointMember:name []",
                "$listAllPointMember:name[,,,,]",
                "$listAllPointMember:name [,,,,]",
                "$listAllPointMember:name[,,,,]FILL",
                "$listAllPointMember:name[,,,,] FILL",
                "$listAllPointMember:name[,,,,]]FILL",
                "$listAllPointMember:name [,,,,]] FILL",
                "$listAllPointMember:name[[,,,,]FILL",
                "$listAllPointMember:name [[,,,,] FILL",
                "$listAllPointMember:name[[,,,,]]FILL",
                "$listAllPointMember:name [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:name", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Nombre, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberParams_listAllPointMemberRange_invalidParams(
    capfd):
    commands = ["$listAllPointMember:range[]",
                "$listAllPointMember:range []",
                "$listAllPointMember:range[,,,,]",
                "$listAllPointMember:range [,,,,]",
                "$listAllPointMember:range[,,,,]FILL",
                "$listAllPointMember:range[,,,,] FILL",
                "$listAllPointMember:range[,,,,]]FILL",
                "$listAllPointMember:range [,,,,]] FILL",
                "$listAllPointMember:range[[,,,,]FILL",
                "$listAllPointMember:range [[,,,,] FILL",
                "$listAllPointMember:range[[,,,,]]FILL",
                "$listAllPointMember:range [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:range", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Rango, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberParams_listAllPointMemberEvent_invalidParams(
    capfd):
    commands = ["$listAllPointMember:event[]",
                "$listAllPointMember:event []",
                "$listAllPointMember:event[,,,,]",
                "$listAllPointMember:event [,,,,]",
                "$listAllPointMember:event[,,,,]FILL",
                "$listAllPointMember:event[,,,,] FILL",
                "$listAllPointMember:event[,,,,]]FILL",
                "$listAllPointMember:event [,,,,]] FILL",
                "$listAllPointMember:event[[,,,,]FILL",
                "$listAllPointMember:event [[,,,,] FILL",
                "$listAllPointMember:event[[,,,,]]FILL",
                "$listAllPointMember:event [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Evento, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberParams_listAllPointMemberIdEvent_invalidParams(
    capfd):
    commands = ["$listAllPointMember:id&event[]",
                "$listAllPointMember:id&event []",
                "$listAllPointMember:id&event[,,,,]",
                "$listAllPointMember:id&event [,,,,]",
                "$listAllPointMember:id&event[,,,,]FILL",
                "$listAllPointMember:id&event[,,,,] FILL",
                "$listAllPointMember:id&event[,,,,]]FILL",
                "$listAllPointMember:id&event [,,,,]] FILL",
                "$listAllPointMember:id&event[[,,,,]FILL",
                "$listAllPointMember:id&event [[,,,,] FILL",
                "$listAllPointMember:id&event[[,,,,]]FILL",
                "$listAllPointMember:id&event [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:id&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_ID, Evento, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberParams_listAllPointMemberNameEvent_invalidParams(
    capfd):
    commands = ["$listAllPointMember:name&event[]",
                "$listAllPointMember:name&event []",
                "$listAllPointMember:name&event[,,,,]",
                "$listAllPointMember:name&event [,,,,]",
                "$listAllPointMember:name&event[,,,,]FILL",
                "$listAllPointMember:name&event[,,,,] FILL",
                "$listAllPointMember:name&event[,,,,]]FILL",
                "$listAllPointMember:name&event [,,,,]] FILL",
                "$listAllPointMember:name&event[[,,,,]FILL",
                "$listAllPointMember:name&event [[,,,,] FILL",
                "$listAllPointMember:name&event[[,,,,]]FILL",
                "$listAllPointMember:name&event [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:name&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Nombre, Evento, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberParams_listAllPointMemberRangeEvent_invalidParams(
    capfd):
    commands = ["$listAllPointMember:range&event[]",
                "$listAllPointMember:range&event []",
                "$listAllPointMember:range&event[,,,,]",
                "$listAllPointMember:range&event [,,,,]",
                "$listAllPointMember:range&event[,,,,]FILL",
                "$listAllPointMember:range&event[,,,,] FILL",
                "$listAllPointMember:range&event[,,,,]]FILL",
                "$listAllPointMember:range&event [,,,,]] FILL",
                "$listAllPointMember:range&event[[,,,,]FILL",
                "$listAllPointMember:range&event [[,,,,] FILL",
                "$listAllPointMember:range&event[[,,,,]]FILL",
                "$listAllPointMember:range&event [[,,,,]] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:range&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Rango, Evento, Fecha 1, Fecha 2_]**\n" in out