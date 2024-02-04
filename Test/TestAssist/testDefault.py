import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Helpers.helpers import Helpers
from collections import namedtuple

testData = {
    "id" : "",
    "memcreate" : "Avalonicus",
    "memupdate" : "Ammy",
    "menoexist" : "Member-[noexist]",
    "evcreate" : "defprismaganada",
    "evupdate" : "avaconpelea",
    "evnoexist" : "Event-[noexist]",
    "datecreate" : "25-01-2300",
    "dateupdate" : "26-01-2300"
}

Message = namedtuple('Message', ['author', 'content'])
Client = namedtuple('Client', ['user'])
app = AppHandler()

@pytest.mark.asyncio
async def testDef_addAssist(capfd):
    command = f"$addAssist [{testData['memcreate']}, "\
              f"{testData['evcreate']}, {testData['datecreate']}]"
    message = Message(author="test", content=command)
    client = Client(user="test")
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addAssist", app.setData,
                       Helpers.setStruct("asistencia"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["id"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "La ___asistencia___ ha sido creada con exito sobre el "\
          f"**_ID_** \'{testData['id']}\'.\n" in out

@pytest.mark.asyncio
async def testDef_listAssistId_add(capfd):
    command = f"$listAssist:id [{testData['id']}]"
    message = Message(author="test", content=command)
    client = Client(user="test")
    hdlr = MessageHandler(message, client, True)
    await hdlr.dFMsg("listAssist:id", app.getDatas,
                     Helpers.getStruct("asistencia", ["id"]))
    out, _ = capfd.readouterr()
    assert "**___Asistencias___** **___encontradas:___**\n" in out
    assert f"{testData['id']}" in out
    assert f"{testData['memcreate']}" in out
    assert f"{testData['evcreate']}" in out
    assert f"{testData['datecreate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def testDef_updAssistId(capfd):
    commands = [f"$updAssist:id[{testData['id']},"
                f"{testData['memupdate']},"\
                f"{testData['evupdate']},"
                f"{testData['dateupdate']}]",
                f"$updAssist:id [{testData['id']}, "
                f"{testData['memupdate']}, "\
                f"{testData['evupdate']}, "
                f"{testData['dateupdate']}]",
                f"$updAssist:id [ {testData['id']} , "
                f"{testData['memupdate']} , "\
                f"{testData['evupdate']} , "
                f"{testData['dateupdate']} ] ",
                f"$updAssist:id [ {testData['id']} , "
                f"{testData['memupdate']} , "\
                f"{testData['evupdate']} , "
                f"{testData['dateupdate']} ]FILL",
                f"$updAssist:id [ {testData['id']} , "
                f"{testData['memupdate']} , "\
                f"{testData['evupdate']} , "
                f"{testData['dateupdate']} ] FILL "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updAssist:id", app.updateData,
                           Helpers.updStruct("asistencia", "id"))
        out, _ = capfd.readouterr()
        assert "La ___asistencia___ ha sido actualizada con exito.\n" in out

@pytest.mark.asyncio
async def testDef_listAssist(capfd):
    commands = [f"$listAssist",
                f"$listAssist ",
                f"$listAssistFILL",
                f"$listAssist FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist", app.getDatas,
                         Helpers.getStruct("asistencia"))
        out, _ = capfd.readouterr()
        assert "**___Asistencias___** **___encontradas:___**\n" in out
        assert f"{testData['id']}" in out
        assert f"{testData['memupdate']}" in out
        assert f"{testData['evupdate']}" in out
        assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def testDef_listAssistId(capfd):
    commands = [f"$listAssist:id[{testData['id']}]",
                f"$listAssist:id [{testData['id']}]",
                f"$listAssist:id [ {testData['id']} ] ",
                f"$listAssist:id [ {testData['id']} ]FILL",
                f"$listAssist:id [ {testData['id']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:id", app.getDatas,
                         Helpers.getStruct("asistencia", ["id"]))
        out, _ = capfd.readouterr()
        assert "**___Asistencias___** **___encontradas:___**\n" in out
        assert f"{testData['id']}" in out
        assert f"{testData['memupdate']}" in out
        assert f"{testData['evupdate']}" in out
        assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def testDef_listAssistMember(capfd):
    commands = [f"$listAssist:member[{testData['memupdate']}]",
                f"$listAssist:member [{testData['memupdate']}]",
                f"$listAssist:member [ {testData['memupdate']} ] ",
                f"$listAssist:member [ {testData['memupdate']} ]FILL",
                f"$listAssist:member [ {testData['memupdate']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member", app.getDatas,
                         Helpers.getStruct("asistencia", ["integrante"]))
        out, _ = capfd.readouterr()
        assert "**___Asistencias___** **___encontradas:___**\n" in out
        assert f"{testData['id']}" in out
        assert f"{testData['memupdate']}" in out
        assert f"{testData['evupdate']}" in out
        assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def testDef_listAssistEvent(capfd):
    commands = [f"$listAssist:event[{testData['evupdate']}]",
                f"$listAssist:event [{testData['evupdate']}]",
                f"$listAssist:event [ {testData['evupdate']} ] ",
                f"$listAssist:event [ {testData['evupdate']} ]FILL",
                f"$listAssist:event [ {testData['evupdate']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:event", app.getDatas,
                         Helpers.getStruct("asistencia", ["evento"]))
        out, _ = capfd.readouterr()
        assert "**___Asistencias___** **___encontradas:___**\n" in out
        assert f"{testData['id']}" in out
        assert f"{testData['memupdate']}" in out
        assert f"{testData['evupdate']}" in out
        assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def testDef_listAssistDate(capfd):
    commands = [f"$listAssist:date[{testData['dateupdate']},"\
                f"{testData['dateupdate']}]",
                f"$listAssist:date [{testData['dateupdate']}, "\
                f"{testData['dateupdate']}]",
                f"$listAssist:date [ {testData['dateupdate']} , "\
                f"{testData['dateupdate']} ] ",
                f"$listAssist:date [ {testData['dateupdate']} , "\
                f"{testData['dateupdate']} ]FILL",
                f"$listAssist:date [ {testData['dateupdate']} , "\
                f"{testData['dateupdate']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:date", app.getDatas,
                         Helpers.getStruct("asistencia", ["date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "**___Asistencias___** **___encontradas:___**\n" in out
        assert f"{testData['id']}" in out
        assert f"{testData['memupdate']}" in out
        assert f"{testData['evupdate']}" in out
        assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def testDef_listAssistMemberEvent(capfd):
    commands = [f"$listAssist:member&event[{testData['memupdate']},"\
                f"{testData['evupdate']}]",
                f"$listAssist:member&event [{testData['memupdate']}, "\
                f"{testData['evupdate']}]",
                f"$listAssist:member&event [ {testData['memupdate']} , "\
                f"{testData['evupdate']} ] ",
                f"$listAssist:member&event [ {testData['memupdate']} , "\
                f"{testData['evupdate']} ]FILL",
                f"$listAssist:member&event [ {testData['memupdate']} , "\
                f"{testData['evupdate']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "evento"]))
        out, _ = capfd.readouterr()
        assert "**___Asistencias___** **___encontradas:___**\n" in out
        assert f"{testData['id']}" in out
        assert f"{testData['memupdate']}" in out
        assert f"{testData['evupdate']}" in out
        assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def testDef_listAssistMemberDate(capfd):
    commands = [f"$listAssist:member&date[{testData['memupdate']},"\
                f"{testData['dateupdate']},{testData['dateupdate']}]",
                f"$listAssist:member&date [{testData['memupdate']}, "\
                f"{testData['dateupdate']}, {testData['dateupdate']}]",
                f"$listAssist:member&date [ {testData['memupdate']} , "\
                f"{testData['dateupdate']} , {testData['dateupdate']} ] ",
                f"$listAssist:member&date [ {testData['memupdate']} , "\
                f"{testData['dateupdate']} , {testData['dateupdate']} ]FILL",
                f"$listAssist:member&date [ {testData['memupdate']} , "\
                f"{testData['dateupdate']} , {testData['dateupdate']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "**___Asistencias___** **___encontradas:___**\n" in out
        assert f"{testData['id']}" in out
        assert f"{testData['memupdate']}" in out
        assert f"{testData['evupdate']}" in out
        assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def testDef_listAssistEventDate(capfd):
    commands = [f"$listAssist:event&date[{testData['evupdate']},"\
                f"{testData['dateupdate']},{testData['dateupdate']}]",
                f"$listAssist:event&date [{testData['evupdate']}, "\
                f"{testData['dateupdate']}, {testData['dateupdate']}]",
                f"$listAssist:event&date [ {testData['evupdate']} , "\
                f"{testData['dateupdate']} , {testData['dateupdate']} ] ",
                f"$listAssist:event&date [ {testData['evupdate']} , "\
                f"{testData['dateupdate']} , {testData['dateupdate']} ]FILL",
                f"$listAssist:event&date [ {testData['evupdate']} , "\
                f"{testData['dateupdate']} , {testData['dateupdate']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["evento", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "**___Asistencias___** **___encontradas:___**\n" in out
        assert f"{testData['id']}" in out
        assert f"{testData['memupdate']}" in out
        assert f"{testData['evupdate']}" in out
        assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def testDef_listAssistMemberEventDate(capfd):
    commands = [f"$listAssist:member&event&date[{testData['memupdate']},"\
                f"{testData['evupdate']},{testData['dateupdate']},"\
                f"{testData['dateupdate']}]",
                f"$listAssist:member&event&date [{testData['memupdate']}, "\
                f"{testData['evupdate']}, {testData['dateupdate']}, "\
                f"{testData['dateupdate']} ]",
                f"$listAssist:member&event&date [ {testData['memupdate']} , "\
                f"{testData['evupdate']} , {testData['dateupdate']} , "\
                f"{testData['dateupdate']} ] ",
                f"$listAssist:member&event&date [ {testData['memupdate']} , "\
                f"{testData['evupdate']} , {testData['dateupdate']} , "\
                f"{testData['dateupdate']} ]FILL",
                f"$listAssist:member&event&date [ {testData['memupdate']} , "\
                f"{testData['evupdate']} , {testData['dateupdate']} , "\
                f"{testData['dateupdate']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event&date",
                         app.getDatas, Helpers.getStruct("asistencia",
                         ["integrante", "evento", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "**___Asistencias___** **___encontradas:___**\n" in out
        assert f"{testData['id']}" in out
        assert f"{testData['memupdate']}" in out
        assert f"{testData['evupdate']}" in out
        assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def testDef_listAssist_e(capfd):
    commands = [f"$listAssist"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist", app.getDatas,
                             Helpers.getStruct("asistencia"))
            out, _ = capfd.readouterr()
            assert "**___Asistencias___** **___encontradas:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testDef_listAssistId_e(capfd):
    commands = [f"$listAssist:id[{testData['id']}]",
                f"$listAssist:id [{testData['id']}]",
                f"$listAssist:id [ {testData['id']} ]"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:id", app.getDatas,
                             Helpers.getStruct("asistencia", ["id"]))
            out, _ = capfd.readouterr()
            assert "**___Asistencias___** **___encontradas:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testDef_listAssistMember_e(capfd):
    commands = [f"$listAssist:member[{testData['memupdate']}]",
                f"$listAssist:member [{testData['memupdate']}]",
                f"$listAssist:member [ {testData['memupdate']} ]"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member", app.getDatas,
                             Helpers.getStruct("asistencia", ["integrante"]))
            out, _ = capfd.readouterr()
            assert "**___Asistencias___** **___encontradas:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testDef_listAssistEvent_e(capfd):
    commands = [f"$listAssist:event[{testData['evupdate']}]",
                f"$listAssist:event [{testData['evupdate']}]",
                f"$listAssist:event [ {testData['evupdate']} ]"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:event", app.getDatas,
                             Helpers.getStruct("asistencia", ["evento"]))
            out, _ = capfd.readouterr()
            assert "**___Asistencias___** **___encontradas:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testDef_listAssistDate_e(capfd):
    commands = [f"$listAssist:date[{testData['dateupdate']},"\
                f"{testData['dateupdate']}]",
                f"$listAssist:date [{testData['dateupdate']}, "\
                f"{testData['dateupdate']}]",
                f"$listAssist:date [ {testData['dateupdate']} , "\
                f"{testData['dateupdate']} ]"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:date", app.getDatas,
                             Helpers.getStruct("asistencia",
                             ["date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert "**___Asistencias___** **___encontradas:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testDef_listAssistMemberDate_e(capfd):
    commands = [f"$listAssist:member&date[{testData['memupdate']},"\
                f"{testData['dateupdate']},{testData['dateupdate']}]",
                f"$listAssist:member&date [{testData['memupdate']}, "\
                f"{testData['dateupdate']}, {testData['dateupdate']}]",
                f"$listAssist:member&date [ {testData['memupdate']} , "\
                f"{testData['dateupdate']} , {testData['dateupdate']} ]"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                             Helpers.getStruct("asistencia",
                             ["integrante", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert "**___Asistencias___** **___encontradas:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testDef_listAssistEventDate_e(capfd):
    commands = [f"$listAssist:event&date[{testData['evupdate']},"\
                f"{testData['dateupdate']},{testData['dateupdate']}]",
                f"$listAssist:event&date [{testData['evupdate']}, "\
                f"{testData['dateupdate']}, {testData['dateupdate']}]",
                f"$listAssist:event&date [ {testData['evupdate']} , "\
                f"{testData['dateupdate']} , {testData['dateupdate']} ]"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                             Helpers.getStruct("asistencia",
                             ["evento", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert "**___Asistencias___** **___encontradas:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testDef_listAssistMemberEventDate_e(capfd):
    commands = [f"$listAssist:member&event&date[{testData['memupdate']},"\
                f"{testData['evupdate']},{testData['dateupdate']},"\
                f"{testData['dateupdate']}]",
                f"$listAssist:member&event&date [{testData['memupdate']}, "\
                f"{testData['evupdate']}, {testData['dateupdate']}, "\
                f"{testData['dateupdate']} ]",
                f"$listAssist:member&event&date [ {testData['memupdate']} , "\
                f"{testData['evupdate']} , {testData['dateupdate']} , "\
                f"{testData['dateupdate']} ]"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&event&date",
                             app.getDatas, Helpers.getStruct("asistencia",
                             ["integrante", "evento", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert "**___Asistencias___** **___encontradas:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testDef_listAssist_e_incomplete(capfd):
    commands = [f"$listAssist"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist", app.getDatas,
                             Helpers.getStruct("asistencia"))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert "**$listAssist** **> e**\n" in out

@pytest.mark.asyncio
async def testDef_listAssistId_e_incomplete(capfd):
    commands = [f"$listAssist:id[{testData['id']}]",
                f"$listAssist:id [{testData['id']}]",
                f"$listAssist:id [ {testData['id']} ]"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:id", app.getDatas,
                             Helpers.getStruct("asistencia", ["id"]))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert f"**$listAssist:id** **[**{testData['id']}**]** "\
                    "**> e**\n" in out

@pytest.mark.asyncio
async def testDef_listAssistMember_e_incomplete(capfd):
    commands = [f"$listAssist:member[{testData['memupdate']}]",
                f"$listAssist:member [{testData['memupdate']}]",
                f"$listAssist:member [ {testData['memupdate']} ]"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member", app.getDatas,
                             Helpers.getStruct("asistencia", ["integrante"]))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert f"**$listAssist:member** "\
                   f"**[**{testData['memupdate']}**]** "\
                    "**> e**\n" in out

@pytest.mark.asyncio
async def testDef_listAssistEvent_e_incomplete(capfd):
    commands = [f"$listAssist:event[{testData['evupdate']}]",
                f"$listAssist:event [{testData['evupdate']}]",
                f"$listAssist:event [ {testData['evupdate']} ]"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:event", app.getDatas,
                             Helpers.getStruct("asistencia", ["evento"]))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert f"**$listAssist:event** "\
                   f"**[**{testData['evupdate']}**]** "\
                    "**> e**\n" in out

@pytest.mark.asyncio
async def testDef_listAssistDate_e_incomplete(capfd):
    commands = [f"$listAssist:date[{testData['dateupdate']},"\
                f"{testData['dateupdate']}]",
                f"$listAssist:date [{testData['dateupdate']}, "\
                f"{testData['dateupdate']}]",
                f"$listAssist:date [ {testData['dateupdate']} , "\
                f"{testData['dateupdate']} ]"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:date", app.getDatas,
                             Helpers.getStruct("asistencia",
                             ["date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert "**$listAssist:date** "\
                   "**[**" + \
                   testData['dateupdate'] + ", " + \
                   testData['dateupdate'] + \
                   "**]** "\
                   "**> e**\n" in out

@pytest.mark.asyncio
async def testDef_listAssistMemberDate_e_incomplete(capfd):
    commands = [f"$listAssist:member&date[{testData['memupdate']},"\
                f"{testData['dateupdate']},{testData['dateupdate']}]",
                f"$listAssist:member&date [{testData['memupdate']}, "\
                f"{testData['dateupdate']}, {testData['dateupdate']}]",
                f"$listAssist:member&date [ {testData['memupdate']} , "\
                f"{testData['dateupdate']} , {testData['dateupdate']} ]"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                             Helpers.getStruct("asistencia",
                             ["integrante", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert "**$listAssist:member&date** "\
                   "**[**" + \
                   testData['memupdate'] + ", " + \
                   testData['dateupdate'] + ", " + \
                   testData['dateupdate'] + \
                   "**]** "\
                   "**> e**\n" in out

@pytest.mark.asyncio
async def testDef_listAssistEventDate_e_incomplete(capfd):
    commands = [f"$listAssist:event&date[{testData['evupdate']},"\
                f"{testData['dateupdate']},{testData['dateupdate']}]",
                f"$listAssist:event&date [{testData['evupdate']}, "\
                f"{testData['dateupdate']}, {testData['dateupdate']}]",
                f"$listAssist:event&date [ {testData['evupdate']} , "\
                f"{testData['dateupdate']} , {testData['dateupdate']} ]"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                             Helpers.getStruct("asistencia",
                             ["evento", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert "**$listAssist:event&date** "\
                   "**[**" + \
                   testData['evupdate'] + ", " + \
                   testData['dateupdate'] + ", " + \
                   testData['dateupdate'] + \
                   "**]** "\
                   "**> e**\n" in out

@pytest.mark.asyncio
async def testDef_listAssistMemberEventDate_e_incomplete(capfd):
    commands = [f"$listAssist:member&event&date[{testData['memupdate']},"\
                f"{testData['evupdate']},{testData['dateupdate']},"\
                f"{testData['dateupdate']}]",
                f"$listAssist:member&event&date [{testData['memupdate']}, "\
                f"{testData['evupdate']}, {testData['dateupdate']}, "\
                f"{testData['dateupdate']} ]",
                f"$listAssist:member&event&date [ {testData['memupdate']} , "\
                f"{testData['evupdate']} , {testData['dateupdate']} , "\
                f"{testData['dateupdate']} ]"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listAssist:member&event&date",
                             app.getDatas, Helpers.getStruct("asistencia",
                             ["integrante", "evento", "date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert "**$listAssist:member&event&date** "\
                   "**[**" + \
                   testData['memupdate'] + ", " + \
                   testData['evupdate'] + ", " + \
                   testData['dateupdate'] + ", " + \
                   testData['dateupdate'] + \
                   "**]** "\
                   "**> e**\n" in out

@pytest.mark.asyncio
async def testDef_delAssistId(capfd):
    command = f"$delAssist:id [{testData['id']}]"
    message = Message(author="test", content=command)
    client = Client(user="test")
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delAssist:id", app.deleteData,
                       Helpers.delStruct("asistencia", "id"))
    out, _ = capfd.readouterr()
    assert "La ___asistencia___ ha sido eliminada con exito.\n" in out

@pytest.mark.asyncio
async def testDef_addAssist_memberNoExist(capfd):
    commands = [f"$addAssist [{testData['menoexist']}, "\
                f"{testData['evcreate']}, "\
                f"{testData['datecreate']}]",
                f"$addAssist [  {testData['menoexist']}  , "\
                f"{testData['evcreate']}, "\
                f"{testData['datecreate']}]",
                f"$addAssist [  {testData['menoexist']}  , "\
                f"{testData['evnoexist']}, "\
                f"{testData['datecreate']}]",
                f"$addAssist [  {testData['menoexist']}  , "\
                f"  {testData['evnoexist']}  , "\
                f"{testData['datecreate']}]",
                f"$addAssist [  {testData['menoexist']}  , "\
                f"  {testData['evnoexist']}  , "\
                f"{testData['datecreate']}] "\
                 "FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addAssist", app.setData,
                           Helpers.setStruct("asistencia"))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['menoexist']}' "\
                "ingresado en el campo "\
                "**_Integrante_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testDef_addAssist_eventNoExist(capfd):
    commands = [f"$addAssist [{testData['memcreate']}, "\
                f"{testData['evnoexist']}, "\
                f"{testData['datecreate']}]",
                f"$addAssist [  {testData['memcreate']}  , "\
                f"{testData['evnoexist']}, "\
                f"{testData['datecreate']}]",
                f"$addAssist [  {testData['memcreate']}  , "\
                f"{testData['evnoexist']}, "\
                f"{testData['datecreate']}]",
                f"$addAssist [  {testData['memcreate']}  , "\
                f"  {testData['evnoexist']}  , "\
                f"{testData['datecreate']}]",
                f"$addAssist [  {testData['memcreate']}  , "\
                f"  {testData['evnoexist']}  , "\
                f"{testData['datecreate']}] "\
                 "FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addAssist", app.setData,
                           Helpers.setStruct("asistencia"))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['evnoexist']}' "\
                "ingresado en el campo "\
                "**_Evento_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testDef_updAssistId_idNoExist(capfd):
    commands = [f"$updAssist:id[{testData['id']},"
                f"{testData['memupdate']},"\
                f"{testData['evupdate']},"
                f"{testData['dateupdate']}]",
                f"$updAssist:id [{testData['id']}, "
                f"{testData['memupdate']}, "\
                f"{testData['evupdate']}, "
                f"{testData['dateupdate']}]",
                f"$updAssist:id [ {testData['id']} , "
                f"{testData['memupdate']} , "\
                f"{testData['evupdate']} , "
                f"{testData['dateupdate']} ] ",
                f"$updAssist:id [ {testData['id']} , "
                f"{testData['memupdate']} , "\
                f"{testData['evupdate']} , "
                f"{testData['dateupdate']} ]FILL",
                f"$updAssist:id [ {testData['id']} , "
                f"{testData['memupdate']} , "\
                f"{testData['evupdate']} , "
                f"{testData['dateupdate']} ] FILL "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updAssist:id", app.updateData,
                           Helpers.updStruct("asistencia", "id"))
        out, _ = capfd.readouterr()
        assert f"La ___asistencia___ de **_ID_** '{testData['id']}' "\
                "no se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def testDef_updAssistId_memberNoExist(capfd):
    commands = [f"$updAssist:id[{testData['id']},"
                f"{testData['menoexist']},"\
                f"{testData['evupdate']},"
                f"{testData['dateupdate']}]",
                f"$updAssist:id [{testData['id']}, "
                f"{testData['menoexist']}, "\
                f"{testData['evupdate']}, "
                f"{testData['dateupdate']}]",
                f"$updAssist:id [ {testData['id']} , "
                f"{testData['menoexist']} , "\
                f"{testData['evnoexist']} , "
                f"{testData['dateupdate']} ] ",
                f"$updAssist:id [ {testData['id']} , "
                f"{testData['menoexist']} , "\
                f"{testData['evnoexist']} , "
                f"{testData['dateupdate']} ]FILL",
                f"$updAssist:id [ {testData['id']} , "
                f"{testData['menoexist']} , "\
                f"{testData['evnoexist']} , "
                f"{testData['dateupdate']} ] FILL "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updAssist:id", app.updateData,
                           Helpers.updStruct("asistencia", "id"))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['menoexist']}' "\
                "ingresado en el campo "\
                "**_Integrante_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testDef_updAssistId_eventNoExist(capfd):
    commands = [f"$updAssist:id[{testData['id']},"
                f"{testData['memupdate']},"\
                f"{testData['evnoexist']},"
                f"{testData['dateupdate']}]",
                f"$updAssist:id [{testData['id']}, "
                f"{testData['memupdate']}, "\
                f"{testData['evnoexist']}, "
                f"{testData['dateupdate']}]",
                f"$updAssist:id [ {testData['id']} , "
                f"{testData['memupdate']} , "\
                f"{testData['evnoexist']} , "
                f"{testData['dateupdate']} ] ",
                f"$updAssist:id [ {testData['id']} , "
                f"{testData['memupdate']} , "\
                f"{testData['evnoexist']} , "
                f"{testData['dateupdate']} ]FILL",
                f"$updAssist:id [ {testData['id']} , "
                f"{testData['memupdate']} , "\
                f"{testData['evnoexist']} , "
                f"{testData['dateupdate']} ] FILL "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updAssist:id", app.updateData,
                           Helpers.updStruct("asistencia", "id"))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['evnoexist']}' "\
                "ingresado en el campo "\
                "**_Evento_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testDef_delAssistId_idNoExist(capfd):
    commands = [f"$delAssist:id[{testData['id']}]",
                f"$delAssist:id [{testData['id']}]",
                f"$delAssist:id [ {testData['id']} ]",
                f"$delAssist:id [ {testData['id']} ]FILL",
                f"$delAssist:id [ {testData['id']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delAssist:id", app.deleteData,
                           Helpers.delStruct("asistencia", "id"))
        out, _ = capfd.readouterr()
        assert f"La ___asistencia___ de **_ID_** '{testData['id']}' "\
                "no se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def testDef_listAssistId_idNoExist(capfd):
    commands = [f"$listAssist:id[{testData['id']}]",
                f"$listAssist:id [{testData['id']}]",
                f"$listAssist:id [ {testData['id']} ] ",
                f"$listAssist:id [ {testData['id']} ]FILL",
                f"$listAssist:id [ {testData['id']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:id", app.getDatas,
                         Helpers.getStruct("asistencia", ["id"]))
        out, _ = capfd.readouterr()
        assert "No se encontraron ___asistencias___ "\
               "para la consulta realizada.\n" in out

@pytest.mark.asyncio
async def testDef_listAssistMember_memberNoExist(capfd):
    commands = [f"$listAssist:member[{testData['menoexist']}]",
                f"$listAssist:member [{testData['menoexist']}]",
                f"$listAssist:member [ {testData['menoexist']} ] ",
                f"$listAssist:member [ {testData['menoexist']} ]FILL",
                f"$listAssist:member [ {testData['menoexist']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member", app.getDatas,
                         Helpers.getStruct("asistencia", ["integrante"]))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['menoexist']}' "\
                "ingresado en el campo "\
                "**_Integrante_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testDef_listAssistEvent_eventNoExist(capfd):
    commands = [f"$listAssist:event[{testData['evnoexist']}]",
                f"$listAssist:event [{testData['evnoexist']}]",
                f"$listAssist:event [ {testData['evnoexist']} ] ",
                f"$listAssist:event [ {testData['evnoexist']} ]FILL",
                f"$listAssist:event [ {testData['evnoexist']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:event", app.getDatas,
                         Helpers.getStruct("asistencia", ["evento"]))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['evnoexist']}' "\
                "ingresado en el campo "\
                "**_Evento_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testDef_listAssistDate_dateNoExist(capfd):
    commands = [f"$listAssist:date[{testData['dateupdate']},"\
                f"{testData['dateupdate']}]",
                f"$listAssist:date [{testData['dateupdate']}, "\
                f"{testData['dateupdate']}]",
                f"$listAssist:date [ {testData['dateupdate']} , "\
                f"{testData['dateupdate']} ] ",
                f"$listAssist:date [ {testData['dateupdate']} , "\
                f"{testData['dateupdate']} ]FILL",
                f"$listAssist:date [ {testData['dateupdate']} , "\
                f"{testData['dateupdate']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:date", app.getDatas,
                         Helpers.getStruct("asistencia", ["date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No se encontraron ___asistencias___ "\
               "para la consulta realizada.\n" in out

@pytest.mark.asyncio
async def testDef_listAssistMemberEvent_memberNoExist(capfd):
    commands = [f"$listAssist:member&event[{testData['menoexist']},"\
                f"{testData['evupdate']}]",
                f"$listAssist:member&event [{testData['menoexist']}, "\
                f"{testData['evupdate']}]",
                f"$listAssist:member&event [ {testData['menoexist']} , "\
                f"{testData['evnoexist']} ] ",
                f"$listAssist:member&event [ {testData['menoexist']} , "\
                f"{testData['evnoexist']} ]FILL",
                f"$listAssist:member&event [ {testData['menoexist']} , "\
                f"{testData['evnoexist']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "evento"]))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['menoexist']}' "\
                "ingresado en el campo "\
                "**_Integrante_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testDef_listAssistMemberEvent_eventNoExist(capfd):
    commands = [f"$listAssist:member&event[{testData['memcreate']},"\
                f"{testData['evnoexist']}]",
                f"$listAssist:member&event [{testData['memcreate']}, "\
                f"{testData['evnoexist']}]",
                f"$listAssist:member&event [ {testData['memcreate']} , "\
                f"{testData['evnoexist']} ] ",
                f"$listAssist:member&event [ {testData['memcreate']} , "\
                f"{testData['evnoexist']} ]FILL",
                f"$listAssist:member&event [ {testData['memcreate']} , "\
                f"{testData['evnoexist']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "evento"]))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['evnoexist']}' "\
                "ingresado en el campo "\
                "**_Evento_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testDef_listAssistMemberDate_memberNoExist(capfd):
    commands = [f"$listAssist:member&date[{testData['menoexist']},"\
                f"{testData['dateupdate']},{testData['dateupdate']}]",
                f"$listAssist:member&date [{testData['menoexist']}, "\
                f"{testData['dateupdate']}, {testData['dateupdate']}]",
                f"$listAssist:member&date [ {testData['menoexist']} , "\
                f"{testData['dateupdate']} , {testData['dateupdate']} ] ",
                f"$listAssist:member&date [ {testData['menoexist']} , "\
                f"{testData['dateupdate']} , {testData['dateupdate']} ]FILL",
                f"$listAssist:member&date [ {testData['menoexist']} , "\
                f"{testData['dateupdate']} , {testData['dateupdate']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['menoexist']}' "\
                "ingresado en el campo "\
                "**_Integrante_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testDef_listAssistMemberDate_dateNoExist(capfd):
    commands = [f"$listAssist:member&date[{testData['memupdate']},"\
                f"{testData['dateupdate']},{testData['dateupdate']}]",
                f"$listAssist:member&date [{testData['memupdate']}, "\
                f"{testData['dateupdate']}, {testData['dateupdate']}]",
                f"$listAssist:member&date [ {testData['memupdate']} , "\
                f"{testData['dateupdate']} , {testData['dateupdate']} ] ",
                f"$listAssist:member&date [ {testData['memupdate']} , "\
                f"{testData['dateupdate']} , {testData['dateupdate']} ]FILL",
                f"$listAssist:member&date [ {testData['memupdate']} , "\
                f"{testData['dateupdate']} , {testData['dateupdate']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No se encontraron ___asistencias___ "\
               "para la consulta realizada.\n" in out

@pytest.mark.asyncio
async def testDef_listAssistEventDate_eventNoExist(capfd):
    commands = [f"$listAssist:event&date[{testData['evnoexist']},"\
                f"{testData['dateupdate']},{testData['dateupdate']}]",
                f"$listAssist:event&date [{testData['evnoexist']}, "\
                f"{testData['dateupdate']}, {testData['dateupdate']}]",
                f"$listAssist:event&date [ {testData['evnoexist']} , "\
                f"{testData['dateupdate']} , {testData['dateupdate']} ] ",
                f"$listAssist:event&date [ {testData['evnoexist']} , "\
                f"{testData['dateupdate']} , {testData['dateupdate']} ]FILL",
                f"$listAssist:event&date [ {testData['evnoexist']} , "\
                f"{testData['dateupdate']} , {testData['dateupdate']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["evento", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['evnoexist']}' "\
                "ingresado en el campo "\
                "**_Evento_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testDef_listAssistEventDate_dateNoExist(capfd):
    commands = [f"$listAssist:event&date[{testData['evupdate']},"\
                f"{testData['dateupdate']},{testData['dateupdate']}]",
                f"$listAssist:event&date [{testData['evupdate']}, "\
                f"{testData['dateupdate']}, {testData['dateupdate']}]",
                f"$listAssist:event&date [ {testData['evupdate']} , "\
                f"{testData['dateupdate']} , {testData['dateupdate']} ] ",
                f"$listAssist:event&date [ {testData['evupdate']} , "\
                f"{testData['dateupdate']} , {testData['dateupdate']} ]FILL",
                f"$listAssist:event&date [ {testData['evupdate']} , "\
                f"{testData['dateupdate']} , {testData['dateupdate']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["evento", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No se encontraron ___asistencias___ "\
               "para la consulta realizada.\n" in out

@pytest.mark.asyncio
async def testDef_listAssistMemberEventDate_memberNoExist(capfd):
    commands = [f"$listAssist:member&event&date[{testData['menoexist']},"\
                f"{testData['evupdate']},{testData['dateupdate']},"\
                f"{testData['dateupdate']}]",
                f"$listAssist:member&event&date [{testData['menoexist']}, "\
                f"{testData['evupdate']}, {testData['dateupdate']}, "\
                f"{testData['dateupdate']} ]",
                f"$listAssist:member&event&date [ {testData['menoexist']} , "\
                f"{testData['evnoexist']} , {testData['dateupdate']} , "\
                f"{testData['dateupdate']} ] ",
                f"$listAssist:member&event&date [ {testData['menoexist']} , "\
                f"{testData['evnoexist']} , {testData['dateupdate']} , "\
                f"{testData['dateupdate']} ]FILL",
                f"$listAssist:member&event&date [ {testData['menoexist']} , "\
                f"{testData['evnoexist']} , {testData['dateupdate']} , "\
                f"{testData['dateupdate']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event&date",
                         app.getDatas, Helpers.getStruct("asistencia",
                         ["integrante", "evento", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['menoexist']}' "\
                "ingresado en el campo "\
                "**_Integrante_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testDef_listAssistMemberEventDate_eventNoExist(capfd):
    commands = [f"$listAssist:member&event&date[{testData['memupdate']},"\
                f"{testData['evnoexist']},{testData['dateupdate']},"\
                f"{testData['dateupdate']}]",
                f"$listAssist:member&event&date [{testData['memupdate']}, "\
                f"{testData['evnoexist']}, {testData['dateupdate']}, "\
                f"{testData['dateupdate']} ]",
                f"$listAssist:member&event&date [ {testData['memupdate']} , "\
                f"{testData['evnoexist']} , {testData['dateupdate']} , "\
                f"{testData['dateupdate']} ] ",
                f"$listAssist:member&event&date [ {testData['memupdate']} , "\
                f"{testData['evnoexist']} , {testData['dateupdate']} , "\
                f"{testData['dateupdate']} ]FILL",
                f"$listAssist:member&event&date [ {testData['memupdate']} , "\
                f"{testData['evnoexist']} , {testData['dateupdate']} , "\
                f"{testData['dateupdate']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event&date",
                         app.getDatas, Helpers.getStruct("asistencia",
                         ["integrante", "evento", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['evnoexist']}' "\
                "ingresado en el campo "\
                "**_Evento_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def testDef_listAssistMemberEventDate_dateNoExist(capfd):
    commands = [f"$listAssist:member&event&date[{testData['memupdate']},"\
                f"{testData['evupdate']},{testData['dateupdate']},"\
                f"{testData['dateupdate']}]",
                f"$listAssist:member&event&date [{testData['memupdate']}, "\
                f"{testData['evupdate']}, {testData['dateupdate']}, "\
                f"{testData['dateupdate']} ]",
                f"$listAssist:member&event&date [ {testData['memupdate']} , "\
                f"{testData['evupdate']} , {testData['dateupdate']} , "\
                f"{testData['dateupdate']} ] ",
                f"$listAssist:member&event&date [ {testData['memupdate']} , "\
                f"{testData['evupdate']} , {testData['dateupdate']} , "\
                f"{testData['dateupdate']} ]FILL",
                f"$listAssist:member&event&date [ {testData['memupdate']} , "\
                f"{testData['evupdate']} , {testData['dateupdate']} , "\
                f"{testData['dateupdate']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event&date",
                         app.getDatas, Helpers.getStruct("asistencia",
                         ["integrante", "evento", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "No se encontraron ___asistencias___ "\
               "para la consulta realizada.\n" in out