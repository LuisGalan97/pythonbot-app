import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Helpers.helpers import Helpers
from collections import namedtuple

Message = namedtuple('Message', ['author', 'content'])
Client = namedtuple('Client', ['user'])
app = AppHandler()

@pytest.mark.asyncio
async def testMemberParams_addMember_invalidParams(capfd):
    commands = ["$addMember[]",
                "$addMember []",
                "$addMember[,,,,]",
                "$addMember [,,,,]",
                "$addMember[,,,,]FILL",
                "$addMember[,,,,] FILL",
                "$addMember[,,,,]]FILL",
                "$addMember [,,,,]] FILL",
                "$addMember[[,,,,]FILL",
                "$addMember [[,,,,] FILL",
                "$addMember[[,,,,]]FILL",
                "$addMember [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addMember", app.setData,
                           Helpers.setStruct("member"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Nombre, Rango, Fecha_]**\n" in out

@pytest.mark.asyncio
async def testMemberParams_updMemberId_invalidParams(capfd):
    commands = ["$updMember:id[]",
                "$updMember:id []",
                "$updMember:id[,,,,]",
                "$updMember:id [,,,,]",
                "$updMember:id[,,,,]FILL",
                "$updMember:id[,,,,] FILL",
                "$updMember:id[,,,,]]FILL",
                "$updMember:id [,,,,]] FILL",
                "$updMember:id[[,,,,]FILL",
                "$updMember:id [[,,,,] FILL",
                "$updMember:id[[,,,,]]FILL",
                "$updMember:id [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:id", app.updateData,
                           Helpers.updStruct("member", "id"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_ID, Nombre, Rango, Fecha_]**\n" in out

@pytest.mark.asyncio
async def testMemberParams_updMemberName_invalidParams(capfd):
    commands = ["$updMember:name[]",
                "$updMember:name []",
                "$updMember:name[,,,,]",
                "$updMember:name [,,,,]",
                "$updMember:name[,,,,]FILL",
                "$updMember:name[,,,,] FILL",
                "$updMember:name[,,,,]]FILL",
                "$updMember:name [,,,,]] FILL",
                "$updMember:name[[,,,,]FILL",
                "$updMember:name [[,,,,] FILL",
                "$updMember:name[[,,,,]]FILL",
                "$updMember:name [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:name", app.updateData,
                           Helpers.updStruct("member", "name"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Nombre, Rango, Fecha_]**\n" in out

@pytest.mark.asyncio
async def testMemberParams_delMemberId_invalidParams(capfd):
    commands = ["$delMember:id[,,,,]",
                "$delMember:id [,,,,]",
                "$delMember:id[,,,,]FILL",
                "$delMember:id[,,,,] FILL",
                "$delMember:id[,,,,]]FILL",
                "$delMember:id [,,,,]] FILL",
                "$delMember:id[[,,,,]FILL",
                "$delMember:id [[,,,,] FILL",
                "$delMember:id[[,,,,]]FILL",
                "$delMember:id [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delMember:id", app.deleteData,
                           Helpers.delStruct("member", "id"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_ID_]**\n" in out

@pytest.mark.asyncio
async def testMemberParams_delMemberName_invalidParams(capfd):
    commands = ["$delMember:name[,,,,]",
                "$delMember:name [,,,,]",
                "$delMember:name[,,,,]FILL",
                "$delMember:name[,,,,] FILL",
                "$delMember:name[,,,,]]FILL",
                "$delMember:name [,,,,]] FILL",
                "$delMember:name[[,,,,]FILL",
                "$delMember:name [[,,,,] FILL",
                "$delMember:name[[,,,,]]FILL",
                "$delMember:name [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delMember:name", app.deleteData,
                           Helpers.delStruct("member", "name"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Nombre_]**\n" in out

@pytest.mark.asyncio
async def testMemberParams_listMemberId_invalidParams(capfd):
    commands = ["$listMember:id[,,,,]",
                "$listMember:id [,,,,]",
                "$listMember:id[,,,,]FILL",
                "$listMember:id[,,,,] FILL",
                "$listMember:id[,,,,]]FILL",
                "$listMember:id [,,,,]] FILL",
                "$listMember:id[[,,,,]FILL",
                "$listMember:id [[,,,,] FILL",
                "$listMember:id[[,,,,]]FILL",
                "$listMember:id [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:id", app.getDatas,
                         Helpers.getStruct("member", ["id"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_ID_]**\n" in out

@pytest.mark.asyncio
async def testMemberParams_listMemberName_invalidParams(capfd):
    commands = ["$listMember:name[,,,,]",
                "$listMember:name [,,,,]",
                "$listMember:name[,,,,]FILL",
                "$listMember:name[,,,,] FILL",
                "$listMember:name[,,,,]]FILL",
                "$listMember:name [,,,,]] FILL",
                "$listMember:name[[,,,,]FILL",
                "$listMember:name [[,,,,] FILL",
                "$listMember:name[[,,,,]]FILL",
                "$listMember:name [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:name", app.getDatas,
                         Helpers.getStruct("member", ["name"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Nombre_]**\n" in out

@pytest.mark.asyncio
async def testMemberParams_listMemberRange_invalidParams(capfd):
    commands = ["$listMember:range[,,,,]",
                "$listMember:range [,,,,]",
                "$listMember:range[,,,,]FILL",
                "$listMember:range[,,,,] FILL",
                "$listMember:range[,,,,]]FILL",
                "$listMember:range [,,,,]] FILL",
                "$listMember:range[[,,,,]FILL",
                "$listMember:range [[,,,,] FILL",
                "$listMember:range[[,,,,]]FILL",
                "$listMember:range [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:range", app.getDatas,
                         Helpers.getStruct("member", ["range"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Rango_]**\n" in out

@pytest.mark.asyncio
async def testMemberParams_listMemberDate_invalidParams(capfd):
    commands = ["$listMember:date[]",
                "$listMember:date []",
                "$listMember:date[,,,,]",
                "$listMember:date [,,,,]",
                "$listMember:date[,,,,]FILL",
                "$listMember:date[,,,,] FILL",
                "$listMember:date[,,,,]]FILL",
                "$listMember:date [,,,,]] FILL",
                "$listMember:date[[,,,,]FILL",
                "$listMember:date [[,,,,] FILL",
                "$listMember:date[[,,,,]]FILL",
                "$listMember:date [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:date", app.getDatas,
                         Helpers.getStruct("member", ["date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Fecha 1, Fecha 2_]**\n" in out