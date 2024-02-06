import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Helpers.helpers import Helpers
from collections import namedtuple

testData = {
    "id" : "",
    "namecreate" : "TestRangeCreated",
    "nameupdate" : "TestRangeUpdated",
    "nameexist" : "General de alianza",
    "controlcreate" : 2,
    "controlupdate" : 3,
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

@pytest.mark.asyncio
async def testRangeDefault_addRange(capfd):
    command = f"$addRange [{testData['namecreate']}, "\
              f"{testData['controlcreate']}, {testData['descreate']}]"
    message = Message(author=author, content=command)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addRange", app.setData,
                       Helpers.setStruct("range"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["id"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "El ___rango___ ha sido creado con exito sobre el "\
          f"**_ID_** \'{testData['id']}\'.\n" in out

@pytest.mark.asyncio
async def testRangeDefault_addRange_exist(capfd):
    commands = [f"$addRange[{testData['namecreate']},"\
               f"{testData['controlcreate']},"\
               f"{testData['descreate']}]",
               f"$addRange [{testData['namecreate']}, "\
               f"{testData['controlcreate']}, "\
               f"{testData['descreate']}]",
               f"$addRange [ {testData['namecreate']} , "\
               f" {testData['controlcreate']} , "\
               f" {testData['descreate']} ]",
               f"$addRange [ {testData['namecreate']} , "\
               f" {testData['controlcreate']} , "\
               f" {testData['descreate']} ]FILL ",
               f"$addRange [ {testData['namecreate']} , "\
               f" {testData['controlcreate']} , "\
               f" {testData['descreate']} ] FILL"]
    for command in commands:
        message = Message(author=author, content=command)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addRange", app.setData,
                           Helpers.setStruct("range"))
        out, _ = capfd.readouterr()
        assert f"El ___rango___ de **_Nombre_** "\
               f"\'{testData['namecreate']}\' "\
                "ya se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def testRangeDefault_listRangeId_add(capfd):
    command = f"$listRange:id [{testData['id']}]"
    message = Message(author=author, content=command)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.dFMsg("listRange:id", app.getDatas,
                     Helpers.getStruct("range", ["id"]))
    out, _ = capfd.readouterr()
    assert "**___Rangos___** **___encontrados:___**\n" in out
    assert f"{testData['id']}" in out
    assert f"{testData['namecreate']}" in out
    assert f"{testData['controlcreate']}" in out
    assert f"{testData['descreate']}" in out

@pytest.mark.asyncio
async def testRangeDefault_listRangeName_add(capfd):
    command = f"$listRange:name [{testData['namecreate']}]"
    message = Message(author=author, content=command)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.dFMsg("listRange:name", app.getDatas,
                     Helpers.getStruct("range", ["name"]))
    out, _ = capfd.readouterr()
    assert "**___Rangos___** **___encontrados:___**\n" in out
    assert f"{testData['id']}" in out
    assert f"{testData['namecreate']}" in out
    assert f"{testData['controlcreate']}" in out
    assert f"{testData['descreate']}" in out

@pytest.mark.asyncio
async def testRangeDefault_updRangeId(capfd):
    commands = [f"$updRange:id[{testData['id']},{testData['nameupdate']},"\
                f"{testData['controlupdate']},{testData['descreate']}]",
                f"$updRange:id [{testData['id']}, {testData['nameupdate']}, "\
                f"{testData['controlupdate']}, {testData['descreate']}]",
                f"$updRange:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['controlupdate']} , {testData['descreate']} ] ",
                f"$updRange:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['controlupdate']} , {testData['descreate']} ]FILL",
                f"$updRange:id [ {testData['id']} ,"\
                f"{testData['nameupdate']} , "\
                f"{testData['controlupdate']} , "\
                f"{testData['descreate']} ] FILL "]
    for command in commands:
        message = Message(author=author, content=command)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updRange:id", app.updateData,
                           Helpers.updStruct("range", "id"))
        out, _ = capfd.readouterr()
        assert "El ___rango___ ha sido actualizado con exito.\n" in out

@pytest.mark.asyncio
async def testRangeDefault_updRangeId_nameExist(capfd):
    commands = [f"$updRange:id[{testData['id']},{testData['nameexist']},"\
                f"{testData['controlupdate']},{testData['descreate']}]",
                f"$updRange:id [{testData['id']}, {testData['nameexist']}, "\
                f"{testData['controlupdate']}, {testData['descreate']}]",
                f"$updRange:id [ {testData['id']} , "\
                f"{testData['nameexist']} , "\
                f"{testData['controlupdate']} , {testData['descreate']} ] ",
                f"$updRange:id [ {testData['id']} , "\
                f"{testData['nameexist']} , "\
                f"{testData['controlupdate']} , {testData['descreate']} ]FILL",
                f"$updRange:id [ {testData['id']} ,"\
                f"{testData['nameexist']} , "\
                f"{testData['controlupdate']} , "\
                f"{testData['descreate']} ] FILL "]
    for command in commands:
        message = Message(author=author, content=command)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updRange:id", app.updateData,
                           Helpers.updStruct("range", "id"))
        out, _ = capfd.readouterr()
        assert f"El ___rango___ de **_Nombre_** "\
               f"\'{testData['nameexist']}\' "\
                "ya se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def testRangeDefault_updRangeName(capfd):
    commands = [f"$updRange:name[{testData['nameupdate']},"\
                f"{testData['controlupdate']},{testData['desupdate']}]",
                f"$updRange:name [{testData['nameupdate']}, "\
                f"{testData['controlupdate']}, {testData['desupdate']}]",
                f"$updRange:name [ {testData['nameupdate']} , "\
                f"{testData['controlupdate']} , {testData['desupdate']} ] ",
                f"$updRange:name [ {testData['nameupdate']} , "\
                f"{testData['controlupdate']} , {testData['desupdate']} ]FILL",
                f"$updRange:name [ {testData['nameupdate']} , "\
                f"{testData['controlupdate']} , "\
                f"{testData['desupdate']} ] FILL "]
    for command in commands:
        message = Message(author=author, content=command)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updRange:name", app.updateData,
                           Helpers.updStruct("range", "name"))
        out, _ = capfd.readouterr()
        assert "El ___rango___ ha sido actualizado con exito.\n" in out

