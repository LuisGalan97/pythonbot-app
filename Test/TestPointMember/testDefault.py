import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Helpers.helpers import Helpers
from collections import namedtuple

testData = {
    "idrange" : "",
    "ranname" : "TestRangeName",
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
async def testPointMemberDefault_addRange(capfd):
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
async def testPointMemberDefault_addMember(capfd):
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
async def testPointMemberDefault_addEvent_1(capfd):
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
async def testPointMemberDefault_addEvent_2(capfd):
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
async def testPointMemberDefault_addEvent_3(capfd):
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
async def testPointMemberDefault_addAssist_1(capfd):
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
async def testPointMemberDefault_addAssist_2(capfd):
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
async def testPointMemberDefault_addAssist_3(capfd):
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
async def testPointMemberDefault_addAssist_4(capfd):
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
async def testPointMemberDefault_addAssist_5(capfd):
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
async def testPointMemberDefault_addAssist_6(capfd):
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
async def testPointMemberDefault_addAssist_7(capfd):
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
async def testPointMemberDefault_addAssist_8(capfd):
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
async def testPointMemberDefault_addAssist_9(capfd):
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
async def testPointMemberDefault_addAssist_10(capfd):
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
async def testPointMemberDefault_addAssist_11(capfd):
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
async def testPointMemberDefault_addAssist_12(capfd):
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
async def testPointMemberDefault_listPointMember_partial(capfd):
    commands = [f"$listPointMember[{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listPointMember [{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listPointMember [ {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listPointMember [ {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listPointMember [ {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
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
async def testPointMemberDefault_listPointMember_total(capfd):
    commands = [f"$listPointMember[{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listPointMember [{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listPointMember [ {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listPointMember [ {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listPointMember [ {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
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
async def testPointMemberDefault_listPointMemberId_partial(capfd):
    commands = [f"$listPointMember:id[{testData['idmember']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:id [{testData['idmember']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:id [ {testData['idmember']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listPointMember:id [ {testData['idmember']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listPointMember:id [ {testData['idmember']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
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
async def testPointMemberDefault_listPointMemberId_total(capfd):
    commands = [f"$listPointMember:id[{testData['idmember']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:id [{testData['idmember']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:id [ {testData['idmember']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listPointMember:id [ {testData['idmember']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listPointMember:id [ {testData['idmember']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
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
async def testPointMemberDefault_listPointMemberName_partial(capfd):
    commands = [f"$listPointMember:name[{testData['memname']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:name [{testData['memname']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:name [ {testData['memname']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listPointMember:name [ {testData['memname']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listPointMember:name [ {testData['memname']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
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
async def testPointMemberDefault_listPointMemberName_total(capfd):
    commands = [f"$listPointMember:name[{testData['memname']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:name [{testData['memname']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:name [ {testData['memname']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listPointMember:name [ {testData['memname']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listPointMember:name [ {testData['memname']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
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
async def testPointMemberDefault_listPointMemberRange_partial(capfd):
    commands = [f"$listPointMember:range[{testData['ranname']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:range [{testData['ranname']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:range [ {testData['ranname']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listPointMember:range [ {testData['ranname']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listPointMember:range [ {testData['ranname']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
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
async def testPointMemberDefault_listPointMemberRange_total(capfd):
    commands = [f"$listPointMember:range[{testData['ranname']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:range [{testData['ranname']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:range [ {testData['ranname']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listPointMember:range [ {testData['ranname']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listPointMember:range [ {testData['ranname']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
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
async def testPointMemberDefault_listPointMemberEvent1_partial(capfd):
    commands = [f"$listPointMember:event[{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:event [{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:event [ {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listPointMember:event [ {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listPointMember:event [ {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
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
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 2*testData['evpoints_1']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testPointMemberDefault_listPointMemberEvent1_total(capfd):
    commands = [f"$listPointMember:event[{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:event [{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:event [ {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listPointMember:event [ {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listPointMember:event [ {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
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
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 4*testData['evpoints_1']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testPointMemberDefault_listPointMemberEvent2_partial(capfd):
    commands = [f"$listPointMember:event[{testData['evname_2']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:event [{testData['evname_2']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:event [ {testData['evname_2']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listPointMember:event [ {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listPointMember:event [ {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
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
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 2*testData['evpoints_2']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testPointMemberDefault_listPointMemberEvent2_total(capfd):
    commands = [f"$listPointMember:event[{testData['evname_2']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:event [{testData['evname_2']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:event [ {testData['evname_2']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listPointMember:event [ {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listPointMember:event [ {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
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
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 4*testData['evpoints_2']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testPointMemberDefault_listPointMemberEvent3_partial(capfd):
    commands = [f"$listPointMember:event[{testData['evname_3']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:event [{testData['evname_3']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:event [ {testData['evname_3']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listPointMember:event [ {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listPointMember:event [ {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
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
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 2*testData['evpoints_3']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testPointMemberDefault_listPointMemberEvent3_total(capfd):
    commands = [f"$listPointMember:event[{testData['evname_3']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:event [{testData['evname_3']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:event [ {testData['evname_3']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listPointMember:event [ {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listPointMember:event [ {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
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
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['idmember']}" in out
        assert f"{testData['memname']}" in out
        assert f"{testData['ranname']}" in out
        assert f"{testData['memdate'].replace('-','/')}" in out
        assert "Ninguno" in out
        totalPoints = 4*testData['evpoints_3']
        assert str(totalPoints) in out

@pytest.mark.asyncio
async def testPointMemberDefault_listPointMemberIdEvent1_partial(capfd):
    commands = [f"$listPointMember:id&event[{testData['idmember']},"\
                f"{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:id&event [{testData['idmember']}, "
                f"{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:id&event", app.getDatas,
                     Helpers.getStruct("member",
                                       ["id",
                                        "event",
                                        "assist_date_1",
                                        "assist_date_2"]))
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
async def testPointMemberDefault_listPointMemberIdEvent1_total(capfd):
    commands = [f"$listPointMember:id&event[{testData['idmember']},"\
                f"{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:id&event [{testData['idmember']}, "
                f"{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:id&event", app.getDatas,
                     Helpers.getStruct("member",
                                       ["id",
                                        "event",
                                        "assist_date_1",
                                        "assist_date_2"]))
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
async def testPointMemberDefault_listPointMemberIdEvent2_partial(capfd):
    commands = [f"$listPointMember:id&event[{testData['idmember']},"\
                f"{testData['evname_2']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:id&event [{testData['idmember']}, "
                f"{testData['evname_2']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_2']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:id&event", app.getDatas,
                     Helpers.getStruct("member",
                                       ["id",
                                        "event",
                                        "assist_date_1",
                                        "assist_date_2"]))
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
async def testPointMemberDefault_listPointMemberIdEvent2_total(capfd):
    commands = [f"$listPointMember:id&event[{testData['idmember']},"\
                f"{testData['evname_2']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:id&event [{testData['idmember']}, "
                f"{testData['evname_2']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_2']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:id&event", app.getDatas,
                     Helpers.getStruct("member",
                                       ["id",
                                        "event",
                                        "assist_date_1",
                                        "assist_date_2"]))
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
async def testPointMemberDefault_listPointMemberIdEvent3_partial(capfd):
    commands = [f"$listPointMember:id&event[{testData['idmember']},"\
                f"{testData['evname_3']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:id&event [{testData['idmember']}, "
                f"{testData['evname_3']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_3']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:id&event", app.getDatas,
                     Helpers.getStruct("member",
                                       ["id",
                                        "event",
                                        "assist_date_1",
                                        "assist_date_2"]))
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
async def testPointMemberDefault_listPointMemberIdEvent3_total(capfd):
    commands = [f"$listPointMember:id&event[{testData['idmember']},"\
                f"{testData['evname_3']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:id&event [{testData['idmember']}, "
                f"{testData['evname_3']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_3']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listPointMember:id&event [ {testData['idmember']} ,"\
                f" {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:id&event", app.getDatas,
                     Helpers.getStruct("member",
                                       ["id",
                                        "event",
                                        "assist_date_1",
                                        "assist_date_2"]))
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
async def testPointMemberDefault_listPointMemberNameEvent1_partial(capfd):
    commands = [f"$listPointMember:name&event[{testData['memname']},"\
                f"{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:name&event [{testData['memname']}, "
                f"{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:name&event", app.getDatas,
                     Helpers.getStruct("member",
                                       ["name",
                                        "event",
                                        "assist_date_1",
                                        "assist_date_2"]))
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
async def testPointMemberDefault_listPointMemberNameEvent1_total(capfd):
    commands = [f"$listPointMember:name&event[{testData['memname']},"\
                f"{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:name&event [{testData['memname']}, "
                f"{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:name&event", app.getDatas,
                     Helpers.getStruct("member",
                                       ["name",
                                        "event",
                                        "assist_date_1",
                                        "assist_date_2"]))
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
async def testPointMemberDefault_listPointMemberNameEvent2_partial(capfd):
    commands = [f"$listPointMember:name&event[{testData['memname']},"\
                f"{testData['evname_2']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:name&event [{testData['memname']}, "
                f"{testData['evname_2']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_2']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:name&event", app.getDatas,
                     Helpers.getStruct("member",
                                       ["name",
                                        "event",
                                        "assist_date_1",
                                        "assist_date_2"]))
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
async def testPointMemberDefault_listPointMemberNameEvent2_total(capfd):
    commands = [f"$listPointMember:name&event[{testData['memname']},"\
                f"{testData['evname_2']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:name&event [{testData['memname']}, "
                f"{testData['evname_2']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_2']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:name&event", app.getDatas,
                     Helpers.getStruct("member",
                                       ["name",
                                        "event",
                                        "assist_date_1",
                                        "assist_date_2"]))
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
async def testPointMemberDefault_listPointMemberNameEvent3_partial(capfd):
    commands = [f"$listPointMember:name&event[{testData['memname']},"\
                f"{testData['evname_3']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:name&event [{testData['memname']}, "
                f"{testData['evname_3']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_3']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:name&event", app.getDatas,
                     Helpers.getStruct("member",
                                       ["name",
                                        "event",
                                        "assist_date_1",
                                        "assist_date_2"]))
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
async def testPointMemberDefault_listPointMemberNameEvent3_total(capfd):
    commands = [f"$listPointMember:name&event[{testData['memname']},"\
                f"{testData['evname_3']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:name&event [{testData['memname']}, "
                f"{testData['evname_3']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_3']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listPointMember:name&event [ {testData['memname']} ,"\
                f" {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:name&event", app.getDatas,
                     Helpers.getStruct("member",
                                       ["name",
                                        "event",
                                        "assist_date_1",
                                        "assist_date_2"]))
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
async def testPointMemberDefault_listPointMemberRangeEvent1_partial(capfd):
    commands = [f"$listPointMember:range&event[{testData['ranname']},"\
                f"{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:range&event [{testData['ranname']}, "
                f"{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:range&event", app.getDatas,
                     Helpers.getStruct("member",
                                       ["range",
                                        "event",
                                        "assist_date_1",
                                        "assist_date_2"]))
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
async def testPointMemberDefault_listPointMemberRangeEvent1_total(capfd):
    commands = [f"$listPointMember:range&event[{testData['ranname']},"\
                f"{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:range&event [{testData['ranname']}, "
                f"{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_1']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_1']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:range&event", app.getDatas,
                     Helpers.getStruct("member",
                                       ["range",
                                        "event",
                                        "assist_date_1",
                                        "assist_date_2"]))
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
async def testPointMemberDefault_listPointMemberRangeEvent2_partial(capfd):
    commands = [f"$listPointMember:range&event[{testData['ranname']},"\
                f"{testData['evname_2']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:range&event [{testData['ranname']}, "
                f"{testData['evname_2']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_2']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:range&event", app.getDatas,
                     Helpers.getStruct("member",
                                       ["range",
                                        "event",
                                        "assist_date_1",
                                        "assist_date_2"]))
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
async def testPointMemberDefault_listPointMemberRangeEvent2_total(capfd):
    commands = [f"$listPointMember:range&event[{testData['ranname']},"\
                f"{testData['evname_2']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:range&event [{testData['ranname']}, "
                f"{testData['evname_2']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_2']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_2']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:range&event", app.getDatas,
                     Helpers.getStruct("member",
                                       ["range",
                                        "event",
                                        "assist_date_1",
                                        "assist_date_2"]))
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
async def testPointMemberDefault_listPointMemberRangeEvent3_partial(capfd):
    commands = [f"$listPointMember:range&event[{testData['ranname']},"\
                f"{testData['evname_3']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:range&event [{testData['ranname']}, "
                f"{testData['evname_3']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_6']}]",
                f"$listPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_3']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] ",
                f"$listPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ]FILL",
                f"$listPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_6']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:range&event", app.getDatas,
                     Helpers.getStruct("member",
                                       ["range",
                                        "event",
                                        "assist_date_1",
                                        "assist_date_2"]))
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
async def testPointMemberDefault_listPointMemberRangeEvent3_total(capfd):
    commands = [f"$listPointMember:range&event[{testData['ranname']},"\
                f"{testData['evname_3']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:range&event [{testData['ranname']}, "
                f"{testData['evname_3']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_3']}, "\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] ",
                f"$listPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ]FILL",
                f"$listPointMember:range&event [ {testData['ranname']} ,"\
                f" {testData['evname_3']} ,"\
                f" {testData['assistdate_1']} , "\
                f"{testData['assistdate_12']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listPointMember:range&event", app.getDatas,
                     Helpers.getStruct("member",
                                       ["range",
                                        "event",
                                        "assist_date_1",
                                        "assist_date_2"]))
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
async def testPointMemberDefault_listPointMember_e(capfd):
    commands = [f"$listPointMember[{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listPointMember [{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listPointMember [ {testData['assistdate_1']} , "\
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
            await hdlr.dFMsg("listPointMember", app.getDatas,
                             Helpers.getStruct("member",
                                               ["assist_date_1",
                                                "assist_date_2"]))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testPointMemberDefault_listPointMemberId_e(capfd):
    commands = [f"$listPointMember:id[{testData['idmember']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:id [{testData['idmember']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:id [ {testData['idmember']}, "\
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
            await hdlr.dFMsg("listPointMember:id", app.getDatas,
                             Helpers.getStruct("member",
                                               ["id",
                                                "assist_date_1",
                                                "assist_date_2"]))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testPointMemberDefault_listPointMemberName_e(capfd):
    commands = [f"$listPointMember:name[{testData['memname']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:name [{testData['memname']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:name [ {testData['memname']}, "\
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
            await hdlr.dFMsg("listPointMember:name", app.getDatas,
                             Helpers.getStruct("member",
                                               ["name",
                                                "assist_date_1",
                                                "assist_date_2"]))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testPointMemberDefault_listPointMemberRange_e(capfd):
    commands = [f"$listPointMember:range[{testData['ranname']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:range [{testData['ranname']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:range [ {testData['ranname']}, "\
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
            await hdlr.dFMsg("listPointMember:range", app.getDatas,
                             Helpers.getStruct("member",
                                               ["range",
                                                "assist_date_1",
                                                "assist_date_2"]))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testPointMemberDefault_listPointMemberEvent_e(capfd):
    commands = [f"$listPointMember:event[{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:event [{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:event [ {testData['evname_1']}, "\
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
            await hdlr.dFMsg("listPointMember:event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["event",
                                                "assist_date_1",
                                                "assist_date_2"]))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testPointMemberDefault_listPointMemberIdEvent_e(capfd):
    commands = [f"$listPointMember:id&event[{testData['idmember']},"\
                f"{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:id&event [{testData['idmember']}, "
                f"{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:id&event [ {testData['idmember']} ,"\
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
            await hdlr.dFMsg("listPointMember:id&event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["id",
                                                "event",
                                                "assist_date_1",
                                                "assist_date_2"]))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testPointMemberDefault_listPointMemberNameEvent_e(capfd):
    commands = [f"$listPointMember:name&event[{testData['memname']},"\
                f"{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:name&event [{testData['memname']}, "
                f"{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:name&event [ {testData['memname']} ,"\
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
            await hdlr.dFMsg("listPointMember:name&event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["name",
                                                "event",
                                                "assist_date_1",
                                                "assist_date_2"]))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testPointMemberDefault_listPointMemberRangeEvent_e(capfd):
    commands = [f"$listPointMember:range&event[{testData['ranname']},"\
                f"{testData['evname_1']},"\
                f"{testData['assistdate_1']},"\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:range&event [{testData['ranname']}, "
                f"{testData['evname_1']}, "\
                f"{testData['assistdate_1']}, "\
                f"{testData['assistdate_12']}]",
                f"$listPointMember:range&event [ {testData['ranname']} ,"\
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
            await hdlr.dFMsg("listPointMember:range&event", app.getDatas,
                             Helpers.getStruct("member",
                                               ["range",
                                                "event",
                                                "assist_date_1",
                                                "assist_date_2"]))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testPointMemberDefault_delAssistId_1(capfd):
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
async def testPointMemberDefault_delAssistId_2(capfd):
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
async def testPointMemberDefault_delAssistId_3(capfd):
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
async def testPointMemberDefault_delAssistId_4(capfd):
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
async def testPointMemberDefault_delAssistId_5(capfd):
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
async def testPointMemberDefault_delAssistId_6(capfd):
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
async def testPointMemberDefault_delAssistId_7(capfd):
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
async def testPointMemberDefault_delAssistId_8(capfd):
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
async def testPointMemberDefault_delAssistId_9(capfd):
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
async def testPointMemberDefault_delAssistId_10(capfd):
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
async def testPointMemberDefault_delAssistId_11(capfd):
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
async def testPointMemberDefault_delAssistId_12(capfd):
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
async def testPointMemberDefault_delEventId_1(capfd):
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
async def testPointMemberDefault_delEventId_2(capfd):
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
async def testPointMemberDefault_delEventId_3(capfd):
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
async def testPointMemberDefault_delMemberId(capfd):
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
async def testPointMemberDefault_delRangeId(capfd):
    command = f"$delRange:id [{testData['idrange']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delRange:id", app.deleteData,
                       Helpers.delStruct("range", "id"))
    out, _ = capfd.readouterr()
    assert "El ___rango___ ha sido eliminado con exito.\n" in out

'''
@pytest.mark.asyncio
async def testMemberDefault_addMember(capfd):
    command = f"$addMember [{testData['namecreate']}, "\
              f"{testData['rancreate']}, {testData['datecreate']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addMember", app.setData,
                       Helpers.setStruct("member"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["id"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "El ___integrante___ ha sido creado con exito sobre el "\
          f"**_ID_** \'{testData['id']}\'.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_addMember_exist(capfd):
    commands = [f"$addMember[{testData['namecreate']},"\
                f"{testData['rancreate']},"\
                f"{testData['datecreate']}]",
                f"$addMember [{testData['namecreate']}, "\
                f"{testData['rancreate']}, "\
                f"{testData['datecreate']}]",
                f"$addMember [ {testData['namecreate']} , "\
                f" {testData['rancreate']} , "\
                f" {testData['datecreate']} ]",
                f"$addMember [ {testData['namecreate']} , "\
                f" {testData['rancreate']} , "\
                f" {testData['datecreate']} ]FILL",
                f"$addMember [ {testData['namecreate']} , "\
                f" {testData['rancreate']} , "\
                f" {testData['datecreate']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addMember", app.setData,
                           Helpers.setStruct("member"))
        out, _ = capfd.readouterr()
        assert f"El ___integrante___ de **_Nombre_** "\
               f"\'{testData['namecreate']}\' "\
                "ya se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberId_add(capfd):
    command = f"$listMember:id [{testData['id']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.dFMsg("listMember:id", app.getDatas,
                     Helpers.getStruct("member", ["id"]))
    out, _ = capfd.readouterr()
    assert "**___Integrantes___** **___encontrados:___**\n" in out
    assert f"{testData['id']}" in out
    assert f"{testData['namecreate']}" in out
    assert f"{testData['rancreate']}" in out
    assert f"{testData['datecreate'].replace('-','/')}" in out
    assert "Ninguno" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberName_add(capfd):
    command = f"$listMember:name [{testData['namecreate']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.dFMsg("listMember:name", app.getDatas,
                     Helpers.getStruct("member", ["name"]))
    out, _ = capfd.readouterr()
    assert "**___Integrantes___** **___encontrados:___**\n" in out
    assert f"{testData['id']}" in out
    assert f"{testData['namecreate']}" in out
    assert f"{testData['rancreate']}" in out
    assert f"{testData['datecreate'].replace('-','/')}" in out
    assert "Ninguno" in out

@pytest.mark.asyncio
async def testMemberDefault_updMemberId(capfd):
    commands = [f"$updMember:id[{testData['id']},{testData['nameupdate']},"\
                f"{testData['rancreate']},{testData['dateupdate']}]",
                f"$updMember:id [{testData['id']}, {testData['nameupdate']}, "\
                f"{testData['rancreate']}, {testData['dateupdate']}]",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['rancreate']} , {testData['dateupdate']} ] ",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['rancreate']} , {testData['dateupdate']} ]FILL",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['rancreate']} , {testData['dateupdate']} ] FILL "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:id", app.updateData,
                           Helpers.updStruct("member", "id"))
        out, _ = capfd.readouterr()
        assert "El ___integrante___ ha sido actualizado con exito.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_updMemberId_nameExist(capfd):
    commands = [f"$updMember:id[{testData['id']},{testData['nameexist']},"\
                f"{testData['rancreate']},{testData['dateupdate']}]",
                f"$updMember:id [{testData['id']}, {testData['nameexist']}, "\
                f"{testData['rancreate']}, {testData['dateupdate']}]",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameexist']} , "\
                f"{testData['rancreate']} , {testData['dateupdate']} ] ",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameexist']} , "\
                f"{testData['rancreate']} , {testData['dateupdate']} ]FILL",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameexist']} , "\
                f"{testData['rancreate']} , {testData['dateupdate']} ] FILL "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:id", app.updateData,
                           Helpers.updStruct("member", "id"))
        out, _ = capfd.readouterr()
        assert f"El ___integrante___ de **_Nombre_** "\
               f"\'{testData['nameexist']}\' "\
                "ya se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_updMemberName(capfd):
    commands = [f"$updMember:name[{testData['nameupdate']},"\
                f"{testData['ranupdate']},{testData['dateupdate']}]",
                f"$updMember:name [{testData['nameupdate']}, "\
                f"{testData['ranupdate']}, {testData['dateupdate']}]",
                f"$updMember:name [ {testData['nameupdate']} , "\
                f"{testData['ranupdate']} , {testData['dateupdate']} ] ",
                f"$updMember:name [ {testData['nameupdate']} , "\
                f"{testData['ranupdate']} , {testData['dateupdate']} ]FILL",
                f"$updMember:name [ {testData['nameupdate']} , "\
                f"{testData['ranupdate']} , {testData['dateupdate']} ] FILL "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:name", app.updateData,
                           Helpers.updStruct("member", "name"))
        out, _ = capfd.readouterr()
        assert "El ___integrante___ ha sido actualizado con exito.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_listMember(capfd):
    commands = [f"$listMember",
                f"$listMember ",
                f"$listMemberFILL",
                f"$listMember FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember", app.getDatas,
                         Helpers.getStruct("member"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['id']}" in out
        assert f"{testData['nameupdate']}" in out
        assert f"{testData['ranupdate']}" in out
        assert f"{testData['datecreate'].replace('-','/')}" in out
        assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberId(capfd):
    commands = [f"$listMember:id[{testData['id']}]",
                f"$listMember:id [{testData['id']}]",
                f"$listMember:id [ {testData['id']} ] ",
                f"$listMember:id [ {testData['id']} ]FILL",
                f"$listMember:id [ {testData['id']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:id", app.getDatas,
                         Helpers.getStruct("member", ["id"]))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['id']}" in out
        assert f"{testData['nameupdate']}" in out
        assert f"{testData['ranupdate']}" in out
        assert f"{testData['datecreate'].replace('-','/')}" in out
        assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberName(capfd):
    commands = [f"$listMember:name[{testData['nameupdate']}]",
                f"$listMember:name [{testData['nameupdate']}]",
                f"$listMember:name [ {testData['nameupdate']} ] ",
                f"$listMember:name [ {testData['nameupdate']} ]FILL",
                f"$listMember:name [ {testData['nameupdate']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:name", app.getDatas,
                         Helpers.getStruct("member", ["name"]))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['id']}" in out
        assert f"{testData['nameupdate']}" in out
        assert f"{testData['ranupdate']}" in out
        assert f"{testData['datecreate'].replace('-','/')}" in out
        assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberRange(capfd):
    commands = [f"$listMember:range[{testData['ranupdate']}]",
                f"$listMember:range [{testData['ranupdate']}]",
                f"$listMember:range [ {testData['ranupdate']} ] ",
                f"$listMember:range [ {testData['ranupdate']} ]FILL",
                f"$listMember:range [ {testData['ranupdate']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:range", app.getDatas,
                         Helpers.getStruct("member", ["range"]))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['id']}" in out
        assert f"{testData['nameupdate']}" in out
        assert f"{testData['ranupdate']}" in out
        assert f"{testData['datecreate'].replace('-','/')}" in out
        assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberDate(capfd):
    commands = [f"$listMember:date[{testData['datecreate']},"\
                f"{testData['datecreate']}]",
                f"$listMember:date [{testData['datecreate']}, "\
                f"{testData['datecreate']}]",
                f"$listMember:date [ {testData['datecreate']} , "\
                f"{testData['datecreate']} ] ",
                f"$listMember:date [ {testData['datecreate']} , "\
                f"{testData['datecreate']} ]FILL",
                f"$listMember:date [ {testData['datecreate']} , "\
                f"{testData['datecreate']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:date", app.getDatas,
                         Helpers.getStruct("member", ["date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**\n" in out
        assert f"{testData['id']}" in out
        assert f"{testData['nameupdate']}" in out
        assert f"{testData['ranupdate']}" in out
        assert f"{testData['datecreate'].replace('-','/')}" in out
        assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def testMemberDefault_listMember_e(capfd):
    commands = [f"$listMember"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember", app.getDatas,
                             Helpers.getStruct("member"))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberId_e(capfd):
    commands = [f"$listMember:id[{testData['id']}]",
                f"$listMember:id [{testData['id']}]",
                f"$listMember:id [ {testData['id']} ]"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember:id", app.getDatas,
                             Helpers.getStruct("member", ["id"]))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberName_e(capfd):
    commands = [f"$listMember:name[{testData['nameupdate']}]",
                f"$listMember:name [{testData['nameupdate']}]",
                f"$listMember:name [ {testData['nameupdate']} ]"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember:name", app.getDatas,
                             Helpers.getStruct("member", ["name"]))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberRange_e(capfd):
    commands = [f"$listMember:range[{testData['ranupdate']}]",
                f"$listMember:range [{testData['ranupdate']}]",
                f"$listMember:range [ {testData['ranupdate']} ]"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember:range", app.getDatas,
                             Helpers.getStruct("member", ["range"]))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberDate_e(capfd):
    commands = [f"$listMember:date[{testData['datecreate']},"\
                f"{testData['datecreate']}]",
                f"$listMember:date [{testData['datecreate']}, "\
                f"{testData['datecreate']}]",
                f"$listMember:date [ {testData['datecreate']} , "\
                f"{testData['datecreate']} ]"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember:date", app.getDatas,
                             Helpers.getStruct("member",
                             ["date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testMemberDefault_listMember_eIncomplete(capfd):
    commands = [f"$listMember"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember", app.getDatas,
                             Helpers.getStruct("member"))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert "**$listMember** **> e**\n" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberId_eIncomplete(capfd):
    commands = [f"$listMember:id[{testData['id']}]",
                f"$listMember:id [{testData['id']}]",
                f"$listMember:id [ {testData['id']} ]"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember:id", app.getDatas,
                             Helpers.getStruct("member", ["id"]))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert f"**$listMember:id** **[**{testData['id']}**]** "\
                    "**> e**\n" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberName_eIncomplete(capfd):
    commands = [f"$listMember:name[{testData['nameupdate']}]",
                f"$listMember:name [{testData['nameupdate']}]",
                f"$listMember:name [ {testData['nameupdate']} ]"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember:name", app.getDatas,
                             Helpers.getStruct("member", ["name"]))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert f"**$listMember:name** **[**{testData['nameupdate']}**]** "\
                    "**> e**\n" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberRange_eIncomplete(capfd):
    commands = [f"$listMember:range[{testData['ranupdate']}]",
                f"$listMember:range [{testData['ranupdate']}]",
                f"$listMember:range [ {testData['ranupdate']} ]"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember:range", app.getDatas,
                             Helpers.getStruct("member", ["range"]))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert f"**$listMember:range** **[**{testData['ranupdate']}**]** "\
                    "**> e**\n" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberDate_eIncomplete(capfd):
    commands = [f"$listMember:date[{testData['datecreate']},"\
                f"{testData['datecreate']}]",
                f"$listMember:date [{testData['datecreate']}, "\
                f"{testData['datecreate']}]",
                f"$listMember:date [ {testData['datecreate']} , "\
                f"{testData['datecreate']} ]"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember:date", app.getDatas,
                             Helpers.getStruct("member",
                             ["date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert "**$listMember:date** "\
                   "**[**" + \
                   testData['datecreate'] + ", " + \
                   testData['datecreate'] + \
                   "**]** "\
                   "**> e**\n" in out

@pytest.mark.asyncio
async def testMemberDefault_delMemberId(capfd):
    command = f"$delMember:id [{testData['id']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delMember:id", app.deleteData,
                       Helpers.delStruct("member", "id"))
    out, _ = capfd.readouterr()
    assert "El ___integrante___ ha sido eliminado con exito.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_addMember_delName(capfd):
    command = f"$addMember [{testData['namecreate']}, "\
              f"{testData['rancreate']}, {testData['datecreate']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addMember", app.setData,
                       Helpers.setStruct("member"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["id"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "El ___integrante___ ha sido creado con exito sobre el "\
          f"**_ID_** \'{testData['id']}\'.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_delMemberName(capfd):
    command = f"$delMember:name [{testData['namecreate']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delMember:name", app.deleteData,
                       Helpers.delStruct("member", "name"))
    out, _ = capfd.readouterr()
    assert "El ___integrante___ ha sido eliminado con exito.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_addMember_rangeNoExist(capfd):
    command = f"$addMember [{testData['namecreate']}, "\
              f"{testData['ranoexist']}, {testData['datecreate']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addMember", app.setData,
                       Helpers.setStruct("member"))
    out, _ = capfd.readouterr()
    assert f"El valor '{testData['ranoexist']}' "\
            "ingresado en el campo "\
            "**_Rango_** no fue encontrado en la "\
            "base de datos.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_updMemberId_idNoExist(capfd):
    commands = [f"$updMember:id[{testData['id']},{testData['nameupdate']},"\
                f"{testData['rancreate']},{testData['dateupdate']}]",
                f"$updMember:id [{testData['id']}, {testData['nameupdate']}, "\
                f"{testData['rancreate']}, {testData['dateupdate']}]",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['rancreate']} , {testData['dateupdate']} ] ",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['rancreate']} , {testData['dateupdate']} ]FILL",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['rancreate']} , {testData['dateupdate']} ] FILL "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:id", app.updateData,
                           Helpers.updStruct("member", "id"))
        out, _ = capfd.readouterr()
        assert f"El ___integrante___ de **_ID_** '{testData['id']}' "\
                "no se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_updMemberId_rangeNoExist(capfd):
    commands = [f"$updMember:id[{testData['id']},{testData['nameupdate']},"\
                f"{testData['ranoexist']},{testData['dateupdate']}]",
                f"$updMember:id [{testData['id']}, {testData['nameupdate']}, "\
                f"{testData['ranoexist']}, {testData['dateupdate']}]",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['ranoexist']} , {testData['dateupdate']} ] ",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['ranoexist']} , {testData['dateupdate']} ]FILL",
                f"$updMember:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['ranoexist']} , {testData['dateupdate']} ] FILL "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:id", app.updateData,
                           Helpers.updStruct("member", "id"))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['ranoexist']}' "\
                "ingresado en el campo "\
                "**_Rango_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_updMemberName_nameNoExist(capfd):
    commands = [f"$updMember:name[{testData['nameupdate']},"\
                f"{testData['ranupdate']},{testData['dateupdate']}]",
                f"$updMember:name [{testData['nameupdate']}, "\
                f"{testData['ranupdate']}, {testData['dateupdate']}]",
                f"$updMember:name [ {testData['nameupdate']} , "\
                f"{testData['ranupdate']} , {testData['dateupdate']} ] ",
                f"$updMember:name [ {testData['nameupdate']} , "\
                f"{testData['ranupdate']} , {testData['dateupdate']} ]FILL",
                f"$updMember:name [ {testData['nameupdate']} , "\
                f"{testData['ranupdate']} , {testData['dateupdate']} ] FILL "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:name", app.updateData,
                           Helpers.updStruct("member", "name"))
        out, _ = capfd.readouterr()
        assert f"El ___integrante___ de **_Nombre_** "\
               f"'{testData['nameupdate']}' "\
                "no se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_updMemberName_rangeNoExist(capfd):
    commands = [f"$updMember:name[{testData['nameupdate']},"\
                f"{testData['ranoexist']},{testData['dateupdate']}]",
                f"$updMember:name [{testData['nameupdate']}, "\
                f"{testData['ranoexist']}, {testData['dateupdate']}]",
                f"$updMember:name [ {testData['nameupdate']} , "\
                f"{testData['ranoexist']} , {testData['dateupdate']} ] ",
                f"$updMember:name [ {testData['nameupdate']} , "\
                f"{testData['ranoexist']} , {testData['dateupdate']} ]FILL",
                f"$updMember:name [ {testData['nameupdate']} , "\
                f"{testData['ranoexist']} , {testData['dateupdate']} ] FILL "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:name", app.updateData,
                           Helpers.updStruct("member", "name"))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['ranoexist']}' "\
                "ingresado en el campo "\
                "**_Rango_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_delMemberId_idNoExist(capfd):
    commands = [f"$delMember:id[{testData['id']}]",
                f"$delMember:id [{testData['id']}]",
                f"$delMember:id [ {testData['id']} ]",
                f"$delMember:id [ {testData['id']} ]FILL",
                f"$delMember:id [ {testData['id']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delMember:id", app.deleteData,
                           Helpers.delStruct("member", "id"))
        out, _ = capfd.readouterr()
        assert f"El ___integrante___ de **_ID_** '{testData['id']}' "\
                "no se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_delMemberName_nameNoExist(capfd):
    commands = [f"$delMember:name[{testData['namecreate']}]",
                f"$delMember:name [{testData['namecreate']}]",
                f"$delMember:name [ {testData['namecreate']} ]",
                f"$delMember:name [ {testData['namecreate']} ]FILL",
                f"$delMember:name [ {testData['namecreate']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delMember:name", app.deleteData,
                           Helpers.delStruct("member", "name"))
        out, _ = capfd.readouterr()
        assert f"El ___integrante___ de **_Nombre_** "\
               f"'{testData['namecreate']}' "\
                "no se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberId_idNoExist(capfd):
    commands = [f"$listMember:id[{testData['id']}]",
                f"$listMember:id [{testData['id']}]",
                f"$listMember:id [ {testData['id']} ] ",
                f"$listMember:id [ {testData['id']} ]FILL",
                f"$listMember:id [ {testData['id']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:id", app.getDatas,
                         Helpers.getStruct("member", ["id"]))
        out, _ = capfd.readouterr()
        assert "No se encontraron ___integrantes___ "\
               "para la consulta realizada.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberName_nameNoExist(capfd):
    commands = [f"$listMember:name[{testData['nameupdate']}]",
                f"$listMember:name [{testData['nameupdate']}]",
                f"$listMember:name [ {testData['nameupdate']} ] ",
                f"$listMember:name [ {testData['nameupdate']} ]FILL",
                f"$listMember:name [ {testData['nameupdate']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:name", app.getDatas,
                         Helpers.getStruct("member", ["name"]))
        out, _ = capfd.readouterr()
        assert "No se encontraron ___integrantes___ "\
               "para la consulta realizada.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberRange_rangeNoExist(capfd):
    commands = [f"$listMember:range[{testData['ranoexist']}]",
                f"$listMember:range [{testData['ranoexist']}]",
                f"$listMember:range [ {testData['ranoexist']} ] ",
                f"$listMember:range [ {testData['ranoexist']} ]FILL",
                f"$listMember:range [ {testData['ranoexist']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:range", app.getDatas,
                         Helpers.getStruct("member", ["range"]))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['ranoexist']}' "\
                "ingresado en el campo "\
                "**_Rango_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testMemberDefault_listMemberDate_dateNoExist(capfd):
    commands = [f"$listMember:date[{testData['datecreate']},"\
                f"{testData['datecreate']}]",
                f"$listMember:date [{testData['datecreate']}, "\
                f"{testData['datecreate']}]",
                f"$listMember:date [ {testData['datecreate']} , "\
                f"{testData['datecreate']} ] ",
                f"$listMember:date [ {testData['datecreate']} , "\
                f"{testData['datecreate']} ]FILL",
                f"$listMember:date [ {testData['datecreate']} , "\
                f"{testData['datecreate']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:date", app.getDatas,
                         Helpers.getStruct("member", ["date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No se encontraron ___integrantes___ "\
               "para la consulta realizada.\n" in out

'''