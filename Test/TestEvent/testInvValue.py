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
async def test_addEvent_name_empty(capfd):
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
async def test_addEvent_name_long(capfd):
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
async def test_addEvent_name_startchar(capfd):
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
async def test_addEvent_name_spechar(capfd):
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
async def test_addEvent_name_repeatchar(capfd):
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
async def test_addEvent_points_empty(capfd):
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
async def test_addEvent_points_invalid(capfd):
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
async def test_addEvent_description_empty(capfd):
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
async def test_addEvent_description_long(capfd):
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
async def test_addEvent_description_startchar(capfd):
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
async def test_addEvent_description_spechar(capfd):
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
async def test_addEvent_description_repeatchar(capfd):
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
async def test_updEventId_id_empty(capfd):
    value = ""
    commands = [f"$updEvent:id[{value},"\
                f"{testData['member']},"\
                f"{testData['points']},"\
                f"{testData['desc']}]",
                f"$updEvent:id [{value}, "\
                f"{testData['member']}, "\
                f"{testData['points']}, "\
                f"{testData['desc']} ]",
                f"$updEvent:id [ {value} , "\
                f" {testData['member']} , "\
                f" {testData['points']} , "\
                f" {testData['desc']} ] ",
                f"$updEvent:id [ {value} , "\
                f" {testData['member']} , "\
                f" {testData['points']} , "\
                f" {testData['desc']} ]FILL",
                f"$updEvent:id [ {value} , "\
                f" {testData['member']} , "\
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
async def test_updEventId_id_invalid(capfd):
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


'''
#--------------------Test $updAssist:id [*, Integrante, *, *]------------------
@pytest.mark.asyncio
async def test_updAssistId_member_empty(capfd):
    value = ""
    commands = [f"$updAssist:id[{testData['id']},"\
                f"{value},"\
                f"{testData['event']},"\
                f"{testData['date']}]",
                f"$updAssist:id [{testData['id']}, "\
                f"{value}, "\
                f"{testData['event']}, "\
                f"{testData['date']} ]",
                f"$updAssist:id [ {testData['id']} , "\
                f" {value} , "\
                f" {testData['event']} , "\
                f" {testData['date']} ] ",
                f"$updAssist:id [ {testData['id']} , "\
                f" {value} , "\
                f" {testData['event']} , "\
                f" {testData['date']} ]FILL",
                f"$updAssist:id [ {testData['id']} , "\
                f" {value} , "\
                f" {testData['event']} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updAssist:id", app.updateData,
                           Helpers.updStruct("asistencia", "id"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Integrante_**\n" in out

@pytest.mark.asyncio
async def test_updAssistId_member_long(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$updAssist:id[{testData['id']},"\
                f"{value},"\
                f"{testData['event']},"\
                f"{testData['date']}]",
                f"$updAssist:id [{testData['id']}, "\
                f"{value}, "\
                f"{testData['event']}, "\
                f"{testData['date']} ]",
                f"$updAssist:id [ {testData['id']} , "\
                f" {value} , "\
                f" {testData['event']} , "\
                f" {testData['date']} ] ",
                f"$updAssist:id [ {testData['id']} , "\
                f" {value} , "\
                f" {testData['event']} , "\
                f" {testData['date']} ]FILL",
                f"$updAssist:id [ {testData['id']} , "\
                f" {value} , "\
                f" {testData['event']} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updAssist:id", app.updateData,
                           Helpers.updStruct("asistencia", "id"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Integrante_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def test_updAssistId_member_startchar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$updAssist:id[{testData['id']},"\
                    f"{value},"\
                    f"{testData['event']},"\
                    f"{testData['date']}]",
                    f"$updAssist:id [{testData['id']}, "\
                    f"{value}, "\
                    f"{testData['event']}, "\
                    f"{testData['date']} ]",
                    f"$updAssist:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['event']} , "\
                    f" {testData['date']} ] ",
                    f"$updAssist:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['event']} , "\
                    f" {testData['date']} ]FILL",
                    f"$updAssist:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['event']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updAssist:id", app.updateData,
                               Helpers.updStruct("asistencia", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Integrante_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def test_updAssistId_member_spechar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$updAssist:id[{testData['id']},"\
                    f"{value},"\
                    f"{testData['event']},"\
                    f"{testData['date']}]",
                    f"$updAssist:id [{testData['id']}, "\
                    f"{value}, "\
                    f"{testData['event']}, "\
                    f"{testData['date']} ]",
                    f"$updAssist:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['event']} , "\
                    f" {testData['date']} ] ",
                    f"$updAssist:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['event']} , "\
                    f" {testData['date']} ]FILL",
                    f"$updAssist:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['event']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updAssist:id", app.updateData,
                               Helpers.updStruct("asistencia", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Integrante_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def test_updAssistId_member_repeatchar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$updAssist:id[{testData['id']},"\
                    f"{value},"\
                    f"{testData['event']},"\
                    f"{testData['date']}]",
                    f"$updAssist:id [{testData['id']}, "\
                    f"{value}, "\
                    f"{testData['event']}, "\
                    f"{testData['date']} ]",
                    f"$updAssist:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['event']} , "\
                    f" {testData['date']} ] ",
                    f"$updAssist:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['event']} , "\
                    f" {testData['date']} ]FILL",
                    f"$updAssist:id [ {testData['id']} , "\
                    f" {value} , "\
                    f" {testData['event']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updAssist:id", app.updateData,
                               Helpers.updStruct("asistencia", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Integrante_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#----------------------Test $updAssist:id [*, *, Evento, *]--------------------
@pytest.mark.asyncio
async def test_updAssistId_event_empty(capfd):
    value = ""
    commands = [f"$updAssist:id[{testData['id']},"\
                f"{testData['member']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$updAssist:id [{testData['id']}, "\
                f"{testData['member']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$updAssist:id [ {testData['id']} , "\
                f" {testData['member']} , "\
                f" {value} , "\
                f" {testData['date']} ] ",
                f"$updAssist:id [ {testData['id']} , "\
                f" {testData['member']} , "\
                f" {value} , "\
                f" {testData['date']} ]FILL",
                f"$updAssist:id [ {testData['id']} , "\
                f" {testData['member']} , "\
                f" {value} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updAssist:id", app.updateData,
                           Helpers.updStruct("asistencia", "id"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Evento_**\n" in out

@pytest.mark.asyncio
async def test_updAssistId_event_long(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$updAssist:id[{testData['id']},"\
                f"{testData['member']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$updAssist:id [{testData['id']}, "\
                f"{testData['member']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$updAssist:id [ {testData['id']} , "\
                f" {testData['member']} , "\
                f" {value} , "\
                f" {testData['date']} ] ",
                f"$updAssist:id [ {testData['id']} , "\
                f" {testData['member']} , "\
                f" {value} , "\
                f" {testData['date']} ]FILL",
                f"$updAssist:id [ {testData['id']} , "\
                f" {testData['member']} , "\
                f" {value} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updAssist:id", app.updateData,
                           Helpers.updStruct("asistencia", "id"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Evento_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def test_updAssistId_event_startchar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$updAssist:id[{testData['id']},"\
                    f"{testData['member']},"\
                    f"{value},"\
                    f"{testData['date']}]",
                    f"$updAssist:id [{testData['id']}, "\
                    f"{testData['member']}, "\
                    f"{value}, "\
                    f"{testData['date']} ]",
                    f"$updAssist:id [ {testData['id']} , "\
                    f" {testData['member']} , "\
                    f" {value} , "\
                    f" {testData['date']} ] ",
                    f"$updAssist:id [ {testData['id']} , "\
                    f" {testData['member']} , "\
                    f" {value} , "\
                    f" {testData['date']} ]FILL",
                    f"$updAssist:id [ {testData['id']} , "\
                    f" {testData['member']} , "\
                    f" {value} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updAssist:id", app.updateData,
                               Helpers.updStruct("asistencia", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def test_updAssistId_event_spechar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$updAssist:id[{testData['id']},"\
                    f"{testData['member']},"\
                    f"{value},"\
                    f"{testData['date']}]",
                    f"$updAssist:id [{testData['id']}, "\
                    f"{testData['member']}, "\
                    f"{value}, "\
                    f"{testData['date']} ]",
                    f"$updAssist:id [ {testData['id']} , "\
                    f" {testData['member']} , "\
                    f" {value} , "\
                    f" {testData['date']} ] ",
                    f"$updAssist:id [ {testData['id']} , "\
                    f" {testData['member']} , "\
                    f" {value} , "\
                    f" {testData['date']} ]FILL",
                    f"$updAssist:id [ {testData['id']} , "\
                    f" {testData['member']} , "\
                    f" {value} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updAssist:id", app.updateData,
                               Helpers.updStruct("asistencia", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def test_updAssistId_event_repeatchar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$updAssist:id[{testData['id']},"\
                    f"{testData['member']},"\
                    f"{value},"\
                    f"{testData['date']}]",
                    f"$updAssist:id [{testData['id']}, "\
                    f"{testData['member']}, "\
                    f"{value}, "\
                    f"{testData['date']} ]",
                    f"$updAssist:id [ {testData['id']} , "\
                    f" {testData['member']} , "\
                    f" {value} , "\
                    f" {testData['date']} ] ",
                    f"$updAssist:id [ {testData['id']} , "\
                    f" {testData['member']} , "\
                    f" {value} , "\
                    f" {testData['date']} ]FILL",
                    f"$updAssist:id [ {testData['id']} , "\
                    f" {testData['member']} , "\
                    f" {value} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updAssist:id", app.updateData,
                               Helpers.updStruct("asistencia", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Evento_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#----------------------Test $updAssist:id [*, *, *, Fecha]--------------------
@pytest.mark.asyncio
async def test_updAssistId_date_empty(capfd):
    value = ""
    commands = [f"$updAssist:id[{testData['id']},"\
                f"{testData['member']},"\
                f"{testData['event']},"\
                f"{value}]",
                f"$updAssist:id [{testData['id']}, "\
                f"{testData['member']}, "\
                f"{testData['event']}, "\
                f"{value} ]",
                f"$updAssist:id [ {testData['id']} , "\
                f" {testData['member']} , "\
                f" {testData['event']} , "\
                f" {value} ] ",
                f"$updAssist:id [ {testData['id']} , "\
                f" {testData['member']} , "\
                f" {testData['event']} , "\
                f" {value} ]FILL",
                f"$updAssist:id [ {testData['id']} , "\
                f" {testData['member']} , "\
                f" {testData['event']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updAssist:id", app.updateData,
                           Helpers.updStruct("asistencia", "id"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha_**\n" in out

@pytest.mark.asyncio
async def test_updAssistId_date_invalid(capfd):
    value = "test"
    commands = [f"$updAssist:id[{testData['id']},"\
                f"{testData['member']},"\
                f"{testData['event']},"\
                f"{value}]",
                f"$updAssist:id [{testData['id']}, "\
                f"{testData['member']}, "\
                f"{testData['event']}, "\
                f"{value} ]",
                f"$updAssist:id [ {testData['id']} , "\
                f" {testData['member']} , "\
                f" {testData['event']} , "\
                f" {value} ] ",
                f"$updAssist:id [ {testData['id']} , "\
                f" {testData['member']} , "\
                f" {testData['event']} , "\
                f" {value} ]FILL",
                f"$updAssist:id [ {testData['id']} , "\
                f" {testData['member']} , "\
                f" {testData['event']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updAssist:id", app.updateData,
                           Helpers.updStruct("asistencia", "id"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha_** "\
                "es invalido.\n" in out
#------------------------------$delAssist:id [ID]------------------------------
@pytest.mark.asyncio
async def test_delAssistId_id_empty(capfd):
    value = ""
    commands = [f"$delAssist:id[{value}],",
                f"$delAssist:id [{value} ], ",
                f"$delAssist:id [ {value} ], ",
                f"$delAssist:id [ {value} ]FILL",
                f"$delAssist:id [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delAssist:id", app.deleteData,
                           Helpers.delStruct("asistencia", "id"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_ID_**\n" in out

@pytest.mark.asyncio
async def test_delAssistId_id_invalid(capfd):
    value = "test"
    commands = [f"$delAssist:id[{value}],",
                f"$delAssist:id [{value} ], ",
                f"$delAssist:id [ {value} ], ",
                f"$delAssist:id [ {value} ]FILL",
                f"$delAssist:id [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delAssist:id", app.deleteData,
                           Helpers.delStruct("asistencia", "id"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_ID_** "\
                "es invalido.\n" in out

#------------------------------$listAssist:id [ID]-----------------------------
@pytest.mark.asyncio
async def test_listAssistId_id_empty(capfd):
    value = ""
    commands = [f"$listAssist:id[{value}],",
                f"$listAssist:id [{value} ], ",
                f"$listAssist:id [ {value} ], ",
                f"$listAssist:id [ {value} ]FILL",
                f"$listAssist:id [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:id", app.getDatas,
                         Helpers.getStruct("asistencia", ["id"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_ID_**\n" in out

@pytest.mark.asyncio
async def test_listAssistId_id_invalid(capfd):
    value = "test"
    commands = [f"$listAssist:id[{value}],",
                f"$listAssist:id [{value} ], ",
                f"$listAssist:id [ {value} ], ",
                f"$listAssist:id [ {value} ]FILL",
                f"$listAssist:id [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:id", app.getDatas,
                         Helpers.getStruct("asistencia", ["id"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_ID_** "\
                "es invalido.\n" in out

#---------------------Test $listAssist:member [Integrante]---------------------
@pytest.mark.asyncio
async def test_listAssistMember_member_empty(capfd):
    value = ""
    commands = [f"$listAssist:member[{value}]",
                f"$listAssist:member [{value} ]",
                f"$listAssist:member [ {value} ]",
                f"$listAssist:member [ {value} ]FILL",
                f"$listAssist:member [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member", app.getDatas,
                         Helpers.getStruct("asistencia", ["integrante"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Integrante_**\n" in out

@pytest.mark.asyncio
async def test_listAssistMember_member_long(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$listAssist:member[{value}]",
                f"$listAssist:member [{value} ]",
                f"$listAssist:member [ {value} ]",
                f"$listAssist:member [ {value} ]FILL",
                f"$listAssist:member [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member", app.getDatas,
                         Helpers.getStruct("asistencia", ["integrante"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Integrante_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def test_listAssistMember_member_startchar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$listAssist:member[{value}]",
                    f"$listAssist:member [{value} ]",
                    f"$listAssist:member [ {value} ]",
                    f"$listAssist:member [ {value} ]FILL",
                    f"$listAssist:member [ {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member", app.getDatas,
                             Helpers.getStruct("asistencia", ["integrante"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Integrante_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def test_listAssistMember_member_spechar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$listAssist:member[{value}]",
                    f"$listAssist:member [{value} ]",
                    f"$listAssist:member [ {value} ]",
                    f"$listAssist:member [ {value} ]FILL",
                    f"$listAssist:member [ {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member", app.getDatas,
                             Helpers.getStruct("asistencia", ["integrante"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Integrante_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def test_listAssistMember_member_repeatchar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$listAssist:member[{value}]",
                    f"$listAssist:member [{value} ]",
                    f"$listAssist:member [ {value} ]",
                    f"$listAssist:member [ {value} ]FILL",
                    f"$listAssist:member [ {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member", app.getDatas,
                             Helpers.getStruct("asistencia", ["integrante"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Integrante_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#------------------------Test $listAssist:event [Evento]-----------------------
@pytest.mark.asyncio
async def test_listAssistEvent_event_empty(capfd):
    value = ""
    commands = [f"$listAssist:event[{value}]",
                f"$listAssist:event [{value} ]",
                f"$listAssist:event [ {value} ]",
                f"$listAssist:event [ {value} ]FILL",
                f"$listAssist:event [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:event", app.getDatas,
                         Helpers.getStruct("asistencia", ["evento"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Evento_**\n" in out

@pytest.mark.asyncio
async def test_listAssistEvent_event_long(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$listAssist:event[{value}]",
                f"$listAssist:event [{value} ]",
                f"$listAssist:event [ {value} ]",
                f"$listAssist:event [ {value} ]FILL",
                f"$listAssist:event [ {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:event", app.getDatas,
                         Helpers.getStruct("asistencia", ["evento"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Evento_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def test_listAssistEvent_event_startchar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$listAssist:event[{value}]",
                    f"$listAssist:event [{value} ]",
                    f"$listAssist:event [ {value} ]",
                    f"$listAssist:event [ {value} ]FILL",
                    f"$listAssist:event [ {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:event", app.getDatas,
                             Helpers.getStruct("asistencia", ["evento"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def test_listAssistEvent_event_spechar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$listAssist:event[{value}]",
                    f"$listAssist:event [{value} ]",
                    f"$listAssist:event [ {value} ]",
                    f"$listAssist:event [ {value} ]FILL",
                    f"$listAssist:event [ {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:event", app.getDatas,
                             Helpers.getStruct("asistencia", ["evento"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def test_listAssistEvent_event_repeatchar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$listAssist:event[{value}]",
                    f"$listAssist:event [{value} ]",
                    f"$listAssist:event [ {value} ]",
                    f"$listAssist:event [ {value} ]FILL",
                    f"$listAssist:event [ {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:event", app.getDatas,
                             Helpers.getStruct("asistencia", ["evento"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Evento_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#----------------------Test $listAssist:date [Fecha 1, *]----------------------
@pytest.mark.asyncio
async def test_listAssistDate_date1_empty(capfd):
    value = ""
    commands = [f"$listAssist:date[{value},"\
                f"{testData['date']}]",
                f"$listAssist:date [{value}, "\
                f"{testData['date']} ]",
                f"$listAssist:date [ {value} ,"\
                f" {testData['date']} ]",
                f"$listAssist:date [ {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listAssist:date [ {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 1_**\n" in out

@pytest.mark.asyncio
async def test_listAssistDate_date1_invalid(capfd):
    value = "test"
    commands = [f"$listAssist:date[{value},"\
                f"{testData['date']}]",
                f"$listAssist:date [{value}, "\
                f"{testData['date']} ]",
                f"$listAssist:date [ {value} ,"\
                f" {testData['date']} ]",
                f"$listAssist:date [ {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listAssist:date [ {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 1_** "\
                "es invalido.\n" in out

#----------------------Test $listAssist:date [*, Fecha 2]----------------------
@pytest.mark.asyncio
async def test_listAssistDate_date2_empty(capfd):
    value = ""
    commands = [f"$listAssist:date[{testData['date']},"\
                f"{value}]",
                f"$listAssist:date [{testData['date']}, "\
                f"{value} ]",
                f"$listAssist:date [ {testData['date']} ,"\
                f" {value} ]",
                f"$listAssist:date [ {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listAssist:date [ {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 2_**\n" in out

@pytest.mark.asyncio
async def test_listAssistDate_date2_invalid(capfd):
    value = "test"
    commands = [f"$listAssist:date[{testData['date']},"\
                f"{value}]",
                f"$listAssist:date [{testData['date']}, "\
                f"{value} ]",
                f"$listAssist:date [ {testData['date']} ,"\
                f" {value} ]",
                f"$listAssist:date [ {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listAssist:date [ {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 2_** "\
                "es invalido.\n" in out

#-------------------Test $listAssist:member&event [Integrante, *]--------------
@pytest.mark.asyncio
async def test_listAssistMemberEvent_member_empty(capfd):
    value = ""
    commands = [f"$listAssist:member&event[{value},"\
                f"{testData['event']}]",
                f"$listAssist:member&event [{value}, "\
                f"{testData['event']} ]",
                f"$listAssist:member&event [ {value} , "\
                f" {testData['event']} ] ",
                f"$listAssist:member&event [ {value} , "\
                f" {testData['event']} ]FILL",
                f"$listAssist:member&event [ {value} , "\
                f" {testData['event']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "evento"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Integrante_**\n" in out

@pytest.mark.asyncio
async def test_listAssistMemberEvent_member_long(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$listAssist:member&event[{value},"\
                f"{testData['event']}]",
                f"$listAssist:member&event [{value}, "\
                f"{testData['event']} ]",
                f"$listAssist:member&event [ {value} , "\
                f" {testData['event']} ] ",
                f"$listAssist:member&event [ {value} , "\
                f" {testData['event']} ]FILL",
                f"$listAssist:member&event [ {value} , "\
                f" {testData['event']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "evento"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Integrante_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def test_listAssistMemberEvent_member_startchar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$listAssist:member&event[{value},"\
                    f"{testData['event']}]",
                    f"$listAssist:member&event [{value}, "\
                    f"{testData['event']} ]",
                    f"$listAssist:member&event [ {value} , "\
                    f" {testData['event']} ] ",
                    f"$listAssist:member&event [ {value} , "\
                    f" {testData['event']} ]FILL",
                    f"$listAssist:member&event [ {value} , "\
                    f" {testData['event']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&event", app.getDatas,
                             Helpers.getStruct("asistencia",
                             ["integrante", "evento"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Integrante_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def test_listAssistMemberEvent_member_spechar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$listAssist:member&event[{value},"\
                    f"{testData['event']}]",
                    f"$listAssist:member&event [{value}, "\
                    f"{testData['event']} ]",
                    f"$listAssist:member&event [ {value} , "\
                    f" {testData['event']} ] ",
                    f"$listAssist:member&event [ {value} , "\
                    f" {testData['event']} ]FILL",
                    f"$listAssist:member&event [ {value} , "\
                    f" {testData['event']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&event", app.getDatas,
                             Helpers.getStruct("asistencia",
                             ["integrante", "evento"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Integrante_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def test_listAssistMemberEvent_member_repeatchar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$listAssist:member&event[{value},"\
                    f"{testData['event']}]",
                    f"$listAssist:member&event [{value}, "\
                    f"{testData['event']} ]",
                    f"$listAssist:member&event [ {value} , "\
                    f" {testData['event']} ] ",
                    f"$listAssist:member&event [ {value} , "\
                    f" {testData['event']} ]FILL",
                    f"$listAssist:member&event [ {value} , "\
                    f" {testData['event']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&event", app.getDatas,
                             Helpers.getStruct("asistencia",
                             ["integrante", "evento"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Integrante_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#--------------------Test $listAssist:member&event [*, Evento]-----------------
@pytest.mark.asyncio
async def test_listAssistMemberEvent_event_empty(capfd):
    value = ""
    commands = [f"$listAssist:member&event[{testData['member']},"\
                f"{value}]",
                f"$listAssist:member&event [{testData['member']}, "\
                f"{value} ]",
                f"$listAssist:member&event [ {testData['member']} , "\
                f" {value} ] ",
                f"$listAssist:member&event [ {testData['member']} , "\
                f" {value} ]FILL",
                f"$listAssist:member&event [ {testData['member']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "evento"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Evento_**\n" in out

@pytest.mark.asyncio
async def test_listAssistMemberEvent_event_long(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$listAssist:member&event[{testData['member']},"\
                f"{value}]",
                f"$listAssist:member&event [{testData['member']}, "\
                f"{value} ]",
                f"$listAssist:member&event [ {testData['member']} , "\
                f" {value} ] ",
                f"$listAssist:member&event [ {testData['member']} , "\
                f" {value} ]FILL",
                f"$listAssist:member&event [ {testData['member']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "evento"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Evento_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def test_listAssistMemberEvent_event_startchar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$listAssist:member&event[{testData['member']},"\
                    f"{value}]",
                    f"$listAssist:member&event [{testData['member']}, "\
                    f"{value} ]",
                    f"$listAssist:member&event [ {testData['member']} , "\
                    f" {value} ] ",
                    f"$listAssist:member&event [ {testData['member']} , "\
                    f" {value} ]FILL",
                    f"$listAssist:member&event [ {testData['member']} , "\
                    f" {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&event", app.getDatas,
                             Helpers.getStruct("asistencia",
                             ["integrante", "evento"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def test_listAssistMemberEvent_event_spechar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$listAssist:member&event[{testData['member']},"\
                    f"{value}]",
                    f"$listAssist:member&event [{testData['member']}, "\
                    f"{value} ]",
                    f"$listAssist:member&event [ {testData['member']} , "\
                    f" {value} ] ",
                    f"$listAssist:member&event [ {testData['member']} , "\
                    f" {value} ]FILL",
                    f"$listAssist:member&event [ {testData['member']} , "\
                    f" {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&event", app.getDatas,
                             Helpers.getStruct("asistencia",
                             ["integrante", "evento"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def test_listAssistMemberEvent_event_repeatchar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$listAssist:member&event[{testData['member']},"\
                    f"{value}]",
                    f"$listAssist:member&event [{testData['member']}, "\
                    f"{value} ]",
                    f"$listAssist:member&event [ {testData['member']} , "\
                    f" {value} ] ",
                    f"$listAssist:member&event [ {testData['member']} , "\
                    f" {value} ]FILL",
                    f"$listAssist:member&event [ {testData['member']} , "\
                    f" {value} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&event", app.getDatas,
                             Helpers.getStruct("asistencia",
                             ["integrante", "evento"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Evento_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#-----------------Test $listAssist:member&date [Integrante, *, *]--------------
@pytest.mark.asyncio
async def test_listAssistMemberDate_member_empty(capfd):
    value = ""
    commands = [f"$listAssist:member&date[{value},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listAssist:member&date [{value}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listAssist:member&date [ {value} , "\
                f" {testData['date']} , "\
                f" {testData['date']} ] ",
                f"$listAssist:member&date [ {value} , "\
                f" {testData['date']} , "\
                f" {testData['date']} ]FILL",
                f"$listAssist:member&date [ {value} , "\
                f" {testData['date']} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Integrante_**\n" in out

@pytest.mark.asyncio
async def test_listAssisMemberDate_member_long(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$listAssist:member&date[{value},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listAssist:member&date [{value}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listAssist:member&date [ {value} , "\
                f" {testData['date']} , "\
                f" {testData['date']} ] ",
                f"$listAssist:member&date [ {value} , "\
                f" {testData['date']} , "\
                f" {testData['date']} ]FILL",
                f"$listAssist:member&date [ {value} , "\
                f" {testData['date']} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Integrante_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def test_listAssisMemberDate_member_startchar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$listAssist:member&date[{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAssist:member&date [{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAssist:member&date [ {value} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ] ",
                    f"$listAssist:member&date [ {value} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ]FILL",
                    f"$listAssist:member&date [ {value} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                             Helpers.getStruct("asistencia",
                             ["integrante", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Integrante_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def test_listAssisMemberDate_member_spechar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$listAssist:member&date[{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAssist:member&date [{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAssist:member&date [ {value} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ] ",
                    f"$listAssist:member&date [ {value} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ]FILL",
                    f"$listAssist:member&date [ {value} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                             Helpers.getStruct("asistencia",
                             ["integrante", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Integrante_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def test_listAssisMemberDate_member_repeatchar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$listAssist:member&date[{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAssist:member&date [{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAssist:member&date [ {value} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ] ",
                    f"$listAssist:member&date [ {value} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ]FILL",
                    f"$listAssist:member&date [ {value} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                             Helpers.getStruct("asistencia",
                             ["integrante", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Integrante_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#-------------------Test $listAssist:member&date [*, Fecha 1, *]---------------
@pytest.mark.asyncio
async def test_listAssistMemberDate_date1_empty(capfd):
    value = ""
    commands = [f"$listAssist:member&date[{testData['member']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$listAssist:member&date [{testData['member']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$listAssist:member&date [ {testData['member']} , "\
                f" {value} , "\
                f" {testData['date']} ] ",
                f"$listAssist:member&date [ {testData['member']} , "\
                f" {value} , "\
                f" {testData['date']} ]FILL",
                f"$listAssist:member&date [ {testData['member']} , "\
                f" {value} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 1_**\n" in out

@pytest.mark.asyncio
async def test_listAssisMemberDate_date1_invalid(capfd):
    value = "test"
    commands = [f"$listAssist:member&date[{testData['member']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$listAssist:member&date [{testData['member']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$listAssist:member&date [ {testData['member']} , "\
                f" {value} , "\
                f" {testData['date']} ] ",
                f"$listAssist:member&date [ {testData['member']} , "\
                f" {value} , "\
                f" {testData['date']} ]FILL",
                f"$listAssist:member&date [ {testData['member']} , "\
                f" {value} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 1_** "\
                "es invalido.\n" in out

#------------------Test $listAssist:member&date [*, *, Fecha 2]----------------
@pytest.mark.asyncio
async def test_listAssistMemberDate_date2_empty(capfd):
    value = ""
    commands = [f"$listAssist:member&date[{testData['member']},"\
                f"{testData['date']},"\
                f"{value}]",
                f"$listAssist:member&date [{testData['member']}, "\
                f"{testData['date']}, "\
                f"{value} ]",
                f"$listAssist:member&date [ {testData['member']} , "\
                f" {testData['date']} , "\
                f" {value} ] ",
                f"$listAssist:member&date [ {testData['member']} , "\
                f" {testData['date']} , "\
                f" {value} ]FILL",
                f"$listAssist:member&date [ {testData['member']} , "\
                f" {testData['date']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 2_**\n" in out

@pytest.mark.asyncio
async def test_listAssisMemberDate_date2_invalid(capfd):
    value = "test"
    commands = [f"$listAssist:member&date[{testData['member']},"\
                f"{testData['date']},"\
                f"{value}]",
                f"$listAssist:member&date [{testData['member']}, "\
                f"{testData['date']}, "\
                f"{value} ]",
                f"$listAssist:member&date [ {testData['member']} , "\
                f" {testData['date']} , "\
                f" {value} ] ",
                f"$listAssist:member&date [ {testData['member']} , "\
                f" {testData['date']} , "\
                f" {value} ]FILL",
                f"$listAssist:member&date [ {testData['member']} , "\
                f" {testData['date']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 2_** "\
                "es invalido.\n" in out

#-----------------Test $listAssist:event&date [Evento, *, *]--------------
@pytest.mark.asyncio
async def test_listAssistEventDate_event_empty(capfd):
    value = ""
    commands = [f"$listAssist:event&date[{value},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listAssist:event&date [{value}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listAssist:event&date [ {value} , "\
                f" {testData['date']} , "\
                f" {testData['date']} ] ",
                f"$listAssist:event&date [ {value} , "\
                f" {testData['date']} , "\
                f" {testData['date']} ]FILL",
                f"$listAssist:event&date [ {value} , "\
                f" {testData['date']} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["evento", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Evento_**\n" in out

@pytest.mark.asyncio
async def test_listAssisEventDate_event_long(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$listAssist:event&date[{value},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listAssist:event&date [{value}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listAssist:event&date [ {value} , "\
                f" {testData['date']} , "\
                f" {testData['date']} ] ",
                f"$listAssist:event&date [ {value} , "\
                f" {testData['date']} , "\
                f" {testData['date']} ]FILL",
                f"$listAssist:event&date [ {value} , "\
                f" {testData['date']} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["evento", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Evento_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def test_listAssisEventDate_event_startchar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$listAssist:event&date[{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAssist:event&date [{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAssist:event&date [ {value} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ] ",
                    f"$listAssist:event&date [ {value} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ]FILL",
                    f"$listAssist:event&date [ {value} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                             Helpers.getStruct("asistencia",
                             ["evento", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def test_listAssisEventDate_event_spechar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$listAssist:event&date[{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAssist:event&date [{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAssist:event&date [ {value} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ] ",
                    f"$listAssist:event&date [ {value} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ]FILL",
                    f"$listAssist:event&date [ {value} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                             Helpers.getStruct("asistencia",
                             ["evento", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def test_listAssisEventDate_event_repeatchar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$listAssist:event&date[{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAssist:event&date [{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAssist:event&date [ {value} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ] ",
                    f"$listAssist:event&date [ {value} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ]FILL",
                    f"$listAssist:event&date [ {value} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                             Helpers.getStruct("asistencia",
                             ["evento", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Evento_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#-------------------Test $listAssist:event&date [*, Fecha 1, *]---------------
@pytest.mark.asyncio
async def test_listAssistEventDate_date1_empty(capfd):
    value = ""
    commands = [f"$listAssist:event&date[{testData['event']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$listAssist:event&date [{testData['event']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$listAssist:event&date [ {testData['event']} , "\
                f" {value} , "\
                f" {testData['date']} ] ",
                f"$listAssist:event&date [ {testData['event']} , "\
                f" {value} , "\
                f" {testData['date']} ]FILL",
                f"$listAssist:event&date [ {testData['event']} , "\
                f" {value} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["evento", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 1_**\n" in out

@pytest.mark.asyncio
async def test_listAssisEventDate_date1_invalid(capfd):
    value = "test"
    commands = [f"$listAssist:event&date[{testData['event']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$listAssist:event&date [{testData['event']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$listAssist:event&date [ {testData['event']} , "\
                f" {value} , "\
                f" {testData['date']} ] ",
                f"$listAssist:event&date [ {testData['event']} , "\
                f" {value} , "\
                f" {testData['date']} ]FILL",
                f"$listAssist:event&date [ {testData['event']} , "\
                f" {value} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["evento", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 1_** "\
                "es invalido.\n" in out

#------------------Test $listAssist:event&date [*, *, Fecha 2]----------------
@pytest.mark.asyncio
async def test_listAssistEventDate_date2_empty(capfd):
    value = ""
    commands = [f"$listAssist:event&date[{testData['event']},"\
                f"{testData['date']},"\
                f"{value}]",
                f"$listAssist:event&date [{testData['event']}, "\
                f"{testData['date']}, "\
                f"{value} ]",
                f"$listAssist:event&date [ {testData['event']} , "\
                f" {testData['date']} , "\
                f" {value} ] ",
                f"$listAssist:event&date [ {testData['event']} , "\
                f" {testData['date']} , "\
                f" {value} ]FILL",
                f"$listAssist:event&date [ {testData['event']} , "\
                f" {testData['date']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["evento", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 2_**\n" in out

@pytest.mark.asyncio
async def test_listAssisEventDate_date2_invalid(capfd):
    value = "test"
    commands = [f"$listAssist:event&date[{testData['event']},"\
                f"{testData['date']},"\
                f"{value}]",
                f"$listAssist:event&date [{testData['event']}, "\
                f"{testData['date']}, "\
                f"{value} ]",
                f"$listAssist:event&date [ {testData['event']} , "\
                f" {testData['date']} , "\
                f" {value} ] ",
                f"$listAssist:event&date [ {testData['event']} , "\
                f" {testData['date']} , "\
                f" {value} ]FILL",
                f"$listAssist:event&date [ {testData['event']} , "\
                f" {testData['date']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["evento", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 2_** "\
                "es invalido.\n" in out

#------------Test $listAssist:member&event&date [Integrante, *, *, *]----------
@pytest.mark.asyncio
async def test_listAssistMemberEventDate_member_empty(capfd):
    value = ""
    commands = [f"$listAssist:member&event&date[{value},"\
                f"{testData['event']},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listAssist:member&event&date [{value}, "\
                f"{testData['event']}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listAssist:member&event&date [ {value} , "\
                f" {testData['event']} , "\
                f" {testData['date']} , "\
                f" {testData['date']} ] ",
                f"$listAssist:member&event&date [ {value} , "\
                f" {testData['event']} , "\
                f" {testData['date']} , "\
                f" {testData['date']} ]FILL",
                f"$listAssist:member&event&date [ {value} , "\
                f" {testData['event']} , "\
                f" {testData['date']} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "evento", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Integrante_**\n" in out

@pytest.mark.asyncio
async def test_listAssisMemberEventDate_member_long(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$listAssist:member&event&date[{value},"\
                f"{testData['event']},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listAssist:member&event&date [{value}, "\
                f"{testData['event']}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listAssist:member&event&date [ {value} , "\
                f" {testData['event']} , "\
                f" {testData['date']} , "\
                f" {testData['date']} ] ",
                f"$listAssist:member&event&date [ {value} , "\
                f" {testData['event']} , "\
                f" {testData['date']} , "\
                f" {testData['date']} ]FILL",
                f"$listAssist:member&event&date [ {value} , "\
                f" {testData['event']} , "\
                f" {testData['date']} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "evento", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Integrante_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def test_listAssisMemberEventDate_member_startchar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$listAssist:member&event&date[{value},"\
                    f"{testData['event']},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAssist:member&event&date [{value}, "\
                    f"{testData['event']}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAssist:member&event&date [ {value} , "\
                    f" {testData['event']} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ] ",
                    f"$listAssist:member&event&date [ {value} , "\
                    f" {testData['event']} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ]FILL",
                    f"$listAssist:member&event&date [ {value} , "\
                    f" {testData['event']} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                             Helpers.getStruct("asistencia",
                             ["integrante", "evento", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Integrante_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def test_listAssisMemberEventDate_member_spechar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$listAssist:member&event&date[{value},"\
                    f"{testData['event']},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAssist:member&event&date [{value}, "\
                    f"{testData['event']}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAssist:member&event&date [ {value} , "\
                    f" {testData['event']} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ] ",
                    f"$listAssist:member&event&date [ {value} , "\
                    f" {testData['event']} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ]FILL",
                    f"$listAssist:member&event&date [ {value} , "\
                    f" {testData['event']} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                             Helpers.getStruct("asistencia",
                             ["integrante", "evento", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Integrante_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def test_listAssisMemberEventDate_member_repeatchar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$listAssist:member&event&date[{value},"\
                    f"{testData['event']},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAssist:member&event&date [{value}, "\
                    f"{testData['event']}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAssist:member&event&date [ {value} , "\
                    f" {testData['event']} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ] ",
                    f"$listAssist:member&event&date [ {value} , "\
                    f" {testData['event']} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ]FILL",
                    f"$listAssist:member&event&date [ {value} , "\
                    f" {testData['event']} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                             Helpers.getStruct("asistencia",
                             ["integrante", "evento", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Integrante_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#------------Test $listAssist:member&event&date [*, Evento, *, *]----------
@pytest.mark.asyncio
async def test_listAssistMemberEventDate_event_empty(capfd):
    value = ""
    commands = [f"$listAssist:member&event&date[{testData['member']},"\
                f"{value},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listAssist:member&event&date [{testData['member']}, "\
                f"{value}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listAssist:member&event&date [ {testData['member']} , "\
                f" {value} , "\
                f" {testData['date']} , "\
                f" {testData['date']} ] ",
                f"$listAssist:member&event&date [ {testData['member']} , "\
                f" {value} , "\
                f" {testData['date']} , "\
                f" {testData['date']} ]FILL",
                f"$listAssist:member&event&date [ {testData['member']} , "\
                f" {value} , "\
                f" {testData['date']} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "evento", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Evento_**\n" in out

@pytest.mark.asyncio
async def test_listAssisMemberEventDate_event_long(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$listAssist:member&event&date[{testData['member']},"\
                f"{value},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listAssist:member&event&date [{testData['member']}, "\
                f"{value}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listAssist:member&event&date [ {testData['member']} , "\
                f" {value} , "\
                f" {testData['date']} , "\
                f" {testData['date']} ] ",
                f"$listAssist:member&event&date [ {testData['member']} , "\
                f" {value} , "\
                f" {testData['date']} , "\
                f" {testData['date']} ]FILL",
                f"$listAssist:member&event&date [ {testData['member']} , "\
                f" {value} , "\
                f" {testData['date']} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "evento", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Evento_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def test_listAssisMemberEventDate_event_startchar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$listAssist:member&event&date[{testData['member']},"\
                    f"{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAssist:member&event&date [{testData['member']}, "\
                    f"{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAssist:member&event&date [ {testData['member']} , "\
                    f" {value} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ] ",
                    f"$listAssist:member&event&date [ {testData['member']} , "\
                    f" {value} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ]FILL",
                    f"$listAssist:member&event&date [ {testData['member']} , "\
                    f" {value} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                             Helpers.getStruct("asistencia",
                             ["integrante", "evento", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def test_listAssisMemberEventDate_event_spechar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$listAssist:member&event&date[{testData['member']},"\
                    f"{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAssist:member&event&date [{testData['member']}, "\
                    f"{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAssist:member&event&date [ {testData['member']} , "\
                    f" {value} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ] ",
                    f"$listAssist:member&event&date [ {testData['member']} , "\
                    f" {value} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ]FILL",
                    f"$listAssist:member&event&date [ {testData['member']} , "\
                    f" {value} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                             Helpers.getStruct("asistencia",
                             ["integrante", "evento", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def test_listAssisMemberEventDate_event_repeatchar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$listAssist:member&event&date[{testData['member']},"\
                    f"{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAssist:member&event&date [{testData['member']}, "\
                    f"{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAssist:member&event&date [ {testData['member']} , "\
                    f" {value} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ] ",
                    f"$listAssist:member&event&date [ {testData['member']} , "\
                    f" {value} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ]FILL",
                    f"$listAssist:member&event&date [ {testData['member']} , "\
                    f" {value} , "\
                    f" {testData['date']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                             Helpers.getStruct("asistencia",
                             ["integrante", "evento", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Evento_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#--------------Test $listAssist:member&event&date [*, Fecha 1, *, *]-----------
@pytest.mark.asyncio
async def test_listAssistMemberEventDate_date1_empty(capfd):
    value = ""
    commands = [f"$listAssist:member&event&date[{testData['member']},"\
                f"{testData['event']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$listAssist:member&event&date [{testData['member']}, "\
                f"{testData['event']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$listAssist:member&event&date [ {testData['member']} , "\
                f" {testData['event']} , "\
                f" {value} , "\
                f" {testData['date']} ] ",
                f"$listAssist:member&event&date [ {testData['member']} , "\
                f" {testData['event']} , "\
                f" {value} , "\
                f" {testData['date']} ]FILL",
                f"$listAssist:member&event&date [ {testData['member']} , "\
                f" {testData['event']} , "\
                f" {value} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "evento", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 1_**\n" in out

@pytest.mark.asyncio
async def test_listAssisMemberEventDate_date1_invalid(capfd):
    value = "test"
    commands = [f"$listAssist:member&event&date[{testData['member']},"\
                f"{testData['event']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$listAssist:member&event&date [{testData['member']}, "\
                f"{testData['event']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$listAssist:member&event&date [ {testData['member']} , "\
                f" {testData['event']} , "\
                f" {value} , "\
                f" {testData['date']} ] ",
                f"$listAssist:member&event&date [ {testData['member']} , "\
                f" {testData['event']} , "\
                f" {value} , "\
                f" {testData['date']} ]FILL",
                f"$listAssist:member&event&date [ {testData['member']} , "\
                f" {testData['event']} , "\
                f" {value} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "evento", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 1_** "\
                "es invalido.\n" in out

#-------------Test $listAssist:member&event&date [*, *, *, Fecha 2]------------
@pytest.mark.asyncio
async def test_listAssistMemberEventDate_date2_empty(capfd):
    value = ""
    commands = [f"$listAssist:member&event&date[{testData['member']},"\
                f"{testData['event']},"\
                f"{testData['date']},"\
                f"{value}]",
                f"$listAssist:member&event&date [{testData['member']}, "\
                f"{testData['event']}, "\
                f"{testData['date']}, "\
                f"{value} ]",
                f"$listAssist:member&event&date [ {testData['member']} , "\
                f" {testData['event']} , "\
                f" {testData['date']} , "\
                f" {value} ] ",
                f"$listAssist:member&event&date [ {testData['member']} , "\
                f" {testData['event']} , "\
                f" {testData['date']} , "\
                f" {value} ]FILL",
                f"$listAssist:member&event&date [ {testData['member']} , "\
                f" {testData['event']} , "\
                f" {testData['date']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "evento", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 2_**\n" in out

@pytest.mark.asyncio
async def test_listAssisMemberEventDate_date2_invalid(capfd):
    value = "test"
    commands = [f"$listAssist:member&event&date[{testData['member']},"\
                f"{testData['event']},"\
                f"{testData['date']},"\
                f"{value}]",
                f"$listAssist:member&event&date [{testData['member']}, "\
                f"{testData['event']}, "\
                f"{testData['date']}, "\
                f"{value} ]",
                f"$listAssist:member&event&date [ {testData['member']} , "\
                f" {testData['event']} , "\
                f" {testData['date']} , "\
                f" {value} ] ",
                f"$listAssist:member&event&date [ {testData['member']} , "\
                f" {testData['event']} , "\
                f" {testData['date']} , "\
                f" {value} ]FILL",
                f"$listAssist:member&event&date [ {testData['member']} , "\
                f" {testData['event']} , "\
                f" {testData['date']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "evento", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 2_** "\
                "es invalido.\n" in out
'''