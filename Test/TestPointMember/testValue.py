import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Helpers.helpers import Helpers
from collections import namedtuple

testData = {
    "id" : "1",
    "name" : "TestMember",
    "range" : "General de alianza",
    "event" : "defprismaganada",
    "date" : "25/01/2100"
}

Message = namedtuple('Message', ['author', 'content', 'channel'])
Channel = namedtuple('Channel', ['name'])
Client = namedtuple('Client', ['user'])
name = 'test'
author = "test"
user = "test"
app = AppHandler()

#---------------------Test $listPointMember [Fecha 1, *]----------------------
@pytest.mark.asyncio
async def testPointMemberValue_listPointMember_date1Empty(capfd):
    value = ""
    commands = [f"$listPointMember[{value},"\
                f"{testData['date']}]",
                f"$listPointMember [{value}, "\
                f"{testData['date']} ]",
                f"$listPointMember [ {value} ,"\
                f" {testData['date']} ]",
                f"$listPointMember [ {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listPointMember [ {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember", app.getDatas,
                         Helpers.getStruct("member",
                                           ["assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 1_**\n" in out

@pytest.mark.asyncio
async def testPointMemberValue_listPointMember_date1Invalid(capfd):
    value = "test"
    commands = [f"$listPointMember[{value},"\
                f"{testData['date']}]",
                f"$listPointMember [{value}, "\
                f"{testData['date']} ]",
                f"$listPointMember [ {value} ,"\
                f" {testData['date']} ]",
                f"$listPointMember [ {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listPointMember [ {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember", app.getDatas,
                         Helpers.getStruct("member",
                                           ["assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 1_** "\
                "es invalido.\n" in out

#----------------------Test $listPointMember [*, Fecha 2]----------------------
@pytest.mark.asyncio
async def testPointMemberValue_listPointMember_date2Empty(capfd):
    value = ""
    commands = [f"$listPointMember[{testData['date']},"\
                f"{value}]",
                f"$listPointMember [{testData['date']}, "\
                f"{value} ]",
                f"$listPointMember [ {testData['date']} ,"\
                f" {value} ]",
                f"$listPointMember [ {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listPointMember [ {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember", app.getDatas,
                         Helpers.getStruct("member",
                                           ["assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 2_**\n" in out

@pytest.mark.asyncio
async def testPointMemberValue_listPointMember_date2Invalid(capfd):
    value = "test"
    commands = [f"$listPointMember[{testData['date']},"\
                f"{value}]",
                f"$listPointMember [{testData['date']}, "\
                f"{value} ]",
                f"$listPointMember [ {testData['date']} ,"\
                f" {value} ]",
                f"$listPointMember [ {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listPointMember [ {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember", app.getDatas,
                         Helpers.getStruct("member",
                                           ["assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 2_** "\
                "es invalido.\n" in out

#-------------------Test $listPointMember:id [ID, *, *]----------------------
@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberId_idEmpty(capfd):
    value = ""
    commands = [f"$listPointMember:id[{value},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listPointMember:id [{value}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listPointMember:id [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]",
                f"$listPointMember:id [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]FILL",
                f"$listPointMember:id [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:id", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_ID_**\n" in out

@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberId_idInvalid(capfd):
    value = "test"
    commands = [f"$listPointMember:id[{value},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listPointMember:id [{value}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listPointMember:id [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]",
                f"$listPointMember:id [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]FILL",
                f"$listPointMember:id [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:id", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_ID_** "\
                "es invalido.\n" in out

#------------------Test $listPointMember:id [*, Fecha 1, *]--------------------
@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberId_date1Empty(capfd):
    value = ""
    commands = [f"$listPointMember:id[{testData['id']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$listPointMember:id [{testData['id']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$listPointMember:id [ {testData['id']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]",
                f"$listPointMember:id [ {testData['id']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listPointMember:id [ {testData['id']} ,"\
                f" {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:id", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 1_**\n" in out

@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberId_date1Invalid(capfd):
    value = "test"
    commands = [f"$listPointMember:id[{testData['id']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$listPointMember:id [{testData['id']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$listPointMember:id [ {testData['id']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]",
                f"$listPointMember:id [ {testData['id']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listPointMember:id [ {testData['id']} ,"\
                f" {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:id", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 1_** "\
                "es invalido.\n" in out

#------------------Test $listPointMember:id [*, *, Fecha 2]--------------------
@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberId_date2Empty(capfd):
    value = ""
    commands = [f"$listPointMember:id[{testData['id']},"\
                f"{testData['date']},"\
                f"{value}]",
                f"$listPointMember:id [{testData['id']}, "\
                f"{testData['date']}, "\
                f"{value} ]",
                f"$listPointMember:id [ {testData['id']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]",
                f"$listPointMember:id [ {testData['id']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listPointMember:id [ {testData['id']} ,"\
                f" {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:id", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 2_**\n" in out

@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberId_date2Invalid(capfd):
    value = "test"
    commands = [f"$listPointMember:id[{testData['id']},"\
                f"{testData['date']},"\
                f"{value}]",
                f"$listPointMember:id [{testData['id']}, "\
                f"{testData['date']}, "\
                f"{value} ]",
                f"$listPointMember:id [ {testData['id']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]",
                f"$listPointMember:id [ {testData['id']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listPointMember:id [ {testData['id']} ,"\
                f" {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:id", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 2_** "\
                "es invalido.\n" in out


#-------------------Test $listPointMember:name [Nombre, *, *]------------------
@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberName_nameEmpty(capfd):
    value = ""
    commands = [f"$listPointMember:name[{value},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listPointMember:name [{value}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listPointMember:name [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]",
                f"$listPointMember:name [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]FILL",
                f"$listPointMember:name [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:name", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Nombre_**\n" in out

@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberName_nameLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$listPointMember:name[{value},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listPointMember:name [{value}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listPointMember:name [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]",
                f"$listPointMember:name [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]FILL",
                f"$listPointMember:name [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:name", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Nombre_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberName_nameStartChar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$listPointMember:name[{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listPointMember:name [{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listPointMember:name [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listPointMember:name [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listPointMember:name [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listPointMember:name", app.getDatas,
                             Helpers.getStruct("member",
                                               ["name",
                                                "assist_date_1",
                                                "assist_date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberName_nameSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$listPointMember:name[{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listPointMember:name [{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listPointMember:name [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listPointMember:name [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listPointMember:name [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listPointMember:name", app.getDatas,
                             Helpers.getStruct("member",
                                               ["name",
                                                "assist_date_1",
                                                "assist_date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberName_nameRepeatChar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$listPointMember:name[{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listPointMember:name [{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listPointMember:name [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listPointMember:name [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listPointMember:name [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listPointMember:name", app.getDatas,
                             Helpers.getStruct("member",
                                               ["name",
                                                "assist_date_1",
                                                "assist_date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Nombre_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#----------------Test $listPointMember:name [*, Fecha 1, *]--------------------
@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberName_date1Empty(capfd):
    value = ""
    commands = [f"$listPointMember:name[{testData['name']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$listPointMember:name [{testData['name']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$listPointMember:name [ {testData['name']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]",
                f"$listPointMember:name [ {testData['name']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listPointMember:name [ {testData['name']} ,"\
                f" {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:name", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 1_**\n" in out

@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberName_date1Invalid(capfd):
    value = "test"
    commands = [f"$listPointMember:name[{testData['name']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$listPointMember:name [{testData['name']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$listPointMember:name [ {testData['name']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]",
                f"$listPointMember:name [ {testData['name']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listPointMember:name [ {testData['name']} ,"\
                f" {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:name", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 1_** "\
                "es invalido.\n" in out

#-----------------Test $listPointMember:name [*, *, Fecha 2]-------------------
@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberName_date2Empty(capfd):
    value = ""
    commands = [f"$listPointMember:name[{testData['name']},"\
                f"{testData['date']},"\
                f"{value}]",
                f"$listPointMember:name [{testData['name']}, "\
                f"{testData['date']}, "\
                f"{value} ]",
                f"$listPointMember:name [ {testData['name']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]",
                f"$listPointMember:name [ {testData['name']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listPointMember:name [ {testData['name']} ,"\
                f" {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:name", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 2_**\n" in out

@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberName_date2Invalid(capfd):
    value = "test"
    commands = [f"$listPointMember:name[{testData['name']},"\
                f"{testData['date']},"\
                f"{value}]",
                f"$listPointMember:name [{testData['name']}, "\
                f"{testData['date']}, "\
                f"{value} ]",
                f"$listPointMember:name [ {testData['name']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]",
                f"$listPointMember:name [ {testData['name']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listPointMember:name [ {testData['name']} ,"\
                f" {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:name", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 2_** "\
                "es invalido.\n" in out

#-------------------Test $listPointMember:range [Rango, *, *]------------------
@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberRange_rangeEmpty(capfd):
    value = ""
    commands = [f"$listPointMember:range[{value},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listPointMember:range [{value}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listPointMember:range [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]",
                f"$listPointMember:range [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]FILL",
                f"$listPointMember:range [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:range", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Rango_**\n" in out

@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberRange_rangeLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$listPointMember:range[{value},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listPointMember:range [{value}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listPointMember:range [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]",
                f"$listPointMember:range [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]FILL",
                f"$listPointMember:range [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:range", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Rango_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberRange_rangeStartChar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$listPointMember:range[{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listPointMember:range [{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listPointMember:range [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listPointMember:range [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listPointMember:range [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listPointMember:range", app.getDatas,
                             Helpers.getStruct("member",
                                               ["range",
                                                "assist_date_1",
                                                "assist_date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Rango_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberRange_rangeSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$listPointMember:range[{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listPointMember:range [{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listPointMember:range [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listPointMember:range [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listPointMember:range [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listPointMember:range", app.getDatas,
                             Helpers.getStruct("member",
                                               ["range",
                                                "assist_date_1",
                                                "assist_date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Rango_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberRange_rangeRepeatChar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$listPointMember:range[{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listPointMember:range [{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listPointMember:range [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listPointMember:range [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listPointMember:range [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listPointMember:range", app.getDatas,
                             Helpers.getStruct("member",
                                               ["range",
                                                "assist_date_1",
                                                "assist_date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Rango_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#----------------Test $listPointMember:range [*, Fecha 1, *]-------------------
@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberRange_date1Empty(capfd):
    value = ""
    commands = [f"$listPointMember:range[{testData['range']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$listPointMember:range [{testData['range']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$listPointMember:range [ {testData['range']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]",
                f"$listPointMember:range [ {testData['range']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listPointMember:range [ {testData['range']} ,"\
                f" {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:range", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 1_**\n" in out

@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberRange_date1Invalid(capfd):
    value = "test"
    commands = [f"$listPointMember:range[{testData['range']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$listPointMember:range [{testData['range']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$listPointMember:range [ {testData['range']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]",
                f"$listPointMember:range [ {testData['range']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listPointMember:range [ {testData['range']} ,"\
                f" {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:range", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 1_** "\
                "es invalido.\n" in out

#----------------Test $listPointMember:range [*, *, Fecha 2]-------------------
@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberRange_date2Empty(capfd):
    value = ""
    commands = [f"$listPointMember:range[{testData['range']},"\
                f"{testData['date']},"\
                f"{value}]",
                f"$listPointMember:range [{testData['range']}, "\
                f"{testData['date']}, "\
                f"{value} ]",
                f"$listPointMember:range [ {testData['range']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]",
                f"$listPointMember:range [ {testData['range']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listPointMember:range [ {testData['range']} ,"\
                f" {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:range", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 2_**\n" in out

@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberRange_date2Invalid(capfd):
    value = "test"
    commands = [f"$listPointMember:range[{testData['range']},"\
                f"{testData['date']},"\
                f"{value}]",
                f"$listPointMember:range [{testData['range']}, "\
                f"{testData['date']}, "\
                f"{value} ]",
                f"$listPointMember:range [ {testData['range']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]",
                f"$listPointMember:range [ {testData['range']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listPointMember:range [ {testData['range']} ,"\
                f" {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:range", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 2_** "\
                "es invalido.\n" in out

#-------------------Test $listPointMember:event [Evento, *, *]-----------------
@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberEvent_eventEmpty(capfd):
    value = ""
    commands = [f"$listPointMember:event[{value},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listPointMember:event [{value}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listPointMember:event [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]",
                f"$listPointMember:event [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]FILL",
                f"$listPointMember:event [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["event",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Evento_**\n" in out

@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberEvent_eventLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$listPointMember:event[{value},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listPointMember:event [{value}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listPointMember:event [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]",
                f"$listPointMember:event [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]FILL",
                f"$listPointMember:event [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["event",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Evento_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberEvent_eventStartChar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$listPointMember:event[{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listPointMember:event [{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listPointMember:event [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listPointMember:event [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listPointMember:event [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listPointMember:event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["event",
                                                "assist_date_1",
                                                "assist_date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberEvent_eventSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$listPointMember:event[{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listPointMember:event [{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listPointMember:event [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listPointMember:event [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listPointMember:event [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listPointMember:event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["event",
                                                "assist_date_1",
                                                "assist_date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberEvent_eventRepeatChar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$listPointMember:event[{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listPointMember:event [{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listPointMember:event [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listPointMember:event [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listPointMember:event [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listPointMember:event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["event",
                                                "assist_date_1",
                                                "assist_date_2"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Evento_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#----------------Test $listPointMember:event [*, Fecha 1, *]-------------------
@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberEvent_date1Empty(capfd):
    value = ""
    commands = [f"$listPointMember:event[{testData['event']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$listPointMember:event [{testData['event']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$listPointMember:event [ {testData['event']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]",
                f"$listPointMember:event [ {testData['event']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listPointMember:event [ {testData['event']} ,"\
                f" {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["event",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 1_**\n" in out

@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberEvent_date1Invalid(capfd):
    value = "test"
    commands = [f"$listPointMember:event[{testData['event']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$listPointMember:event [{testData['event']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$listPointMember:event [ {testData['event']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]",
                f"$listPointMember:event [ {testData['event']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listPointMember:event [ {testData['event']} ,"\
                f" {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["event",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 1_** "\
                "es invalido.\n" in out

#----------------Test $listPointMember:event [*, *, Fecha 2]-------------------
@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberEvent_date2Empty(capfd):
    value = ""
    commands = [f"$listPointMember:event[{testData['event']},"\
                f"{testData['date']},"\
                f"{value}]",
                f"$listPointMember:event [{testData['event']}, "\
                f"{testData['date']}, "\
                f"{value} ]",
                f"$listPointMember:event [ {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]",
                f"$listPointMember:event [ {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listPointMember:event [ {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["event",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 2_**\n" in out

@pytest.mark.asyncio
async def testPointMemberValue_listPointMemberEvent_date2Invalid(capfd):
    value = "test"
    commands = [f"$listPointMember:event[{testData['event']},"\
                f"{testData['date']},"\
                f"{value}]",
                f"$listPointMember:event [{testData['event']}, "\
                f"{testData['date']}, "\
                f"{value} ]",
                f"$listPointMember:event [ {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]",
                f"$listPointMember:event [ {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listPointMember:event [ {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["event",
                                            "assist_date_1",
                                            "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 2_** "\
                "es invalido.\n" in out
'''
#-----------------------------$listMember:id [ID]------------------------------
@pytest.mark.asyncio
async def testMemberValue_listMemberId_idEmpty(capfd):
    value = ""
    commands = [f"$listMember:id[{value}],",
                f"$listMember:id [{value} ], ",
                f"$listMember:id [ {value} ], ",
                f"$listMember:id [ {value} ]FILL",
                f"$listMember:id [ {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:id", app.getDatas,
                         Helpers.getStruct("member", ["id"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_ID_**\n" in out

@pytest.mark.asyncio
async def testMemberValue_listMemberId_idInvalid(capfd):
    value = "test"
    commands = [f"$listMember:id[{value}],",
                f"$listMember:id [{value} ], ",
                f"$listMember:id [ {value} ], ",
                f"$listMember:id [ {value} ]FILL",
                f"$listMember:id [ {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:id", app.getDatas,
                         Helpers.getStruct("member", ["id"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_ID_** "\
                "es invalido.\n" in out

#-----------------------Test $listMember:name [Nombre]-------------------------
@pytest.mark.asyncio
async def testMemberValue_listMemberName_nameEmpty(capfd):
    value = ""
    commands = [f"$listMember:name[{value}]",
                f"$listMember:name [{value} ]",
                f"$listMember:name [ {value} ]",
                f"$listMember:name [ {value} ]FILL",
                f"$listMember:name [ {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:name", app.getDatas,
                         Helpers.getStruct("member", ["name"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Nombre_**\n" in out

@pytest.mark.asyncio
async def testMemberValue_listMemberName_nameLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$listMember:name[{value}]",
                f"$listMember:name [{value} ]",
                f"$listMember:name [ {value} ]",
                f"$listMember:name [ {value} ]FILL",
                f"$listMember:name [ {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:name", app.getDatas,
                         Helpers.getStruct("member", ["name"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Nombre_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testMemberValue_listMemberName_nameStartChar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$listMember:name[{value}]",
                    f"$listMember:name [{value} ]",
                    f"$listMember:name [ {value} ]",
                    f"$listMember:name [ {value} ]FILL",
                    f"$listMember:name [ {value} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember:name", app.getDatas,
                             Helpers.getStruct("member", ["name"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testMemberValue_listMemberName_nameSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$listMember:name[{value}]",
                    f"$listMember:name [{value} ]",
                    f"$listMember:name [ {value} ]",
                    f"$listMember:name [ {value} ]FILL",
                    f"$listMember:name [ {value} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember:name", app.getDatas,
                             Helpers.getStruct("member", ["name"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testMemberValue_listMemberName_nameRepeatChar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$listMember:name[{value}]",
                    f"$listMember:name [{value} ]",
                    f"$listMember:name [ {value} ]",
                    f"$listMember:name [ {value} ]FILL",
                    f"$listMember:name [ {value} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember:name", app.getDatas,
                             Helpers.getStruct("member", ["name"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Nombre_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#---------------------Test $listMember:range [Rango]---------------------
@pytest.mark.asyncio
async def testMemberValue_listMemberRange_rangeEmpty(capfd):
    value = ""
    commands = [f"$listMember:range[{value}]",
                f"$listMember:range [{value} ]",
                f"$listMember:range [ {value} ]",
                f"$listMember:range [ {value} ]FILL",
                f"$listMember:range [ {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:range", app.getDatas,
                         Helpers.getStruct("member", ["range"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Rango_**\n" in out

@pytest.mark.asyncio
async def testMemberValue_listMemberRange_rangeLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$listMember:range[{value}]",
                f"$listMember:range [{value} ]",
                f"$listMember:range [ {value} ]",
                f"$listMember:range [ {value} ]FILL",
                f"$listMember:range [ {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:range", app.getDatas,
                         Helpers.getStruct("member", ["range"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Rango_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testMemberValue_listMemberRange_rangeStartChar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$listMember:range[{value}]",
                    f"$listMember:range [{value} ]",
                    f"$listMember:range [ {value} ]",
                    f"$listMember:range [ {value} ]FILL",
                    f"$listMember:range [ {value} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember:range", app.getDatas,
                             Helpers.getStruct("member", ["range"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Rango_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testMemberValue_listMemberRange_rangeSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$listMember:range[{value}]",
                    f"$listMember:range [{value} ]",
                    f"$listMember:range [ {value} ]",
                    f"$listMember:range [ {value} ]FILL",
                    f"$listMember:range [ {value} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember:range", app.getDatas,
                             Helpers.getStruct("member", ["range"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Rango_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testMemberValue_listMemberRange_rangeRepeatChar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$listMember:range[{value}]",
                    f"$listMember:range [{value} ]",
                    f"$listMember:range [ {value} ]",
                    f"$listMember:range [ {value} ]FILL",
                    f"$listMember:range [ {value} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember:range", app.getDatas,
                             Helpers.getStruct("member", ["range"]))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Rango_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#----------------------Test $listMember:date [Fecha 1, *]----------------------
@pytest.mark.asyncio
async def testMemberValue_listMemberDate_date1Empty(capfd):
    value = ""
    commands = [f"$listMember:date[{value},"\
                f"{testData['date']}]",
                f"$listMember:date [{value}, "\
                f"{testData['date']} ]",
                f"$listMember:date [ {value} ,"\
                f" {testData['date']} ]",
                f"$listMember:date [ {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listMember:date [ {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:date", app.getDatas,
                         Helpers.getStruct("member", ["date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 1_**\n" in out

@pytest.mark.asyncio
async def testMemberValue_listMemberDate_date1Invalid(capfd):
    value = "test"
    commands = [f"$listMember:date[{value},"\
                f"{testData['date']}]",
                f"$listMember:date [{value}, "\
                f"{testData['date']} ]",
                f"$listMember:date [ {value} ,"\
                f" {testData['date']} ]",
                f"$listMember:date [ {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listMember:date [ {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:date", app.getDatas,
                         Helpers.getStruct("member", ["date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 1_** "\
                "es invalido.\n" in out

#----------------------Test $listMember:date [*, Fecha 2]----------------------
@pytest.mark.asyncio
async def testMemberValue_listMemberDate_date2Empty(capfd):
    value = ""
    commands = [f"$listMember:date[{testData['date']},"\
                f"{value}]",
                f"$listMember:date [{testData['date']}, "\
                f"{value} ]",
                f"$listMember:date [ {testData['date']} ,"\
                f" {value} ]",
                f"$listMember:date [ {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listMember:date [ {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:date", app.getDatas,
                         Helpers.getStruct("member", ["date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 2_**\n" in out

@pytest.mark.asyncio
async def testMemberValue_listMemberDate_date2Invalid(capfd):
    value = "test"
    commands = [f"$listMember:date[{testData['date']},"\
                f"{value}]",
                f"$listMember:date [{testData['date']}, "\
                f"{value} ]",
                f"$listMember:date [ {testData['date']} ,"\
                f" {value} ]",
                f"$listMember:date [ {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listMember:date [ {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:date", app.getDatas,
                         Helpers.getStruct("member", ["date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 2_** "\
                "es invalido.\n" in out
'''