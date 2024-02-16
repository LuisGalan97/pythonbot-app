import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Helpers.helpers import Helpers
from collections import namedtuple

testData = {
    "idrange" : "",
    "ranname" : "TestRangeName",
    "ranexist" : "General de alianza",
    "rancontrol" : 5,
    "randes" : "TestRangeDescription",
    "idmember" : "",
    "memname" : "TestMemberName",
    "memdate" : "25/01/2100",
    "idevent_1" : "",
    "evname_1" : "TestEventName1",
    "evpoints_1" : 5,
    "idevent_2" : "",
    "evname_2" : "TestEventName2",
    "evpoints_2" : 8,
    "idevent_3" : "",
    "evname_3" : "TestEventName3",
    "evpoints_3" : 11,
    "evdes" : "TestEventDescription",
    "idassist_1" : "",
    "assistdate_1" : "01/06/2100",
    "idassist_2" : "",
    "assistdate_2" : "01/07/2100",
    "idassist_3" : "",
    "assistdate_3" : "01/08/2100",
    "idassist_4" : "",
    "assistdate_4" : "01/09/2100",
    "idassist_5" : "",
    "assistdate_5" : "01/10/2100",
    "idassist_6" : "",
    "assistdate_6" : "01/11/2100",
    "idassist_7" : "",
    "assistdate_7" : "01/12/2100",
    "idassist_8" : "",
    "assistdate_8" : "01/01/2101",
    "idassist_9" : "",
    "assistdate_9" : "01/02/2101",
    "idassist_10" : "",
    "assistdate_10" : "01/03/2101",
    "idassist_11" : "",
    "assistdate_11" : "01/04/2101",
    "idassist_12" : "",
    "assistdate_12" : "01/05/2101"
}

Message = namedtuple('Message', ['author', 'content', 'channel'])
Channel = namedtuple('Channel', ['name'])
Client = namedtuple('Client', ['user'])
name = 'test'
author = "test"
user = "test"
app = AppHandler()

