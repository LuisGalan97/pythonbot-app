import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Helpers.helpers import Helpers
from collections import namedtuple

testData = {
    "id" : "1",
    "name" : "TestRange",
    "control" : 5,
    "desc" : "Descripción"
}

Message = namedtuple('Message', ['author', 'content'])
Client = namedtuple('Client', ['user'])
app = AppHandler()

#----------------------Test $addRange [Nombre, *, *]----------------------
@pytest.mark.asyncio
async def testRangeValue_addRange_nameEmpty(capfd):
    value = ""
    commands = [f"$addRange[{value},"\
                f"{testData['control']},"\
                f"{testData['desc']}]",
                f"$addRange [{value}, "\
                f"{testData['control']}, "\
                f"{testData['desc']} ]",
                f"$addRange [ {value} , "\
                f" {testData['control']} , "\
                f" {testData['desc']} ] ",
                f"$addRange [ {value} , "\
                f" {testData['control']} , "\
                f" {testData['desc']} ]FILL",
                f"$addRange [ {value} , "\
                f" {testData['control']} , "\
                f" {testData['desc']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addRange", app.setData,
                           Helpers.setStruct("rango"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Nombre_**\n" in out

@pytest.mark.asyncio
async def testRangeValue_addRange_nameLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$addRange[{value},"\
                f"{testData['control']},"\
                f"{testData['desc']}]",
                f"$addRange [{value}, "\
                f"{testData['control']}, "\
                f"{testData['desc']} ]",
                f"$addRange [ {value} , "\
                f" {testData['control']} , "\
                f" {testData['desc']} ] ",
                f"$addRange [ {value} , "\
                f" {testData['control']} , "\
                f" {testData['desc']} ]FILL",
                f"$addRange [ {value} , "\
                f" {testData['control']} , "\
                f" {testData['desc']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addRange", app.setData,
                           Helpers.setStruct("rango"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Nombre_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testRangeValue_addRange_nameStartChar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$addRange[{value},"\
                    f"{testData['control']},"\
                    f"{testData['desc']}]",
                    f"$addRange [{value}, "\
                    f"{testData['control']}, "\
                    f"{testData['desc']} ]",
                    f"$addRange [ {value} , "\
                    f" {testData['control']} , "\
                    f" {testData['desc']} ] ",
                    f"$addRange [ {value} , "\
                    f" {testData['control']} , "\
                    f" {testData['desc']} ]FILL",
                    f"$addRange [ {value} , "\
                    f" {testData['control']} , "\
                    f" {testData['desc']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addRange", app.setData,
                               Helpers.setStruct("rango"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testRangeValue_addRange_nameSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$addRange[{value},"\
                    f"{testData['control']},"\
                    f"{testData['desc']}]",
                    f"$addRange [{value}, "\
                    f"{testData['control']}, "\
                    f"{testData['desc']} ]",
                    f"$addRange [ {value} , "\
                    f" {testData['control']} , "\
                    f" {testData['desc']} ] ",
                    f"$addRange [ {value} , "\
                    f" {testData['control']} , "\
                    f" {testData['desc']} ]FILL",
                    f"$addRange [ {value} , "\
                    f" {testData['control']} , "\
                    f" {testData['desc']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addRange", app.setData,
                               Helpers.setStruct("rango"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testRangeValue_addRange_nameRepeatChar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$addRange[{value},"\
                    f"{testData['control']},"\
                    f"{testData['desc']}]",
                    f"$addRange [{value}, "\
                    f"{testData['control']}, "\
                    f"{testData['desc']} ]",
                    f"$addRange [ {value} , "\
                    f" {testData['control']} , "\
                    f" {testData['desc']} ] ",
                    f"$addRange [ {value} , "\
                    f" {testData['control']} , "\
                    f" {testData['desc']} ]FILL",
                    f"$addRange [ {value} , "\
                    f" {testData['control']} , "\
                    f" {testData['desc']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addRange", app.setData,
                               Helpers.setStruct("rango"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Nombre_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#-----------------------Test $addRange [*, Control, *]-------------------------
@pytest.mark.asyncio
async def testRangeValue_addRange_controlEmpty(capfd):
    value = ""
    commands = [f"$addRange[{testData['name']},"\
                f"{value},"\
                f"{testData['desc']}]",
                f"$addRange [{testData['name']}, "\
                f"{value}, "\
                f"{testData['desc']} ]",
                f"$addRange [ {testData['name']} , "\
                f" {value} , "\
                f" {testData['desc']} ] ",
                f"$addRange [ {testData['name']} , "\
                f" {value}  , "\
                f" {testData['desc']} ]FILL",
                f"$addRange [ {testData['name']} , "\
                f" {value}  , "\
                f" {testData['desc']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addRange", app.setData,
                           Helpers.setStruct("rango"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Puntos_**\n" in out

@pytest.mark.asyncio
async def testRangeValue_addRange_controlInvalid(capfd):
    value = "test"
    commands = [f"$addRange[{testData['name']},"\
                f"{value},"\
                f"{testData['desc']}]",
                f"$addRange [{testData['name']}, "\
                f"{value}, "\
                f"{testData['desc']} ]",
                f"$addRange [ {testData['name']} , "\
                f" {value} , "\
                f" {testData['desc']} ] ",
                f"$addRange [ {testData['name']} , "\
                f" {value}  , "\
                f" {testData['desc']} ]FILL",
                f"$addRange [ {testData['name']} , "\
                f" {value}  , "\
                f" {testData['desc']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addRange", app.setData,
                           Helpers.setStruct("rango"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Puntos_** "\
                "es invalido.\n" in out

#----------------------Test $addRange [*, *, Descripción]----------------------
@pytest.mark.asyncio
async def testRangeValue_addRange_descriptionEmpty(capfd):
    value = ""
    commands = [f"$addRange[{testData['name']},"\
                f"{testData['control']},"\
                f"{value}]",
                f"$addRange [{testData['name']}, "\
                f"{testData['control']}, "\
                f"{value} ]",
                f"$addRange [ {testData['name']} , "\
                f" {testData['control']} , "\
                f" {value} ] ",
                f"$addRange [ {testData['name']} , "\
                f" {testData['control']} , "\
                f" {value} ]FILL",
                f"$addRange [ {testData['name']} , "\
                f" {testData['control']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addRange", app.setData,
                           Helpers.setStruct("rango"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Descripción_**\n" in out

@pytest.mark.asyncio
async def testRangeValue_addRange_descriptionLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$addRange[{testData['name']},"\
                f"{testData['control']},"\
                f"{value}]",
                f"$addRange [{testData['name']}, "\
                f"{testData['control']}, "\
                f"{value} ]",
                f"$addRange [ {testData['name']} , "\
                f" {testData['control']} , "\
                f" {value} ] ",
                f"$addRange [ {testData['name']} , "\
                f" {testData['control']} , "\
                f" {value} ]FILL",
                f"$addRange [ {testData['name']} , "\
                f" {testData['control']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addRange", app.setData,
                           Helpers.setStruct("rango"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Descripción_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testRangeValue_addRange_descriptionStartChar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$addRange[{testData['name']},"\
                    f"{testData['control']},"\
                    f"{value}]",
                    f"$addRange [{testData['name']}, "\
                    f"{testData['control']}, "\
                    f"{value} ]",
                    f"$addRange [ {testData['name']} , "\
                    f" {testData['control']} , "\
                    f" {value} ] ",
                    f"$addRange [ {testData['name']} , "\
                    f" {testData['control']} , "\
                    f" {value} ]FILL",
                    f"$addRange [ {testData['name']} , "\
                    f" {testData['control']} , "\
                    f" {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addRange", app.setData,
                               Helpers.setStruct("rango"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Descripción_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testRangeValue_addRange_descriptionSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$addRange[{testData['name']},"\
                    f"{testData['control']},"\
                    f"{value}]",
                    f"$addRange [{testData['name']}, "\
                    f"{testData['control']}, "\
                    f"{value} ]",
                    f"$addRange [ {testData['name']} , "\
                    f" {testData['control']} , "\
                    f" {value} ] ",
                    f"$addRange [ {testData['name']} , "\
                    f" {testData['control']} , "\
                    f" {value} ]FILL",
                    f"$addRange [ {testData['name']} , "\
                    f" {testData['control']} , "\
                    f" {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addRange", app.setData,
                               Helpers.setStruct("rango"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Descripción_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testRangeValue_addRange_descriptionRepeatChar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$addRange[{testData['name']},"\
                    f"{testData['control']},"\
                    f"{value}]",
                    f"$addRange [{testData['name']}, "\
                    f"{testData['control']}, "\
                    f"{value} ]",
                    f"$addRange [ {testData['name']} , "\
                    f" {testData['control']} , "\
                    f" {value} ] ",
                    f"$addRange [ {testData['name']} , "\
                    f" {testData['control']} , "\
                    f" {value} ]FILL",
                    f"$addRange [ {testData['name']} , "\
                    f" {testData['control']} , "\
                    f" {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addRange", app.setData,
                               Helpers.setStruct("rango"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Descripción_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#------------------------Test $updRange:id [ID, *, *, *]----------------------
@pytest.mark.asyncio
async def testRangeValue_updRangeId_idEmpty(capfd):
    value = ""
    commands = [f"$updRange:id[{value},"\
                f"{testData['name']},"\
                f"{testData['control']},"\
                f"{testData['desc']}]",
                f"$updRange:id [{value}, "\
                f"{testData['name']}, "\
                f"{testData['control']}, "\
                f"{testData['desc']} ]",
                f"$updRange:id [ {value} , "\
                f" {testData['name']} , "\
                f" {testData['control']} , "\
                f" {testData['desc']} ] ",
                f"$updRange:id [ {value} , "\
                f" {testData['name']} , "\
                f" {testData['control']} , "\
                f" {testData['desc']} ]FILL",
                f"$updRange:id [ {value} , "\
                f" {testData['name']} , "\
                f" {testData['control']} , "\
                f" {testData['desc']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updRange:id", app.updateData,
                           Helpers.updStruct("rango", "id"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_ID_**\n" in out

@pytest.mark.asyncio
async def testRangeValue_updRangeId_idInvalid(capfd):
    value = "test"
    commands = [f"$updRange:id[{value},"\
                f"{testData['name']},"\
                f"{testData['control']},"\
                f"{testData['desc']}]",
                f"$updRange:id [{value}, "\
                f"{testData['name']}, "\
                f"{testData['control']}, "\
                f"{testData['desc']} ]",
                f"$updRange:id [ {value} , "\
                f" {testData['name']} , "\
                f" {testData['control']} , "\
                f" {testData['desc']} ] ",
                f"$updRange:id [ {value} , "\
                f" {testData['name']} , "\
                f" {testData['control']} , "\
                f" {testData['desc']} ]FILL",
                f"$updRange:id [ {value} , "\
                f" {testData['name']} , "\
                f" {testData['control']} , "\
                f" {testData['desc']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updRange:id", app.updateData,
                           Helpers.updStruct("rango", "id"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_ID_** "\
                "es invalido.\n" in out

#----------------------Test $updRange:id [*, Nombre, *, *]---------------------
@pytest.mark.asyncio
async def testRangeValue_updRangeId_nameEmpty(capfd):
    value = ""
    commands = [f"$updRange:id[{testData['id']},"
                f"{value},"\
                f"{testData['control']},"\
                f"{testData['desc']}]",
                f"$updRange:id [{testData['id']}, "\
                f"{value}, "\
                f"{testData['control']}, "\
                f"{testData['desc']} ]",
                f"$updRange:id [ {testData['id']} , "\
                f" {value} , "\
                f" {testData['control']} , "\
                f" {testData['desc']} ] ",
                f"$updRange:id [ {testData['id']} , "\
                f" {value} , "\
                f" {testData['control']} , "\
                f" {testData['desc']} ]FILL",
                f"$updRange:id [ {testData['id']} , "\
                f" {value} , "\
                f" {testData['control']} , "\
                f" {testData['desc']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updRange:id", app.updateData,
                           Helpers.updStruct("rango", "id"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Nombre_**\n" in out

@pytest.mark.asyncio
async def testRangeValue_updRangeId_nameLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$updRange:id[{testData['id']},"
                f"{value},"\
                f"{testData['control']},"\
                f"{testData['desc']}]",
                f"$updRange:id [{testData['id']}, "\
                f"{value}, "\
                f"{testData['control']}, "\
                f"{testData['desc']} ]",
                f"$updRange:id [ {testData['id']} , "\
                f" {value} , "\
                f" {testData['control']} , "\
                f" {testData['desc']} ] ",
                f"$updRange:id [ {testData['id']} , "\
                f" {value} , "\
                f" {testData['control']} , "\
                f" {testData['desc']} ]FILL",
                f"$updRange:id [ {testData['id']} , "\
                f" {value} , "\
                f" {testData['control']} , "\
                f" {testData['desc']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updRange:id", app.updateData,
                           Helpers.updStruct("rango", "id"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Nombre_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testRangeValue_updRangeId_nameStartChar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$updRange:id[{testData['id']},"
                    f"{value},"\
                    f"{testData['control']},"\
                    f"{testData['desc']}]",
                    f"$updRange:id [{testData['id']}, "\
                    f"{value}, "\
                    f"{testData['control']}, "\
                    f"{testData['desc']} ]",
                    f"$updRange:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['control']} , "\
                    f" {testData['desc']} ] ",
                    f"$updRange:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['control']} , "\
                    f" {testData['desc']} ]FILL",
                    f"$updRange:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['control']} , "\
                    f" {testData['desc']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updRange:id", app.updateData,
                               Helpers.updStruct("rango", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testRangeValue_updRangeId_nameSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$updRange:id[{testData['id']},"
                    f"{value},"\
                    f"{testData['control']},"\
                    f"{testData['desc']}]",
                    f"$updRange:id [{testData['id']}, "\
                    f"{value}, "\
                    f"{testData['control']}, "\
                    f"{testData['desc']} ]",
                    f"$updRange:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['control']} , "\
                    f" {testData['desc']} ] ",
                    f"$updRange:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['control']} , "\
                    f" {testData['desc']} ]FILL",
                    f"$updRange:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['control']} , "\
                    f" {testData['desc']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updRange:id", app.updateData,
                               Helpers.updStruct("rango", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testRangeValue_updRangeId_nameRepeatChar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$updRange:id[{testData['id']},"
                    f"{value},"\
                    f"{testData['control']},"\
                    f"{testData['desc']}]",
                    f"$updRange:id [{testData['id']}, "\
                    f"{value}, "\
                    f"{testData['control']}, "\
                    f"{testData['desc']} ]",
                    f"$updRange:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['control']} , "\
                    f" {testData['desc']} ] ",
                    f"$updRange:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['control']} , "\
                    f" {testData['desc']} ]FILL",
                    f"$updRange:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['control']} , "\
                    f" {testData['desc']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updRange:id", app.updateData,
                               Helpers.updStruct("rango", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Nombre_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#--------------------Test $updRange:id [*, *, Control, *]-----------------------
@pytest.mark.asyncio
async def testRangeValue_updRangeId_controlEmpty(capfd):
    value = ""
    commands = [f"$updRange:id[{testData['id']},"
                f"{testData['name']},"\
                f"{value},"\
                f"{testData['desc']}]",
                f"$updRange:id [{testData['id']}, "\
                f"{testData['name']}, "\
                f"{value}, "\
                f"{testData['desc']} ]",
                f"$updRange:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {value} , "\
                f" {testData['desc']} ] ",
                f"$updRange:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {value}  , "\
                f" {testData['desc']} ]FILL",
                f"$updRange:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {value}  , "\
                f" {testData['desc']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updRange:id", app.updateData,
                           Helpers.updStruct("rango", "id"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Puntos_**\n" in out

@pytest.mark.asyncio
async def testRangeValue_updRangeId_controlInvalid(capfd):
    value = "test"
    commands = [f"$updRange:id[{testData['id']},"
                f"{testData['name']},"\
                f"{value},"\
                f"{testData['desc']}]",
                f"$updRange:id [{testData['id']}, "\
                f"{testData['name']}, "\
                f"{value}, "\
                f"{testData['desc']} ]",
                f"$updRange:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {value} , "\
                f" {testData['desc']} ] ",
                f"$updRange:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {value}  , "\
                f" {testData['desc']} ]FILL",
                f"$updRange:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {value}  , "\
                f" {testData['desc']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updRange:id", app.updateData,
                           Helpers.updStruct("rango", "id"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Puntos_** "\
                "es invalido.\n" in out

#-------------------Test $updRange:id [*, *, *, Descripción]-------------------
@pytest.mark.asyncio
async def testRangeValue_updRangeId_descriptionEmpty(capfd):
    value = ""
    commands = [f"$updRange:id[{testData['id']},"
                f"{testData['name']},"\
                f"{testData['control']},"\
                f"{value}]",
                f"$updRange:id [{testData['id']}, "\
                f"{testData['name']}, "\
                f"{testData['control']}, "\
                f"{value} ]",
                f"$updRange:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {testData['control']} , "\
                f" {value} ] ",
                f"$updRange:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {testData['control']} , "\
                f" {value} ]FILL",
                f"$updRange:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {testData['control']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updRange:id", app.updateData,
                           Helpers.updStruct("rango", "id"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Descripción_**\n" in out

@pytest.mark.asyncio
async def testRangeValue_updRangeId_descriptionLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$updRange:id[{testData['id']},"
                f"{testData['name']},"\
                f"{testData['control']},"\
                f"{value}]",
                f"$updRange:id [{testData['id']}, "\
                f"{testData['name']}, "\
                f"{testData['control']}, "\
                f"{value} ]",
                f"$updRange:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {testData['control']} , "\
                f" {value} ] ",
                f"$updRange:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {testData['control']} , "\
                f" {value} ]FILL",
                f"$updRange:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {testData['control']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updRange:id", app.updateData,
                           Helpers.updStruct("rango", "id"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Descripción_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testRangeValue_updRangeId_descriptionStartChar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$updRange:id[{testData['id']},"
                    f"{testData['name']},"\
                    f"{testData['control']},"\
                    f"{value}]",
                    f"$updRange:id [{testData['id']}, "\
                    f"{testData['name']}, "\
                    f"{testData['control']}, "\
                    f"{value} ]",
                    f"$updRange:id [ {testData['id']} , "\
                    f" {testData['name']} , "\
                    f" {testData['control']} , "\
                    f" {value} ] ",
                    f"$updRange:id [ {testData['id']} , "\
                    f" {testData['name']} , "\
                    f" {testData['control']} , "\
                    f" {value} ]FILL",
                    f"$updRange:id [ {testData['id']} , "\
                    f" {testData['name']} , "\
                    f" {testData['control']} , "\
                    f" {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updRange:id", app.updateData,
                               Helpers.updStruct("rango", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Descripción_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testRangeValue_updRangeId_descriptionSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$updRange:id[{testData['id']},"
                    f"{testData['name']},"\
                    f"{testData['control']},"\
                    f"{value}]",
                    f"$updRange:id [{testData['id']}, "\
                    f"{testData['name']}, "\
                    f"{testData['control']}, "\
                    f"{value} ]",
                    f"$updRange:id [ {testData['id']} , "\
                    f" {testData['name']} , "\
                    f" {testData['control']} , "\
                    f" {value} ] ",
                    f"$updRange:id [ {testData['id']} , "\
                    f" {testData['name']} , "\
                    f" {testData['control']} , "\
                    f" {value} ]FILL",
                    f"$updRange:id [ {testData['id']} , "\
                    f" {testData['name']} , "\
                    f" {testData['control']} , "\
                    f" {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updRange:id", app.updateData,
                               Helpers.updStruct("rango", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Descripción_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testRangeValue_updRangeId_descriptionRepeatChar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$updRange:id[{testData['id']},"
                    f"{testData['name']},"\
                    f"{testData['control']},"\
                    f"{value}]",
                    f"$updRange:id [{testData['id']}, "\
                    f"{testData['name']}, "\
                    f"{testData['control']}, "\
                    f"{value} ]",
                    f"$updRange:id [ {testData['id']} , "\
                    f" {testData['name']} , "\
                    f" {testData['control']} , "\
                    f" {value} ] ",
                    f"$updRange:id [ {testData['id']} , "\
                    f" {testData['name']} , "\
                    f" {testData['control']} , "\
                    f" {value} ]FILL",
                    f"$updRange:id [ {testData['id']} , "\
                    f" {testData['name']} , "\
                    f" {testData['control']} , "\
                    f" {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updRange:id", app.updateData,
                               Helpers.updStruct("rango", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Descripción_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#----------------------Test $updRange:name [Nombre, *, *]----------------------
@pytest.mark.asyncio
async def testRangeValue_updRangeName_nameEmpty(capfd):
    value = ""
    commands = [f"$updRange:name[{value},"\
                f"{testData['control']},"\
                f"{testData['desc']}]",
                f"$updRange:name [{value}, "\
                f"{testData['control']}, "\
                f"{testData['desc']} ]",
                f"$updRange:name [ {value} , "\
                f" {testData['control']} , "\
                f" {testData['desc']} ] ",
                f"$updRange:name [ {value} , "\
                f" {testData['control']} , "\
                f" {testData['desc']} ]FILL",
                f"$updRange:name [ {value} , "\
                f" {testData['control']} , "\
                f" {testData['desc']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updRange:name", app.updateData,
                           Helpers.updStruct("rango", "name"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Nombre_**\n" in out

@pytest.mark.asyncio
async def testRangeValue_updRangeName_nameLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$updRange:name[{value},"\
                f"{testData['control']},"\
                f"{testData['desc']}]",
                f"$updRange:name [{value}, "\
                f"{testData['control']}, "\
                f"{testData['desc']} ]",
                f"$updRange:name [ {value} , "\
                f" {testData['control']} , "\
                f" {testData['desc']} ] ",
                f"$updRange:name [ {value} , "\
                f" {testData['control']} , "\
                f" {testData['desc']} ]FILL",
                f"$updRange:name [ {value} , "\
                f" {testData['control']} , "\
                f" {testData['desc']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updRange:name", app.updateData,
                           Helpers.updStruct("rango", "name"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Nombre_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testRangeValue_updRangeName_nameStartChar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$updRange:name[{value},"\
                    f"{testData['control']},"\
                    f"{testData['desc']}]",
                    f"$updRange:name [{value}, "\
                    f"{testData['control']}, "\
                    f"{testData['desc']} ]",
                    f"$updRange:name [ {value} , "\
                    f" {testData['control']} , "\
                    f" {testData['desc']} ] ",
                    f"$updRange:name [ {value} , "\
                    f" {testData['control']} , "\
                    f" {testData['desc']} ]FILL",
                    f"$updRange:name [ {value} , "\
                    f" {testData['control']} , "\
                    f" {testData['desc']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updRange:name", app.updateData,
                               Helpers.updStruct("rango", "name"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testRangeValue_updRangeName_nameSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$updRange:name[{value},"\
                    f"{testData['control']},"\
                    f"{testData['desc']}]",
                    f"$updRange:name [{value}, "\
                    f"{testData['control']}, "\
                    f"{testData['desc']} ]",
                    f"$updRange:name [ {value} , "\
                    f" {testData['control']} , "\
                    f" {testData['desc']} ] ",
                    f"$updRange:name [ {value} , "\
                    f" {testData['control']} , "\
                    f" {testData['desc']} ]FILL",
                    f"$updRange:name [ {value} , "\
                    f" {testData['control']} , "\
                    f" {testData['desc']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updRange:name", app.updateData,
                               Helpers.updStruct("rango", "name"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testRangeValue_updRangeName_nameRepeatChar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$updRange:name[{value},"\
                    f"{testData['control']},"\
                    f"{testData['desc']}]",
                    f"$updRange:name [{value}, "\
                    f"{testData['control']}, "\
                    f"{testData['desc']} ]",
                    f"$updRange:name [ {value} , "\
                    f" {testData['control']} , "\
                    f" {testData['desc']} ] ",
                    f"$updRange:name [ {value} , "\
                    f" {testData['control']} , "\
                    f" {testData['desc']} ]FILL",
                    f"$updRange:name [ {value} , "\
                    f" {testData['control']} , "\
                    f" {testData['desc']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updRange:name", app.updateData,
                               Helpers.updStruct("rango", "name"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Nombre_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#---------------------Test $updRange:name [*, Control, *]-----------------------
@pytest.mark.asyncio
async def testRangeValue_updRangeName_controlEmpty(capfd):
    value = ""
    commands = [f"$updRange:name[{testData['name']},"\
                f"{value},"\
                f"{testData['desc']}]",
                f"$updRange:name [{testData['name']}, "\
                f"{value}, "\
                f"{testData['desc']} ]",
                f"$updRange:name [ {testData['name']} , "\
                f" {value} , "\
                f" {testData['desc']} ] ",
                f"$updRange:name [ {testData['name']} , "\
                f" {value}  , "\
                f" {testData['desc']} ]FILL",
                f"$updRange:name [ {testData['name']} , "\
                f" {value}  , "\
                f" {testData['desc']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updRange:name", app.updateData,
                           Helpers.updStruct("rango", "name"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Puntos_**\n" in out

@pytest.mark.asyncio
async def testRangeValue_updRangeName_controlInvalid(capfd):
    value = "test"
    commands = [f"$updRange:name[{testData['name']},"\
                f"{value},"\
                f"{testData['desc']}]",
                f"$updRange:name [{testData['name']}, "\
                f"{value}, "\
                f"{testData['desc']} ]",
                f"$updRange:name [ {testData['name']} , "\
                f" {value} , "\
                f" {testData['desc']} ] ",
                f"$updRange:name [ {testData['name']} , "\
                f" {value}  , "\
                f" {testData['desc']} ]FILL",
                f"$updRange:name [ {testData['name']} , "\
                f" {value}  , "\
                f" {testData['desc']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updRange:name", app.updateData,
                           Helpers.updStruct("rango", "name"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Puntos_** "\
                "es invalido.\n" in out

#-------------------Test $updRange:name [*, *, Descripción]--------------------
@pytest.mark.asyncio
async def testRangeValue_updRangeName_descriptionEmpty(capfd):
    value = ""
    commands = [f"$updRange:name[{testData['name']},"\
                f"{testData['control']},"\
                f"{value}]",
                f"$updRange:name [{testData['name']}, "\
                f"{testData['control']}, "\
                f"{value} ]",
                f"$updRange:name [ {testData['name']} , "\
                f" {testData['control']} , "\
                f" {value} ] ",
                f"$updRange:name [ {testData['name']} , "\
                f" {testData['control']} , "\
                f" {value} ]FILL",
                f"$updRange:name [ {testData['name']} , "\
                f" {testData['control']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updRange:name", app.updateData,
                           Helpers.updStruct("rango", "name"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Descripción_**\n" in out

@pytest.mark.asyncio
async def testRangeValue_updRangeName_descriptionLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$updRange:name[{testData['name']},"\
                f"{testData['control']},"\
                f"{value}]",
                f"$updRange:name [{testData['name']}, "\
                f"{testData['control']}, "\
                f"{value} ]",
                f"$updRange:name [ {testData['name']} , "\
                f" {testData['control']} , "\
                f" {value} ] ",
                f"$updRange:name [ {testData['name']} , "\
                f" {testData['control']} , "\
                f" {value} ]FILL",
                f"$updRange:name [ {testData['name']} , "\
                f" {testData['control']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updRange:name", app.updateData,
                           Helpers.updStruct("rango", "name"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Descripción_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testRangeValue_updRangeName_descriptionStartChar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$updRange:name[{testData['name']},"\
                    f"{testData['control']},"\
                    f"{value}]",
                    f"$updRange:name [{testData['name']}, "\
                    f"{testData['control']}, "\
                    f"{value} ]",
                    f"$updRange:name [ {testData['name']} , "\
                    f" {testData['control']} , "\
                    f" {value} ] ",
                    f"$updRange:name [ {testData['name']} , "\
                    f" {testData['control']} , "\
                    f" {value} ]FILL",
                    f"$updRange:name [ {testData['name']} , "\
                    f" {testData['control']} , "\
                    f" {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updRange:name", app.updateData,
                               Helpers.updStruct("rango", "name"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Descripción_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testRangeValue_updRangeName_descriptionSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$updRange:name[{testData['name']},"\
                    f"{testData['control']},"\
                    f"{value}]",
                    f"$updRange:name [{testData['name']}, "\
                    f"{testData['control']}, "\
                    f"{value} ]",
                    f"$updRange:name [ {testData['name']} , "\
                    f" {testData['control']} , "\
                    f" {value} ] ",
                    f"$updRange:name [ {testData['name']} , "\
                    f" {testData['control']} , "\
                    f" {value} ]FILL",
                    f"$updRange:name [ {testData['name']} , "\
                    f" {testData['control']} , "\
                    f" {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updRange:name", app.updateData,
                               Helpers.updStruct("rango", "name"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Descripción_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testRangeValue_updRangeName_descriptionRepeatChar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$updRange:name[{testData['name']},"\
                    f"{testData['control']},"\
                    f"{value}]",
                    f"$updRange:name [{testData['name']}, "\
                    f"{testData['control']}, "\
                    f"{value} ]",
                    f"$updRange:name [ {testData['name']} , "\
                    f" {testData['control']} , "\
                    f" {value} ] ",
                    f"$updRange:name [ {testData['name']} , "\
                    f" {testData['control']} , "\
                    f" {value} ]FILL",
                    f"$updRange:name [ {testData['name']} , "\
                    f" {testData['control']} , "\
                    f" {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updRange:name", app.updateData,
                               Helpers.updStruct("rango", "name"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Descripción_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#-------------------------------$delRange:id [ID]------------------------------
@pytest.mark.asyncio
async def testRangeValue_delRangeId_idEmpty(capfd):
    value = ""
    commands = [f"$delRange:id[{value}],",
                f"$delRange:id [{value} ], ",
                f"$delRange:id [ {value} ], ",
                f"$delRange:id [ {value} ]FILL",
                f"$delRange:id [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delRange:id", app.deleteData,
                           Helpers.delStruct("rango", "id"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_ID_**\n" in out

@pytest.mark.asyncio
async def testRangeValue_delRangeId_idInvalid(capfd):
    value = "test"
    commands = [f"$delRange:id[{value}],",
                f"$delRange:id [{value} ], ",
                f"$delRange:id [ {value} ], ",
                f"$delRange:id [ {value} ]FILL",
                f"$delRange:id [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delRange:id", app.deleteData,
                           Helpers.delStruct("rango", "id"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_ID_** "\
                "es invalido.\n" in out

#-------------------------Test $delRange:name [Nombre]-------------------------
@pytest.mark.asyncio
async def testRangeValue_delRangeName_nameEmpty(capfd):
    value = ""
    commands = [f"$delRange:name[{value}]",
                f"$delRange:name [{value} ]",
                f"$delRange:name [ {value} ]",
                f"$delRange:name [ {value} ]FILL",
                f"$delRange:name [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delRange:name", app.deleteData,
                           Helpers.delStruct("rango", "name"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Nombre_**\n" in out

@pytest.mark.asyncio
async def testRangeValue_delRangeName_nameLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$delRange:name[{value}]",
                f"$delRange:name [{value} ]",
                f"$delRange:name [ {value} ]",
                f"$delRange:name [ {value} ]FILL",
                f"$delRange:name [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delRange:name", app.deleteData,
                           Helpers.delStruct("rango", "name"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Nombre_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testRangeValue_delRangeName_nameStartChar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$delRange:name[{value}]",
                    f"$delRange:name [{value} ]",
                    f"$delRange:name [ {value} ]",
                    f"$delRange:name [ {value} ]FILL",
                    f"$delRange:name [ {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("delRange:name", app.deleteData,
                               Helpers.delStruct("rango", "name"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testRangeValue_delRangeName_nameSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$delRange:name[{value}]",
                    f"$delRange:name [{value} ]",
                    f"$delRange:name [ {value} ]",
                    f"$delRange:name [ {value} ]FILL",
                    f"$delRange:name [ {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("delRange:name", app.deleteData,
                               Helpers.delStruct("rango", "name"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testRangeValue_delRangeName_nameRepeatChar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$delRange:name[{value}]",
                    f"$delRange:name [{value} ]",
                    f"$delRange:name [ {value} ]",
                    f"$delRange:name [ {value} ]FILL",
                    f"$delRange:name [ {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("delRange:name", app.deleteData,
                               Helpers.delStruct("rango", "name"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Nombre_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#------------------------------$listRange:id [ID]------------------------------
@pytest.mark.asyncio
async def testRangeValue_listRangeId_idEmpty(capfd):
    value = ""
    commands = [f"$listRange:id[{value}],",
                f"$listRange:id [{value} ], ",
                f"$listRange:id [ {value} ], ",
                f"$listRange:id [ {value} ]FILL",
                f"$listRange:id [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listRange:id", app.getDatas,
                         Helpers.getStruct("rango", ["id"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_ID_**\n" in out

@pytest.mark.asyncio
async def testRangeValue_listRangeId_idInvalid(capfd):
    value = "test"
    commands = [f"$listRange:id[{value}],",
                f"$listRange:id [{value} ], ",
                f"$listRange:id [ {value} ], ",
                f"$listRange:id [ {value} ]FILL",
                f"$listRange:id [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listRange:id", app.getDatas,
                         Helpers.getStruct("rango", ["id"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_ID_** "\
                "es invalido.\n" in out

#------------------------Test $listRange:name [Nombre]-------------------------
@pytest.mark.asyncio
async def testRangeValue_listRangeName_nameEmpty(capfd):
    value = ""
    commands = [f"$listRange:name[{value}]",
                f"$listRange:name [{value} ]",
                f"$listRange:name [ {value} ]",
                f"$listRange:name [ {value} ]FILL",
                f"$listRange:name [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listRange:name", app.getDatas,
                         Helpers.getStruct("rango", ["name"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Nombre_**\n" in out

@pytest.mark.asyncio
async def testRangeValue_listRangeName_nameLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$listRange:name[{value}]",
                f"$listRange:name [{value} ]",
                f"$listRange:name [ {value} ]",
                f"$listRange:name [ {value} ]FILL",
                f"$listRange:name [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listRange:name", app.getDatas,
                         Helpers.getStruct("rango", ["name"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Nombre_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testRangeValue_listRangeName_nameStartChar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$listRange:name[{value}]",
                    f"$listRange:name [{value} ]",
                    f"$listRange:name [ {value} ]",
                    f"$listRange:name [ {value} ]FILL",
                    f"$listRange:name [ {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listRange:name", app.getDatas,
                             Helpers.getStruct("rango", ["name"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testRangeValue_listRangeName_nameSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$listRange:name[{value}]",
                    f"$listRange:name [{value} ]",
                    f"$listRange:name [ {value} ]",
                    f"$listRange:name [ {value} ]FILL",
                    f"$listRange:name [ {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listRange:name", app.getDatas,
                             Helpers.getStruct("rango", ["name"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testRangeValue_listRangeName_nameRepeatChar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$listRange:name[{value}]",
                    f"$listRange:name [{value} ]",
                    f"$listRange:name [ {value} ]",
                    f"$listRange:name [ {value} ]FILL",
                    f"$listRange:name [ {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listRange:name", app.getDatas,
                             Helpers.getStruct("rango", ["name"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Nombre_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out