import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Helpers.helpers import Helpers
from collections import namedtuple

testData = {
    "id" : "1",
    "name" : "TestEvent",
    "points" : 5,
    "desc" : "Descripción"
}

Message = namedtuple('Message', ['author', 'content'])
Client = namedtuple('Client', ['user'])
app = AppHandler()

#----------------------Test $addEvent [Nombre, *, *]----------------------
@pytest.mark.asyncio
async def testValue_addEvent_name_empty(capfd):
    value = ""
    commands = [f"$addEvent[{value},"\
                f"{testData['points']},"\
                f"{testData['desc']}]",
                f"$addEvent [{value}, "\
                f"{testData['points']}, "\
                f"{testData['desc']} ]",
                f"$addEvent [ {value} , "\
                f" {testData['points']} , "\
                f" {testData['desc']} ] ",
                f"$addEvent [ {value} , "\
                f" {testData['points']} , "\
                f" {testData['desc']} ]FILL",
                f"$addEvent [ {value} , "\
                f" {testData['points']} , "\
                f" {testData['desc']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addEvent", app.setData,
                           Helpers.setStruct("evento"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Nombre_**\n" in out

@pytest.mark.asyncio
async def testValue_addEvent_name_long(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$addEvent[{value},"\
                f"{testData['points']},"\
                f"{testData['desc']}]",
                f"$addEvent [{value}, "\
                f"{testData['points']}, "\
                f"{testData['desc']} ]",
                f"$addEvent [ {value} , "\
                f" {testData['points']} , "\
                f" {testData['desc']} ] ",
                f"$addEvent [ {value} , "\
                f" {testData['points']} , "\
                f" {testData['desc']} ]FILL",
                f"$addEvent [ {value} , "\
                f" {testData['points']} , "\
                f" {testData['desc']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addEvent", app.setData,
                           Helpers.setStruct("evento"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Nombre_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testValue_addEvent_name_startchar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$addEvent[{value},"\
                    f"{testData['points']},"\
                    f"{testData['desc']}]",
                    f"$addEvent [{value}, "\
                    f"{testData['points']}, "\
                    f"{testData['desc']} ]",
                    f"$addEvent [ {value} , "\
                    f" {testData['points']} , "\
                    f" {testData['desc']} ] ",
                    f"$addEvent [ {value} , "\
                    f" {testData['points']} , "\
                    f" {testData['desc']} ]FILL",
                    f"$addEvent [ {value} , "\
                    f" {testData['points']} , "\
                    f" {testData['desc']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addEvent", app.setData,
                               Helpers.setStruct("evento"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testValue_addEvent_name_spechar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$addEvent[{value},"\
                    f"{testData['points']},"\
                    f"{testData['desc']}]",
                    f"$addEvent [{value}, "\
                    f"{testData['points']}, "\
                    f"{testData['desc']} ]",
                    f"$addEvent [ {value} , "\
                    f" {testData['points']} , "\
                    f" {testData['desc']} ] ",
                    f"$addEvent [ {value} , "\
                    f" {testData['points']} , "\
                    f" {testData['desc']} ]FILL",
                    f"$addEvent [ {value} , "\
                    f" {testData['points']} , "\
                    f" {testData['desc']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addEvent", app.setData,
                               Helpers.setStruct("evento"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testValue_addEvent_name_repeatchar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$addEvent[{value},"\
                    f"{testData['points']},"\
                    f"{testData['desc']}]",
                    f"$addEvent [{value}, "\
                    f"{testData['points']}, "\
                    f"{testData['desc']} ]",
                    f"$addEvent [ {value} , "\
                    f" {testData['points']} , "\
                    f" {testData['desc']} ] ",
                    f"$addEvent [ {value} , "\
                    f" {testData['points']} , "\
                    f" {testData['desc']} ]FILL",
                    f"$addEvent [ {value} , "\
                    f" {testData['points']} , "\
                    f" {testData['desc']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addEvent", app.setData,
                               Helpers.setStruct("evento"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Nombre_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#-----------------------Test $addEvent [*, Puntos, *]-------------------------
@pytest.mark.asyncio
async def testValue_addEvent_points_empty(capfd):
    value = ""
    commands = [f"$addEvent[{testData['name']},"\
                f"{value},"\
                f"{testData['desc']}]",
                f"$addEvent [{testData['name']}, "\
                f"{value}, "\
                f"{testData['desc']} ]",
                f"$addEvent [ {testData['name']} , "\
                f" {value} , "\
                f" {testData['desc']} ] ",
                f"$addEvent [ {testData['name']} , "\
                f" {value}  , "\
                f" {testData['desc']} ]FILL",
                f"$addEvent [ {testData['name']} , "\
                f" {value}  , "\
                f" {testData['desc']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addEvent", app.setData,
                           Helpers.setStruct("evento"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Puntos_**\n" in out

@pytest.mark.asyncio
async def testValue_addEvent_points_invalid(capfd):
    value = "test"
    commands = [f"$addEvent[{testData['name']},"\
                f"{value},"\
                f"{testData['desc']}]",
                f"$addEvent [{testData['name']}, "\
                f"{value}, "\
                f"{testData['desc']} ]",
                f"$addEvent [ {testData['name']} , "\
                f" {value} , "\
                f" {testData['desc']} ] ",
                f"$addEvent [ {testData['name']} , "\
                f" {value}  , "\
                f" {testData['desc']} ]FILL",
                f"$addEvent [ {testData['name']} , "\
                f" {value}  , "\
                f" {testData['desc']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addEvent", app.setData,
                           Helpers.setStruct("evento"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Puntos_** "\
                "es invalido.\n" in out

#----------------------Test $addEvent [*, *, Descripción]----------------------
@pytest.mark.asyncio
async def testValue_addEvent_description_empty(capfd):
    value = ""
    commands = [f"$addEvent[{testData['name']},"\
                f"{testData['points']},"\
                f"{value}]",
                f"$addEvent [{testData['name']}, "\
                f"{testData['points']}, "\
                f"{value} ]",
                f"$addEvent [ {testData['name']} , "\
                f" {testData['points']} , "\
                f" {value} ] ",
                f"$addEvent [ {testData['name']} , "\
                f" {testData['points']} , "\
                f" {value} ]FILL",
                f"$addEvent [ {testData['name']} , "\
                f" {testData['points']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addEvent", app.setData,
                           Helpers.setStruct("evento"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Descripción_**\n" in out

@pytest.mark.asyncio
async def testValue_addEvent_description_long(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$addEvent[{testData['name']},"\
                f"{testData['points']},"\
                f"{value}]",
                f"$addEvent [{testData['name']}, "\
                f"{testData['points']}, "\
                f"{value} ]",
                f"$addEvent [ {testData['name']} , "\
                f" {testData['points']} , "\
                f" {value} ] ",
                f"$addEvent [ {testData['name']} , "\
                f" {testData['points']} , "\
                f" {value} ]FILL",
                f"$addEvent [ {testData['name']} , "\
                f" {testData['points']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addEvent", app.setData,
                           Helpers.setStruct("evento"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Descripción_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testValue_addEvent_description_startchar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$addEvent[{testData['name']},"\
                    f"{testData['points']},"\
                    f"{value}]",
                    f"$addEvent [{testData['name']}, "\
                    f"{testData['points']}, "\
                    f"{value} ]",
                    f"$addEvent [ {testData['name']} , "\
                    f" {testData['points']} , "\
                    f" {value} ] ",
                    f"$addEvent [ {testData['name']} , "\
                    f" {testData['points']} , "\
                    f" {value} ]FILL",
                    f"$addEvent [ {testData['name']} , "\
                    f" {testData['points']} , "\
                    f" {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addEvent", app.setData,
                               Helpers.setStruct("evento"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Descripción_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testValue_addEvent_description_spechar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$addEvent[{testData['name']},"\
                    f"{testData['points']},"\
                    f"{value}]",
                    f"$addEvent [{testData['name']}, "\
                    f"{testData['points']}, "\
                    f"{value} ]",
                    f"$addEvent [ {testData['name']} , "\
                    f" {testData['points']} , "\
                    f" {value} ] ",
                    f"$addEvent [ {testData['name']} , "\
                    f" {testData['points']} , "\
                    f" {value} ]FILL",
                    f"$addEvent [ {testData['name']} , "\
                    f" {testData['points']} , "\
                    f" {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addEvent", app.setData,
                               Helpers.setStruct("evento"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Descripción_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testValue_addEvent_description_repeatchar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$addEvent[{testData['name']},"\
                    f"{testData['points']},"\
                    f"{value}]",
                    f"$addEvent [{testData['name']}, "\
                    f"{testData['points']}, "\
                    f"{value} ]",
                    f"$addEvent [ {testData['name']} , "\
                    f" {testData['points']} , "\
                    f" {value} ] ",
                    f"$addEvent [ {testData['name']} , "\
                    f" {testData['points']} , "\
                    f" {value} ]FILL",
                    f"$addEvent [ {testData['name']} , "\
                    f" {testData['points']} , "\
                    f" {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addEvent", app.setData,
                               Helpers.setStruct("evento"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Descripción_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#------------------------Test $updEvent:id [ID, *, *, *]----------------------
@pytest.mark.asyncio
async def testValue_updEventId_id_empty(capfd):
    value = ""
    commands = [f"$updEvent:id[{value},"\
                f"{testData['name']},"\
                f"{testData['points']},"\
                f"{testData['desc']}]",
                f"$updEvent:id [{value}, "\
                f"{testData['name']}, "\
                f"{testData['points']}, "\
                f"{testData['desc']} ]",
                f"$updEvent:id [ {value} , "\
                f" {testData['name']} , "\
                f" {testData['points']} , "\
                f" {testData['desc']} ] ",
                f"$updEvent:id [ {value} , "\
                f" {testData['name']} , "\
                f" {testData['points']} , "\
                f" {testData['desc']} ]FILL",
                f"$updEvent:id [ {value} , "\
                f" {testData['name']} , "\
                f" {testData['points']} , "\
                f" {testData['desc']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updEvent:id", app.updateData,
                           Helpers.updStruct("evento", "id"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_ID_**\n" in out

@pytest.mark.asyncio
async def testValue_updEventId_id_invalid(capfd):
    value = "test"
    commands = [f"$updEvent:id[{value},"\
                f"{testData['name']},"\
                f"{testData['points']},"\
                f"{testData['desc']}]",
                f"$updEvent:id [{value}, "\
                f"{testData['name']}, "\
                f"{testData['points']}, "\
                f"{testData['desc']} ]",
                f"$updEvent:id [ {value} , "\
                f" {testData['name']} , "\
                f" {testData['points']} , "\
                f" {testData['desc']} ] ",
                f"$updEvent:id [ {value} , "\
                f" {testData['name']} , "\
                f" {testData['points']} , "\
                f" {testData['desc']} ]FILL",
                f"$updEvent:id [ {value} , "\
                f" {testData['name']} , "\
                f" {testData['points']} , "\
                f" {testData['desc']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updEvent:id", app.updateData,
                           Helpers.updStruct("evento", "id"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_ID_** "\
                "es invalido.\n" in out

#----------------------Test $updEvent:id [*, Nombre, *, *]---------------------
@pytest.mark.asyncio
async def testValue_updEventId_name_empty(capfd):
    value = ""
    commands = [f"$updEvent:id[{testData['id']},"
                f"{value},"\
                f"{testData['points']},"\
                f"{testData['desc']}]",
                f"$updEvent:id [{testData['id']}, "\
                f"{value}, "\
                f"{testData['points']}, "\
                f"{testData['desc']} ]",
                f"$updEvent:id [ {testData['id']} , "\
                f" {value} , "\
                f" {testData['points']} , "\
                f" {testData['desc']} ] ",
                f"$updEvent:id [ {testData['id']} , "\
                f" {value} , "\
                f" {testData['points']} , "\
                f" {testData['desc']} ]FILL",
                f"$updEvent:id [ {testData['id']} , "\
                f" {value} , "\
                f" {testData['points']} , "\
                f" {testData['desc']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updEvent:id", app.updateData,
                           Helpers.updStruct("evento", "id"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Nombre_**\n" in out

@pytest.mark.asyncio
async def testValue_updEventId_name_long(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$updEvent:id[{testData['id']},"
                f"{value},"\
                f"{testData['points']},"\
                f"{testData['desc']}]",
                f"$updEvent:id [{testData['id']}, "\
                f"{value}, "\
                f"{testData['points']}, "\
                f"{testData['desc']} ]",
                f"$updEvent:id [ {testData['id']} , "\
                f" {value} , "\
                f" {testData['points']} , "\
                f" {testData['desc']} ] ",
                f"$updEvent:id [ {testData['id']} , "\
                f" {value} , "\
                f" {testData['points']} , "\
                f" {testData['desc']} ]FILL",
                f"$updEvent:id [ {testData['id']} , "\
                f" {value} , "\
                f" {testData['points']} , "\
                f" {testData['desc']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updEvent:id", app.updateData,
                           Helpers.updStruct("evento", "id"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Nombre_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testValue_updEventId_name_startchar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$updEvent:id[{testData['id']},"
                    f"{value},"\
                    f"{testData['points']},"\
                    f"{testData['desc']}]",
                    f"$updEvent:id [{testData['id']}, "\
                    f"{value}, "\
                    f"{testData['points']}, "\
                    f"{testData['desc']} ]",
                    f"$updEvent:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['points']} , "\
                    f" {testData['desc']} ] ",
                    f"$updEvent:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['points']} , "\
                    f" {testData['desc']} ]FILL",
                    f"$updEvent:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['points']} , "\
                    f" {testData['desc']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updEvent:id", app.updateData,
                               Helpers.updStruct("evento", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testValue_updEventId_name_spechar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$updEvent:id[{testData['id']},"
                    f"{value},"\
                    f"{testData['points']},"\
                    f"{testData['desc']}]",
                    f"$updEvent:id [{testData['id']}, "\
                    f"{value}, "\
                    f"{testData['points']}, "\
                    f"{testData['desc']} ]",
                    f"$updEvent:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['points']} , "\
                    f" {testData['desc']} ] ",
                    f"$updEvent:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['points']} , "\
                    f" {testData['desc']} ]FILL",
                    f"$updEvent:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['points']} , "\
                    f" {testData['desc']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updEvent:id", app.updateData,
                               Helpers.updStruct("evento", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testValue_updEventId_name_repeatchar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$updEvent:id[{testData['id']},"
                    f"{value},"\
                    f"{testData['points']},"\
                    f"{testData['desc']}]",
                    f"$updEvent:id [{testData['id']}, "\
                    f"{value}, "\
                    f"{testData['points']}, "\
                    f"{testData['desc']} ]",
                    f"$updEvent:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['points']} , "\
                    f" {testData['desc']} ] ",
                    f"$updEvent:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['points']} , "\
                    f" {testData['desc']} ]FILL",
                    f"$updEvent:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['points']} , "\
                    f" {testData['desc']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updEvent:id", app.updateData,
                               Helpers.updStruct("evento", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Nombre_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#--------------------Test $updEvent:id [*, *, Puntos, *]-----------------------
@pytest.mark.asyncio
async def testValue_updEventId_points_empty(capfd):
    value = ""
    commands = [f"$updEvent:id[{testData['id']},"
                f"{testData['name']},"\
                f"{value},"\
                f"{testData['desc']}]",
                f"$updEvent:id [{testData['id']}, "\
                f"{testData['name']}, "\
                f"{value}, "\
                f"{testData['desc']} ]",
                f"$updEvent:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {value} , "\
                f" {testData['desc']} ] ",
                f"$updEvent:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {value}  , "\
                f" {testData['desc']} ]FILL",
                f"$updEvent:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {value}  , "\
                f" {testData['desc']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updEvent:id", app.updateData,
                           Helpers.updStruct("evento", "id"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Puntos_**\n" in out

@pytest.mark.asyncio
async def testValue_updEventId_points_invalid(capfd):
    value = "test"
    commands = [f"$updEvent:id[{testData['id']},"
                f"{testData['name']},"\
                f"{value},"\
                f"{testData['desc']}]",
                f"$updEvent:id [{testData['id']}, "\
                f"{testData['name']}, "\
                f"{value}, "\
                f"{testData['desc']} ]",
                f"$updEvent:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {value} , "\
                f" {testData['desc']} ] ",
                f"$updEvent:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {value}  , "\
                f" {testData['desc']} ]FILL",
                f"$updEvent:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {value}  , "\
                f" {testData['desc']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updEvent:id", app.updateData,
                           Helpers.updStruct("evento", "id"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Puntos_** "\
                "es invalido.\n" in out

#-------------------Test $updEvent:id [*, *, *, Descripción]-------------------
@pytest.mark.asyncio
async def testValue_updEventId_description_empty(capfd):
    value = ""
    commands = [f"$updEvent:id[{testData['id']},"
                f"{testData['name']},"\
                f"{testData['points']},"\
                f"{value}]",
                f"$updEvent:id [{testData['id']}, "\
                f"{testData['name']}, "\
                f"{testData['points']}, "\
                f"{value} ]",
                f"$updEvent:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {testData['points']} , "\
                f" {value} ] ",
                f"$updEvent:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {testData['points']} , "\
                f" {value} ]FILL",
                f"$updEvent:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {testData['points']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updEvent:id", app.updateData,
                           Helpers.updStruct("evento", "id"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Descripción_**\n" in out

@pytest.mark.asyncio
async def testValue_updEventId_description_long(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$updEvent:id[{testData['id']},"
                f"{testData['name']},"\
                f"{testData['points']},"\
                f"{value}]",
                f"$updEvent:id [{testData['id']}, "\
                f"{testData['name']}, "\
                f"{testData['points']}, "\
                f"{value} ]",
                f"$updEvent:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {testData['points']} , "\
                f" {value} ] ",
                f"$updEvent:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {testData['points']} , "\
                f" {value} ]FILL",
                f"$updEvent:id [ {testData['id']} , "\
                f" {testData['name']} , "\
                f" {testData['points']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updEvent:id", app.updateData,
                           Helpers.updStruct("evento", "id"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Descripción_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testValue_updEventId_description_startchar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$updEvent:id[{testData['id']},"
                    f"{testData['name']},"\
                    f"{testData['points']},"\
                    f"{value}]",
                    f"$updEvent:id [{testData['id']}, "\
                    f"{testData['name']}, "\
                    f"{testData['points']}, "\
                    f"{value} ]",
                    f"$updEvent:id [ {testData['id']} , "\
                    f" {testData['name']} , "\
                    f" {testData['points']} , "\
                    f" {value} ] ",
                    f"$updEvent:id [ {testData['id']} , "\
                    f" {testData['name']} , "\
                    f" {testData['points']} , "\
                    f" {value} ]FILL",
                    f"$updEvent:id [ {testData['id']} , "\
                    f" {testData['name']} , "\
                    f" {testData['points']} , "\
                    f" {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updEvent:id", app.updateData,
                               Helpers.updStruct("evento", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Descripción_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testValue_updEventId_description_spechar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$updEvent:id[{testData['id']},"
                    f"{testData['name']},"\
                    f"{testData['points']},"\
                    f"{value}]",
                    f"$updEvent:id [{testData['id']}, "\
                    f"{testData['name']}, "\
                    f"{testData['points']}, "\
                    f"{value} ]",
                    f"$updEvent:id [ {testData['id']} , "\
                    f" {testData['name']} , "\
                    f" {testData['points']} , "\
                    f" {value} ] ",
                    f"$updEvent:id [ {testData['id']} , "\
                    f" {testData['name']} , "\
                    f" {testData['points']} , "\
                    f" {value} ]FILL",
                    f"$updEvent:id [ {testData['id']} , "\
                    f" {testData['name']} , "\
                    f" {testData['points']} , "\
                    f" {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updEvent:id", app.updateData,
                               Helpers.updStruct("evento", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Descripción_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testValue_updEventId_description_repeatchar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$updEvent:id[{testData['id']},"
                    f"{testData['name']},"\
                    f"{testData['points']},"\
                    f"{value}]",
                    f"$updEvent:id [{testData['id']}, "\
                    f"{testData['name']}, "\
                    f"{testData['points']}, "\
                    f"{value} ]",
                    f"$updEvent:id [ {testData['id']} , "\
                    f" {testData['name']} , "\
                    f" {testData['points']} , "\
                    f" {value} ] ",
                    f"$updEvent:id [ {testData['id']} , "\
                    f" {testData['name']} , "\
                    f" {testData['points']} , "\
                    f" {value} ]FILL",
                    f"$updEvent:id [ {testData['id']} , "\
                    f" {testData['name']} , "\
                    f" {testData['points']} , "\
                    f" {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updEvent:id", app.updateData,
                               Helpers.updStruct("evento", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Descripción_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#----------------------Test $updEvent:name [Nombre, *, *]----------------------
@pytest.mark.asyncio
async def testValue_updEventName_name_empty(capfd):
    value = ""
    commands = [f"$updEvent:name[{value},"\
                f"{testData['points']},"\
                f"{testData['desc']}]",
                f"$updEvent:name [{value}, "\
                f"{testData['points']}, "\
                f"{testData['desc']} ]",
                f"$updEvent:name [ {value} , "\
                f" {testData['points']} , "\
                f" {testData['desc']} ] ",
                f"$updEvent:name [ {value} , "\
                f" {testData['points']} , "\
                f" {testData['desc']} ]FILL",
                f"$updEvent:name [ {value} , "\
                f" {testData['points']} , "\
                f" {testData['desc']} ] FILL"]
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
async def testValue_updEventName_name_long(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$updEvent:name[{value},"\
                f"{testData['points']},"\
                f"{testData['desc']}]",
                f"$updEvent:name [{value}, "\
                f"{testData['points']}, "\
                f"{testData['desc']} ]",
                f"$updEvent:name [ {value} , "\
                f" {testData['points']} , "\
                f" {testData['desc']} ] ",
                f"$updEvent:name [ {value} , "\
                f" {testData['points']} , "\
                f" {testData['desc']} ]FILL",
                f"$updEvent:name [ {value} , "\
                f" {testData['points']} , "\
                f" {testData['desc']} ] FILL"]
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
async def testValue_updEventName_name_startchar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$updEvent:name[{value},"\
                    f"{testData['points']},"\
                    f"{testData['desc']}]",
                    f"$updEvent:name [{value}, "\
                    f"{testData['points']}, "\
                    f"{testData['desc']} ]",
                    f"$updEvent:name [ {value} , "\
                    f" {testData['points']} , "\
                    f" {testData['desc']} ] ",
                    f"$updEvent:name [ {value} , "\
                    f" {testData['points']} , "\
                    f" {testData['desc']} ]FILL",
                    f"$updEvent:name [ {value} , "\
                    f" {testData['points']} , "\
                    f" {testData['desc']} ] FILL"]
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
async def testValue_updEventName_name_spechar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$updEvent:name[{value},"\
                    f"{testData['points']},"\
                    f"{testData['desc']}]",
                    f"$updEvent:name [{value}, "\
                    f"{testData['points']}, "\
                    f"{testData['desc']} ]",
                    f"$updEvent:name [ {value} , "\
                    f" {testData['points']} , "\
                    f" {testData['desc']} ] ",
                    f"$updEvent:name [ {value} , "\
                    f" {testData['points']} , "\
                    f" {testData['desc']} ]FILL",
                    f"$updEvent:name [ {value} , "\
                    f" {testData['points']} , "\
                    f" {testData['desc']} ] FILL"]
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
async def testValue_updEventName_name_repeatchar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$updEvent:name[{value},"\
                    f"{testData['points']},"\
                    f"{testData['desc']}]",
                    f"$updEvent:name [{value}, "\
                    f"{testData['points']}, "\
                    f"{testData['desc']} ]",
                    f"$updEvent:name [ {value} , "\
                    f" {testData['points']} , "\
                    f" {testData['desc']} ] ",
                    f"$updEvent:name [ {value} , "\
                    f" {testData['points']} , "\
                    f" {testData['desc']} ]FILL",
                    f"$updEvent:name [ {value} , "\
                    f" {testData['points']} , "\
                    f" {testData['desc']} ] FILL"]
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
async def testValue_updEventName_points_empty(capfd):
    value = ""
    commands = [f"$updEvent:name[{testData['name']},"\
                f"{value},"\
                f"{testData['desc']}]",
                f"$updEvent:name [{testData['name']}, "\
                f"{value}, "\
                f"{testData['desc']} ]",
                f"$updEvent:name [ {testData['name']} , "\
                f" {value} , "\
                f" {testData['desc']} ] ",
                f"$updEvent:name [ {testData['name']} , "\
                f" {value}  , "\
                f" {testData['desc']} ]FILL",
                f"$updEvent:name [ {testData['name']} , "\
                f" {value}  , "\
                f" {testData['desc']} ] FILL"]
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
async def testValue_updEventName_points_invalid(capfd):
    value = "test"
    commands = [f"$updEvent:name[{testData['name']},"\
                f"{value},"\
                f"{testData['desc']}]",
                f"$updEvent:name [{testData['name']}, "\
                f"{value}, "\
                f"{testData['desc']} ]",
                f"$updEvent:name [ {testData['name']} , "\
                f" {value} , "\
                f" {testData['desc']} ] ",
                f"$updEvent:name [ {testData['name']} , "\
                f" {value}  , "\
                f" {testData['desc']} ]FILL",
                f"$updEvent:name [ {testData['name']} , "\
                f" {value}  , "\
                f" {testData['desc']} ] FILL"]
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
async def testValue_updEventName_description_empty(capfd):
    value = ""
    commands = [f"$updEvent:name[{testData['name']},"\
                f"{testData['points']},"\
                f"{value}]",
                f"$updEvent:name [{testData['name']}, "\
                f"{testData['points']}, "\
                f"{value} ]",
                f"$updEvent:name [ {testData['name']} , "\
                f" {testData['points']} , "\
                f" {value} ] ",
                f"$updEvent:name [ {testData['name']} , "\
                f" {testData['points']} , "\
                f" {value} ]FILL",
                f"$updEvent:name [ {testData['name']} , "\
                f" {testData['points']} , "\
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
async def testValue_updEventName_description_long(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$updEvent:name[{testData['name']},"\
                f"{testData['points']},"\
                f"{value}]",
                f"$updEvent:name [{testData['name']}, "\
                f"{testData['points']}, "\
                f"{value} ]",
                f"$updEvent:name [ {testData['name']} , "\
                f" {testData['points']} , "\
                f" {value} ] ",
                f"$updEvent:name [ {testData['name']} , "\
                f" {testData['points']} , "\
                f" {value} ]FILL",
                f"$updEvent:name [ {testData['name']} , "\
                f" {testData['points']} , "\
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
async def testValue_updEventName_description_startchar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$updEvent:name[{testData['name']},"\
                    f"{testData['points']},"\
                    f"{value}]",
                    f"$updEvent:name [{testData['name']}, "\
                    f"{testData['points']}, "\
                    f"{value} ]",
                    f"$updEvent:name [ {testData['name']} , "\
                    f" {testData['points']} , "\
                    f" {value} ] ",
                    f"$updEvent:name [ {testData['name']} , "\
                    f" {testData['points']} , "\
                    f" {value} ]FILL",
                    f"$updEvent:name [ {testData['name']} , "\
                    f" {testData['points']} , "\
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
async def testValue_updEventName_description_spechar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$updEvent:name[{testData['name']},"\
                    f"{testData['points']},"\
                    f"{value}]",
                    f"$updEvent:name [{testData['name']}, "\
                    f"{testData['points']}, "\
                    f"{value} ]",
                    f"$updEvent:name [ {testData['name']} , "\
                    f" {testData['points']} , "\
                    f" {value} ] ",
                    f"$updEvent:name [ {testData['name']} , "\
                    f" {testData['points']} , "\
                    f" {value} ]FILL",
                    f"$updEvent:name [ {testData['name']} , "\
                    f" {testData['points']} , "\
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
async def testValue_updEventName_description_repeatchar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$updEvent:name[{testData['name']},"\
                    f"{testData['points']},"\
                    f"{value}]",
                    f"$updEvent:name [{testData['name']}, "\
                    f"{testData['points']}, "\
                    f"{value} ]",
                    f"$updEvent:name [ {testData['name']} , "\
                    f" {testData['points']} , "\
                    f" {value} ] ",
                    f"$updEvent:name [ {testData['name']} , "\
                    f" {testData['points']} , "\
                    f" {value} ]FILL",
                    f"$updEvent:name [ {testData['name']} , "\
                    f" {testData['points']} , "\
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
async def testValue_delEventId_id_empty(capfd):
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
async def testValue_delEventId_id_invalid(capfd):
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
async def testValue_delEventName_name_empty(capfd):
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
async def testValue_delEventName_name_long(capfd):
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
async def testValue_delEventName_name_startchar(capfd):
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
async def testValue_delEventName_name_spechar(capfd):
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
async def testValue_delEventName_name_repeatchar(capfd):
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
async def testValue_listEventId_id_empty(capfd):
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
async def testValue_listEventId_id_invalid(capfd):
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
async def testValue_listEventName_name_empty(capfd):
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
async def testValue_listEventName_name_long(capfd):
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
async def testValue_listEventName_name_startchar(capfd):
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
async def testValue_listEventName_name_spechar(capfd):
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
async def testValue_listEventName_name_repeatchar(capfd):
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