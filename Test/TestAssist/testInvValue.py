import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Helpers.helpers import Helpers
from collections import namedtuple

testData = {
    "id" : "1",
    "member" : "Avalonicus",
    "event" : "defprismaganada",
    "date" : "25-01-2300",
}

Message = namedtuple('Message', ['author', 'content'])
Client = namedtuple('Client', ['user'])
app = AppHandler()

#----------------------Test $addAssist [Integrante, *, *]----------------------
@pytest.mark.asyncio
async def test_addAssist_member_empty(capfd):
    value = ""
    commands = [f"$addAssist[{value},"\
                f"{testData['event']},"\
                f"{testData['date']}]",
                f"$addAssist [{value}, "\
                f"{testData['event']}, "\
                f"{testData['date']} ]",
                f"$addAssist [ {value} , "\
                f" {testData['event']} , "\
                f" {testData['date']} ] ",
                f"$addAssist [ {value} , "\
                f" {testData['event']} , "\
                f" {testData['date']} ]FILL",
                f"$addAssist [ {value} , "\
                f" {testData['event']} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addAssist", app.setData,
                           Helpers.setStruct("asistencia"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Integrante_**\n" in out

pytest.mark.asyncio
async def test_addAssist_member_long(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$addAssist[{value},"\
                f"{testData['event']},"\
                f"{testData['date']}]",
                f"$addAssist [{value}, "\
                f"{testData['event']}, "\
                f"{testData['date']} ]",
                f"$addAssist [ {value} , "\
                f" {testData['event']} , "\
                f" {testData['date']} ] ",
                f"$addAssist [ {value} , "\
                f" {testData['event']} , "\
                f" {testData['date']} ]FILL",
                f"$addAssist [ {value} , "\
                f" {testData['event']} , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addAssist", app.setData,
                           Helpers.setStruct("asistencia"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Integrante_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def test_addAssist_member_startchar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$addAssist[{value},"\
                    f"{testData['event']},"\
                    f"{testData['date']}]",
                    f"$addAssist [{value}, "\
                    f"{testData['event']}, "\
                    f"{testData['date']} ]",
                    f"$addAssist [ {value} , "\
                    f" {testData['event']} , "\
                    f" {testData['date']} ] ",
                    f"$addAssist [ {value} , "\
                    f" {testData['event']} , "\
                    f" {testData['date']} ]FILL",
                    f"$addAssist [ {value} , "\
                    f" {testData['event']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addAssist", app.setData,
                               Helpers.setStruct("asistencia"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Integrante_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def test_addAssist_member_spechar(capfd):
    values = ["test/", "test{", "te/st", "te|st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$addAssist[{value},"\
                    f"{testData['event']},"\
                    f"{testData['date']}]",
                    f"$addAssist [{value}, "\
                    f"{testData['event']}, "\
                    f"{testData['date']} ]",
                    f"$addAssist [ {value} , "\
                    f" {testData['event']} , "\
                    f" {testData['date']} ] ",
                    f"$addAssist [ {value} , "\
                    f" {testData['event']} , "\
                    f" {testData['date']} ]FILL",
                    f"$addAssist [ {value} , "\
                    f" {testData['event']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addAssist", app.setData,
                               Helpers.setStruct("asistencia"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Integrante_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def test_addAssist_member_repeatchar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$addAssist[{value},"\
                    f"{testData['event']},"\
                    f"{testData['date']}]",
                    f"$addAssist [{value}, "\
                    f"{testData['event']}, "\
                    f"{testData['date']} ]",
                    f"$addAssist [ {value} , "\
                    f" {testData['event']} , "\
                    f" {testData['date']} ] ",
                    f"$addAssist [ {value} , "\
                    f" {testData['event']} , "\
                    f" {testData['date']} ]FILL",
                    f"$addAssist [ {value} , "\
                    f" {testData['event']} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addAssist", app.setData,
                               Helpers.setStruct("asistencia"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Integrante_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#-----------------------Test $addAssist [* ,Evento, *]-------------------------
@pytest.mark.asyncio
async def test_addAssist_event_empty(capfd):
    value = ""
    commands = [f"$addAssist[{testData['member']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$addAssist [{testData['member']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$addAssist [ {testData['member']} , "\
                f" {value} , "\
                f" {testData['date']} ] ",
                f"$addAssist [ {testData['member']} , "\
                f" {value}  , "\
                f" {testData['date']} ]FILL",
                f"$addAssist [ {testData['member']} , "\
                f" {value}  , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addAssist", app.setData,
                           Helpers.setStruct("asistencia"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Evento_**\n" in out

async def test_addAssist_event_long(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$addAssist[{testData['member']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$addAssist [{testData['member']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$addAssist [ {testData['member']} , "\
                f" {value} , "\
                f" {testData['date']} ] ",
                f"$addAssist [ {testData['member']} , "\
                f" {value}  , "\
                f" {testData['date']} ]FILL",
                f"$addAssist [ {testData['member']} , "\
                f" {value}  , "\
                f" {testData['date']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addAssist", app.setData,
                           Helpers.setStruct("asistencia"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Evento_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def test_addAssist_event_startchar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$addAssist[{testData['member']},"\
                    f"{value},"\
                    f"{testData['date']}]",
                    f"$addAssist [{testData['member']}, "\
                    f"{value}, "\
                    f"{testData['date']} ]",
                    f"$addAssist [ {testData['member']} , "\
                    f" {value} , "\
                    f" {testData['date']} ] ",
                    f"$addAssist [ {testData['member']} , "\
                    f" {value} , "\
                    f" {testData['date']} ]FILL",
                    f"$addAssist [ {testData['member']} , "\
                    f" {value} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addAssist", app.setData,
                               Helpers.setStruct("asistencia"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def test_addAssist_event_spechar(capfd):
    values = ["test/", "test{", "te/st", "te|st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$addAssist[{testData['member']},"\
                    f"{value},"\
                    f"{testData['date']}]",
                    f"$addAssist [{testData['member']}, "\
                    f"{value}, "\
                    f"{testData['date']} ]",
                    f"$addAssist [ {testData['member']} , "\
                    f" {value} , "\
                    f" {testData['date']} ] ",
                    f"$addAssist [ {testData['member']} , "\
                    f" {value} , "\
                    f" {testData['date']} ]FILL",
                    f"$addAssist [ {testData['member']} , "\
                    f" {value} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addAssist", app.setData,
                               Helpers.setStruct("asistencia"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def test_addAssist_event_repeatchar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$addAssist[{testData['member']},"\
                    f"{value},"\
                    f"{testData['date']}]",
                    f"$addAssist [{testData['member']}, "\
                    f"{value}, "\
                    f"{testData['date']} ]",
                    f"$addAssist [ {testData['member']} , "\
                    f" {value} , "\
                    f" {testData['date']} ] ",
                    f"$addAssist [ {testData['member']} , "\
                    f" {value} , "\
                    f" {testData['date']} ]FILL",
                    f"$addAssist [ {testData['member']} , "\
                    f" {value} , "\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            message = Message(author="test", content=command)
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addAssist", app.setData,
                               Helpers.setStruct("asistencia"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Evento_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#-------------------------Test $addAssist [*, *, Fecha]------------------------
@pytest.mark.asyncio
async def test_addAssist_date_empty(capfd):
    value = ""
    commands = [f"$addAssist[{testData['member']},"\
                f"{testData['event']},"\
                f"{value}]",
                f"$addAssist [{testData['member']}, "\
                f"{testData['event']}, "\
                f"{value} ]",
                f"$addAssist [ {testData['member']} , "\
                f" {testData['event']} , "\
                f" {value} ] ",
                f"$addAssist [ {testData['member']} , "\
                f" {testData['event']} , "\
                f" {value} ]FILL",
                f"$addAssist [ {testData['member']} , "\
                f" {testData['event']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addAssist", app.setData,
                           Helpers.setStruct("asistencia"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha_**\n" in out

@pytest.mark.asyncio
async def test_addAssist_date_invalid(capfd):
    value = "test"
    commands = [f"$addAssist[{testData['member']},"\
                f"{testData['event']},"\
                f"{value}]",
                f"$addAssist [{testData['member']}, "\
                f"{testData['event']}, "\
                f"{value} ]",
                f"$addAssist [ {testData['member']} , "\
                f" {testData['event']} , "\
                f" {value} ] ",
                f"$addAssist [ {testData['member']} , "\
                f" {testData['event']} , "\
                f" {value} ]FILL",
                f"$addAssist [ {testData['member']} , "\
                f" {testData['event']} , "\
                f" {value} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addAssist", app.setData,
                           Helpers.setStruct("asistencia"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha_** "\
                "es invalido.\n" in out

#------------------------Test $updAssist:id [ID, *, *, *]----------------------
@pytest.mark.asyncio
async def test_updAssistId_id_empty(capfd):
    value = ""
    commands = [f"$updAssist:id[{value},"\
                f"{testData['member']},"\
                f"{testData['event']},"\
                f"{testData['date']}]",
                f"$updAssist:id [{value}, "\
                f"{testData['member']}, "\
                f"{testData['event']}, "\
                f"{testData['date']} ]",
                f"$updAssist:id [ {value} , "\
                f" {testData['member']} , "\
                f" {testData['event']} , "\
                f" {testData['date']} ] ",
                f"$updAssist:id [ {value} , "\
                f" {testData['member']} , "\
                f" {testData['event']} , "\
                f" {testData['date']} ]FILL",
                f"$updAssist:id [ {value} , "\
                f" {testData['member']} , "\
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
               "**_ID_**\n" in out

@pytest.mark.asyncio
async def test_updAssistId_id_invalid(capfd):
    value = "test"
    commands = [f"$updAssist:id[{value},"\
                f"{testData['member']},"\
                f"{testData['event']},"\
                f"{testData['date']}]",
                f"$updAssist:id [{value}, "\
                f"{testData['member']}, "\
                f"{testData['event']}, "\
                f"{testData['date']} ]",
                f"$updAssist:id [ {value} , "\
                f" {testData['member']} , "\
                f" {testData['event']} , "\
                f" {testData['date']} ] ",
                f"$updAssist:id [ {value} , "\
                f" {testData['member']} , "\
                f" {testData['event']} , "\
                f" {testData['date']} ]FILL",
                f"$updAssist:id [ {value} , "\
                f" {testData['member']} , "\
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
               f"**_ID_** "\
                "es invalido.\n" in out

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
    values = ["test/", "test{", "te/st", "te|st",
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
    values = ["test/", "test{", "te/st", "te|st",
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
'''
#-----------------------------$listAssist:id [ID]------------------------------

@pytest.mark.asyncio
async def test_listAssistId_invalidParams(capfd):
    commands = ["$listAssist:id[,,,,]",
                "$listAssist:id [,,,,]",
                "$listAssist:id[,,,,]FILL",
                "$listAssist:id[,,,,] FILL",
                "$listAssist:id[,,,,]]FILL",
                "$listAssist:id [,,,,]] FILL",
                "$listAssist:id[[,,,,]FILL",
                "$listAssist:id [[,,,,] FILL",
                "$listAssist:id[[,,,,]]FILL",
                "$listAssist:id [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:id", app.getDatas,
                         Helpers.getStruct("asistencia", ["id"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_ID_]**\n" in out

@pytest.mark.asyncio
async def test_listAssistMember_invalidParams(capfd):
    commands = ["$listAssist:member[,,,,]",
                "$listAssist:member [,,,,]",
                "$listAssist:member[,,,,]FILL",
                "$listAssist:member[,,,,] FILL",
                "$listAssist:member[,,,,]]FILL",
                "$listAssist:member [,,,,]] FILL",
                "$listAssist:member[[,,,,]FILL",
                "$listAssist:member [[,,,,] FILL",
                "$listAssist:member[[,,,,]]FILL",
                "$listAssist:member [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member", app.getDatas,
                         Helpers.getStruct("asistencia", ["integrante"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Integrante_]**\n" in out

@pytest.mark.asyncio
async def test_listAssistEvent_invalidParams(capfd):
    commands = ["$listAssist:event[,,,,]",
                "$listAssist:event [,,,,]",
                "$listAssist:event[,,,,]FILL",
                "$listAssist:event[,,,,] FILL",
                "$listAssist:event[,,,,]]FILL",
                "$listAssist:event [,,,,]] FILL",
                "$listAssist:event[[,,,,]FILL",
                "$listAssist:event [[,,,,] FILL",
                "$listAssist:event[[,,,,]]FILL",
                "$listAssist:event [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:event", app.getDatas,
                         Helpers.getStruct("asistencia", ["evento"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Evento_]**\n" in out

@pytest.mark.asyncio
async def test_listAssistDate_invalidParams(capfd):
    commands = ["$listAssist:date[]",
                "$listAssist:date []",
                "$listAssist:date[,,,,]",
                "$listAssist:date [,,,,]",
                "$listAssist:date[,,,,]FILL",
                "$listAssist:date[,,,,] FILL",
                "$listAssist:date[,,,,]]FILL",
                "$listAssist:date [,,,,]] FILL",
                "$listAssist:date[[,,,,]FILL",
                "$listAssist:date [[,,,,] FILL",
                "$listAssist:date[[,,,,]]FILL",
                "$listAssist:date [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def test_listAssistMemberEvent_invalidParams(capfd):
    commands = ["$listAssist:member&event[]",
                "$listAssist:member&event []",
                "$listAssist:member&event[,,,,]",
                "$listAssist:member&event [,,,,]",
                "$listAssist:member&event[,,,,]FILL",
                "$listAssist:member&event[,,,,] FILL",
                "$listAssist:member&event[,,,,]]FILL",
                "$listAssist:member&event [,,,,]] FILL",
                "$listAssist:member&event[[,,,,]FILL",
                "$listAssist:member&event [[,,,,] FILL",
                "$listAssist:member&event[[,,,,]]FILL",
                "$listAssist:member&event [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "evento"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Integrante, Evento_]**\n" in out

@pytest.mark.asyncio
async def test_listAssistMemberDate_invalidParams(capfd):
    commands = ["$listAssist:member&date[]",
                "$listAssist:member&date []",
                "$listAssist:member&date[,,,,]",
                "$listAssist:member&date [,,,,]",
                "$listAssist:member&date[,,,,]FILL",
                "$listAssist:member&date[,,,,] FILL",
                "$listAssist:member&date[,,,,]]FILL",
                "$listAssist:member&date [,,,,]] FILL",
                "$listAssist:member&date[[,,,,]FILL",
                "$listAssist:member&date [[,,,,] FILL",
                "$listAssist:member&date[[,,,,]]FILL",
                "$listAssist:member&date [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Integrante, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def test_listAssistEventDate_invalidParams(capfd):
    commands = ["$listAssist:event&date[]",
                "$listAssist:event&date []",
                "$listAssist:event&date[,,,,]",
                "$listAssist:event&date [,,,,]",
                "$listAssist:event&date[,,,,]FILL",
                "$listAssist:event&date[,,,,] FILL",
                "$listAssist:event&date[,,,,]]FILL",
                "$listAssist:event&date [,,,,]] FILL",
                "$listAssist:event&date[[,,,,]FILL",
                "$listAssist:event&date [[,,,,] FILL",
                "$listAssist:event&date[[,,,,]]FILL",
                "$listAssist:event&date [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["evento", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Evento, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def test_listAssistMemberEventDate_invalidParams(capfd):
    commands = ["$listAssist:member&event&date[]",
                "$listAssist:member&event&date []",
                "$listAssist:member&event&date[,,,,]",
                "$listAssist:member&event&date [,,,,]",
                "$listAssist:member&event&date[,,,,]FILL",
                "$listAssist:member&event&date[,,,,] FILL",
                "$listAssist:member&event&date[,,,,]]FILL",
                "$listAssist:member&event&date [,,,,]] FILL",
                "$listAssist:member&event&date[[,,,,]FILL",
                "$listAssist:member&event&date [[,,,,] FILL",
                "$listAssist:member&event&date[[,,,,]]FILL",
                "$listAssist:member&event&date [[,,,,]] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "evento", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "Datos ingresados invalidos, "\
               "recuerda que debes ingresar:\n" in out
        assert "**[_Integrante, Evento, Fecha 1, Fecha 2_]**\n" in out
'''