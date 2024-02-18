import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Certs.certificates import Certificates
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
permissions = Certificates()

#---------------------Test $listAllPointMember [Fecha 1, *]--------------------
@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMember_date1Empty(capfd):
    value = ""
    commands = [f"$listAllPointMember[{value},"\
                f"{testData['date']}]",
                f"$listAllPointMember [{value}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember [ {value} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember [ {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember [ {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember", app.getDatas,
                         Helpers.getStruct("member",
                                           ["date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 1_**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMember_date1Invalid(capfd):
    value = "test"
    commands = [f"$listAllPointMember[{value},"\
                f"{testData['date']}]",
                f"$listAllPointMember [{value}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember [ {value} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember [ {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember [ {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember", app.getDatas,
                         Helpers.getStruct("member",
                                           ["date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 1_** "\
                "es invalido.\n" in out

#----------------------Test $listAllPointMember [*, Fecha 2]-------------------
@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMember_date2Empty(capfd):
    value = ""
    commands = [f"$listAllPointMember[{testData['date']},"\
                f"{value}]",
                f"$listAllPointMember [{testData['date']}, "\
                f"{value} ]",
                f"$listAllPointMember [ {testData['date']} ,"\
                f" {value} ]",
                f"$listAllPointMember [ {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listAllPointMember [ {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember", app.getDatas,
                         Helpers.getStruct("member",
                                           ["date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 2_**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMember_date2Invalid(capfd):
    value = "test"
    commands = [f"$listAllPointMember[{testData['date']},"\
                f"{value}]",
                f"$listAllPointMember [{testData['date']}, "\
                f"{value} ]",
                f"$listAllPointMember [ {testData['date']} ,"\
                f" {value} ]",
                f"$listAllPointMember [ {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listAllPointMember [ {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember", app.getDatas,
                         Helpers.getStruct("member",
                                           ["date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 2_** "\
                "es invalido.\n" in out

#-------------------Test $listAllPointMember:id [ID, *, *]---------------------
@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberId_idEmpty(capfd):
    value = ""
    commands = [f"$listAllPointMember:id[{value},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listAllPointMember:id [{value}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:id [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:id [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:id [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:id", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_ID_**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberId_idInvalid(capfd):
    value = "test"
    commands = [f"$listAllPointMember:id[{value},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listAllPointMember:id [{value}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:id [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:id [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:id [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:id", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_ID_** "\
                "es invalido.\n" in out

#-----------------Test $listAllPointMember:id [*, Fecha 1, *]------------------
@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberId_date1Empty(capfd):
    value = ""
    commands = [f"$listAllPointMember:id[{testData['id']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$listAllPointMember:id [{testData['id']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:id [ {testData['id']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:id [ {testData['id']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:id [ {testData['id']} ,"\
                f" {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:id", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 1_**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberId_date1Invalid(capfd):
    value = "test"
    commands = [f"$listAllPointMember:id[{testData['id']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$listAllPointMember:id [{testData['id']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:id [ {testData['id']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:id [ {testData['id']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:id [ {testData['id']} ,"\
                f" {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:id", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 1_** "\
                "es invalido.\n" in out

#------------------Test $listAllPointMember:id [*, *, Fecha 2]-----------------
@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberId_date2Empty(capfd):
    value = ""
    commands = [f"$listAllPointMember:id[{testData['id']},"\
                f"{testData['date']},"\
                f"{value}]",
                f"$listAllPointMember:id [{testData['id']}, "\
                f"{testData['date']}, "\
                f"{value} ]",
                f"$listAllPointMember:id [ {testData['id']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]",
                f"$listAllPointMember:id [ {testData['id']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listAllPointMember:id [ {testData['id']} ,"\
                f" {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:id", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 2_**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberId_date2Invalid(capfd):
    value = "test"
    commands = [f"$listAllPointMember:id[{testData['id']},"\
                f"{testData['date']},"\
                f"{value}]",
                f"$listAllPointMember:id [{testData['id']}, "\
                f"{testData['date']}, "\
                f"{value} ]",
                f"$listAllPointMember:id [ {testData['id']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]",
                f"$listAllPointMember:id [ {testData['id']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listAllPointMember:id [ {testData['id']} ,"\
                f" {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:id", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 2_** "\
                "es invalido.\n" in out

#-------------------Test $listAllPointMember:name [Nombre, *, *]---------------
@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberName_nameEmpty(capfd):
    value = ""
    commands = [f"$listAllPointMember:name[{value},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listAllPointMember:name [{value}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:name [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:name [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:name [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:name", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Nombre_**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberName_nameLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$listAllPointMember:name[{value},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listAllPointMember:name [{value}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:name [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:name [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:name [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:name", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Nombre_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberName_nameStartChar(capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$listAllPointMember:name[{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAllPointMember:name [{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAllPointMember:name [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listAllPointMember:name [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listAllPointMember:name [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listAllPointMember:name", app.getDatas,
                             Helpers.getStruct("member",
                                               ["name",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberName_nameSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$listAllPointMember:name[{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAllPointMember:name [{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAllPointMember:name [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listAllPointMember:name [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listAllPointMember:name [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listAllPointMember:name", app.getDatas,
                             Helpers.getStruct("member",
                                               ["name",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberName_nameRepeatChar(capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$listAllPointMember:name[{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAllPointMember:name [{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAllPointMember:name [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listAllPointMember:name [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listAllPointMember:name [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listAllPointMember:name", app.getDatas,
                             Helpers.getStruct("member",
                                               ["name",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Nombre_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#----------------Test $listAllPointMember:name [*, Fecha 1, *]-----------------
@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberName_date1Empty(capfd):
    value = ""
    commands = [f"$listAllPointMember:name[{testData['name']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$listAllPointMember:name [{testData['name']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:name [ {testData['name']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:name [ {testData['name']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:name [ {testData['name']} ,"\
                f" {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:name", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 1_**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberName_date1Invalid(capfd):
    value = "test"
    commands = [f"$listAllPointMember:name[{testData['name']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$listAllPointMember:name [{testData['name']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:name [ {testData['name']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:name [ {testData['name']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:name [ {testData['name']} ,"\
                f" {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:name", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 1_** "\
                "es invalido.\n" in out

#-----------------Test $listAllPointMember:name [*, *, Fecha 2]----------------
@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberName_date2Empty(capfd):
    value = ""
    commands = [f"$listAllPointMember:name[{testData['name']},"\
                f"{testData['date']},"\
                f"{value}]",
                f"$listAllPointMember:name [{testData['name']}, "\
                f"{testData['date']}, "\
                f"{value} ]",
                f"$listAllPointMember:name [ {testData['name']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]",
                f"$listAllPointMember:name [ {testData['name']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listAllPointMember:name [ {testData['name']} ,"\
                f" {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:name", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 2_**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberName_date2Invalid(capfd):
    value = "test"
    commands = [f"$listAllPointMember:name[{testData['name']},"\
                f"{testData['date']},"\
                f"{value}]",
                f"$listAllPointMember:name [{testData['name']}, "\
                f"{testData['date']}, "\
                f"{value} ]",
                f"$listAllPointMember:name [ {testData['name']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]",
                f"$listAllPointMember:name [ {testData['name']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listAllPointMember:name [ {testData['name']} ,"\
                f" {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:name", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 2_** "\
                "es invalido.\n" in out

#-------------------Test $listAllPointMember:range [Rango, *, *]---------------
@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberRange_rangeEmpty(capfd):
    value = ""
    commands = [f"$listAllPointMember:range[{value},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listAllPointMember:range [{value}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:range [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:range [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:range [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:range", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Rango_**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberRange_rangeLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$listAllPointMember:range[{value},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listAllPointMember:range [{value}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:range [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:range [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:range [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:range", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Rango_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberRange_rangeStartChar(
    capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$listAllPointMember:range[{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAllPointMember:range [{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAllPointMember:range [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listAllPointMember:range [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listAllPointMember:range [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listAllPointMember:range", app.getDatas,
                             Helpers.getStruct("member",
                                               ["range",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Rango_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberRange_rangeSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$listAllPointMember:range[{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAllPointMember:range [{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAllPointMember:range [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listAllPointMember:range [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listAllPointMember:range [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listAllPointMember:range", app.getDatas,
                             Helpers.getStruct("member",
                                               ["range",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Rango_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberRange_rangeRepeatChar(
    capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$listAllPointMember:range[{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAllPointMember:range [{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAllPointMember:range [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listAllPointMember:range [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listAllPointMember:range [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listAllPointMember:range", app.getDatas,
                             Helpers.getStruct("member",
                                               ["range",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Rango_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#----------------Test $listAllPointMember:range [*, Fecha 1, *]----------------
@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberRange_date1Empty(capfd):
    value = ""
    commands = [f"$listAllPointMember:range[{testData['range']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$listAllPointMember:range [{testData['range']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:range [ {testData['range']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:range [ {testData['range']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:range [ {testData['range']} ,"\
                f" {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:range", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 1_**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberRange_date1Invalid(capfd):
    value = "test"
    commands = [f"$listAllPointMember:range[{testData['range']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$listAllPointMember:range [{testData['range']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:range [ {testData['range']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:range [ {testData['range']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:range [ {testData['range']} ,"\
                f" {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:range", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 1_** "\
                "es invalido.\n" in out

#----------------Test $listAllPointMember:range [*, *, Fecha 2]----------------
@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberRange_date2Empty(capfd):
    value = ""
    commands = [f"$listAllPointMember:range[{testData['range']},"\
                f"{testData['date']},"\
                f"{value}]",
                f"$listAllPointMember:range [{testData['range']}, "\
                f"{testData['date']}, "\
                f"{value} ]",
                f"$listAllPointMember:range [ {testData['range']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]",
                f"$listAllPointMember:range [ {testData['range']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listAllPointMember:range [ {testData['range']} ,"\
                f" {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:range", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 2_**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberRange_date2Invalid(capfd):
    value = "test"
    commands = [f"$listAllPointMember:range[{testData['range']},"\
                f"{testData['date']},"\
                f"{value}]",
                f"$listAllPointMember:range [{testData['range']}, "\
                f"{testData['date']}, "\
                f"{value} ]",
                f"$listAllPointMember:range [ {testData['range']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]",
                f"$listAllPointMember:range [ {testData['range']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listAllPointMember:range [ {testData['range']} ,"\
                f" {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:range", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 2_** "\
                "es invalido.\n" in out

#-------------------Test $listAllPointMember:event [Evento, *, *]--------------
@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberEvent_eventEmpty(capfd):
    value = ""
    commands = [f"$listAllPointMember:event[{value},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listAllPointMember:event [{value}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:event [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:event [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:event [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Evento_**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberEvent_eventLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$listAllPointMember:event[{value},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listAllPointMember:event [{value}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:event [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:event [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:event [ {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Evento_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberEvent_eventStartChar(
    capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$listAllPointMember:event[{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAllPointMember:event [{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAllPointMember:event [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listAllPointMember:event [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listAllPointMember:event [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listAllPointMember:event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["event",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberEvent_eventSpeChar(capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$listAllPointMember:event[{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAllPointMember:event [{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAllPointMember:event [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listAllPointMember:event [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listAllPointMember:event [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listAllPointMember:event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["event",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberEvent_eventRepeatChar(
    capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$listAllPointMember:event[{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAllPointMember:event [{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAllPointMember:event [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listAllPointMember:event [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listAllPointMember:event [ {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listAllPointMember:event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["event",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Evento_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#----------------Test $listAllPointMember:event [*, Fecha 1, *]----------------
@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberEvent_date1Empty(capfd):
    value = ""
    commands = [f"$listAllPointMember:event[{testData['event']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$listAllPointMember:event [{testData['event']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:event [ {testData['event']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:event [ {testData['event']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:event [ {testData['event']} ,"\
                f" {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 1_**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberEvent_date1Invalid(capfd):
    value = "test"
    commands = [f"$listAllPointMember:event[{testData['event']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$listAllPointMember:event [{testData['event']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:event [ {testData['event']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:event [ {testData['event']} ,"\
                f" {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:event [ {testData['event']} ,"\
                f" {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 1_** "\
                "es invalido.\n" in out

#----------------Test $listAllPointMember:event [*, *, Fecha 2]----------------
@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberEvent_date2Empty(capfd):
    value = ""
    commands = [f"$listAllPointMember:event[{testData['event']},"\
                f"{testData['date']},"\
                f"{value}]",
                f"$listAllPointMember:event [{testData['event']}, "\
                f"{testData['date']}, "\
                f"{value} ]",
                f"$listAllPointMember:event [ {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]",
                f"$listAllPointMember:event [ {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listAllPointMember:event [ {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 2_**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberEvent_date2Invalid(capfd):
    value = "test"
    commands = [f"$listAllPointMember:event[{testData['event']},"\
                f"{testData['date']},"\
                f"{value}]",
                f"$listAllPointMember:event [{testData['event']}, "\
                f"{testData['date']}, "\
                f"{value} ]",
                f"$listAllPointMember:event [ {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]",
                f"$listAllPointMember:event [ {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listAllPointMember:event [ {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 2_** "\
                "es invalido.\n" in out

#---------------Test $listAllPointMember:id&event [ID, *, *, *]---------------
@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberIdEvent_idEmpty(capfd):
    value = ""
    commands = [f"$listAllPointMember:id&event[{value},"\
                f"{testData['event']},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listAllPointMember:id&event [{value}, "\
                f"{testData['event']}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:id&event [ {value} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:id&event [ {value} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:id&event [ {value} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:id&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_ID_**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberIdEvent_idInvalid(capfd):
    value = "test"
    commands = [f"$listAllPointMember:id&event[{value},"\
                f"{testData['event']},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listAllPointMember:id&event [{value}, "\
                f"{testData['event']}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:id&event [ {value} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:id&event [ {value} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:id&event [ {value} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:id&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_ID_** "\
                "es invalido.\n" in out

#---------------Test $listAllPointMember:id&event [*, Evento, *, *]------------
@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberIdEvent_eventEmpty(capfd):
    value = ""
    commands = [f"$listAllPointMember:id&event[{testData['id']},"\
                f"{value},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listAllPointMember:id&event [{testData['id']}, "\
                f"{value}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:id&event [ {testData['id']} ,"\
                f" {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:id&event [ {testData['id']} ,"\
                f" {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:id&event [ {testData['id']} ,"\
                f" {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:id&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Evento_**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberIdEvent_eventLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$listAllPointMember:id&event[{testData['id']},"\
                f"{value},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listAllPointMember:id&event [{testData['id']}, "\
                f"{value}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:id&event [ {testData['id']} ,"\
                f" {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:id&event [ {testData['id']} ,"\
                f" {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:id&event [ {testData['id']} ,"\
                f" {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:id&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Evento_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberIdEvent_eventStartChar(
    capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$listAllPointMember:id&event[{testData['id']},"\
                    f"{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAllPointMember:id&event [{testData['id']}, "\
                    f"{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAllPointMember:id&event [ {testData['id']} ,"\
                    f" {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listAllPointMember:id&event [ {testData['id']} ,"\
                    f" {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listAllPointMember:id&event [ {testData['id']} ,"\
                    f" {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listAllPointMember:id&event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["id",
                                                "event",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberIdEvent_eventSpeChar(
    capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$listAllPointMember:id&event[{testData['id']},"\
                    f"{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAllPointMember:id&event [{testData['id']}, "\
                    f"{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAllPointMember:id&event [ {testData['id']} ,"\
                    f" {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listAllPointMember:id&event [ {testData['id']} ,"\
                    f" {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listAllPointMember:id&event [ {testData['id']} ,"\
                    f" {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listAllPointMember:id&event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["id",
                                                "event",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberIdEvent_eventRepeatChar(
    capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$listAllPointMember:id&event[{testData['id']},"\
                    f"{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAllPointMember:id&event [{testData['id']}, "\
                    f"{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAllPointMember:id&event [ {testData['id']} ,"\
                    f" {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listAllPointMember:id&event [ {testData['id']} ,"\
                    f" {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listAllPointMember:id&event [ {testData['id']} ,"\
                    f" {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listAllPointMember:id&event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["id",
                                                "event",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Evento_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#--------------Test $listAllPointMember:id&event [*, *, Fecha 1, *]------------
@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberIdEvent_date1Empty(capfd):
    value = ""
    commands = [f"$listAllPointMember:id&event[{testData['id']},"\
                f"{testData['event']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$listAllPointMember:id&event [{testData['id']}, "\
                f"{testData['event']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:id&event [ {testData['id']} ,"\
                f" {testData['event']}, "\
                f" {value} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:id&event [ {testData['id']} ,"\
                f" {testData['event']}, "\
                f" {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:id&event [ {testData['id']} ,"\
                f" {testData['event']}, "\
                f" {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:id&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 1_**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberIdEvent_date1Invalid(
    capfd):
    value = "test"
    commands = [f"$listAllPointMember:id&event[{testData['id']},"\
                f"{testData['event']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$listAllPointMember:id&event [{testData['id']}, "\
                f"{testData['event']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:id&event [ {testData['id']} ,"\
                f" {testData['event']}, "\
                f" {value} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:id&event [ {testData['id']} ,"\
                f" {testData['event']}, "\
                f" {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:id&event [ {testData['id']} ,"\
                f" {testData['event']}, "\
                f" {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:id&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 1_** "\
                "es invalido.\n" in out

#--------------Test $listAllPointMember:id&event [*, *, *, Fecha 2]------------
@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberIdEvent_date2Empty(capfd):
    value = ""
    commands = [f"$listAllPointMember:id&event[{testData['id']},"\
                f"{testData['event']},"\
                f"{testData['date']},"\
                f"{value}]",
                f"$listAllPointMember:id&event [{testData['id']}, "\
                f"{testData['event']}, "\
                f"{testData['date']}, "\
                f"{value} ]",
                f"$listAllPointMember:id&event [ {testData['id']} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]",
                f"$listAllPointMember:id&event [ {testData['id']} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listAllPointMember:id&event [ {testData['id']} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:id&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 2_**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberIdEvent_date2Invalid(
    capfd):
    value = "test"
    commands = [f"$listAllPointMember:id&event[{testData['id']},"\
                f"{testData['event']},"\
                f"{testData['date']},"\
                f"{value}]",
                f"$listAllPointMember:id&event [{testData['id']}, "\
                f"{testData['event']}, "\
                f"{testData['date']}, "\
                f"{value} ]",
                f"$listAllPointMember:id&event [ {testData['id']} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]",
                f"$listAllPointMember:id&event [ {testData['id']} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listAllPointMember:id&event [ {testData['id']} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:id&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 2_** "\
                "es invalido.\n" in out

#--------------Test $listAllPointMember:name&event [Nombre, *, *, *]-----------
@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberNameEvent_nameEmpty(capfd):
    value = ""
    commands = [f"$listAllPointMember:name&event[{value},"\
                f"{testData['event']},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listAllPointMember:name&event [{value}, "\
                f"{testData['event']}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:name&event [ {value} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:name&event [ {value} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:name&event [ {value} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:name&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Nombre_**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberNameEvent_nameLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$listAllPointMember:name&event[{value},"\
                f"{testData['event']},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listAllPointMember:name&event [{value}, "\
                f"{testData['event']}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:name&event [ {value} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:name&event [ {value} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:name&event [ {value} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:name&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Nombre_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberNameEvent_nameStartChar(
    capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$listAllPointMember:name&event[{value},"\
                    f"{testData['event']},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAllPointMember:name&event [{value}, "\
                    f"{testData['event']}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAllPointMember:name&event [ {value} ,"\
                    f" {testData['event']} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listAllPointMember:name&event [ {value} ,"\
                    f" {testData['event']} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listAllPointMember:name&event [ {value} ,"\
                    f" {testData['event']} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listAllPointMember:name&event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["name",
                                                "event",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberNameEvent_nameSpeChar(
    capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$listAllPointMember:name&event[{value},"\
                    f"{testData['event']},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAllPointMember:name&event [{value}, "\
                    f"{testData['event']}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAllPointMember:name&event [ {value} ,"\
                    f" {testData['event']} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listAllPointMember:name&event [ {value} ,"\
                    f" {testData['event']} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listAllPointMember:name&event [ {value} ,"\
                    f" {testData['event']} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listAllPointMember:name&event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["name",
                                                "event",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Nombre_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberNameEvent_nameRepeatChar(
    capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$listAllPointMember:name&event[{value},"\
                    f"{testData['event']},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAllPointMember:name&event [{value}, "\
                    f"{testData['event']}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAllPointMember:name&event [ {value} ,"\
                    f" {testData['event']} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listAllPointMember:name&event [ {value} ,"\
                    f" {testData['event']} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listAllPointMember:name&event [ {value} ,"\
                    f" {testData['event']} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listAllPointMember:name&event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["name",
                                                "event",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Nombre_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#--------------Test $listAllPointMember:name&event [*, Evento, *, *]-----------
@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberNameEvent_eventEmpty(
    capfd):
    value = ""
    commands = [f"$listAllPointMember:name&event[{testData['name']},"\
                f"{value},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listAllPointMember:name&event [{testData['name']}, "\
                f"{value}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:name&event [ {testData['name']} ,"\
                f" {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:name&event [ {testData['name']} ,"\
                f" {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:name&event [ {testData['name']} ,"\
                f" {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:name&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Evento_**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberNameEvent_eventLong(capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$listAllPointMember:name&event[{testData['name']},"\
                f"{value},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listAllPointMember:name&event [{testData['name']}, "\
                f"{value}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:name&event [ {testData['name']} ,"\
                f" {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:name&event [ {testData['name']} ,"\
                f" {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:name&event [ {testData['name']} ,"\
                f" {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:name&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Evento_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberNameEvent_eventStartChar(
    capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$listAllPointMember:name&event[{testData['name']},"\
                    f"{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAllPointMember:name&event [{testData['name']}, "\
                    f"{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAllPointMember:name&event [ {testData['name']} ,"\
                    f" {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listAllPointMember:name&event [ {testData['name']} ,"\
                    f" {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listAllPointMember:name&event [ {testData['name']} ,"\
                    f" {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listAllPointMember:name&event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["name",
                                                "event",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberNameEvent_eventSpeChar(
    capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$listAllPointMember:name&event[{testData['name']},"\
                    f"{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAllPointMember:name&event [{testData['name']}, "\
                    f"{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAllPointMember:name&event [ {testData['name']} ,"\
                    f" {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listAllPointMember:name&event [ {testData['name']} ,"\
                    f" {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listAllPointMember:name&event [ {testData['name']} ,"\
                    f" {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listAllPointMember:name&event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["name",
                                                "event",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberNameEvent_eventRepeatChar(
    capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$listAllPointMember:name&event[{testData['name']},"\
                    f"{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAllPointMember:name&event [{testData['name']}, "\
                    f"{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAllPointMember:name&event [ {testData['name']} ,"\
                    f" {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listAllPointMember:name&event [ {testData['name']} ,"\
                    f" {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listAllPointMember:name&event [ {testData['name']} ,"\
                    f" {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listAllPointMember:name&event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["name",
                                                "event",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Evento_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#--------------Test $listAllPointMember:name&event [*, *, Fecha 1, *]----------
@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberNameEvent_date1Empty(
    capfd):
    value = ""
    commands = [f"$listAllPointMember:name&event[{testData['name']},"\
                f"{testData['event']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$listAllPointMember:name&event [{testData['name']}, "\
                f"{testData['event']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:name&event [ {testData['name']} ,"\
                f" {testData['event']}, "\
                f" {value} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:name&event [ {testData['name']} ,"\
                f" {testData['event']}, "\
                f" {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:name&event [ {testData['name']} ,"\
                f" {testData['event']}, "\
                f" {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:name&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 1_**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberNameEvent_date1Invalid(
    capfd):
    value = "test"
    commands = [f"$listAllPointMember:name&event[{testData['name']},"\
                f"{testData['event']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$listAllPointMember:name&event [{testData['name']}, "\
                f"{testData['event']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:name&event [ {testData['name']} ,"\
                f" {testData['event']}, "\
                f" {value} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:name&event [ {testData['name']} ,"\
                f" {testData['event']}, "\
                f" {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:name&event [ {testData['name']} ,"\
                f" {testData['event']}, "\
                f" {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:name&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 1_** "\
                "es invalido.\n" in out

#--------------Test $listAllPointMember:name&event [*, *, *, Fecha 2]----------
@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberNameEvent_date2Empty(
    capfd):
    value = ""
    commands = [f"$listAllPointMember:name&event[{testData['name']},"\
                f"{testData['event']},"\
                f"{testData['date']},"\
                f"{value}]",
                f"$listAllPointMember:name&event [{testData['name']}, "\
                f"{testData['event']}, "\
                f"{testData['date']}, "\
                f"{value} ]",
                f"$listAllPointMember:name&event [ {testData['name']} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]",
                f"$listAllPointMember:name&event [ {testData['name']} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listAllPointMember:name&event [ {testData['name']} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:name&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 2_**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberNameEvent_date2Invalid(
    capfd):
    value = "test"
    commands = [f"$listAllPointMember:name&event[{testData['name']},"\
                f"{testData['event']},"\
                f"{testData['date']},"\
                f"{value}]",
                f"$listAllPointMember:name&event [{testData['name']}, "\
                f"{testData['event']}, "\
                f"{testData['date']}, "\
                f"{value} ]",
                f"$listAllPointMember:name&event [ {testData['name']} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]",
                f"$listAllPointMember:name&event [ {testData['name']} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listAllPointMember:name&event [ {testData['name']} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:name&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 2_** "\
                "es invalido.\n" in out

#--------------Test $listAllPointMember:range&event [Rango, *, *, *]-----------
@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberRangeEvent_rangeEmpty(
    capfd):
    value = ""
    commands = [f"$listAllPointMember:range&event[{value},"\
                f"{testData['event']},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listAllPointMember:range&event [{value}, "\
                f"{testData['event']}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:range&event [ {value} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:range&event [ {value} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:range&event [ {value} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:range&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Rango_**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberRangeEvent_rangeLong(
    capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$listAllPointMember:range&event[{value},"\
                f"{testData['event']},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listAllPointMember:range&event [{value}, "\
                f"{testData['event']}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:range&event [ {value} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:range&event [ {value} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:range&event [ {value} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:range&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Rango_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberRangeEvent_rangeStartChar(
    capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$listAllPointMember:range&event[{value},"\
                    f"{testData['event']},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAllPointMember:range&event [{value}, "\
                    f"{testData['event']}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAllPointMember:range&event [ {value} ,"\
                    f" {testData['event']} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listAllPointMember:range&event [ {value} ,"\
                    f" {testData['event']} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listAllPointMember:range&event [ {value} ,"\
                    f" {testData['event']} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listAllPointMember:range&event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["range",
                                                "event",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Rango_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberRangeEvent_rangeSpeChar(
    capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$listAllPointMember:range&event[{value},"\
                    f"{testData['event']},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAllPointMember:range&event [{value}, "\
                    f"{testData['event']}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAllPointMember:range&event [ {value} ,"\
                    f" {testData['event']} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listAllPointMember:range&event [ {value} ,"\
                    f" {testData['event']} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listAllPointMember:range&event [ {value} ,"\
                    f" {testData['event']} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listAllPointMember:range&event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["range",
                                                "event",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Rango_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberRangeEvent_rangeRepeatChar(
    capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$listAllPointMember:range&event[{value},"\
                    f"{testData['event']},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAllPointMember:range&event [{value}, "\
                    f"{testData['event']}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAllPointMember:range&event [ {value} ,"\
                    f" {testData['event']} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listAllPointMember:range&event [ {value} ,"\
                    f" {testData['event']} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listAllPointMember:range&event [ {value} ,"\
                    f" {testData['event']} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listAllPointMember:range&event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["range",
                                                "event",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Rango_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#--------------Test $listAllPointMember:range&event [*, Evento, *, *]----------
@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberRangeEvent_eventEmpty(
    capfd):
    value = ""
    commands = [f"$listAllPointMember:range&event[{testData['range']},"\
                f"{value},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listAllPointMember:range&event [{testData['range']}, "\
                f"{value}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:range&event [ {testData['range']} ,"\
                f" {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:range&event [ {testData['range']} ,"\
                f" {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:range&event [ {testData['range']} ,"\
                f" {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:range&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Evento_**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberRangeEvent_eventLong(
    capfd):
    value = "abcdefghijklmnñopkrstuvwxyz"\
            "abcdefghijklmnñopkrstuvwxyz"
    commands = [f"$listAllPointMember:range&event[{testData['range']},"\
                f"{value},"\
                f"{testData['date']},"\
                f"{testData['date']}]",
                f"$listAllPointMember:range&event [{testData['range']}, "\
                f"{value}, "\
                f"{testData['date']}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:range&event [ {testData['range']} ,"\
                f" {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:range&event [ {testData['range']} ,"\
                f" {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:range&event [ {testData['range']} ,"\
                f" {value} ,"\
                f" {testData['date']} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:range&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado "\
                "en el campo "\
               f"**_Evento_** "\
                "no debe exceder los 50 caracteres.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberRangeEvent_eventStartChar(
    capfd):
    values = ["1test", "[test", "{test", "/test", "|test",
             "@test", "*test"]
    for value in values:
        commands = [f"$listAllPointMember:range&event[{testData['range']},"\
                    f"{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAllPointMember:range&event [{testData['range']}, "\
                    f"{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAllPointMember:range&event [ {testData['range']} ,"\
                    f" {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listAllPointMember:range&event [ {testData['range']} ,"\
                    f" {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listAllPointMember:range&event [ {testData['range']} ,"\
                    f" {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listAllPointMember:range&event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["range",
                                                "event",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe comenzar con valores "\
                    "numericos ni caracteres especiales.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberRangeEvent_eventSpeChar(
    capfd):
    values = ["test/", "test{", "te/st", "te\\st",
              "tes@t", "tes*t", "tes--t", "tes||t"]
    for value in values:
        commands = [f"$listAllPointMember:range&event[{testData['range']},"\
                    f"{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAllPointMember:range&event [{testData['range']}, "\
                    f"{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAllPointMember:range&event [ {testData['range']} ,"\
                    f" {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listAllPointMember:range&event [ {testData['range']} ,"\
                    f" {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listAllPointMember:range&event [ {testData['range']} ,"\
                    f" {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listAllPointMember:range&event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["range",
                                                "event",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado en el campo "\
                    "**_Evento_** no debe contener caracteres "\
                    "especiales a excepcion de **-** o **|**.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberRangeEvent_eventRepeatChar(
    capfd):
    values = ["t-e-s-t", "t|e|s|t", "t[e[st", "t]e]st"]
    for value in values:
        commands = [f"$listAllPointMember:range&event[{testData['range']},"\
                    f"{value},"\
                    f"{testData['date']},"\
                    f"{testData['date']}]",
                    f"$listAllPointMember:range&event [{testData['range']}, "\
                    f"{value}, "\
                    f"{testData['date']}, "\
                    f"{testData['date']} ]",
                    f"$listAllPointMember:range&event [ {testData['range']} ,"\
                    f" {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]",
                    f"$listAllPointMember:range&event [ {testData['range']} ,"\
                    f" {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ]FILL",
                    f"$listAllPointMember:range&event [ {testData['range']} ,"\
                    f" {value} ,"\
                    f" {testData['date']} ,"\
                    f" {testData['date']} ] FILL"]
        for command in commands:
            channel = Channel(name=name)
            message = Message(author=author, content=command, channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, permissions, True)
            await hdlr.dFMsg("listAllPointMember:range&event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["range",
                                                "event",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert f"El dato '{value}' ingresado "\
                    "en el campo "\
                   f"**_Evento_** "\
                    "no debe repetir mas de dos veces los "\
                    "caracteres **-** **|**, o mas de una "\
                    "vez los caracteres **[** **]**.\n" in out

#--------------Test $listAllPointMember:range&event [*, *, Fecha 1, *]---------
@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberRangeEvent_date1Empty(
    capfd):
    value = ""
    commands = [f"$listAllPointMember:range&event[{testData['range']},"\
                f"{testData['event']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$listAllPointMember:range&event [{testData['range']}, "\
                f"{testData['event']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:range&event [ {testData['range']} ,"\
                f" {testData['event']}, "\
                f" {value} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:range&event [ {testData['range']} ,"\
                f" {testData['event']}, "\
                f" {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:range&event [ {testData['range']} ,"\
                f" {testData['event']}, "\
                f" {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:range&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 1_**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberRangeEvent_date1Invalid(
    capfd):
    value = "test"
    commands = [f"$listAllPointMember:range&event[{testData['range']},"\
                f"{testData['event']},"\
                f"{value},"\
                f"{testData['date']}]",
                f"$listAllPointMember:range&event [{testData['range']}, "\
                f"{testData['event']}, "\
                f"{value}, "\
                f"{testData['date']} ]",
                f"$listAllPointMember:range&event [ {testData['range']} ,"\
                f" {testData['event']}, "\
                f" {value} ,"\
                f" {testData['date']} ]",
                f"$listAllPointMember:range&event [ {testData['range']} ,"\
                f" {testData['event']}, "\
                f" {value} ,"\
                f" {testData['date']} ]FILL",
                f"$listAllPointMember:range&event [ {testData['range']} ,"\
                f" {testData['event']}, "\
                f" {value} ,"\
                f" {testData['date']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:range&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 1_** "\
                "es invalido.\n" in out

#--------------Test $listAllPointMember:range&event [*, *, *, Fecha 2]---------
@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberRangeEvent_date2Empty(
    capfd):
    value = ""
    commands = [f"$listAllPointMember:range&event[{testData['range']},"\
                f"{testData['event']},"\
                f"{testData['date']},"\
                f"{value}]",
                f"$listAllPointMember:range&event [{testData['range']}, "\
                f"{testData['event']}, "\
                f"{testData['date']}, "\
                f"{value} ]",
                f"$listAllPointMember:range&event [ {testData['range']} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]",
                f"$listAllPointMember:range&event [ {testData['range']} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listAllPointMember:range&event [ {testData['range']} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:range&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "No fue ingresado ningun dato en el campo "\
               "**_Fecha 2_**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberValue_listAllPointMemberRangeEvent_date2Invalid(
    capfd):
    value = "test"
    commands = [f"$listAllPointMember:range&event[{testData['range']},"\
                f"{testData['event']},"\
                f"{testData['date']},"\
                f"{value}]",
                f"$listAllPointMember:range&event [{testData['range']}, "\
                f"{testData['event']}, "\
                f"{testData['date']}, "\
                f"{value} ]",
                f"$listAllPointMember:range&event [ {testData['range']} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]",
                f"$listAllPointMember:range&event [ {testData['range']} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ]FILL",
                f"$listAllPointMember:range&event [ {testData['range']} ,"\
                f" {testData['event']} ,"\
                f" {testData['date']} ,"\
                f" {value} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, permissions, True)
        await hdlr.dFMsg("listAllPointMember:range&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El dato '{value}' ingresado en el campo "\
               f"**_Fecha 2_** "\
                "es invalido.\n" in out