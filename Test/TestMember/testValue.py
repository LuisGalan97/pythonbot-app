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
               f"**_ID_** "\
                "es invalido.\n" in out

'''
#----------------------Test $updEvent:name [Nombre, *, *]----------------------
@pytest.mark.asyncio
async def testValue_updEventName_nameEmpty(capfd):
    value = ""
    commands = [f"$updEvent:name[{value},"\
                f"{testData['range']},"\
                f"{testData['date']}]",
                f"$updEvent:name [{value}, "\
                f"{testData['range']}, "\
                f"{testData['date']} ]",
                f"$updEvent:name [ {value} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ] ",
                f"$updEvent:name [ {value} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ]FILL",
                f"$updEvent:name [ {value} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updEvent:name", app.updateData,
                           Helpers.updStruct("evento", "name"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Nombre_**\n" in out

@pytest.mark.asyncio
async def testValue_updEventName_nameLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$updEvent:name[{value},"\
                f"{testData['range']},"\
                f"{testData['date']}]",
                f"$updEvent:name [{value}, "\
                f"{testData['range']}, "\
                f"{testData['date']} ]",
                f"$updEvent:name [ {value} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ] ",
                f"$updEvent:name [ {value} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ]FILL",
                f"$updEvent:name [ {value} , "\
                f" {testData['range']} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updEvent:name", app.updateData,
                           Helpers.updStruct("evento", "name"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Nombre_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testValue_updEventName_nameStartChar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$updEvent:name[{value},"\
                    f"{testData['range']},"\
                    f"{testData['date']}]",
                    f"$updEvent:name [{value}, "\
                    f"{testData['range']}, "\
                    f"{testData['date']} ]",
                    f"$updEvent:name [ {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ] ",
                    f"$updEvent:name [ {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ]FILL",
                    f"$updEvent:name [ {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updEvent:name", app.updateData,
                               Helpers.updStruct("evento", "name"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testValue_updEventName_nameSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$updEvent:name[{value},"\
                    f"{testData['range']},"\
                    f"{testData['date']}]",
                    f"$updEvent:name [{value}, "\
                    f"{testData['range']}, "\
                    f"{testData['date']} ]",
                    f"$updEvent:name [ {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ] ",
                    f"$updEvent:name [ {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ]FILL",
                    f"$updEvent:name [ {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updEvent:name", app.updateData,
                               Helpers.updStruct("evento", "name"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testValue_updEventName_nameRepeatChar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$updEvent:name[{value},"\
                    f"{testData['range']},"\
                    f"{testData['date']}]",
                    f"$updEvent:name [{value}, "\
                    f"{testData['range']}, "\
                    f"{testData['date']} ]",
                    f"$updEvent:name [ {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ] ",
                    f"$updEvent:name [ {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ]FILL",
                    f"$updEvent:name [ {value} , "\
                    f" {testData['range']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updEvent:name", app.updateData,
                               Helpers.updStruct("evento", "name"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Nombre_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#---------------------Test $updEvent:name [*, Puntos, *]-----------------------
@pytest.mark.asyncio
async def testValue_updEventName_rangeEmpty(capfd):
    value = ""
    commands = [f"$updEvent:name[{testData['name']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$updEvent:name [{testData['name']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$updEvent:name [ {testData['name']} , "\
                f" {value} , "\
                f" {testData['date']} ] ",
                f"$updEvent:name [ {testData['name']} , "\
                f" {value}  , "\
                f" {testData['date']} ]FILL",
                f"$updEvent:name [ {testData['name']} , "\
                f" {value}  , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updEvent:name", app.updateData,
                           Helpers.updStruct("evento", "name"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Puntos_**\n" in out

@pytest.mark.asyncio
async def testValue_updEventName_rangeInvalid(capfd):
    value = "test"
    commands = [f"$updEvent:name[{testData['name']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$updEvent:name [{testData['name']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$updEvent:name [ {testData['name']} , "\
                f" {value} , "\
                f" {testData['date']} ] ",
                f"$updEvent:name [ {testData['name']} , "\
                f" {value}  , "\
                f" {testData['date']} ]FILL",
                f"$updEvent:name [ {testData['name']} , "\
                f" {value}  , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updEvent:name", app.updateData,
                           Helpers.updStruct("evento", "name"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Puntos_** "\
                "es invalido.\n" in out

#-------------------Test $updEvent:name [*, *, Descripción]--------------------
@pytest.mark.asyncio
async def testValue_updEventName_dateriptionEmpty(capfd):
    value = ""
    commands = [f"$updEvent:name[{testData['name']},"\
                f"{testData['range']},"\
                f"{value}]",
                f"$updEvent:name [{testData['name']}, "\
                f"{testData['range']}, "\
                f"{value} ]",
                f"$updEvent:name [ {testData['name']} , "\
                f" {testData['range']} , "\
                f" {value} ] ",
                f"$updEvent:name [ {testData['name']} , "\
                f" {testData['range']} , "\
                f" {value} ]FILL",
                f"$updEvent:name [ {testData['name']} , "\
                f" {testData['range']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updEvent:name", app.updateData,
                           Helpers.updStruct("evento", "name"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Descripción_**\n" in out

@pytest.mark.asyncio
async def testValue_updEventName_dateriptionLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$updEvent:name[{testData['name']},"\
                f"{testData['range']},"\
                f"{value}]",
                f"$updEvent:name [{testData['name']}, "\
                f"{testData['range']}, "\
                f"{value} ]",
                f"$updEvent:name [ {testData['name']} , "\
                f" {testData['range']} , "\
                f" {value} ] ",
                f"$updEvent:name [ {testData['name']} , "\
                f" {testData['range']} , "\
                f" {value} ]FILL",
                f"$updEvent:name [ {testData['name']} , "\
                f" {testData['range']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updEvent:name", app.updateData,
                           Helpers.updStruct("evento", "name"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Descripción_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testValue_updEventName_dateriptionStartChar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$updEvent:name[{testData['name']},"\
                    f"{testData['range']},"\
                    f"{value}]",
                    f"$updEvent:name [{testData['name']}, "\
                    f"{testData['range']}, "\
                    f"{value} ]",
                    f"$updEvent:name [ {testData['name']} , "\
                    f" {testData['range']} , "\
                    f" {value} ] ",
                    f"$updEvent:name [ {testData['name']} , "\
                    f" {testData['range']} , "\
                    f" {value} ]FILL",
                    f"$updEvent:name [ {testData['name']} , "\
                    f" {testData['range']} , "\
                    f" {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updEvent:name", app.updateData,
                               Helpers.updStruct("evento", "name"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Descripción_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testValue_updEventName_dateriptionSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$updEvent:name[{testData['name']},"\
                    f"{testData['range']},"\
                    f"{value}]",
                    f"$updEvent:name [{testData['name']}, "\
                    f"{testData['range']}, "\
                    f"{value} ]",
                    f"$updEvent:name [ {testData['name']} , "\
                    f" {testData['range']} , "\
                    f" {value} ] ",
                    f"$updEvent:name [ {testData['name']} , "\
                    f" {testData['range']} , "\
                    f" {value} ]FILL",
                    f"$updEvent:name [ {testData['name']} , "\
                    f" {testData['range']} , "\
                    f" {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updEvent:name", app.updateData,
                               Helpers.updStruct("evento", "name"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Descripción_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testValue_updEventName_dateriptionRepeatChar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$updEvent:name[{testData['name']},"\
                    f"{testData['range']},"\
                    f"{value}]",
                    f"$updEvent:name [{testData['name']}, "\
                    f"{testData['range']}, "\
                    f"{value} ]",
                    f"$updEvent:name [ {testData['name']} , "\
                    f" {testData['range']} , "\
                    f" {value} ] ",
                    f"$updEvent:name [ {testData['name']} , "\
                    f" {testData['range']} , "\
                    f" {value} ]FILL",
                    f"$updEvent:name [ {testData['name']} , "\
                    f" {testData['range']} , "\
                    f" {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updEvent:name", app.updateData,
                               Helpers.updStruct("evento", "name"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Descripción_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#-------------------------------$delEvent:id [ID]------------------------------
@pytest.mark.asyncio
async def testValue_delEventId_idEmpty(capfd):
    value = ""
    commands = [f"$delEvent:id[{value}],",
                f"$delEvent:id [{value} ], ",
                f"$delEvent:id [ {value} ], ",
                f"$delEvent:id [ {value} ]FILL",
                f"$delEvent:id [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delEvent:id", app.deleteData,
                           Helpers.delStruct("evento", "id"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_ID_**\n" in out

@pytest.mark.asyncio
async def testValue_delEventId_idInvalid(capfd):
    value = "test"
    commands = [f"$delEvent:id[{value}],",
                f"$delEvent:id [{value} ], ",
                f"$delEvent:id [ {value} ], ",
                f"$delEvent:id [ {value} ]FILL",
                f"$delEvent:id [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delEvent:id", app.deleteData,
                           Helpers.delStruct("evento", "id"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_ID_** "\
                "es invalido.\n" in out

#-------------------------Test $delEvent:name [Nombre]-------------------------
@pytest.mark.asyncio
async def testValue_delEventName_nameEmpty(capfd):
    value = ""
    commands = [f"$delEvent:name[{value}]",
                f"$delEvent:name [{value} ]",
                f"$delEvent:name [ {value} ]",
                f"$delEvent:name [ {value} ]FILL",
                f"$delEvent:name [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delEvent:name", app.deleteData,
                           Helpers.delStruct("evento", "name"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Nombre_**\n" in out

@pytest.mark.asyncio
async def testValue_delEventName_nameLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$delEvent:name[{value}]",
                f"$delEvent:name [{value} ]",
                f"$delEvent:name [ {value} ]",
                f"$delEvent:name [ {value} ]FILL",
                f"$delEvent:name [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delEvent:name", app.deleteData,
                           Helpers.delStruct("evento", "name"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Nombre_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testValue_delEventName_nameStartChar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$delEvent:name[{value}]",
                    f"$delEvent:name [{value} ]",
                    f"$delEvent:name [ {value} ]",
                    f"$delEvent:name [ {value} ]FILL",
                    f"$delEvent:name [ {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("delEvent:name", app.deleteData,
                               Helpers.delStruct("evento", "name"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testValue_delEventName_nameSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$delEvent:name[{value}]",
                    f"$delEvent:name [{value} ]",
                    f"$delEvent:name [ {value} ]",
                    f"$delEvent:name [ {value} ]FILL",
                    f"$delEvent:name [ {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("delEvent:name", app.deleteData,
                               Helpers.delStruct("evento", "name"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testValue_delEventName_nameRepeatChar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$delEvent:name[{value}]",
                    f"$delEvent:name [{value} ]",
                    f"$delEvent:name [ {value} ]",
                    f"$delEvent:name [ {value} ]FILL",
                    f"$delEvent:name [ {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("delEvent:name", app.deleteData,
                               Helpers.delStruct("evento", "name"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Nombre_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#------------------------------$listEvent:id [ID]------------------------------
@pytest.mark.asyncio
async def testValue_listEventId_idEmpty(capfd):
    value = ""
    commands = [f"$listEvent:id[{value}],",
                f"$listEvent:id [{value} ], ",
                f"$listEvent:id [ {value} ], ",
                f"$listEvent:id [ {value} ]FILL",
                f"$listEvent:id [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listEvent:id", app.getDatas,
                         Helpers.getStruct("evento", ["id"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_ID_**\n" in out

@pytest.mark.asyncio
async def testValue_listEventId_idInvalid(capfd):
    value = "test"
    commands = [f"$listEvent:id[{value}],",
                f"$listEvent:id [{value} ], ",
                f"$listEvent:id [ {value} ], ",
                f"$listEvent:id [ {value} ]FILL",
                f"$listEvent:id [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listEvent:id", app.getDatas,
                         Helpers.getStruct("evento", ["id"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_ID_** "\
                "es invalido.\n" in out

#------------------------Test $listEvent:name [Nombre]-------------------------
@pytest.mark.asyncio
async def testValue_listEventName_nameEmpty(capfd):
    value = ""
    commands = [f"$listEvent:name[{value}]",
                f"$listEvent:name [{value} ]",
                f"$listEvent:name [ {value} ]",
                f"$listEvent:name [ {value} ]FILL",
                f"$listEvent:name [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listEvent:name", app.getDatas,
                         Helpers.getStruct("evento", ["name"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Nombre_**\n" in out

@pytest.mark.asyncio
async def testValue_listEventName_nameLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$listEvent:name[{value}]",
                f"$listEvent:name [{value} ]",
                f"$listEvent:name [ {value} ]",
                f"$listEvent:name [ {value} ]FILL",
                f"$listEvent:name [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listEvent:name", app.getDatas,
                         Helpers.getStruct("evento", ["name"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Nombre_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testValue_listEventName_nameStartChar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$listEvent:name[{value}]",
                    f"$listEvent:name [{value} ]",
                    f"$listEvent:name [ {value} ]",
                    f"$listEvent:name [ {value} ]FILL",
                    f"$listEvent:name [ {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listEvent:name", app.getDatas,
                             Helpers.getStruct("evento", ["name"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testValue_listEventName_nameSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$listEvent:name[{value}]",
                    f"$listEvent:name [{value} ]",
                    f"$listEvent:name [ {value} ]",
                    f"$listEvent:name [ {value} ]FILL",
                    f"$listEvent:name [ {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listEvent:name", app.getDatas,
                             Helpers.getStruct("evento", ["name"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testValue_listEventName_nameRepeatChar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$listEvent:name[{value}]",
                    f"$listEvent:name [{value} ]",
                    f"$listEvent:name [ {value} ]",
                    f"$listEvent:name [ {value} ]FILL",
                    f"$listEvent:name [ {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listEvent:name", app.getDatas,
                             Helpers.getStruct("evento", ["name"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Nombre_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out
'''