@pytest.mark.asyncio
async def testAllPointMemberDefault_addRange(capfd):
    command = f"$addRange [{testData['ranname']}, "\
              f"{testData['rancontrol']}, {testData['randes']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addRange", app.setData,
                       Helpers.setStruct("range"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["idrange"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "El ___rango___ ha sido creado con exito sobre el "\
          f"**_ID_** \'{testData['idrange']}\'.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_addMember(capfd):
    command = f"$addMember [{testData['memname']}, "\
              f"{testData['ranname']}, {testData['memdate']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addMember", app.setData,
                       Helpers.setStruct("member"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["idmember"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "El ___integrante___ ha sido creado con exito sobre el "\
          f"**_ID_** \'{testData['idmember']}\'.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_addEvent_1(capfd):
    command = f"$addEvent [{testData['evname_1']}, "\
              f"{testData['evpoints_1']}, {testData['evdes']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addEvent", app.setData,
                       Helpers.setStruct("event"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["idevent_1"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "El ___evento___ ha sido creado con exito sobre el "\
          f"**_ID_** \'{testData['idevent_1']}\'.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_addEvent_2(capfd):
    command = f"$addEvent [{testData['evname_2']}, "\
              f"{testData['evpoints_2']}, {testData['evdes']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addEvent", app.setData,
                       Helpers.setStruct("event"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["idevent_2"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "El ___evento___ ha sido creado con exito sobre el "\
          f"**_ID_** \'{testData['idevent_2']}\'.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_addEvent_3(capfd):
    command = f"$addEvent [{testData['evname_3']}, "\
              f"{testData['evpoints_3']}, {testData['evdes']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addEvent", app.setData,
                       Helpers.setStruct("event"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["idevent_3"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "El ___evento___ ha sido creado con exito sobre el "\
          f"**_ID_** \'{testData['idevent_3']}\'.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_addAssist_1(capfd):
    command = f"$addAssist [{testData['memname']}, "\
              f"{testData['evname_1']}, {testData['assistdate_1']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addAssist", app.setData,
                       Helpers.setStruct("assist"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["idassist_1"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "La ___asistencia___ ha sido creada con exito sobre el "\
          f"**_ID_** \'{testData['idassist_1']}\'.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_addAssist_2(capfd):
    command = f"$addAssist [{testData['memname']}, "\
              f"{testData['evname_2']}, {testData['assistdate_2']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addAssist", app.setData,
                       Helpers.setStruct("assist"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["idassist_2"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "La ___asistencia___ ha sido creada con exito sobre el "\
          f"**_ID_** \'{testData['idassist_2']}\'.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_addAssist_3(capfd):
    command = f"$addAssist [{testData['memname']}, "\
              f"{testData['evname_3']}, {testData['assistdate_3']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addAssist", app.setData,
                       Helpers.setStruct("assist"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["idassist_3"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "La ___asistencia___ ha sido creada con exito sobre el "\
          f"**_ID_** \'{testData['idassist_3']}\'.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_addAssist_4(capfd):
    command = f"$addAssist [{testData['memname']}, "\
              f"{testData['evname_1']}, {testData['assistdate_4']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addAssist", app.setData,
                       Helpers.setStruct("assist"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["idassist_4"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "La ___asistencia___ ha sido creada con exito sobre el "\
          f"**_ID_** \'{testData['idassist_4']}\'.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_addAssist_5(capfd):
    command = f"$addAssist [{testData['memname']}, "\
              f"{testData['evname_2']}, {testData['assistdate_5']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addAssist", app.setData,
                       Helpers.setStruct("assist"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["idassist_5"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "La ___asistencia___ ha sido creada con exito sobre el "\
          f"**_ID_** \'{testData['idassist_5']}\'.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_addAssist_6(capfd):
    command = f"$addAssist [{testData['memname']}, "\
              f"{testData['evname_3']}, {testData['assistdate_6']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addAssist", app.setData,
                       Helpers.setStruct("assist"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["idassist_6"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "La ___asistencia___ ha sido creada con exito sobre el "\
          f"**_ID_** \'{testData['idassist_6']}\'.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_addAssist_7(capfd):
    command = f"$addAssist [{testData['memname']}, "\
              f"{testData['evname_1']}, {testData['assistdate_7']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addAssist", app.setData,
                       Helpers.setStruct("assist"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["idassist_7"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "La ___asistencia___ ha sido creada con exito sobre el "\
          f"**_ID_** \'{testData['idassist_7']}\'.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_addAssist_8(capfd):
    command = f"$addAssist [{testData['memname']}, "\
              f"{testData['evname_2']}, {testData['assistdate_8']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addAssist", app.setData,
                       Helpers.setStruct("assist"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["idassist_8"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "La ___asistencia___ ha sido creada con exito sobre el "\
          f"**_ID_** \'{testData['idassist_8']}\'.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_addAssist_9(capfd):
    command = f"$addAssist [{testData['memname']}, "\
              f"{testData['evname_3']}, {testData['assistdate_9']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addAssist", app.setData,
                       Helpers.setStruct("assist"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["idassist_9"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "La ___asistencia___ ha sido creada con exito sobre el "\
          f"**_ID_** \'{testData['idassist_9']}\'.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_addAssist_10(capfd):
    command = f"$addAssist [{testData['memname']}, "\
              f"{testData['evname_1']}, {testData['assistdate_10']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addAssist", app.setData,
                       Helpers.setStruct("assist"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["idassist_10"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "La ___asistencia___ ha sido creada con exito sobre el "\
          f"**_ID_** \'{testData['idassist_10']}\'.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_addAssist_11(capfd):
    command = f"$addAssist [{testData['memname']}, "\
              f"{testData['evname_2']}, {testData['assistdate_11']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addAssist", app.setData,
                       Helpers.setStruct("assist"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["idassist_11"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "La ___asistencia___ ha sido creada con exito sobre el "\
          f"**_ID_** \'{testData['idassist_11']}\'.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_addAssist_12(capfd):
    command = f"$addAssist [{testData['memname']}, "\
              f"{testData['evname_3']}, {testData['assistdate_12']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addAssist", app.setData,
                       Helpers.setStruct("assist"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["idassist_12"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "La ___asistencia___ ha sido creada con exito sobre el "\
          f"**_ID_** \'{testData['idassist_12']}\'.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMember_partial(capfd):
    commands = [f"$listAllPointMember[{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember [{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember [ {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listAllPointMember [ {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listAllPointMember [ {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember", app.getDatas,
                         Helpers.getStruct("member",
                                           ["date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = (2*testData['evpoints_1'] +
                       2*testData['evpoints_2'] +
                       2*testData['evpoints_3'])
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMember_total(capfd):
    commands = [f"$listAllPointMember[{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember [{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember [ {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember [ {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listAllPointMember [ {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember", app.getDatas,
                         Helpers.getStruct("member",
                                           ["date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = (4*testData['evpoints_1'] +
                       4*testData['evpoints_2'] +
                       4*testData['evpoints_3'])
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberId_partial(capfd):
    commands = [f"$listAllPointMember:id[{testData['idmember']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:id [{testData['idmember']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:id [ {testData['idmember']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listAllPointMember:id [ {testData['idmember']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listAllPointMember:id [ {testData['idmember']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:id", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = (2*testData['evpoints_1'] +
                       2*testData['evpoints_2'] +
                       2*testData['evpoints_3'])
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberId_total(capfd):
    commands = [f"$listAllPointMember:id[{testData['idmember']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:id [{testData['idmember']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:id [ {testData['idmember']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember:id [ {testData['idmember']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listAllPointMember:id [ {testData['idmember']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:id", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = (4*testData['evpoints_1'] +
                       4*testData['evpoints_2'] +
                       4*testData['evpoints_3'])
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberName_partial(capfd):
    commands = [f"$listAllPointMember:name[{testData['memname']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:name [{testData['memname']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:name [ {testData['memname']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listAllPointMember:name [ {testData['memname']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listAllPointMember:name [ {testData['memname']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:name", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = (2*testData['evpoints_1'] +
                       2*testData['evpoints_2'] +
                       2*testData['evpoints_3'])
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberName_total(capfd):
    commands = [f"$listAllPointMember:name[{testData['memname']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:name [{testData['memname']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:name [ {testData['memname']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember:name [ {testData['memname']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listAllPointMember:name [ {testData['memname']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:name", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = (4*testData['evpoints_1'] +
                       4*testData['evpoints_2'] +
                       4*testData['evpoints_3'])
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberRange_partial(capfd):
    commands = [f"$listAllPointMember:range[{testData['ranname']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:range [{testData['ranname']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:range [ {testData['ranname']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listAllPointMember:range [ {testData['ranname']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listAllPointMember:range [ {testData['ranname']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:range", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = (2*testData['evpoints_1'] +
                       2*testData['evpoints_2'] +
                       2*testData['evpoints_3'])
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberRange_total(capfd):
    commands = [f"$listAllPointMember:range[{testData['ranname']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:range [{testData['ranname']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:range [ {testData['ranname']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember:range [ {testData['ranname']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listAllPointMember:range [ {testData['ranname']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:range", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = (4*testData['evpoints_1'] +
                       4*testData['evpoints_2'] +
                       4*testData['evpoints_3'])
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberEvent1_partial(capfd):
    commands = [f"$listAllPointMember:event[{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:event [{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:event [ {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listAllPointMember:event [ {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listAllPointMember:event [ {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 2*testData['evpoints_1']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberEvent1_total(capfd):
    commands = [f"$listAllPointMember:event[{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:event [{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:event [ {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember:event [ {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listAllPointMember:event [ {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 4*testData['evpoints_1']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberEvent2_partial(capfd):
    commands = [f"$listAllPointMember:event[{testData['evname_2']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:event [{testData['evname_2']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:event [ {testData['evname_2']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listAllPointMember:event [ {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listAllPointMember:event [ {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 2*testData['evpoints_2']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberEvent2_total(capfd):
    commands = [f"$listAllPointMember:event[{testData['evname_2']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:event [{testData['evname_2']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:event [ {testData['evname_2']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember:event [ {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listAllPointMember:event [ {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 4*testData['evpoints_2']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberEvent3_partial(capfd):
    commands = [f"$listAllPointMember:event[{testData['evname_3']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:event [{testData['evname_3']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:event [ {testData['evname_3']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listAllPointMember:event [ {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listAllPointMember:event [ {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 2*testData['evpoints_3']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberEvent3_total(capfd):
    commands = [f"$listAllPointMember:event[{testData['evname_3']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:event [{testData['evname_3']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:event [ {testData['evname_3']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember:event [ {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listAllPointMember:event [ {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 4*testData['evpoints_3']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberIdEvent1_partial(capfd):
    commands = [f"$listAllPointMember:id&event[{testData['idmember']},"\
                f"{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:id&event [{testData['idmember']}, "
                f"{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listAllPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listAllPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:id&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 2*testData['evpoints_1']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberIdEvent1_total(capfd):
    commands = [f"$listAllPointMember:id&event[{testData['idmember']},"\
                f"{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:id&event [{testData['idmember']}, "
                f"{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listAllPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:id&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 4*testData['evpoints_1']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberIdEvent2_partial(capfd):
    commands = [f"$listAllPointMember:id&event[{testData['idmember']},"\
                f"{testData['evname_2']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:id&event [{testData['idmember']}, "
                f"{testData['evname_2']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_2']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listAllPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listAllPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:id&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 2*testData['evpoints_2']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberIdEvent2_total(capfd):
    commands = [f"$listAllPointMember:id&event[{testData['idmember']},"\
                f"{testData['evname_2']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:id&event [{testData['idmember']}, "
                f"{testData['evname_2']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_2']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listAllPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:id&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 4*testData['evpoints_2']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberIdEvent3_partial(capfd):
    commands = [f"$listAllPointMember:id&event[{testData['idmember']},"\
                f"{testData['evname_3']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:id&event [{testData['idmember']}, "
                f"{testData['evname_3']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_3']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listAllPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listAllPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:id&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 2*testData['evpoints_3']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberIdEvent3_total(capfd):
    commands = [f"$listAllPointMember:id&event[{testData['idmember']},"\
                f"{testData['evname_3']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:id&event [{testData['idmember']}, "
                f"{testData['evname_3']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_3']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listAllPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:id&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 4*testData['evpoints_3']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberNameEvent1_partial(
    capfd):
    commands = [f"$listAllPointMember:name&event[{testData['memname']},"\
                f"{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:name&event [{testData['memname']}, "
                f"{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listAllPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listAllPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:name&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 2*testData['evpoints_1']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberNameEvent1_total(capfd):
    commands = [f"$listAllPointMember:name&event[{testData['memname']},"\
                f"{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:name&event [{testData['memname']}, "
                f"{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listAllPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:name&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 4*testData['evpoints_1']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberNameEvent2_partial(
    capfd):
    commands = [f"$listAllPointMember:name&event[{testData['memname']},"\
                f"{testData['evname_2']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:name&event [{testData['memname']}, "
                f"{testData['evname_2']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_2']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listAllPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listAllPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:name&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 2*testData['evpoints_2']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberNameEvent2_total(capfd):
    commands = [f"$listAllPointMember:name&event[{testData['memname']},"\
                f"{testData['evname_2']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:name&event [{testData['memname']}, "
                f"{testData['evname_2']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_2']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listAllPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:name&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 4*testData['evpoints_2']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberNameEvent3_partial(
    capfd):
    commands = [f"$listAllPointMember:name&event[{testData['memname']},"\
                f"{testData['evname_3']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:name&event [{testData['memname']}, "
                f"{testData['evname_3']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_3']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listAllPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listAllPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:name&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 2*testData['evpoints_3']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberNameEvent3_total(capfd):
    commands = [f"$listAllPointMember:name&event[{testData['memname']},"\
                f"{testData['evname_3']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:name&event [{testData['memname']}, "
                f"{testData['evname_3']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_3']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listAllPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:name&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 4*testData['evpoints_3']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberRangeEvent1_partial(
    capfd):
    commands = [f"$listAllPointMember:range&event[{testData['ranname']},"\
                f"{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:range&event [{testData['ranname']}, "
                f"{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listAllPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listAllPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:range&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 2*testData['evpoints_1']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberRangeEvent1_total(capfd):
    commands = [f"$listAllPointMember:range&event[{testData['ranname']},"\
                f"{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:range&event [{testData['ranname']}, "
                f"{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listAllPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:range&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 4*testData['evpoints_1']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberRangeEvent2_partial(
    capfd):
    commands = [f"$listAllPointMember:range&event[{testData['ranname']},"\
                f"{testData['evname_2']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:range&event [{testData['ranname']}, "
                f"{testData['evname_2']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_2']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listAllPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listAllPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:range&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 2*testData['evpoints_2']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberRangeEvent2_total(capfd):
    commands = [f"$listAllPointMember:range&event[{testData['ranname']},"\
                f"{testData['evname_2']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:range&event [{testData['ranname']}, "
                f"{testData['evname_2']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_2']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listAllPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:range&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 4*testData['evpoints_2']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberRangeEvent3_partial(
    capfd):
    commands = [f"$listAllPointMember:range&event[{testData['ranname']},"\
                f"{testData['evname_3']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:range&event [{testData['ranname']}, "
                f"{testData['evname_3']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listAllPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_3']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listAllPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listAllPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:range&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 2*testData['evpoints_3']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberRangeEvent3_total(capfd):
    commands = [f"$listAllPointMember:range&event[{testData['ranname']},"\
                f"{testData['evname_3']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:range&event [{testData['ranname']}, "
                f"{testData['evname_3']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_3']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listAllPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:range&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 4*testData['evpoints_3']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMember_e(capfd):
    commands = [f"$listAllPointMember[{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember [{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember [ {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] "]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAllPointMember", app.getDatas,
                             Helpers.getStruct("member",
                                               ["date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberId_e(capfd):
    commands = [f"$listAllPointMember:id[{testData['idmember']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:id [{testData['idmember']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:id [ {testData['idmember']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] "]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                          channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAllPointMember:id", app.getDatas,
                             Helpers.getStruct("member",
                                               ["id",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberName_e(capfd):
    commands = [f"$listAllPointMember:name[{testData['memname']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:name [{testData['memname']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:name [ {testData['memname']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] "]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                          channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAllPointMember:name", app.getDatas,
                             Helpers.getStruct("member",
                                               ["name",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberRange_e(capfd):
    commands = [f"$listAllPointMember:range[{testData['ranname']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:range [{testData['ranname']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:range [ {testData['ranname']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] "]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                          channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAllPointMember:range", app.getDatas,
                             Helpers.getStruct("member",
                                               ["range",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberEvent_e(capfd):
    commands = [f"$listAllPointMember:event[{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:event [{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:event [ {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] "]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAllPointMember:event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["event",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberIdEvent_e(capfd):
    commands = [f"$listAllPointMember:id&event[{testData['idmember']},"\
                f"{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:id&event [{testData['idmember']}, "
                f"{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] "]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAllPointMember:id&event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["id",
                                                "event",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberNameEvent_e(capfd):
    commands = [f"$listAllPointMember:name&event[{testData['memname']},"\
                f"{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:name&event [{testData['memname']}, "
                f"{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] "]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAllPointMember:name&event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["name",
                                                "event",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberRangeEvent_e(capfd):
    commands = [f"$listAllPointMember:range&event[{testData['ranname']},"\
                f"{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:range&event [{testData['ranname']}, "
                f"{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] "]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAllPointMember:range&event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["range",
                                                "event",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMember_eIncomplete(capfd):
    commands = [f"$listAllPointMember[{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember [{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember [ {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] "]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAllPointMember", app.getDatas,
                             Helpers.getStruct("member",
                                               ["date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert  "**$listAllPointMember** "\
                   f"**[**{testData['assistdate_1']}, "\
                   f"{testData['assistdate_12']}**]** "\
                    "**> e**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberId_eIncomplete(capfd):
    commands = [f"$listAllPointMember:id[{testData['idmember']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:id [{testData['idmember']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:id [ {testData['idmember']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] "]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                          channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAllPointMember:id", app.getDatas,
                             Helpers.getStruct("member",
                                               ["id",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert f"**$listAllPointMember:id** **[**{testData['idmember']}, "\
                   f"{testData['assistdate_1']}, "\
                   f"{testData['assistdate_12']}**]** "\
                    "**> e**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberName_eIncomplete(capfd):
    commands = [f"$listAllPointMember:name[{testData['memname']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:name [{testData['memname']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:name [ {testData['memname']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] "]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                          channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAllPointMember:name", app.getDatas,
                             Helpers.getStruct("member",
                                               ["name",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert  "**$listAllPointMember:name** "\
                   f"**[**{testData['memname']}, "\
                   f"{testData['assistdate_1']}, "\
                   f"{testData['assistdate_12']}**]** "\
                    "**> e**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberRange_eIncomplete(capfd):
    commands = [f"$listAllPointMember:range[{testData['ranname']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:range [{testData['ranname']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:range [ {testData['ranname']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] "]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                          channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAllPointMember:range", app.getDatas,
                             Helpers.getStruct("member",
                                               ["range",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert  "**$listAllPointMember:range** "\
                   f"**[**{testData['ranname']}, "\
                   f"{testData['assistdate_1']}, "\
                   f"{testData['assistdate_12']}**]** "\
                    "**> e**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberEvent_eIncomplete(capfd):
    commands = [f"$listAllPointMember:event[{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:event [{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:event [ {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] "]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAllPointMember:event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["event",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert  "**$listAllPointMember:event** "\
                   f"**[**{testData['evname_1']}, "\
                   f"{testData['assistdate_1']}, "\
                   f"{testData['assistdate_12']}**]** "\
                    "**> e**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberIdEvent_eIncomplete(
    capfd):
    commands = [f"$listAllPointMember:id&event[{testData['idmember']},"\
                f"{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:id&event [{testData['idmember']}, "
                f"{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] "]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAllPointMember:id&event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["id",
                                                "event",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert  "**$listAllPointMember:id&event** "\
                   f"**[**{testData['idmember']}, "\
                   f"{testData['evname_1']}, "\
                   f"{testData['assistdate_1']}, "\
                   f"{testData['assistdate_12']}**]** "\
                    "**> e**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberNameEvent_eIncomplete(
    capfd):
    commands = [f"$listAllPointMember:name&event[{testData['memname']},"\
                f"{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:name&event [{testData['memname']}, "
                f"{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] "]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAllPointMember:name&event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["name",
                                                "event",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert  "**$listAllPointMember:name&event** "\
                   f"**[**{testData['memname']}, "\
                   f"{testData['evname_1']}, "\
                   f"{testData['assistdate_1']}, "\
                   f"{testData['assistdate_12']}**]** "\
                    "**> e**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberRangeEvent_eIncomplete(
    capfd):
    commands = [f"$listAllPointMember:range&event[{testData['ranname']},"\
                f"{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:range&event [{testData['ranname']}, "
                f"{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] "]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAllPointMember:range&event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["range",
                                                "event",
                                                "date_1",
                                                "date_2"],
                                                "atpoints"))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert  "**$listAllPointMember:range&event** "\
                   f"**[**{testData['ranname']}, "\
                   f"{testData['evname_1']}, "\
                   f"{testData['assistdate_1']}, "\
                   f"{testData['assistdate_12']}**]** "\
                    "**> e**\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_delAssistId_1(capfd):
    command = f"$delAssist:id [{testData['idassist_1']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delAssist:id", app.deleteData,
                       Helpers.delStruct("assist", "id"))
    out, _ = capfd.readouterr()
    assert "La ___asistencia___ ha sido eliminada con exito.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_delAssistId_2(capfd):
    command = f"$delAssist:id [{testData['idassist_2']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delAssist:id", app.deleteData,
                       Helpers.delStruct("assist", "id"))
    out, _ = capfd.readouterr()
    assert "La ___asistencia___ ha sido eliminada con exito.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_delAssistId_3(capfd):
    command = f"$delAssist:id [{testData['idassist_3']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delAssist:id", app.deleteData,
                       Helpers.delStruct("assist", "id"))
    out, _ = capfd.readouterr()
    assert "La ___asistencia___ ha sido eliminada con exito.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_delAssistId_4(capfd):
    command = f"$delAssist:id [{testData['idassist_4']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delAssist:id", app.deleteData,
                       Helpers.delStruct("assist", "id"))
    out, _ = capfd.readouterr()
    assert "La ___asistencia___ ha sido eliminada con exito.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_delAssistId_5(capfd):
    command = f"$delAssist:id [{testData['idassist_5']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delAssist:id", app.deleteData,
                       Helpers.delStruct("assist", "id"))
    out, _ = capfd.readouterr()
    assert "La ___asistencia___ ha sido eliminada con exito.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_delAssistId_6(capfd):
    command = f"$delAssist:id [{testData['idassist_6']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delAssist:id", app.deleteData,
                       Helpers.delStruct("assist", "id"))
    out, _ = capfd.readouterr()
    assert "La ___asistencia___ ha sido eliminada con exito.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_delAssistId_7(capfd):
    command = f"$delAssist:id [{testData['idassist_7']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delAssist:id", app.deleteData,
                       Helpers.delStruct("assist", "id"))
    out, _ = capfd.readouterr()
    assert "La ___asistencia___ ha sido eliminada con exito.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_delAssistId_8(capfd):
    command = f"$delAssist:id [{testData['idassist_8']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delAssist:id", app.deleteData,
                       Helpers.delStruct("assist", "id"))
    out, _ = capfd.readouterr()
    assert "La ___asistencia___ ha sido eliminada con exito.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_delAssistId_9(capfd):
    command = f"$delAssist:id [{testData['idassist_9']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delAssist:id", app.deleteData,
                       Helpers.delStruct("assist", "id"))
    out, _ = capfd.readouterr()
    assert "La ___asistencia___ ha sido eliminada con exito.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_delAssistId_10(capfd):
    command = f"$delAssist:id [{testData['idassist_10']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delAssist:id", app.deleteData,
                       Helpers.delStruct("assist", "id"))
    out, _ = capfd.readouterr()
    assert "La ___asistencia___ ha sido eliminada con exito.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_delAssistId_11(capfd):
    command = f"$delAssist:id [{testData['idassist_11']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delAssist:id", app.deleteData,
                       Helpers.delStruct("assist", "id"))
    out, _ = capfd.readouterr()
    assert "La ___asistencia___ ha sido eliminada con exito.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_delAssistId_12(capfd):
    command = f"$delAssist:id [{testData['idassist_12']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delAssist:id", app.deleteData,
                       Helpers.delStruct("assist", "id"))
    out, _ = capfd.readouterr()
    assert "La ___asistencia___ ha sido eliminada con exito.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMember_AssistNoExist(capfd):
    commands = [f"$listAllPointMember[{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember [{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember [ {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember [ {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL ",
                f"$listAllPointMember [ {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember", app.getDatas,
                         Helpers.getStruct("member",
                                           ["date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        assert "0" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberId_AssistNoExist(capfd):
    commands = [f"$listAllPointMember:id[{testData['idmember']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:id [{testData['idmember']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:id [ {testData['idmember']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember:id [ {testData['idmember']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listAllPointMember:id [ {testData['idmember']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:id", app.getDatas,
                         Helpers.getStruct("member",
                                            ["id",
                                             "date_1",
                                             "date_2"],
                                             "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        assert "0" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberName_AssistNoExist(
    capfd):
    commands = [f"$listAllPointMember:name[{testData['memname']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:name [{testData['memname']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:name [ {testData['memname']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember:name [ {testData['memname']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL ",
                f"$listAllPointMember:name [ {testData['memname']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:name", app.getDatas,
                         Helpers.getStruct("member",
                                            ["name",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        assert "0" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberRange_AssistNoExist(
    capfd):
    commands = [f"$listAllPointMember:range[{testData['ranname']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:range [{testData['ranname']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:range [ {testData['ranname']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember:range [ {testData['ranname']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listAllPointMember:range [ {testData['ranname']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:range", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        assert "0" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberEvent_AssistNoExist(
    capfd):
    commands = [f"$listAllPointMember:event[{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:event [{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:event [ {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember:event [ {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listAllPointMember:event [ {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        assert "0" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberIdEvent_AssistNoExist(
    capfd):
    commands = [f"$listAllPointMember:id&event[{testData['idmember']},"\
                f"{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:id&event [{testData['idmember']}, "
                f"{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listAllPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:id&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        assert "0" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberNameEvent_AssistNoExist(
    capfd):
    commands = [f"$listAllPointMember:name&event[{testData['memname']},"\
                f"{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:name&event [{testData['memname']}, "
                f"{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listAllPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:name&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        assert "0" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberRangeEvent_AssistNoExist(
    capfd):
    commands = [f"$listAllPointMember:range&event[{testData['ranname']},"\
                f"{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:range&event [{testData['ranname']}, "
                f"{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listAllPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:range&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        assert "0" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_delEventId_1(capfd):
    command = f"$delEvent:id [{testData['idevent_1']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delEvent:id", app.deleteData,
                       Helpers.delStruct("event", "id"))
    out, _ = capfd.readouterr()
    assert "El ___evento___ ha sido eliminado con exito.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_delEventId_2(capfd):
    command = f"$delEvent:id [{testData['idevent_2']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delEvent:id", app.deleteData,
                       Helpers.delStruct("event", "id"))
    out, _ = capfd.readouterr()
    assert "El ___evento___ ha sido eliminado con exito.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_delEventId_3(capfd):
    command = f"$delEvent:id [{testData['idevent_3']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delEvent:id", app.deleteData,
                       Helpers.delStruct("event", "id"))
    out, _ = capfd.readouterr()
    assert "El ___evento___ ha sido eliminado con exito.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_delMemberId(capfd):
    command = f"$delMember:id [{testData['idmember']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delMember:id", app.deleteData,
                       Helpers.delStruct("member", "id"))
    out, _ = capfd.readouterr()
    assert "El ___integrante___ ha sido eliminado con exito.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_delRangeId(capfd):
    command = f"$delRange:id [{testData['idrange']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delRange:id", app.deleteData,
                       Helpers.delStruct("range", "id"))
    out, _ = capfd.readouterr()
    assert "El ___rango___ ha sido eliminado con exito.\n" in out


@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberRange_RangeNoExist(
    capfd):
    commands = [f"$listAllPointMember:range[{testData['ranname']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:range [{testData['ranname']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:range [ {testData['ranname']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember:range [ {testData['ranname']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listAllPointMember:range [ {testData['ranname']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:range", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['ranname']}' "\
                "ingresado en el campo "\
                "**_Rango_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberEvent_EventNoExist(
    capfd):
    commands = [f"$listAllPointMember:event[{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:event [{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:event [ {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember:event [ {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listAllPointMember:event [ {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['evname_1']}' "\
                "ingresado en el campo "\
                "**_Evento_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberIdEvent_EventNoExist(
    capfd):
    commands = [f"$listAllPointMember:id&event[{testData['idmember']},"\
                f"{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:id&event [{testData['idmember']}, "
                f"{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listAllPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:id&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["id",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['evname_1']}' "\
                "ingresado en el campo "\
                "**_Evento_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberNameEvent_EventNoExist(
    capfd):
    commands = [f"$listAllPointMember:name&event[{testData['memname']},"\
                f"{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:name&event [{testData['memname']}, "
                f"{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listAllPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:name&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["name",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['evname_1']}' "\
                "ingresado en el campo "\
                "**_Evento_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberRangeEvent_RangeNoExist(
    capfd):
    commands = [f"$listAllPointMember:range&event[{testData['ranname']},"\
                f"{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:range&event [{testData['ranname']}, "
                f"{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listAllPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:range&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['ranname']}' "\
                "ingresado en el campo "\
                "**_Rango_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testAllPointMemberDefault_listAllPointMemberRangeEvent_EventNoExist(
    capfd):
    commands = [f"$listAllPointMember:range&event[{testData['ranexist']},"\
                f"{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:range&event [{testData['ranexist']}, "
                f"{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listAllPointMember:range&event [ {testData['ranexist']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listAllPointMember:range&event [ {testData['ranexist']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listAllPointMember:range&event [ {testData['ranexist']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAllPointMember:range&event", app.getDatas,
                         Helpers.getStruct("member",
                                           ["range",
                                            "event",
                                            "date_1",
                                            "date_2"],
                                            "atpoints"))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['evname_1']}' "\
                "ingresado en el campo "\
                "**_Evento_** no fue encontrado en la "\
                "base de datos.\n" in out