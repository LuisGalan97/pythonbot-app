import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
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

Message = namedtuple('Message', ['author', 'content'])
Client = namedtuple('Client', ['user'])
app = AppHandler()

@pytest.mark.asyncio
async def test_addEvent(capfd):
    command = f"$addEvent [{testData['namecreate']}, "\
              f"{testData['pointcreate']}, {testData['descreate']}]"
    message = Message(author="test", content=command)
    client = Client(user="test")
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addEvent", app.setData,
                       Helpers.setStruct("evento"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["id"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "El ___evento___ ha sido creado con exito sobre el " in out
    assert f"**_ID_** \'{testData['id']}\'." in out

@pytest.mark.asyncio
async def test_addEvent_exist(capfd):
    command = f"$addEvent [{testData['namecreate']}, "\
              f"{testData['pointcreate']}, {testData['descreate']}]"
    message = Message(author="test", content=command)
    client = Client(user="test")
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addEvent", app.setData,
                       Helpers.setStruct("evento"))
    out, _ = capfd.readouterr()
    assert f"El ___evento___ de **_Nombre_** \'{testData['namecreate']}\' "\
            "ya se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def test_listEventId_add(capfd):
    command = f"$listEvent:id [{testData['id']}]"
    message = Message(author="test", content=command)
    client = Client(user="test")
    hdlr = MessageHandler(message, client, True)
    await hdlr.dFMsg("listEvent:id", app.getDatas,
                     Helpers.getStruct("evento", ["id"]))
    out, _ = capfd.readouterr()
    assert "**___Eventos___** **___encontrados:___**" in out
    assert f"{testData['id']}" in out
    assert f"{testData['namecreate']}" in out
    assert f"{testData['pointcreate']}" in out
    assert f"{testData['descreate']}" in out

@pytest.mark.asyncio
async def test_listEventName_add(capfd):
    command = f"$listEvent:name [{testData['namecreate']}]"
    message = Message(author="test", content=command)
    client = Client(user="test")
    hdlr = MessageHandler(message, client, True)
    await hdlr.dFMsg("listEvent:name", app.getDatas,
                     Helpers.getStruct("evento", ["name"]))
    out, _ = capfd.readouterr()
    assert "**___Eventos___** **___encontrados:___**" in out
    assert f"{testData['id']}" in out
    assert f"{testData['namecreate']}" in out
    assert f"{testData['pointcreate']}" in out
    assert f"{testData['descreate']}" in out

@pytest.mark.asyncio
async def test_updEventId(capfd):
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
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updEvent:id", app.updateData,
                           Helpers.updStruct("evento", "id"))
        out, _ = capfd.readouterr()
        assert "El ___evento___ ha sido actualizado con exito." in out

@pytest.mark.asyncio
async def test_updEventId_exist(capfd):
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
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updEvent:id", app.updateData,
                           Helpers.updStruct("evento", "id"))
        out, _ = capfd.readouterr()
        assert f"El ___evento___ de **_Nombre_** \'{testData['nameexist']}\' "\
            "ya se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def test_updEventName(capfd):
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
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updEvent:name", app.updateData,
                           Helpers.updStruct("evento", "name"))
        out, _ = capfd.readouterr()
        assert "El ___evento___ ha sido actualizado con exito." in out

@pytest.mark.asyncio
async def test_listEvent(capfd):
    commands = [f"$listEvent",
                f"$listEvent ",
                f"$listEventFILL",
                f"$listEvent FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listEvent", app.getDatas,
                         Helpers.getStruct("evento"))
        out, _ = capfd.readouterr()
        assert "**___Eventos___** **___encontrados:___**" in out
        assert f"{testData['id']}" in out
        assert f"{testData['nameupdate']}" in out
        assert f"{testData['pointupdate']}" in out
        assert f"{testData['desupdate']}" in out

@pytest.mark.asyncio
async def test_listEventId(capfd):
    commands = [f"$listEvent:id[{testData['id']}]",
                f"$listEvent:id [{testData['id']}]",
                f"$listEvent:id [ {testData['id']} ] ",
                f"$listEvent:id [ {testData['id']} ]FILL",
                f"$listEvent:id [ {testData['id']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listEvent:id", app.getDatas,
                         Helpers.getStruct("evento", ["id"]))
        out, _ = capfd.readouterr()
        assert "**___Eventos___** **___encontrados:___**" in out
        assert f"{testData['id']}" in out
        assert f"{testData['nameupdate']}" in out
        assert f"{testData['pointupdate']}" in out
        assert f"{testData['desupdate']}" in out