@pytest.mark.asyncio
async def testRangeDefault_listRange(capfd):
    commands = [f"$listRange",
                f"$listRange ",
                f"$listRangeFILL",
                f"$listRange FILL"]
    for command in commands:
        message = Message(author=author, content=command)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listRange", app.getDatas,
                         Helpers.getStruct("range"))
        out, _ = capfd.readouterr()
        assert "**___Rangos___** **___encontrados:___**\n" in out
        assert f"{testData['id']}" in out
        assert f"{testData['nameupdate']}" in out
        assert f"{testData['controlupdate']}" in out
        assert f"{testData['desupdate']}" in out

@pytest.mark.asyncio
async def testRangeDefault_listRangeId(capfd):
    commands = [f"$listRange:id[{testData['id']}]",
                f"$listRange:id [{testData['id']}]",
                f"$listRange:id [ {testData['id']} ] ",
                f"$listRange:id [ {testData['id']} ]FILL",
                f"$listRange:id [ {testData['id']} ] FILL"]
    for command in commands:
        message = Message(author=author, content=command)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listRange:id", app.getDatas,
                         Helpers.getStruct("range", ["id"]))
        out, _ = capfd.readouterr()
        assert "**___Rangos___** **___encontrados:___**\n" in out
        assert f"{testData['id']}" in out
        assert f"{testData['nameupdate']}" in out
        assert f"{testData['controlupdate']}" in out
        assert f"{testData['desupdate']}" in out

@pytest.mark.asyncio
async def testRangeDefault_listRangeName(capfd):
    commands = [f"$listRange:name[{testData['nameupdate']}]",
                f"$listRange:name [{testData['nameupdate']}]",
                f"$listRange:name [ {testData['nameupdate']} ] ",
                f"$listRange:name [ {testData['nameupdate']} ]FILL",
                f"$listRange:name [ {testData['nameupdate']} ] FILL"]
    for command in commands:
        message = Message(author=author, content=command)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listRange:name", app.getDatas,
                         Helpers.getStruct("range", ["name"]))
        out, _ = capfd.readouterr()
        assert "**___Rangos___** **___encontrados:___**\n" in out
        assert f"{testData['id']}" in out
        assert f"{testData['nameupdate']}" in out
        assert f"{testData['controlupdate']}" in out
        assert f"{testData['desupdate']}" in out

