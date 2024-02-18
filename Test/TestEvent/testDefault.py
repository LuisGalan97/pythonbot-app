import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Certs.certificates import Certificates
from Helpers.helpers import Helpers
from collections import namedtuple

testData = {
    "id" : "",
    "namecreate" : "TestEventCreated",
    "nameupdate" : "TestEventUpdated",
    "nameexist" : "avaconpelea",
    "pointcreate" : 5,
    "pointupdate" : 8,
    "descreate" : "Descripción creada",
    "desupdate" : "Descripción modificada"
}

Message = namedtuple('Message', ['author', 'content', 'channel'])
Channel = namedtuple('Channel', ['name'])
Client = namedtuple('Client', ['user'])
name = 'test'
author = "test"
user = "test"
app = AppHandler()
permissions = Certificates()

@pytest.mark.asyncio
async def testEventDefault_addEvent(capfd):
    command = f"$addEvent [{testData['namecreate']}, "\
              f"{testData['pointcreate']}, {testData['descreate']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addEvent", app.setData,
                       Helpers.setStruct("event"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["id"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "El ___evento___ ha sido creado con exito sobre el "\
          f"**_ID_** \'{testData['id']}\'.\n" in out

@pytest.mark.asyncio
async def testEventDefault_addEvent_exist(capfd):
    commands = [f"$addEvent[{testData['namecreate']},"\
                f"{testData['pointcreate']},"\
                f"{testData['descreate']}]",
                f"$addEvent [{testData['namecreate']}, "\
                f"{testData['pointcreate']}, "\
                f"{testData['descreate']}]",
                f"$addEvent [ {testData['namecreate']} , "\
                f" {testData['pointcreate']} , "\
                f" {testData['descreate']}] ",
                f"$addEvent [ {testData['namecreate']} , "\
                f" {testData['pointcreate']} , "\
                f" {testData['descreate']} ]FILL",
                f"$addEvent [ {testData['namecreate']} , "\
                f" {testData['pointcreate']} , "\
                f" {testData['descreate']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addEvent", app.setData,
                           Helpers.setStruct("event"))
        out, _ = capfd.readouterr()
        assert f"El ___evento___ de **_Nombre_** "\
               f"\'{testData['namecreate']}\' "\
                "ya se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def testEventDefault_listEventId_add(capfd):
    command = f"$listEvent:id [{testData['id']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.dFMsg("listEvent:id", app.getDatas,
                     Helpers.getStruct("event", ["id"]))
    out, _ = capfd.readouterr()
    assert "**___Eventos___** **___encontrados:___**\n" in out
    assert f"{testData['id']}" in out
    assert f"{testData['namecreate']}" in out
    assert f"{testData['pointcreate']}" in out
    assert f"{testData['descreate']}" in out

@pytest.mark.asyncio
async def testEventDefault_listEventName_add(capfd):
    command = f"$listEvent:name [{testData['namecreate']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.dFMsg("listEvent:name", app.getDatas,
                     Helpers.getStruct("event", ["name"]))
    out, _ = capfd.readouterr()
    assert "**___Eventos___** **___encontrados:___**\n" in out
    assert f"{testData['id']}" in out
    assert f"{testData['namecreate']}" in out
    assert f"{testData['pointcreate']}" in out
    assert f"{testData['descreate']}" in out

@pytest.mark.asyncio
async def testEventDefault_updEventId(capfd):
    commands = [f"$updEvent:id[{testData['id']},"\
                f"{testData['nameupdate']},"\
                f"{testData['pointupdate']},{testData['descreate']}]",
                f"$updEvent:id [{testData['id']}, {testData['nameupdate']}, "\
                f"{testData['pointupdate']}, {testData['descreate']}]",
                f"$updEvent:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['pointupdate']} , {testData['descreate']} ] ",
                f"$updEvent:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['pointupdate']} , {testData['descreate']} ]FILL",
                f"$updEvent:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['pointupdate']} , {testData['descreate']} ] FILL "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updEvent:id", app.updateData,
                           Helpers.updStruct("event", "id"))
        out, _ = capfd.readouterr()
        assert "El ___evento___ ha sido actualizado con exito.\n" in out

