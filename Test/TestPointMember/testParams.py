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
async def testPointMemberParams_listPointMember_invalidParams(capfd):
    commands = ["$listPointMember[]",
                "$listPointMember []",
                "$listPointMember[,,,,]",
                "$listPointMember [,,,,]",
                "$listPointMember[,,,,]FILL",
                "$listPointMember[,,,,] FILL",
                "$listPointMember[,,,,]]FILL",
                "$listPointMember [,,,,]] FILL",
                "$listPointMember[[,,,,]FILL",
                "$listPointMember [[,,,,] FILL",
                "$listPointMember[[,,,,]]FILL",
                "$listPointMember [[,,,,]] FILL"]
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
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testPointMemberParams_listPointMemberId_invalidParams(capfd):
    commands = ["$listPointMember:id[]",
                "$listPointMember:id []",
                "$listPointMember:id[,,,,]",
                "$listPointMember:id [,,,,]",
                "$listPointMember:id[,,,,]FILL",
                "$listPointMember:id[,,,,] FILL",
                "$listPointMember:id[,,,,]]FILL",
                "$listPointMember:id [,,,,]] FILL",
                "$listPointMember:id[[,,,,]FILL",
                "$listPointMember:id [[,,,,] FILL",
                "$listPointMember:id[[,,,,]]FILL",
                "$listPointMember:id [[,,,,]] FILL"]
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
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_ID, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testPointMemberParams_listPointMemberName_invalidParams(capfd):
    commands = ["$listPointMember:name[]",
                "$listPointMember:name []",
                "$listPointMember:name[,,,,]",
                "$listPointMember:name [,,,,]",
                "$listPointMember:name[,,,,]FILL",
                "$listPointMember:name[,,,,] FILL",
                "$listPointMember:name[,,,,]]FILL",
                "$listPointMember:name [,,,,]] FILL",
                "$listPointMember:name[[,,,,]FILL",
                "$listPointMember:name [[,,,,] FILL",
                "$listPointMember:name[[,,,,]]FILL",
                "$listPointMember:name [[,,,,]] FILL"]
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
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Nombre, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testPointMemberParams_listPointMemberRange_invalidParams(capfd):
    commands = ["$listPointMember:range[]",
                "$listPointMember:range []",
                "$listPointMember:range[,,,,]",
                "$listPointMember:range [,,,,]",
                "$listPointMember:range[,,,,]FILL",
                "$listPointMember:range[,,,,] FILL",
                "$listPointMember:range[,,,,]]FILL",
                "$listPointMember:range [,,,,]] FILL",
                "$listPointMember:range[[,,,,]FILL",
                "$listPointMember:range [[,,,,] FILL",
                "$listPointMember:range[[,,,,]]FILL",
                "$listPointMember:range [[,,,,]] FILL"]
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
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Rango, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testPointMemberParams_listPointMemberEvent_invalidParams(capfd):
    commands = ["$listPointMember:event[]",
                "$listPointMember:event []",
                "$listPointMember:event[,,,,]",
                "$listPointMember:event [,,,,]",
                "$listPointMember:event[,,,,]FILL",
                "$listPointMember:event[,,,,] FILL",
                "$listPointMember:event[,,,,]]FILL",
                "$listPointMember:event [,,,,]] FILL",
                "$listPointMember:event[[,,,,]FILL",
                "$listPointMember:event [[,,,,] FILL",
                "$listPointMember:event[[,,,,]]FILL",
                "$listPointMember:event [[,,,,]] FILL"]
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
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Evento, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testPointMemberParams_listPointMemberIdEvent_invalidParams(capfd):
    commands = ["$listPointMember:id&event[]",
                "$listPointMember:id&event []",
                "$listPointMember:id&event[,,,,]",
                "$listPointMember:id&event [,,,,]",
                "$listPointMember:id&event[,,,,]FILL",
                "$listPointMember:id&event[,,,,] FILL",
                "$listPointMember:id&event[,,,,]]FILL",
                "$listPointMember:id&event [,,,,]] FILL",
                "$listPointMember:id&event[[,,,,]FILL",
                "$listPointMember:id&event [[,,,,] FILL",
                "$listPointMember:id&event[[,,,,]]FILL",
                "$listPointMember:id&event [[,,,,]] FILL"]
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
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_ID, Evento, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testPointMemberParams_listPointMemberNameEvent_invalidParams(capfd):
    commands = ["$listPointMember:name&event[]",
                "$listPointMember:name&event []",
                "$listPointMember:name&event[,,,,]",
                "$listPointMember:name&event [,,,,]",
                "$listPointMember:name&event[,,,,]FILL",
                "$listPointMember:name&event[,,,,] FILL",
                "$listPointMember:name&event[,,,,]]FILL",
                "$listPointMember:name&event [,,,,]] FILL",
                "$listPointMember:name&event[[,,,,]FILL",
                "$listPointMember:name&event [[,,,,] FILL",
                "$listPointMember:name&event[[,,,,]]FILL",
                "$listPointMember:name&event [[,,,,]] FILL"]
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
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Nombre, Evento, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def testPointMemberParams_listPointMemberRangeEvent_invalidParams(capfd):
    commands = ["$listPointMember:range&event[]",
                "$listPointMember:range&event []",
                "$listPointMember:range&event[,,,,]",
                "$listPointMember:range&event [,,,,]",
                "$listPointMember:range&event[,,,,]FILL",
                "$listPointMember:range&event[,,,,] FILL",
                "$listPointMember:range&event[,,,,]]FILL",
                "$listPointMember:range&event [,,,,]] FILL",
                "$listPointMember:range&event[[,,,,]FILL",
                "$listPointMember:range&event [[,,,,] FILL",
                "$listPointMember:range&event[[,,,,]]FILL",
                "$listPointMember:range&event [[,,,,]] FILL"]
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
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Rango, Evento, Fecha 1, Fecha 2_]**\n" in out