@pytest.mark.asyncio
async def test_listEventName(capfd):
    commands = [f"$listEvent:name[{testData['nameupdate']}]",
                f"$listEvent:name [{testData['nameupdate']}]",
                f"$listEvent:name [ {testData['nameupdate']} ] ",
                f"$listEvent:name [ {testData['nameupdate']} ]FILL",
                f"$listEvent:name [ {testData['nameupdate']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listEvent:name", app.getDatas,
                         Helpers.getStruct("evento", ["name"]))
        out, _ = capfd.readouterr()
        assert "**___Eventos___** **___encontrados:___**" in out
        assert f"{testData['id']}" in out
        assert f"{testData['nameupdate']}" in out
        assert f"{testData['pointupdate']}" in out
        assert f"{testData['desupdate']}" in out

@pytest.mark.asyncio
async def test_listEvent_e(capfd):
    commands = [f"$listEvent"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listEvent", app.getDatas,
                             Helpers.getStruct("evento"))
            out, _ = capfd.readouterr()
            assert "**___Eventos___** **___encontrados:___**" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_listEventId_e(capfd):
    commands = [f"$listEvent:id[{testData['id']}]",
                f"$listEvent:id [{testData['id']}]",
                f"$listEvent:id [ {testData['id']} ]"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listEvent:id", app.getDatas,
                             Helpers.getStruct("evento", ["id"]))
            out, _ = capfd.readouterr()
            assert "**___Eventos___** **___encontrados:___**" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_listEventName_e(capfd):
    commands = [f"$listEvent:name[{testData['nameupdate']}]",
                f"$listEvent:name [{testData['nameupdate']}]",
                f"$listEvent:name [ {testData['nameupdate']} ]"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listEvent:name", app.getDatas,
                             Helpers.getStruct("evento", ["name"]))
            out, _ = capfd.readouterr()
            assert "**___Eventos___** **___encontrados:___**" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_listEvent_e_incomplete(capfd):
    commands = [f"$listEvent"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listEvent", app.getDatas,
                             Helpers.getStruct("evento"))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert "**$listEvent** **> e**\n" in out

@pytest.mark.asyncio
async def test_listEventId_e_incomplete(capfd):
    commands = [f"$listEvent:id[{testData['id']}]",
                f"$listEvent:id [{testData['id']}]",
                f"$listEvent:id [ {testData['id']} ]"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listEvent:id", app.getDatas,
                             Helpers.getStruct("evento", ["id"]))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert f"**$listEvent:id** **[**{testData['id']}**]** "\
                    "**> e**\n" in out

@pytest.mark.asyncio
async def test_listEventName_e_incomplete(capfd):
    commands = [f"$listEvent:name[{testData['nameupdate']}]",
                f"$listEvent:name [{testData['nameupdate']}]",
                f"$listEvent:name [ {testData['nameupdate']} ]"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listEvent:name", app.getDatas,
                             Helpers.getStruct("evento", ["name"]))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert f"**$listEvent:name** **[**{testData['nameupdate']}**]** "\
                    "**> e**\n" in out

@pytest.mark.asyncio
async def test_delEventId(capfd):
    command = f"$delEvent:id [{testData['id']}]"
    message = Message(author="test", content=command)
    client = Client(user="test")
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delEvent:id", app.deleteData,
                       Helpers.delStruct("evento", "id"))
    out, _ = capfd.readouterr()
    assert "El ___evento___ ha sido eliminado con exito." in out

@pytest.mark.asyncio
async def test_addEvent_DelName(capfd):
    command = f"$addEvent [{testData['namecreate']}, "\
              f"{testData['pointcreate']}, {testData['descreate']}]"
    message = Message(author="test", content=command)
    client = Client(user="test")
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addEvent", app.setData,
                       Helpers.setStruct("evento"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["id"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "El ___evento___ ha sido creado con exito sobre el " in out
    assert f"**_ID_** \'{testData['id']}\'." in out

@pytest.mark.asyncio
async def test_delEventName(capfd):
    command = f"$delEvent:name [{testData['namecreate']}]"
    message = Message(author="test", content=command)
    client = Client(user="test")
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delEvent:name", app.deleteData,
                       Helpers.delStruct("evento", "name"))
    out, _ = capfd.readouterr()
    assert "El ___evento___ ha sido eliminado con exito." in out

@pytest.mark.asyncio
async def test_updEventId_idnoexist(capfd):
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
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updEvent:id", app.updateData,
                           Helpers.updStruct("evento", "id"))
        out, _ = capfd.readouterr()
        assert f"El ___evento___ de **_ID_** '{testData['id']}' "\
               "no se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def test_updEventName_namenoexist(capfd):
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
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updEvent:name", app.updateData,
                           Helpers.updStruct("evento", "name"))
        out, _ = capfd.readouterr()
        assert f"El ___evento___ de **_Nombre_** '{testData['nameupdate']}' "\
               "no se encuentra en la base de datos.\n" in out