@pytest.mark.asyncio
async def testEventDefault_updEventId_nameExist(capfd):
    commands = [f"$updEvent:id[{testData['id']},"\
                f"{testData['nameexist']},"\
                f"{testData['pointupdate']},{testData['descreate']}]",
                f"$updEvent:id [{testData['id']}, {testData['nameexist']}, "\
                f"{testData['pointupdate']}, {testData['descreate']}]",
                f"$updEvent:id [ {testData['id']} , "\
                f"{testData['nameexist']} , "\
                f"{testData['pointupdate']} , {testData['descreate']} ] ",
                f"$updEvent:id [ {testData['id']} , "\
                f"{testData['nameexist']} , "\
                f"{testData['pointupdate']} , {testData['descreate']} ]FILL",
                f"$updEvent:id [ {testData['id']} , "\
                f"{testData['nameexist']} , "\
                f"{testData['pointupdate']} , {testData['descreate']} ] FILL "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updEvent:id", app.updateData,
                           Helpers.updStruct("event", "id"))
        out, _ = capfd.readouterr()
        assert f"El ___evento___ de **_Nombre_** \'{testData['nameexist']}\' "\
                "ya se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def testEventDefault_updEventName(capfd):
    commands = [f"$updEvent:name[{testData['nameupdate']},"\
                f"{testData['pointupdate']},{testData['desupdate']}]",
                f"$updEvent:name [{testData['nameupdate']}, "\
                f"{testData['pointupdate']}, {testData['desupdate']}]",
                f"$updEvent:name [ {testData['nameupdate']} , "\
                f"{testData['pointupdate']} , {testData['desupdate']} ] ",
                f"$updEvent:name [ {testData['nameupdate']} , "\
                f"{testData['pointupdate']} , {testData['desupdate']} ]FILL",
                f"$updEvent:name [ {testData['nameupdate']} , "\
                f"{testData['pointupdate']} , {testData['desupdate']} ] FILL "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updEvent:name", app.updateData,
                           Helpers.updStruct("event", "name"))
        out, _ = capfd.readouterr()
        assert "El ___evento___ ha sido actualizado con exito.\n" in out

@pytest.mark.asyncio
async def testEventDefault_listEvent(capfd):
    commands = [f"$listEvent",
                f"$listEvent ",
                f"$listEventFILL",
                f"$listEvent FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listEvent", app.getDatas,
                         Helpers.getStruct("event"))
        out, _ = capfd.readouterr()
        assert "**___Eventos___** **___encontrados:___**\n" in out
        assert f"{testData['id']}" in out
        assert f"{testData['nameupdate']}" in out
        assert f"{testData['pointupdate']}" in out
        assert f"{testData['desupdate']}" in out

@pytest.mark.asyncio
async def testEventDefault_listEventId(capfd):
    commands = [f"$listEvent:id[{testData['id']}]",
                f"$listEvent:id [{testData['id']}]",
                f"$listEvent:id [ {testData['id']} ] ",
                f"$listEvent:id [ {testData['id']} ]FILL",
                f"$listEvent:id [ {testData['id']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listEvent:id", app.getDatas,
                         Helpers.getStruct("event", ["id"]))
        out, _ = capfd.readouterr()
        assert "**___Eventos___** **___encontrados:___**\n" in out
        assert f"{testData['id']}" in out
        assert f"{testData['nameupdate']}" in out
        assert f"{testData['pointupdate']}" in out
        assert f"{testData['desupdate']}" in out

@pytest.mark.asyncio
async def testEventDefault_listEventName(capfd):
    commands = [f"$listEvent:name[{testData['nameupdate']}]",
                f"$listEvent:name [{testData['nameupdate']}]",
                f"$listEvent:name [ {testData['nameupdate']} ] ",
                f"$listEvent:name [ {testData['nameupdate']} ]FILL",
                f"$listEvent:name [ {testData['nameupdate']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listEvent:name", app.getDatas,
                         Helpers.getStruct("event", ["name"]))
        out, _ = capfd.readouterr()
        assert "**___Eventos___** **___encontrados:___**\n" in out
        assert f"{testData['id']}" in out
        assert f"{testData['nameupdate']}" in out
        assert f"{testData['pointupdate']}" in out
        assert f"{testData['desupdate']}" in out

