import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Certs.certificates import Certificates
from Helpers.helpers import Helpers
from collections import namedtuple

testData = {
    "id" : "1",
    "member" : "Avalonicus",
    "event" : "defprismaganada",
    "date" : "25/01/2300",
}

Message = namedtuple('Message', ['author', 'content', 'channel'])
Channel = namedtuple('Channel', ['name'])
Client = namedtuple('Client', ['user'])
name = 'test'
author = "test"
user = "test"
app = AppHandler()
permissions = Certificates()

#----------------------Test $addAssist [Integrante, *, *]----------------------
@pytest.mark.asyncio
async def testAssistValue_addAssist_memberEmpty(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addAssist", app.setData,
                           Helpers.setStruct("assist"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Integrante_**\n" in out

@pytest.mark.asyncio
async def testAssistValue_addAssist_memberLong(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addAssist", app.setData,
                           Helpers.setStruct("assist"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Integrante_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testAssistValue_addAssist_memberStartChar(capfd):
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addAssist", app.setData,
                               Helpers.setStruct("assist"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Integrante_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testAssistValue_addAssist_memberSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addAssist", app.setData,
                               Helpers.setStruct("assist"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Integrante_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testAssistValue_addAssist_memberRepeatChar(capfd):
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addAssist", app.setData,
                               Helpers.setStruct("assist"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Integrante_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#-----------------------Test $addAssist [*, Evento, *]-------------------------
@pytest.mark.asyncio
async def testAssistValue_addAssist_eventEmpty(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addAssist", app.setData,
                           Helpers.setStruct("assist"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Evento_**\n" in out

@pytest.mark.asyncio
async def testAssistValue_addAssist_eventLong(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addAssist", app.setData,
                           Helpers.setStruct("assist"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Evento_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testAssistValue_addAssist_eventStartChar(capfd):
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addAssist", app.setData,
                               Helpers.setStruct("assist"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testAssistValue_addAssist_eventSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addAssist", app.setData,
                               Helpers.setStruct("assist"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testAssistValue_addAssist_eventRepeatChar(capfd):
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("addAssist", app.setData,
                               Helpers.setStruct("assist"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Evento_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#-------------------------Test $addAssist [*, *, Fecha]------------------------
@pytest.mark.asyncio
async def testAssistValue_addAssist_dateEmpty(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addAssist", app.setData,
                           Helpers.setStruct("assist"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha_**\n" in out

@pytest.mark.asyncio
async def testAssistValue_addAssist_dateInvalid(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addAssist", app.setData,
                           Helpers.setStruct("assist"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha_** "\
                "es invalido.\n" in out

#------------------------Test $updAssist:id [ID, *, *, *]----------------------
@pytest.mark.asyncio
async def testAssistValue_updAssistId_idEmpty(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updAssist:id", app.updateData,
                           Helpers.updStruct("assist", "id"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_ID_**\n" in out

@pytest.mark.asyncio
async def testAssistValue_updAssistId_idInvalid(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updAssist:id", app.updateData,
                           Helpers.updStruct("assist", "id"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_ID_** "\
                "es invalido.\n" in out

#--------------------Test $updAssist:id [*, Integrante, *, *]------------------
@pytest.mark.asyncio
async def testAssistValue_updAssistId_memberEmpty(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updAssist:id", app.updateData,
                           Helpers.updStruct("assist", "id"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Integrante_**\n" in out

@pytest.mark.asyncio
async def testAssistValue_updAssistId_memberLong(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updAssist:id", app.updateData,
                           Helpers.updStruct("assist", "id"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Integrante_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testAssistValue_updAssistId_memberStartChar(capfd):
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updAssist:id", app.updateData,
                               Helpers.updStruct("assist", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Integrante_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testAssistValue_updAssistId_memberSpeChar(capfd):
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updAssist:id", app.updateData,
                               Helpers.updStruct("assist", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Integrante_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testAssistValue_updAssistId_memberRepeatChar(capfd):
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updAssist:id", app.updateData,
                               Helpers.updStruct("assist", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Integrante_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#----------------------Test $updAssist:id [*, *, Evento, *]--------------------
@pytest.mark.asyncio
async def testAssistValue_updAssistId_eventEmpty(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updAssist:id", app.updateData,
                           Helpers.updStruct("assist", "id"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Evento_**\n" in out

@pytest.mark.asyncio
async def testAssistValue_updAssistId_eventLong(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updAssist:id", app.updateData,
                           Helpers.updStruct("assist", "id"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Evento_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testAssistValue_updAssistId_eventStartChar(capfd):
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updAssist:id", app.updateData,
                               Helpers.updStruct("assist", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testAssistValue_updAssistId_eventSpeChar(capfd):
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updAssist:id", app.updateData,
                               Helpers.updStruct("assist", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testAssistValue_updAssistId_eventRepeatChar(capfd):
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.contMsg("updAssist:id", app.updateData,
                               Helpers.updStruct("assist", "id"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Evento_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#----------------------Test $updAssist:id [*, *, *, Fecha]--------------------
@pytest.mark.asyncio
async def testAssistValue_updAssistId_dateEmpty(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updAssist:id", app.updateData,
                           Helpers.updStruct("assist", "id"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha_**\n" in out

@pytest.mark.asyncio
async def testAssistValue_updAssistId_dateInvalid(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updAssist:id", app.updateData,
                           Helpers.updStruct("assist", "id"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha_** "\
                "es invalido.\n" in out
#------------------------------$delAssist:id [ID]------------------------------
@pytest.mark.asyncio
async def testAssistValue_delAssistId_idEmpty(capfd):
    value = ""
    commands = [f"$delAssist:id[{value}],",
                f"$delAssist:id [{value} ], ",
                f"$delAssist:id [ {value} ], ",
                f"$delAssist:id [ {value} ]FILL",
                f"$delAssist:id [ {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delAssist:id", app.deleteData,
                           Helpers.delStruct("assist", "id"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_ID_**\n" in out

@pytest.mark.asyncio
async def testAssistValue_delAssistId_idInvalid(capfd):
    value = "test"
    commands = [f"$delAssist:id[{value}],",
                f"$delAssist:id [{value} ], ",
                f"$delAssist:id [ {value} ], ",
                f"$delAssist:id [ {value} ]FILL",
                f"$delAssist:id [ {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delAssist:id", app.deleteData,
                           Helpers.delStruct("assist", "id"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_ID_** "\
                "es invalido.\n" in out

#------------------------------$listAssist:id [ID]-----------------------------
@pytest.mark.asyncio
async def testAssistValue_listAssistId_idEmpty(capfd):
    value = ""
    commands = [f"$listAssist:id[{value}],",
                f"$listAssist:id [{value} ], ",
                f"$listAssist:id [ {value} ], ",
                f"$listAssist:id [ {value} ]FILL",
                f"$listAssist:id [ {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:id", app.getDatas,
                         Helpers.getStruct("assist", ["id"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_ID_**\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistId_idInvalid(capfd):
    value = "test"
    commands = [f"$listAssist:id[{value}],",
                f"$listAssist:id [{value} ], ",
                f"$listAssist:id [ {value} ], ",
                f"$listAssist:id [ {value} ]FILL",
                f"$listAssist:id [ {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:id", app.getDatas,
                         Helpers.getStruct("assist", ["id"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_ID_** "\
                "es invalido.\n" in out

#---------------------Test $listAssist:member [Integrante]---------------------
@pytest.mark.asyncio
async def testAssistValue_listAssistMember_memberEmpty(capfd):
    value = ""
    commands = [f"$listAssist:member[{value}]",
                f"$listAssist:member [{value} ]",
                f"$listAssist:member [ {value} ]",
                f"$listAssist:member [ {value} ]FILL",
                f"$listAssist:member [ {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member", app.getDatas,
                         Helpers.getStruct("assist", ["member"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Integrante_**\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistMember_memberLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$listAssist:member[{value}]",
                f"$listAssist:member [{value} ]",
                f"$listAssist:member [ {value} ]",
                f"$listAssist:member [ {value} ]FILL",
                f"$listAssist:member [ {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member", app.getDatas,
                         Helpers.getStruct("assist", ["member"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Integrante_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistMember_memberStartChar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$listAssist:member[{value}]",
                    f"$listAssist:member [{value} ]",
                    f"$listAssist:member [ {value} ]",
                    f"$listAssist:member [ {value} ]FILL",
                    f"$listAssist:member [ {value} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member", app.getDatas,
                             Helpers.getStruct("assist", ["member"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Integrante_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistMember_memberSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$listAssist:member[{value}]",
                    f"$listAssist:member [{value} ]",
                    f"$listAssist:member [ {value} ]",
                    f"$listAssist:member [ {value} ]FILL",
                    f"$listAssist:member [ {value} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member", app.getDatas,
                             Helpers.getStruct("assist", ["member"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Integrante_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistMember_memberRepeatChar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$listAssist:member[{value}]",
                    f"$listAssist:member [{value} ]",
                    f"$listAssist:member [ {value} ]",
                    f"$listAssist:member [ {value} ]FILL",
                    f"$listAssist:member [ {value} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member", app.getDatas,
                             Helpers.getStruct("assist", ["member"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Integrante_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#------------------------Test $listAssist:event [Evento]-----------------------
@pytest.mark.asyncio
async def testAssistValue_listAssistEvent_eventEmpty(capfd):
    value = ""
    commands = [f"$listAssist:event[{value}]",
                f"$listAssist:event [{value} ]",
                f"$listAssist:event [ {value} ]",
                f"$listAssist:event [ {value} ]FILL",
                f"$listAssist:event [ {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:event", app.getDatas,
                         Helpers.getStruct("assist", ["event"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Evento_**\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistEvent_eventLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$listAssist:event[{value}]",
                f"$listAssist:event [{value} ]",
                f"$listAssist:event [ {value} ]",
                f"$listAssist:event [ {value} ]FILL",
                f"$listAssist:event [ {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:event", app.getDatas,
                         Helpers.getStruct("assist", ["event"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Evento_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistEvent_eventStartChar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$listAssist:event[{value}]",
                    f"$listAssist:event [{value} ]",
                    f"$listAssist:event [ {value} ]",
                    f"$listAssist:event [ {value} ]FILL",
                    f"$listAssist:event [ {value} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:event", app.getDatas,
                             Helpers.getStruct("assist", ["event"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistEvent_eventSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$listAssist:event[{value}]",
                    f"$listAssist:event [{value} ]",
                    f"$listAssist:event [ {value} ]",
                    f"$listAssist:event [ {value} ]FILL",
                    f"$listAssist:event [ {value} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:event", app.getDatas,
                             Helpers.getStruct("assist", ["event"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistEvent_eventRepeatChar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$listAssist:event[{value}]",
                    f"$listAssist:event [{value} ]",
                    f"$listAssist:event [ {value} ]",
                    f"$listAssist:event [ {value} ]FILL",
                    f"$listAssist:event [ {value} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:event", app.getDatas,
                             Helpers.getStruct("assist", ["event"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Evento_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#----------------------Test $listAssist:date [Fecha 1, *]----------------------
@pytest.mark.asyncio
async def testAssistValue_listAssistDate_date1Empty(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:date", app.getDatas,
                         Helpers.getStruct("assist",
                         ["date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 1_**\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistDate_date1Invalid(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:date", app.getDatas,
                         Helpers.getStruct("assist",
                         ["date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 1_** "\
                "es invalido.\n" in out

#----------------------Test $listAssist:date [*, Fecha 2]----------------------
@pytest.mark.asyncio
async def testAssistValue_listAssistDate_date2Empty(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:date", app.getDatas,
                         Helpers.getStruct("assist",
                         ["date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 2_**\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistDate_date2Invalid(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:date", app.getDatas,
                         Helpers.getStruct("assist",
                         ["date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 2_** "\
                "es invalido.\n" in out

#-------------------Test $listAssist:member&event [Integrante, *]--------------
@pytest.mark.asyncio
async def testAssistValue_listAssistMemberEvent_memberEmpty(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event", app.getDatas,
                         Helpers.getStruct("assist",
                         ["member", "event"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Integrante_**\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistMemberEvent_memberLong(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event", app.getDatas,
                         Helpers.getStruct("assist",
                         ["member", "event"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Integrante_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistMemberEvent_memberStartChar(capfd):
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&event", app.getDatas,
                             Helpers.getStruct("assist",
                             ["member", "event"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Integrante_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistMemberEvent_memberSpeChar(capfd):
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&event", app.getDatas,
                             Helpers.getStruct("assist",
                             ["member", "event"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Integrante_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistMemberEvent_memberRepeatChar(capfd):
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&event", app.getDatas,
                             Helpers.getStruct("assist",
                             ["member", "event"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Integrante_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#--------------------Test $listAssist:member&event [*, Evento]-----------------
@pytest.mark.asyncio
async def testAssistValue_listAssistMemberEvent_eventEmpty(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event", app.getDatas,
                         Helpers.getStruct("assist",
                         ["member", "event"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Evento_**\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistMemberEvent_eventLong(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event", app.getDatas,
                         Helpers.getStruct("assist",
                         ["member", "event"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Evento_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistMemberEvent_eventStartChar(capfd):
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&event", app.getDatas,
                             Helpers.getStruct("assist",
                             ["member", "event"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistMemberEvent_eventSpeChar(capfd):
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&event", app.getDatas,
                             Helpers.getStruct("assist",
                             ["member", "event"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistMemberEvent_eventRepeatChar(capfd):
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&event", app.getDatas,
                             Helpers.getStruct("assist",
                             ["member", "event"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Evento_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#-----------------Test $listAssist:member&date [Integrante, *, *]--------------
@pytest.mark.asyncio
async def testAssistValue_listAssistMemberDate_memberEmpty(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                         Helpers.getStruct("assist",
                         ["member", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Integrante_**\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistMemberDate_memberLong(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                         Helpers.getStruct("assist",
                         ["member", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Integrante_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistMemberDate_memberStartChar(capfd):
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                             Helpers.getStruct("assist",
                             ["member", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Integrante_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistMemberDate_memberSpeChar(capfd):
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                             Helpers.getStruct("assist",
                             ["member", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Integrante_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistMemberDate_memberRepeatChar(capfd):
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                             Helpers.getStruct("assist",
                             ["member", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Integrante_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#-------------------Test $listAssist:member&date [*, Fecha 1, *]---------------
@pytest.mark.asyncio
async def testAssistValue_listAssistMemberDate_date1Empty(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                         Helpers.getStruct("assist",
                         ["member", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 1_**\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistMemberDate_date1Invalid(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                         Helpers.getStruct("assist",
                         ["member", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 1_** "\
                "es invalido.\n" in out

#------------------Test $listAssist:member&date [*, *, Fecha 2]----------------
@pytest.mark.asyncio
async def testAssistValue_listAssistMemberDate_date2Empty(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                         Helpers.getStruct("assist",
                         ["member", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 2_**\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistMemberDate_date2Invalid(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                         Helpers.getStruct("assist",
                         ["member", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 2_** "\
                "es invalido.\n" in out

#-----------------Test $listAssist:event&date [Evento, *, *]--------------
@pytest.mark.asyncio
async def testAssistValue_listAssistEventDate_eventEmpty(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                         Helpers.getStruct("assist",
                         ["event", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Evento_**\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistEventDate_eventLong(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                         Helpers.getStruct("assist",
                         ["event", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Evento_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistEventDate_eventStartChar(capfd):
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                             Helpers.getStruct("assist",
                             ["event", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistEventDate_eventSpeChar(capfd):
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                             Helpers.getStruct("assist",
                             ["event", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistEventDate_eventRepeatChar(capfd):
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                             Helpers.getStruct("assist",
                             ["event", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Evento_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#-------------------Test $listAssist:event&date [*, Fecha 1, *]---------------
@pytest.mark.asyncio
async def testAssistValue_listAssistEventDate_date1Empty(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                         Helpers.getStruct("assist",
                         ["event", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 1_**\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistEventDate_date1Invalid(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                         Helpers.getStruct("assist",
                         ["event", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 1_** "\
                "es invalido.\n" in out

#------------------Test $listAssist:event&date [*, *, Fecha 2]----------------
@pytest.mark.asyncio
async def testAssistValue_listAssistEventDate_date2Empty(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                         Helpers.getStruct("assist",
                         ["event", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 2_**\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistEventDate_date2Invalid(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                         Helpers.getStruct("assist",
                         ["event", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 2_** "\
                "es invalido.\n" in out

#------------Test $listAssist:member&event&date [Integrante, *, *, *]----------
@pytest.mark.asyncio
async def testAssistValue_listAssistMemberEventDate_memberEmpty(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                         Helpers.getStruct("assist",
                         ["member", "event", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Integrante_**\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistMemberEventDate_memberLong(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                         Helpers.getStruct("assist",
                         ["member", "event", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Integrante_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistMemberEventDate_memberStartChar(capfd):
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                             Helpers.getStruct("assist",
                             ["member", "event", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Integrante_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistMemberEventDate_memberSpeChar(capfd):
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                             Helpers.getStruct("assist",
                             ["member", "event", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Integrante_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistMemberEventDate_memberRepeatChar(capfd):
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                             Helpers.getStruct("assist",
                             ["member", "event", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Integrante_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#------------Test $listAssist:member&event&date [*, Evento, *, *]----------
@pytest.mark.asyncio
async def testAssistValue_listAssistMemberEventDate_eventEmpty(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                         Helpers.getStruct("assist",
                         ["member", "event", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Evento_**\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistMemberEventDate_eventLong(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                         Helpers.getStruct("assist",
                         ["member", "event", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Evento_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistMemberEventDate_eventStartChar(capfd):
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                             Helpers.getStruct("assist",
                             ["member", "event", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistMemberEventDate_eventSpeChar(capfd):
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                             Helpers.getStruct("assist",
                             ["member", "event", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistMemberEventDate_eventRepeatChar(capfd):
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
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                             Helpers.getStruct("assist",
                             ["member", "event", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Evento_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#--------------Test $listAssist:member&event&date [*, Fecha 1, *, *]-----------
@pytest.mark.asyncio
async def testAssistValue_listAssistMemberEventDate_date1Empty(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                         Helpers.getStruct("assist",
                         ["member", "event", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 1_**\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistMemberEventDate_date1Invalid(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                         Helpers.getStruct("assist",
                         ["member", "event", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 1_** "\
                "es invalido.\n" in out

#-------------Test $listAssist:member&event&date [*, *, *, Fecha 2]------------
@pytest.mark.asyncio
async def testAssistValue_listAssistMemberEventDate_date2Empty(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                         Helpers.getStruct("assist",
                         ["member", "event", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 2_**\n" in out

@pytest.mark.asyncio
async def testAssistValue_listAssistMemberEventDate_date2Invalid(capfd):
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
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                         Helpers.getStruct("assist",
                         ["member", "event", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 2_** "\
                "es invalido.\n" in out