@pytest.mark.asyncio
async def testRangeDefault_listRange_e(capfd):
    commands = [f"$listRange"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author=author, content=f"{command}{eparam}")
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listRange", app.getDatas,
                             Helpers.getStruct("range"))
            out, _ = capfd.readouterr()
            assert "**___Rangos___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testRangeDefault_listRangeId_e(capfd):
    commands = [f"$listRange:id[{testData['id']}]",
                f"$listRange:id [{testData['id']}]",
                f"$listRange:id [ {testData['id']} ]"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author=author, content=f"{command}{eparam}")
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listRange:id", app.getDatas,
                             Helpers.getStruct("range", ["id"]))
            out, _ = capfd.readouterr()
            assert "**___Rangos___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testRangeDefault_listRangeName_e(capfd):
    commands = [f"$listRange:name[{testData['nameupdate']}]",
                f"$listRange:name [{testData['nameupdate']}]",
                f"$listRange:name [ {testData['nameupdate']} ]"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author=author, content=f"{command}{eparam}")
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listRange:name", app.getDatas,
                             Helpers.getStruct("range", ["name"]))
            out, _ = capfd.readouterr()
            assert "**___Rangos___** **___encontrados:___**\n" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testRangeDefault_listRange_eIncomplete(capfd):
    commands = [f"$listRange"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author=author, content=f"{command}{eparam}")
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listRange", app.getDatas,
                             Helpers.getStruct("range"))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert "**$listRange** **> e**\n" in out

@pytest.mark.asyncio
async def testRangeDefault_listRangeId_eIncomplete(capfd):
    commands = [f"$listRange:id[{testData['id']}]",
                f"$listRange:id [{testData['id']}]",
                f"$listRange:id [ {testData['id']} ]"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author=author, content=f"{command}{eparam}")
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listRange:id", app.getDatas,
                             Helpers.getStruct("range", ["id"]))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert f"**$listRange:id** **[**{testData['id']}**]** "\
                    "**> e**\n" in out

@pytest.mark.asyncio
async def testRangeDefault_listRangeName_eIncomplete(capfd):
    commands = [f"$listRange:name[{testData['nameupdate']}]",
                f"$listRange:name [{testData['nameupdate']}]",
                f"$listRange:name [ {testData['nameupdate']} ]"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author=author, content=f"{command}{eparam}")
            client = Client(user=user)
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listRange:name", app.getDatas,
                             Helpers.getStruct("range", ["name"]))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert f"**$listRange:name** **[**{testData['nameupdate']}**]** "\
                    "**> e**\n" in out

@pytest.mark.asyncio
async def testRangeDefault_delRangeId(capfd):
    command = f"$delRange:id [{testData['id']}]"
    message = Message(author=author, content=command)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delRange:id", app.deleteData,
                       Helpers.delStruct("range", "id"))
    out, _ = capfd.readouterr()
    assert "El ___rango___ ha sido eliminado con exito.\n" in out