@pytest.mark.asyncio
async def testEventDefault_listEvent_e(capfd):
    commands = [f"$listEvent"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listEvent", app.getDatas,
                             Helpers.getStruct("event"))
            out, _ = capfd.readouterr()
            assert "**___Eventos___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testEventDefault_listEventId_e(capfd):
    commands = [f"$listEvent:id[{testData['id']}]",
                f"$listEvent:id [{testData['id']}]",
                f"$listEvent:id [ {testData['id']} ]"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listEvent:id", app.getDatas,
                             Helpers.getStruct("event", ["id"]))
            out, _ = capfd.readouterr()
            assert "**___Eventos___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testEventDefault_listEventName_e(capfd):
    commands = [f"$listEvent:name[{testData['nameupdate']}]",
                f"$listEvent:name [{testData['nameupdate']}]",
                f"$listEvent:name [ {testData['nameupdate']} ]"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listEvent:name", app.getDatas,
                             Helpers.getStruct("event", ["name"]))
            out, _ = capfd.readouterr()
            assert "**___Eventos___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testEventDefault_listEvent_eIncomplete(capfd):
    commands = [f"$listEvent"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listEvent", app.getDatas,
                             Helpers.getStruct("event"))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert "**$listEvent** **> e**\n" in out

@pytest.mark.asyncio
async def testEventDefault_listEventId_eIncomplete(capfd):
    commands = [f"$listEvent:id[{testData['id']}]",
                f"$listEvent:id [{testData['id']}]",
                f"$listEvent:id [ {testData['id']} ]"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listEvent:id", app.getDatas,
                             Helpers.getStruct("event", ["id"]))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert f"**$listEvent:id** **[**{testData['id']}**]** "\
                    "**> e**\n" in out

@pytest.mark.asyncio
async def testEventDefault_listEventName_eIncomplete(capfd):
    commands = [f"$listEvent:name[{testData['nameupdate']}]",
                f"$listEvent:name [{testData['nameupdate']}]",
                f"$listEvent:name [ {testData['nameupdate']} ]"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            channel = Channel(name=name)
            message = Message(author=author, content=f"{command}{eparam}",
                              channel=channel)
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listEvent:name", app.getDatas,
                             Helpers.getStruct("event", ["name"]))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert f"**$listEvent:name** **[**{testData['nameupdate']}**]** "\
                    "**> e**\n" in out

@pytest.mark.asyncio
async def testEventDefault_delEventId(capfd):
    command = f"$delEvent:id [{testData['id']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delEvent:id", app.deleteData,
                       Helpers.delStruct("event", "id"))
    out, _ = capfd.readouterr()
    assert "El ___evento___ ha sido eliminado con exito.\n" in out

