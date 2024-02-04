import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Helpers.helpers import Helpers
from collections import namedtuple

Message = namedtuple('Message', ['author', 'content'])
Client = namedtuple('Client', ['user'])
app = AppHandler()

@pytest.mark.asyncio
async def testParams_addRange_invalidParams(capfd):
    commands = ["$addRange[]",
                "$addRange []",
                "$addRange[,,,,]",
                "$addRange [,,,,]",
                "$addRange[,,,,]FILL",
                "$addRange[,,,,] FILL",
                "$addRange[,,,,]]FILL",
                "$addRange [,,,,]] FILL",
                "$addRange[[,,,,]FILL",
                "$addRange [[,,,,] FILL",
                "$addRange[[,,,,]]FILL",
                "$addRange [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addRange", app.setData,
                           Helpers.setStruct("rango"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Nombre, Control, Descripción_]**\n" in out

@pytest.mark.asyncio
async def testParams_updRangeId_invalidParams(capfd):
    commands = ["$updRange:id[]",
                "$updRange:id []",
                "$updRange:id[,,,,]",
                "$updRange:id [,,,,]",
                "$updRange:id[,,,,]FILL",
                "$updRange:id[,,,,] FILL",
                "$updRange:id[,,,,]]FILL",
                "$updRange:id [,,,,]] FILL",
                "$updRange:id[[,,,,]FILL",
                "$updRange:id [[,,,,] FILL",
                "$updRange:id[[,,,,]]FILL",
                "$updRange:id [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updRange:id", app.updateData,
                           Helpers.updStruct("rango", "id"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_ID, Nombre, Control, Descripción_]**\n" in out

@pytest.mark.asyncio
async def testParams_updRangeName_invalidParams(capfd):
    commands = ["$updRange:name[]",
                "$updRange:name []",
                "$updRange:name[,,,,]",
                "$updRange:name [,,,,]",
                "$updRange:name[,,,,]FILL",
                "$updRange:name[,,,,] FILL",
                "$updRange:name[,,,,]]FILL",
                "$updRange:name [,,,,]] FILL",
                "$updRange:name[[,,,,]FILL",
                "$updRange:name [[,,,,] FILL",
                "$updRange:name[[,,,,]]FILL",
                "$updRange:name [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updRange:name", app.updateData,
                           Helpers.updStruct("rango", "name"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Nombre, Control, Descripción_]**\n" in out

@pytest.mark.asyncio
async def testParams_delRangeId_invalidParams(capfd):
    commands = ["$delRange:id[,,,,]",
                "$delRange:id [,,,,]",
                "$delRange:id[,,,,]FILL",
                "$delRange:id[,,,,] FILL",
                "$delRange:id[,,,,]]FILL",
                "$delRange:id [,,,,]] FILL",
                "$delRange:id[[,,,,]FILL",
                "$delRange:id [[,,,,] FILL",
                "$delRange:id[[,,,,]]FILL",
                "$delRange:id [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delRange:id", app.deleteData,
                           Helpers.delStruct("rango", "id"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_ID_]**\n" in out

@pytest.mark.asyncio
async def testParams_delRangeName_invalidParams(capfd):
    commands = ["$delRange:name[,,,,]",
                "$delRange:name [,,,,]",
                "$delRange:name[,,,,]FILL",
                "$delRange:name[,,,,] FILL",
                "$delRange:name[,,,,]]FILL",
                "$delRange:name [,,,,]] FILL",
                "$delRange:name[[,,,,]FILL",
                "$delRange:name [[,,,,] FILL",
                "$delRange:name[[,,,,]]FILL",
                "$delRange:name [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delRange:name", app.deleteData,
                           Helpers.delStruct("rango", "name"))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Nombre_]**\n" in out

@pytest.mark.asyncio
async def testParams_listRangeId_invalidParams(capfd):
    commands = ["$listRange:id[,,,,]",
                "$listRange:id [,,,,]",
                "$listRange:id[,,,,]FILL",
                "$listRange:id[,,,,] FILL",
                "$listRange:id[,,,,]]FILL",
                "$listRange:id [,,,,]] FILL",
                "$listRange:id[[,,,,]FILL",
                "$listRange:id [[,,,,] FILL",
                "$listRange:id[[,,,,]]FILL",
                "$listRange:id [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listRange:id", app.getDatas,
                         Helpers.getStruct("rango", ["id"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_ID_]**\n" in out

@pytest.mark.asyncio
async def testParams_listRangeName_invalidParams(capfd):
    commands = ["$listRange:name[,,,,]",
                "$listRange:name [,,,,]",
                "$listRange:name[,,,,]FILL",
                "$listRange:name[,,,,] FILL",
                "$listRange:name[,,,,]]FILL",
                "$listRange:name [,,,,]] FILL",
                "$listRange:name[[,,,,]FILL",
                "$listRange:name [[,,,,] FILL",
                "$listRange:name[[,,,,]]FILL",
                "$listRange:name [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listRange:name", app.getDatas,
                         Helpers.getStruct("rango", ["name"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Nombre_]**\n" in out