import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Helpers.helpers import Helpers
from collections import namedtuple

testData = {
    "id" : "1",
    "name" : "TestMember",
    "range" : "General de alianza",
    "date" : "25-01-2100"
}

Message = namedtuple('Message', ['author', 'content'])
Client = namedtuple('Client', ['user'])
app = AppHandler()

#----------------------Test $addMember [Nombre, *, *]----------------------
@pytest.mark.asyncio
async def testValue_addMember_nameEmpty(capfd):
    value = ""
    commands = [f"$addMember[{value},"\
                f"{testData['range']},"\
                f"{testData['date']}]",
                f"$addMember [{value}, "\
                f"{testData['range']}, "\
                f"{testData['date']} ]",
                f"$addMember [ {value} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ] ",
                f"$addMember [ {value} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ]FILL",
                f"$addMember [ {value} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addMember", app.setData,
                           Helpers.setStruct("integrante"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Nombre_**\n" in out

@pytest.mark.asyncio
async def testValue_addMember_nameLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$addMember[{value},"\
                f"{testData['range']},"\
                f"{testData['date']}]",
                f"$addMember [{value}, "\
                f"{testData['range']}, "\
                f"{testData['date']} ]",
                f"$addMember [ {value} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ] ",
                f"$addMember [ {value} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ]FILL",
                f"$addMember [ {value} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addMember", app.setData,
                           Helpers.setStruct("integrante"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Nombre_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testValue_addMember_nameStartChar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$addMember[{value},"\
                    f"{testData['range']},"\
                    f"{testData['date']}]",
                    f"$addMember [{value}, "\
                    f"{testData['range']}, "\
                    f"{testData['date']} ]",
                    f"$addMember [ {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ] ",
                    f"$addMember [ {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ]FILL",
                    f"$addMember [ {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addMember", app.setData,
                               Helpers.setStruct("integrante"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testValue_addMember_nameSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$addMember[{value},"\
                    f"{testData['range']},"\
                    f"{testData['date']}]",
                    f"$addMember [{value}, "\
                    f"{testData['range']}, "\
                    f"{testData['date']} ]",
                    f"$addMember [ {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ] ",
                    f"$addMember [ {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ]FILL",
                    f"$addMember [ {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addMember", app.setData,
                               Helpers.setStruct("integrante"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testValue_addMember_nameRepeatChar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$addMember[{value},"\
                    f"{testData['range']},"\
                    f"{testData['date']}]",
                    f"$addMember [{value}, "\
                    f"{testData['range']}, "\
                    f"{testData['date']} ]",
                    f"$addMember [ {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ] ",
                    f"$addMember [ {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ]FILL",
                    f"$addMember [ {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addMember", app.setData,
                               Helpers.setStruct("integrante"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Nombre_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#-----------------------Test $addMember [*, Rango, *]-------------------------
@pytest.mark.asyncio
async def testValue_addMember_rangeEmpty(capfd):
    value = ""
    commands = [f"$addMember[{testData['name']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$addMember [{testData['name']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$addMember [ {testData['name']} , "\
                f" {value} , "\
                f" {testData['date']} ] ",
                f"$addMember [ {testData['name']} , "\
                f" {value}  , "\
                f" {testData['date']} ]FILL",
                f"$addMember [ {testData['name']} , "\
                f" {value}  , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addMember", app.setData,
                           Helpers.setStruct("integrante"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Rango_**\n" in out

@pytest.mark.asyncio
async def testValue_addMember_rangeLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$addMember[{testData['name']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$addMember [{testData['name']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$addMember [ {testData['name']} , "\
                f" {value} , "\
                f" {testData['date']} ] ",
                f"$addMember [ {testData['name']} , "\
                f" {value}  , "\
                f" {testData['date']} ]FILL",
                f"$addMember [ {testData['name']} , "\
                f" {value}  , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addMember", app.setData,
                           Helpers.setStruct("integrante"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Rango_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testValue_addMember_rangeStartChar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$addMember[{testData['name']},"\
                    f"{value},"\
                    f"{testData['date']}]",
                    f"$addMember [{testData['name']}, "\
                    f"{value}, "\
                    f"{testData['date']} ]",
                    f"$addMember [ {testData['name']} , "\
                    f" {value} , "\
                    f" {testData['date']} ] ",
                    f"$addMember [ {testData['name']} , "\
                    f" {value}  , "\
                    f" {testData['date']} ]FILL",
                    f"$addMember [ {testData['name']} , "\
                    f" {value}  , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addMember", app.setData,
                               Helpers.setStruct("integrante"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Rango_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testValue_addMember_rangeSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$addMember[{testData['name']},"\
                    f"{value},"\
                    f"{testData['date']}]",
                    f"$addMember [{testData['name']}, "\
                    f"{value}, "\
                    f"{testData['date']} ]",
                    f"$addMember [ {testData['name']} , "\
                    f" {value} , "\
                    f" {testData['date']} ] ",
                    f"$addMember [ {testData['name']} , "\
                    f" {value}  , "\
                    f" {testData['date']} ]FILL",
                    f"$addMember [ {testData['name']} , "\
                    f" {value}  , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addMember", app.setData,
                               Helpers.setStruct("integrante"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Rango_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testValue_addMember_rangeRepeatChar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$addMember[{testData['name']},"\
                    f"{value},"\
                    f"{testData['date']}]",
                    f"$addMember [{testData['name']}, "\
                    f"{value}, "\
                    f"{testData['date']} ]",
                    f"$addMember [ {testData['name']} , "\
                    f" {value} , "\
                    f" {testData['date']} ] ",
                    f"$addMember [ {testData['name']} , "\
                    f" {value}  , "\
                    f" {testData['date']} ]FILL",
                    f"$addMember [ {testData['name']} , "\
                    f" {value}  , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addMember", app.setData,
                               Helpers.setStruct("integrante"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Rango_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#----------------------Test $addMember [*, *, Fecha]----------------------
@pytest.mark.asyncio
async def testValue_addMember_dateEmpty(capfd):
    value = ""
    commands = [f"$addMember[{testData['name']},"\
                f"{testData['range']},"\
                f"{value}]",
                f"$addMember [{testData['name']}, "\
                f"{testData['range']}, "\
                f"{value} ]",
                f"$addMember [ {testData['name']} , "\
                f" {testData['range']} , "\
                f" {value} ] ",
                f"$addMember [ {testData['name']} , "\
                f" {testData['range']} , "\
                f" {value} ]FILL",
                f"$addMember [ {testData['name']} , "\
                f" {testData['range']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addMember", app.setData,
                           Helpers.setStruct("integrante"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha_**\n" in out

@pytest.mark.asyncio
async def testValue_addMember_dateInvalid(capfd):
    value = "test"
    commands = [f"$addMember[{testData['name']},"\
                f"{testData['range']},"\
                f"{value}]",
                f"$addMember [{testData['name']}, "\
                f"{testData['range']}, "\
                f"{value} ]",
                f"$addMember [ {testData['name']} , "\
                f" {testData['range']} , "\
                f" {value} ] ",
                f"$addMember [ {testData['name']} , "\
                f" {testData['range']} , "\
                f" {value} ]FILL",
                f"$addMember [ {testData['name']} , "\
                f" {testData['range']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addMember", app.setData,
                           Helpers.setStruct("integrante"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha_** "\
                "es invalido.\n" in out

#------------------------Test $updMember:id [ID, *, *, *]----------------------
@pytest.mark.asyncio
async def testValue_updMemberId_idEmpty(capfd):
    value = ""
    commands = [f"$updMember:id[{value},"\
                f"{testData['name']},"\
                f"{testData['range']},"\
                f"{testData['date']}]",
                f"$updMember:id [{value}, "\
                f"{testData['name']}, "\
                f"{testData['range']}, "\
                f"{testData['date']} ]",
                f"$updMember:id [ {value} , "\
                f" {testData['name']} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ] ",
                f"$updMember:id [ {value} , "\
                f" {testData['name']} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ]FILL",
                f"$updMember:id [ {value} , "\
                f" {testData['name']} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:id", app.updateData,
                           Helpers.updStruct("integrante", "id"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_ID_**\n" in out

@pytest.mark.asyncio
async def testValue_updMemberId_idInvalid(capfd):
    value = "test"
    commands = [f"$updMember:id[{value},"\
                f"{testData['name']},"\
                f"{testData['range']},"\
                f"{testData['date']}]",
                f"$updMember:id [{value}, "\
                f"{testData['name']}, "\
                f"{testData['range']}, "\
                f"{testData['date']} ]",
                f"$updMember:id [ {value} , "\
                f" {testData['name']} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ] ",
                f"$updMember:id [ {value} , "\
                f" {testData['name']} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ]FILL",
                f"$updMember:id [ {value} , "\
                f" {testData['name']} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:id", app.updateData,
                           Helpers.updStruct("integrante", "id"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_ID_** "\
                "es invalido.\n" in out

#---------------------Test $updMember:id [*, Nombre, *, *]---------------------
@pytest.mark.asyncio
async def testValue_updMemberId_nameEmpty(capfd):
    value = ""
    commands = [f"$updMember:id[{testData['id']},"
                f"{value},"\
                f"{testData['range']},"\
                f"{testData['date']}]",
                f"$updMember:id [{testData['id']}, "\
                f"{value}, "\
                f"{testData['range']}, "\
                f"{testData['date']} ]",
                f"$updMember:id [ {testData['id']} , "\
                f" {value} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ] ",
                f"$updMember:id [ {testData['id']} , "\
                f" {value} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ]FILL",
                f"$updMember:id [ {testData['id']} , "\
                f" {value} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:id", app.updateData,
                           Helpers.updStruct("integrante", "id"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Nombre_**\n" in out

@pytest.mark.asyncio
async def testValue_updMemberId_nameLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$updMember:id[{testData['id']},"
                f"{value},"\
                f"{testData['range']},"\
                f"{testData['date']}]",
                f"$updMember:id [{testData['id']}, "\
                f"{value}, "\
                f"{testData['range']}, "\
                f"{testData['date']} ]",
                f"$updMember:id [ {testData['id']} , "\
                f" {value} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ] ",
                f"$updMember:id [ {testData['id']} , "\
                f" {value} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ]FILL",
                f"$updMember:id [ {testData['id']} , "\
                f" {value} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:id", app.updateData,
                           Helpers.updStruct("integrante", "id"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Nombre_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testValue_updMemberId_nameStartChar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$updMember:id[{testData['id']},"
                    f"{value},"\
                    f"{testData['range']},"\
                    f"{testData['date']}]",
                    f"$updMember:id [{testData['id']}, "\
                    f"{value}, "\
                    f"{testData['range']}, "\
                    f"{testData['date']} ]",
                    f"$updMember:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ] ",
                    f"$updMember:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ]FILL",
                    f"$updMember:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updMember:id", app.updateData,
                               Helpers.updStruct("integrante", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testValue_updMemberId_nameSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$updMember:id[{testData['id']},"
                    f"{value},"\
                    f"{testData['range']},"\
                    f"{testData['date']}]",
                    f"$updMember:id [{testData['id']}, "\
                    f"{value}, "\
                    f"{testData['range']}, "\
                    f"{testData['date']} ]",
                    f"$updMember:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ] ",
                    f"$updMember:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ]FILL",
                    f"$updMember:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updMember:id", app.updateData,
                               Helpers.updStruct("integrante", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testValue_updMemberId_nameRepeatChar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$updMember:id[{testData['id']},"
                    f"{value},"\
                    f"{testData['range']},"\
                    f"{testData['date']}]",
                    f"$updMember:id [{testData['id']}, "\
                    f"{value}, "\
                    f"{testData['range']}, "\
                    f"{testData['date']} ]",
                    f"$updMember:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ] ",
                    f"$updMember:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ]FILL",
                    f"$updMember:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updMember:id", app.updateData,
                               Helpers.updStruct("integrante", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Nombre_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#--------------------Test $updMember:id [*, *, Rango, *]-----------------------
@pytest.mark.asyncio
async def testValue_updMemberId_rangeEmpty(capfd):
    value = ""
    commands = [f"$updMember:id[{testData['id']},"
                f"{testData['name']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$updMember:id [{testData['id']}, "\
                f"{testData['name']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$updMember:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {value} , "\
                f" {testData['date']} ] ",
                f"$updMember:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {value}  , "\
                f" {testData['date']} ]FILL",
                f"$updMember:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {value}  , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:id", app.updateData,
                           Helpers.updStruct("integrante", "id"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Rango_**\n" in out

@pytest.mark.asyncio
async def testValue_updMemberId_rangeLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$updMember:id[{testData['id']},"
                f"{testData['name']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$updMember:id [{testData['id']}, "\
                f"{testData['name']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$updMember:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {value} , "\
                f" {testData['date']} ] ",
                f"$updMember:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {value}  , "\
                f" {testData['date']} ]FILL",
                f"$updMember:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {value}  , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:id", app.updateData,
                           Helpers.updStruct("integrante", "id"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Rango_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testValue_updMemberId_rangeStartChar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$updMember:id[{testData['id']},"
                    f"{testData['name']},"\
                    f"{value},"\
                    f"{testData['date']}]",
                    f"$updMember:id [{testData['id']}, "\
                    f"{testData['name']}, "\
                    f"{value}, "\
                    f"{testData['date']} ]",
                    f"$updMember:id [ {testData['id']} , "\
                    f" {testData['name']} , "\
                    f" {value} , "\
                    f" {testData['date']} ] ",
                    f"$updMember:id [ {testData['id']} , "\
                    f" {testData['name']} , "\
                    f" {value}  , "\
                    f" {testData['date']} ]FILL",
                    f"$updMember:id [ {testData['id']} , "\
                    f" {testData['name']} , "\
                    f" {value}  , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updMember:id", app.updateData,
                               Helpers.updStruct("integrante", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Rango_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testValue_updMemberId_rangeSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$updMember:id[{testData['id']},"
                    f"{testData['name']},"\
                    f"{value},"\
                    f"{testData['date']}]",
                    f"$updMember:id [{testData['id']}, "\
                    f"{testData['name']}, "\
                    f"{value}, "\
                    f"{testData['date']} ]",
                    f"$updMember:id [ {testData['id']} , "\
                    f" {testData['name']} , "\
                    f" {value} , "\
                    f" {testData['date']} ] ",
                    f"$updMember:id [ {testData['id']} , "\
                    f" {testData['name']} , "\
                    f" {value}  , "\
                    f" {testData['date']} ]FILL",
                    f"$updMember:id [ {testData['id']} , "\
                    f" {testData['name']} , "\
                    f" {value}  , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updMember:id", app.updateData,
                               Helpers.updStruct("integrante", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Rango_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testValue_updMemberId_rangeRepeatChar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$updMember:id[{testData['id']},"
                    f"{testData['name']},"\
                    f"{value},"\
                    f"{testData['date']}]",
                    f"$updMember:id [{testData['id']}, "\
                    f"{testData['name']}, "\
                    f"{value}, "\
                    f"{testData['date']} ]",
                    f"$updMember:id [ {testData['id']} , "\
                    f" {testData['name']} , "\
                    f" {value} , "\
                    f" {testData['date']} ] ",
                    f"$updMember:id [ {testData['id']} , "\
                    f" {testData['name']} , "\
                    f" {value}  , "\
                    f" {testData['date']} ]FILL",
                    f"$updMember:id [ {testData['id']} , "\
                    f" {testData['name']} , "\
                    f" {value}  , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updMember:id", app.updateData,
                               Helpers.updStruct("integrante", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Rango_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#---------------------Test $updMember:id [*, *, *, Fecha]----------------------
@pytest.mark.asyncio
async def testValue_updMemberId_dateEmpty(capfd):
    value = ""
    commands = [f"$updMember:id[{testData['id']},"
                f"{testData['name']},"\
                f"{testData['range']},"\
                f"{value}]",
                f"$updMember:id [{testData['id']}, "\
                f"{testData['name']}, "\
                f"{testData['range']}, "\
                f"{value} ]",
                f"$updMember:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {testData['range']} , "\
                f" {value} ] ",
                f"$updMember:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {testData['range']} , "\
                f" {value} ]FILL",
                f"$updMember:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {testData['range']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:id", app.updateData,
                           Helpers.updStruct("integrante", "id"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha_**\n" in out

@pytest.mark.asyncio
async def testValue_updMemberId_dateInvalid(capfd):
    value = "test"
    commands = [f"$updMember:id[{testData['id']},"
                f"{testData['name']},"\
                f"{testData['range']},"\
                f"{value}]",
                f"$updMember:id [{testData['id']}, "\
                f"{testData['name']}, "\
                f"{testData['range']}, "\
                f"{value} ]",
                f"$updMember:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {testData['range']} , "\
                f" {value} ] ",
                f"$updMember:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {testData['range']} , "\
                f" {value} ]FILL",
                f"$updMember:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {testData['range']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:id", app.updateData,
                           Helpers.updStruct("integrante", "id"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha_** "\
                "es invalido.\n" in out

#---------------------Test $updMember:name [Nombre, *, *]----------------------
@pytest.mark.asyncio
async def testValue_updMemberName_nameEmpty(capfd):
    value = ""
    commands = [f"$updMember:name[{value},"\
                f"{testData['range']},"\
                f"{testData['date']}]",
                f"$updMember:name [{value}, "\
                f"{testData['range']}, "\
                f"{testData['date']} ]",
                f"$updMember:name [ {value} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ] ",
                f"$updMember:name [ {value} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ]FILL",
                f"$updMember:name [ {value} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:name", app.updateData,
                           Helpers.updStruct("integrante", "name"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Nombre_**\n" in out

@pytest.mark.asyncio
async def testValue_updMemberName_nameLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$updMember:name[{value},"\
                f"{testData['range']},"\
                f"{testData['date']}]",
                f"$updMember:name [{value}, "\
                f"{testData['range']}, "\
                f"{testData['date']} ]",
                f"$updMember:name [ {value} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ] ",
                f"$updMember:name [ {value} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ]FILL",
                f"$updMember:name [ {value} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:name", app.updateData,
                           Helpers.updStruct("integrante", "name"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Nombre_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testValue_updMemberName_nameStartChar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$updMember:name[{value},"\
                    f"{testData['range']},"\
                    f"{testData['date']}]",
                    f"$updMember:name [{value}, "\
                    f"{testData['range']}, "\
                    f"{testData['date']} ]",
                    f"$updMember:name [ {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ] ",
                    f"$updMember:name [ {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ]FILL",
                    f"$updMember:name [ {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updMember:name", app.updateData,
                               Helpers.updStruct("integrante", "name"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testValue_updMemberName_nameSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$updMember:name[{value},"\
                    f"{testData['range']},"\
                    f"{testData['date']}]",
                    f"$updMember:name [{value}, "\
                    f"{testData['range']}, "\
                    f"{testData['date']} ]",
                    f"$updMember:name [ {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ] ",
                    f"$updMember:name [ {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ]FILL",
                    f"$updMember:name [ {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updMember:name", app.updateData,
                           Helpers.updStruct("integrante", "name"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testValue_updMemberName_nameRepeatChar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$updMember:name[{value},"\
                    f"{testData['range']},"\
                    f"{testData['date']}]",
                    f"$updMember:name [{value}, "\
                    f"{testData['range']}, "\
                    f"{testData['date']} ]",
                    f"$updMember:name [ {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ] ",
                    f"$updMember:name [ {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ]FILL",
                    f"$updMember:name [ {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updMember:name", app.updateData,
                               Helpers.updStruct("integrante", "name"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Nombre_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#----------------------Test $updMember:name [*, Rango, *]----------------------
@pytest.mark.asyncio
async def testValue_updMemberName_rangeEmpty(capfd):
    value = ""
    commands = [f"$updMember:name[{testData['name']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$updMember:name [{testData['name']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$updMember:name [ {testData['name']} , "\
                f" {value} , "\
                f" {testData['date']} ] ",
                f"$updMember:name [ {testData['name']} , "\
                f" {value}  , "\
                f" {testData['date']} ]FILL",
                f"$updMember:name [ {testData['name']} , "\
                f" {value}  , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:name", app.updateData,
                           Helpers.updStruct("integrante", "name"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Rango_**\n" in out

@pytest.mark.asyncio
async def testValue_updMemberName_rangeLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$updMember:name[{testData['name']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$updMember:name [{testData['name']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$updMember:name [ {testData['name']} , "\
                f" {value} , "\
                f" {testData['date']} ] ",
                f"$updMember:name [ {testData['name']} , "\
                f" {value}  , "\
                f" {testData['date']} ]FILL",
                f"$updMember:name [ {testData['name']} , "\
                f" {value}  , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:name", app.updateData,
                           Helpers.updStruct("integrante", "name"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Rango_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testValue_updMemberName_rangeStartChar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$updMember:name[{testData['name']},"\
                    f"{value},"\
                    f"{testData['date']}]",
                    f"$updMember:name [{testData['name']}, "\
                    f"{value}, "\
                    f"{testData['date']} ]",
                    f"$updMember:name [ {testData['name']} , "\
                    f" {value} , "\
                    f" {testData['date']} ] ",
                    f"$updMember:name [ {testData['name']} , "\
                    f" {value}  , "\
                    f" {testData['date']} ]FILL",
                    f"$updMember:name [ {testData['name']} , "\
                    f" {value}  , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updMember:name", app.updateData,
                               Helpers.updStruct("integrante", "name"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Rango_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testValue_updMemberName_rangeSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$updMember:name[{testData['name']},"\
                    f"{value},"\
                    f"{testData['date']}]",
                    f"$updMember:name [{testData['name']}, "\
                    f"{value}, "\
                    f"{testData['date']} ]",
                    f"$updMember:name [ {testData['name']} , "\
                    f" {value} , "\
                    f" {testData['date']} ] ",
                    f"$updMember:name [ {testData['name']} , "\
                    f" {value}  , "\
                    f" {testData['date']} ]FILL",
                    f"$updMember:name [ {testData['name']} , "\
                    f" {value}  , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updMember:name", app.updateData,
                               Helpers.updStruct("integrante", "name"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Rango_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testValue_updMemberName_rangeRepeatChar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$updMember:name[{testData['name']},"\
                    f"{value},"\
                    f"{testData['date']}]",
                    f"$updMember:name [{testData['name']}, "\
                    f"{value}, "\
                    f"{testData['date']} ]",
                    f"$updMember:name [ {testData['name']} , "\
                    f" {value} , "\
                    f" {testData['date']} ] ",
                    f"$updMember:name [ {testData['name']} , "\
                    f" {value}  , "\
                    f" {testData['date']} ]FILL",
                    f"$updMember:name [ {testData['name']} , "\
                    f" {value}  , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updMember:name", app.updateData,
                               Helpers.updStruct("integrante", "name"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Rango_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#----------------------Test $updMember:name [*, *, Fecha]----------------------
@pytest.mark.asyncio
async def testValue_updMemberName_dateEmpty(capfd):
    value = ""
    commands = [f"$updMember:name[{testData['name']},"\
                f"{testData['range']},"\
                f"{value}]",
                f"$updMember:name [{testData['name']}, "\
                f"{testData['range']}, "\
                f"{value} ]",
                f"$updMember:name [ {testData['name']} , "\
                f" {testData['range']} , "\
                f" {value} ] ",
                f"$updMember:name [ {testData['name']} , "\
                f" {testData['range']} , "\
                f" {value} ]FILL",
                f"$updMember:name [ {testData['name']} , "\
                f" {testData['range']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:name", app.updateData,
                           Helpers.updStruct("integrante", "name"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha_**\n" in out

@pytest.mark.asyncio
async def testValue_updMemberName_dateInvalid(capfd):
    value = "test"
    commands = [f"$updMember:name[{testData['name']},"\
                f"{testData['range']},"\
                f"{value}]",
                f"$updMember:name [{testData['name']}, "\
                f"{testData['range']}, "\
                f"{value} ]",
                f"$updMember:name [ {testData['name']} , "\
                f" {testData['range']} , "\
                f" {value} ] ",
                f"$updMember:name [ {testData['name']} , "\
                f" {testData['range']} , "\
                f" {value} ]FILL",
                f"$updMember:name [ {testData['name']} , "\
                f" {testData['range']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:name", app.updateData,
                           Helpers.updStruct("integrante", "name"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha_** "\
                "es invalido.\n" in out

#------------------------------$delMember:id [ID]------------------------------
@pytest.mark.asyncio
async def testValue_delMemberId_idEmpty(capfd):
    value = ""
    commands = [f"$delMember:id[{value}],",
                f"$delMember:id [{value} ], ",
                f"$delMember:id [ {value} ], ",
                f"$delMember:id [ {value} ]FILL",
                f"$delMember:id [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delMember:id", app.deleteData,
                           Helpers.delStruct("integrante", "id"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_ID_**\n" in out

@pytest.mark.asyncio
async def testValue_delMemberId_idInvalid(capfd):
    value = "test"
    commands = [f"$delMember:id[{value}],",
                f"$delMember:id [{value} ], ",
                f"$delMember:id [ {value} ], ",
                f"$delMember:id [ {value} ]FILL",
                f"$delMember:id [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delMember:id", app.deleteData,
                           Helpers.delStruct("integrante", "id"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_ID_** "\
                "es invalido.\n" in out

#------------------------Test $delMember:name [Nombre]-------------------------
@pytest.mark.asyncio
async def testValue_delMemberName_nameEmpty(capfd):
    value = ""
    commands = [f"$delMember:name[{value}]",
                f"$delMember:name [{value} ]",
                f"$delMember:name [ {value} ]",
                f"$delMember:name [ {value} ]FILL",
                f"$delMember:name [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delMember:name", app.deleteData,
                           Helpers.delStruct("integrante", "name"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Nombre_**\n" in out

@pytest.mark.asyncio
async def testValue_delMemberName_nameLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$delMember:name[{value}]",
                f"$delMember:name [{value} ]",
                f"$delMember:name [ {value} ]",
                f"$delMember:name [ {value} ]FILL",
                f"$delMember:name [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delMember:name", app.deleteData,
                           Helpers.delStruct("integrante", "name"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Nombre_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testValue_delMemberName_nameStartChar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$delMember:name[{value}]",
                    f"$delMember:name [{value} ]",
                    f"$delMember:name [ {value} ]",
                    f"$delMember:name [ {value} ]FILL",
                    f"$delMember:name [ {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("delMember:name", app.deleteData,
                               Helpers.delStruct("integrante", "name"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testValue_delMemberName_nameSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$delMember:name[{value}]",
                    f"$delMember:name [{value} ]",
                    f"$delMember:name [ {value} ]",
                    f"$delMember:name [ {value} ]FILL",
                    f"$delMember:name [ {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("delMember:name", app.deleteData,
                               Helpers.delStruct("integrante", "name"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testValue_delMemberName_nameRepeatChar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$delMember:name[{value}]",
                    f"$delMember:name [{value} ]",
                    f"$delMember:name [ {value} ]",
                    f"$delMember:name [ {value} ]FILL",
                    f"$delMember:name [ {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("delMember:name", app.deleteData,
                               Helpers.delStruct("integrante", "name"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Nombre_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#-----------------------------$listMember:id [ID]------------------------------
@pytest.mark.asyncio
async def testValue_listMemberId_idEmpty(capfd):
    value = ""
    commands = [f"$listMember:id[{value}],",
                f"$listMember:id [{value} ], ",
                f"$listMember:id [ {value} ], ",
                f"$listMember:id [ {value} ]FILL",
                f"$listMember:id [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:id", app.getDatas,
                         Helpers.getStruct("integrante", ["id"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_ID_**\n" in out

@pytest.mark.asyncio
async def testValue_listMemberId_idInvalid(capfd):
    value = "test"
    commands = [f"$listMember:id[{value}],",
                f"$listMember:id [{value} ], ",
                f"$listMember:id [ {value} ], ",
                f"$listMember:id [ {value} ]FILL",
                f"$listMember:id [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:id", app.getDatas,
                         Helpers.getStruct("integrante", ["id"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_ID_** "\
                "es invalido.\n" in out

#-----------------------Test $listMember:name [Nombre]-------------------------
@pytest.mark.asyncio
async def testValue_listMemberName_nameEmpty(capfd):
    value = ""
    commands = [f"$listMember:name[{value}]",
                f"$listMember:name [{value} ]",
                f"$listMember:name [ {value} ]",
                f"$listMember:name [ {value} ]FILL",
                f"$listMember:name [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:name", app.getDatas,
                         Helpers.getStruct("integrante", ["name"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Nombre_**\n" in out

@pytest.mark.asyncio
async def testValue_listMemberName_nameLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$listMember:name[{value}]",
                f"$listMember:name [{value} ]",
                f"$listMember:name [ {value} ]",
                f"$listMember:name [ {value} ]FILL",
                f"$listMember:name [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:name", app.getDatas,
                         Helpers.getStruct("integrante", ["name"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Nombre_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testValue_listMemberName_nameStartChar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$listMember:name[{value}]",
                    f"$listMember:name [{value} ]",
                    f"$listMember:name [ {value} ]",
                    f"$listMember:name [ {value} ]FILL",
                    f"$listMember:name [ {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember:name", app.getDatas,
                             Helpers.getStruct("integrante", ["name"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testValue_listMemberName_nameSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$listMember:name[{value}]",
                    f"$listMember:name [{value} ]",
                    f"$listMember:name [ {value} ]",
                    f"$listMember:name [ {value} ]FILL",
                    f"$listMember:name [ {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember:name", app.getDatas,
                             Helpers.getStruct("integrante", ["name"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testValue_listMemberName_nameRepeatChar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$listMember:name[{value}]",
                    f"$listMember:name [{value} ]",
                    f"$listMember:name [ {value} ]",
                    f"$listMember:name [ {value} ]FILL",
                    f"$listMember:name [ {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember:name", app.getDatas,
                             Helpers.getStruct("integrante", ["name"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Nombre_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#---------------------Test $listMember:range [Rango]---------------------
@pytest.mark.asyncio
async def testValue_listMemberRange_memberEmpty(capfd):
    value = ""
    commands = [f"$listMember:range[{value}]",
                f"$listMember:range [{value} ]",
                f"$listMember:range [ {value} ]",
                f"$listMember:range [ {value} ]FILL",
                f"$listMember:range [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:range", app.getDatas,
                         Helpers.getStruct("integrante", ["rango"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Rango_**\n" in out

@pytest.mark.asyncio
async def testValue_listMemberRange_memberLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$listMember:range[{value}]",
                f"$listMember:range [{value} ]",
                f"$listMember:range [ {value} ]",
                f"$listMember:range [ {value} ]FILL",
                f"$listMember:range [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:range", app.getDatas,
                         Helpers.getStruct("integrante", ["rango"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Rango_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testValue_listMemberRange_memberStartChar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$listMember:range[{value}]",
                    f"$listMember:range [{value} ]",
                    f"$listMember:range [ {value} ]",
                    f"$listMember:range [ {value} ]FILL",
                    f"$listMember:range [ {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember:range", app.getDatas,
                             Helpers.getStruct("integrante", ["rango"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Rango_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testValue_listMemberRange_memberSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$listMember:range[{value}]",
                    f"$listMember:range [{value} ]",
                    f"$listMember:range [ {value} ]",
                    f"$listMember:range [ {value} ]FILL",
                    f"$listMember:range [ {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember:range", app.getDatas,
                             Helpers.getStruct("integrante", ["rango"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Rango_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testValue_listMemberRange_memberRepeatChar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$listMember:range[{value}]",
                    f"$listMember:range [{value} ]",
                    f"$listMember:range [ {value} ]",
                    f"$listMember:range [ {value} ]FILL",
                    f"$listMember:range [ {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember:range", app.getDatas,
                             Helpers.getStruct("integrante", ["rango"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Rango_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out