@pytest.mark.asyncio
async def testEventDefault_addEvent_delName(capfd):
    command = f"$addEvent [{testData['namecreate']}, "\
              f"{testData['pointcreate']}, {testData['descreate']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addEvent", app.setData,
                       Helpers.setStruct("event"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["id"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "El ___evento___ ha sido creado con exito sobre el "\
          f"**_ID_** \'{testData['id']}\'.\n" in out

@pytest.mark.asyncio
async def testEventDefault_delEventName(capfd):
    command = f"$delEvent:name [{testData['namecreate']}]"
    channel = Channel(name=name)
    message = Message(author=author, content=command, channel=channel)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delEvent:name", app.deleteData,
                       Helpers.delStruct("event", "name"))
    out, _ = capfd.readouterr()
    assert "El ___evento___ ha sido eliminado con exito.\n" in out

@pytest.mark.asyncio
async def testEventDefault_updEventId_idNoExist(capfd):
    commands = [f"$updEvent:id[{testData['id']},"\
                f"{testData['nameupdate']},"\
                f"{testData['pointupdate']},{testData['descreate']}]",
                f"$updEvent:id [{testData['id']}, {testData['nameupdate']}, "\
                f"{testData['pointupdate']}, {testData['descreate']}]",
                f"$updEvent:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['pointupdate']} , {testData['descreate']} ] ",
                f"$updEvent:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['pointupdate']} , {testData['descreate']} ]FILL",
                f"$updEvent:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['pointupdate']} , {testData['descreate']} ] FILL "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updEvent:id", app.updateData,
                           Helpers.updStruct("event", "id"))
        out, _ = capfd.readouterr()
        assert f"El ___evento___ de **_ID_** '{testData['id']}' "\
                "no se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def testEventDefault_updEventName_nameNoExist(capfd):
    commands = [f"$updEvent:name[{testData['nameupdate']},"\
                f"{testData['pointupdate']},{testData['desupdate']}]",
                f"$updEvent:name [{testData['nameupdate']}, "\
                f"{testData['pointupdate']}, {testData['desupdate']}]",
                f"$updEvent:name [ {testData['nameupdate']} , "\
                f"{testData['pointupdate']} , {testData['desupdate']} ] ",
                f"$updEvent:name [ {testData['nameupdate']} , "\
                f"{testData['pointupdate']} , {testData['desupdate']} ]FILL",
                f"$updEvent:name [ {testData['nameupdate']} , "\
                f"{testData['pointupdate']} , {testData['desupdate']} ] FILL "]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updEvent:name", app.updateData,
                           Helpers.updStruct("event", "name"))
        out, _ = capfd.readouterr()
        assert f"El ___evento___ de **_Nombre_** '{testData['nameupdate']}' "\
                "no se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def testEventDefault_delEventId_idNoExist(capfd):
    commands = [f"$delEvent:id[{testData['id']}]",
               f"$delEvent:id [{testData['id']}]",
               f"$delEvent:id [ {testData['id']} ]",
               f"$delEvent:id [ {testData['id']} ]FILL",
               f"$delEvent:id [ {testData['id']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delEvent:id", app.deleteData,
                           Helpers.delStruct("event", "id"))
        out, _ = capfd.readouterr()
        assert f"El ___evento___ de **_ID_** '{testData['id']}' "\
                "no se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def testEventDefault_delEventName_nameNoExist(capfd):
    commands = [f"$delEvent:name[{testData['namecreate']}]",
                f"$delEvent:name [{testData['namecreate']}]",
                f"$delEvent:name [ {testData['namecreate']} ]",
                f"$delEvent:name [ {testData['namecreate']} ]FILL",
                f"$delEvent:name [ {testData['namecreate']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delEvent:name", app.deleteData,
                           Helpers.delStruct("event", "name"))
        out, _ = capfd.readouterr()
        assert f"El ___evento___ de **_Nombre_** '{testData['namecreate']}' "\
                "no se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def testEventDefault_listEventId_idNoExist(capfd):
    commands = [f"$listEvent:id[{testData['id']}]",
                f"$listEvent:id [{testData['id']}]",
                f"$listEvent:id [ {testData['id']} ] ",
                f"$listEvent:id [ {testData['id']} ]FILL",
                f"$listEvent:id [ {testData['id']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listEvent:id", app.getDatas,
                         Helpers.getStruct("event", ["id"]))
        out, _ = capfd.readouterr()
        assert "No se encontraron ___eventos___ "\
               "para la consulta realizada.\n" in out

@pytest.mark.asyncio
async def testEventDefault_listEventName_nameNoExist(capfd):
    commands = [f"$listEvent:name[{testData['nameupdate']}]",
                f"$listEvent:name [{testData['nameupdate']}]",
                f"$listEvent:name [ {testData['nameupdate']} ] ",
                f"$listEvent:name [ {testData['nameupdate']} ]FILL",
                f"$listEvent:name [ {testData['nameupdate']} ] FILL"]
    for command in commands:
        channel = Channel(name=name)
        message = Message(author=author, content=command, channel=channel)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listEvent:name", app.getDatas,
                         Helpers.getStruct("event", ["name"]))
        out, _ = capfd.readouterr()
        assert "No se encontraron ___eventos___ "\
               "para la consulta realizada.\n" in out