@pytest.mark.asyncio
async def testRangeDefault_addRange_delName(capfd):
    command = f"$addRange [{testData['namecreate']}, "\
              f"{testData['controlcreate']}, {testData['descreate']}]"
    message = Message(author=author, content=command)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addRange", app.setData,
                       Helpers.setStruct("range"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["id"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "El ___rango___ ha sido creado con exito sobre el "\
          f"**_ID_** \'{testData['id']}\'.\n" in out

@pytest.mark.asyncio
async def testRangeDefault_delRangeName(capfd):
    command = f"$delRange:name [{testData['namecreate']}]"
    message = Message(author=author, content=command)
    client = Client(user=user)
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delRange:name", app.deleteData,
                       Helpers.delStruct("range", "name"))
    out, _ = capfd.readouterr()
    assert "El ___rango___ ha sido eliminado con exito.\n" in out

@pytest.mark.asyncio
async def testRangeDefault_updRangeId_idNoExist(capfd):
    commands = [f"$updRange:id[{testData['id']},{testData['nameupdate']},"\
                f"{testData['controlupdate']},{testData['descreate']}]",
                f"$updRange:id [{testData['id']}, {testData['nameupdate']}, "\
                f"{testData['controlupdate']}, {testData['descreate']}]",
                f"$updRange:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['controlupdate']} , {testData['descreate']} ] ",
                f"$updRange:id [ {testData['id']} , "\
                f"{testData['nameupdate']} , "\
                f"{testData['controlupdate']} , {testData['descreate']} ]FILL",
                f"$updRange:id [ {testData['id']} ,"\
                f"{testData['nameupdate']} , "\
                f"{testData['controlupdate']} , "\
                f"{testData['descreate']} ] FILL "]
    for command in commands:
        message = Message(author=author, content=command)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updRange:id", app.updateData,
                           Helpers.updStruct("range", "id"))
        out, _ = capfd.readouterr()
        assert f"El ___rango___ de **_ID_** '{testData['id']}' "\
                "no se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def testRangeDefault_updRangeName_nameNoExist(capfd):
    commands = [f"$updRange:name[{testData['nameupdate']},"\
                f"{testData['controlupdate']},{testData['desupdate']}]",
                f"$updRange:name [{testData['nameupdate']}, "\
                f"{testData['controlupdate']}, {testData['desupdate']}]",
                f"$updRange:name [ {testData['nameupdate']} , "\
                f"{testData['controlupdate']} , {testData['desupdate']} ] ",
                f"$updRange:name [ {testData['nameupdate']} , "\
                f"{testData['controlupdate']} , {testData['desupdate']} ]FILL",
                f"$updRange:name [ {testData['nameupdate']} , "\
                f"{testData['controlupdate']} , "\
                f"{testData['desupdate']} ] FILL "]
    for command in commands:
        message = Message(author=author, content=command)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updRange:name", app.updateData,
                           Helpers.updStruct("range", "name"))
        out, _ = capfd.readouterr()
        assert f"El ___rango___ de **_Nombre_** "\
               f"'{testData['nameupdate']}' "\
                "no se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def testRangeDefault_delRangeId_idNoExist(capfd):
    commands = [f"$delRange:id[{testData['id']}]",
                f"$delRange:id [{testData['id']}]",
                f"$delRange:id [ {testData['id']} ]",
                f"$delRange:id [ {testData['id']} ]FILL",
                f"$delRange:id [ {testData['id']} ] FILL"]
    for command in commands:
        message = Message(author=author, content=command)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delRange:id", app.deleteData,
                           Helpers.delStruct("range", "id"))
        out, _ = capfd.readouterr()
        assert f"El ___rango___ de **_ID_** '{testData['id']}' "\
                "no se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def testRangeDefault_delRangeName_nameNoExist(capfd):
    commands = [f"$delRange:name[{testData['namecreate']}]",
                f"$delRange:name [{testData['namecreate']}]",
                f"$delRange:name [ {testData['namecreate']} ]",
                f"$delRange:name [ {testData['namecreate']} ]FILL",
                f"$delRange:name [ {testData['namecreate']} ] FILL"]
    for command in commands:
        message = Message(author=author, content=command)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delRange:name", app.deleteData,
                           Helpers.delStruct("range", "name"))
        out, _ = capfd.readouterr()
        assert f"El ___rango___ de **_Nombre_** "\
               f"'{testData['namecreate']}' "\
                "no se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def testRangeDefault_listRangeId_idNoExist(capfd):
    commands = [f"$listRange:id[{testData['id']}]",
                f"$listRange:id [{testData['id']}]",
                f"$listRange:id [ {testData['id']} ] ",
                f"$listRange:id [ {testData['id']} ]FILL",
                f"$listRange:id [ {testData['id']} ] FILL"]
    for command in commands:
        message = Message(author=author, content=command)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listRange:id", app.getDatas,
                         Helpers.getStruct("range", ["id"]))
        out, _ = capfd.readouterr()
        assert "No se encontraron ___rangos___ "\
               "para la consulta realizada.\n" in out

@pytest.mark.asyncio
async def testRangeDefault_listRangeName_nameNoExist(capfd):
    commands = [f"$listRange:name[{testData['nameupdate']}]",
                f"$listRange:name [{testData['nameupdate']}]",
                f"$listRange:name [ {testData['nameupdate']} ] ",
                f"$listRange:name [ {testData['nameupdate']} ]FILL",
                f"$listRange:name [ {testData['nameupdate']} ] FILL"]
    for command in commands:
        message = Message(author=author, content=command)
        client = Client(user=user)
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listRange:name", app.getDatas,
                         Helpers.getStruct("range", ["name"]))
        out, _ = capfd.readouterr()
        assert "No se encontraron ___rangos___ "\
               "para la consulta realizada.\n" in out