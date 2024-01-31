import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Helpers.helpers import Helpers
from collections import namedtuple

testData = {
    "id" : "",
    "namecreate" : "TestMemberCreated",
    "nameupdate" : "TestMemberUpdated",
    "nameexist" : "Avalonicus",
    "rancreate" : "General de alianza",
    "ranupdate" : "General",
    "ranoexist" : "Range-[noexist]",
    "datecreate" : "25-01-2100",
    "dateupdate" : "26-01-2100"
}

Message = namedtuple('Message', ['author', 'content'])
Client = namedtuple('Client', ['user'])
app = AppHandler()

@pytest.mark.asyncio
async def test_addMember(capfd):
    command = f"$addMember [{testData['namecreate']}, "\
              f"{testData['rancreate']}, {testData['datecreate']}]"
    message = Message(author="test", content=command)
    client = Client(user="test")
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addMember", app.setData,
                       Helpers.setStruct("integrante"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["id"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "El ___integrante___ ha sido creado con exito sobre el " in out
    assert f"**_ID_** \'{testData['id']}\'." in out

@pytest.mark.asyncio
async def test_addMember_exist(capfd):
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
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addMember", app.setData,
                           Helpers.setStruct("integrante"))
        out, _ = capfd.readouterr()
        assert f"El ___integrante___ de **_Nombre_** "\
               f"\'{testData['namecreate']}\' "\
                "ya se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def test_listMemberId_add(capfd):
    command = f"$listMember:id [{testData['id']}]"
    message = Message(author="test", content=command)
    client = Client(user="test")
    hdlr = MessageHandler(message, client, True)
    await hdlr.dFMsg("listMember:id", app.getDatas,
                     Helpers.getStruct("integrante", ["id"]))
    out, _ = capfd.readouterr()
    assert "**___Integrantes___** **___encontrados:___**" in out
    assert f"{testData['id']}" in out
    assert f"{testData['namecreate']}" in out
    assert f"{testData['rancreate']}" in out
    assert f"{testData['datecreate'].replace('-','/')}" in out
    assert "Ninguno" in out

@pytest.mark.asyncio
async def test_listMemberName_add(capfd):
    command = f"$listMember:name [{testData['namecreate']}]"
    message = Message(author="test", content=command)
    client = Client(user="test")
    hdlr = MessageHandler(message, client, True)
    await hdlr.dFMsg("listMember:name", app.getDatas,
                     Helpers.getStruct("integrante", ["name"]))
    out, _ = capfd.readouterr()
    assert "**___Integrantes___** **___encontrados:___**" in out
    assert f"{testData['id']}" in out
    assert f"{testData['namecreate']}" in out
    assert f"{testData['rancreate']}" in out
    assert f"{testData['datecreate'].replace('-','/')}" in out
    assert "Ninguno" in out

@pytest.mark.asyncio
async def test_updMemberId(capfd):
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
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:id", app.updateData,
                           Helpers.updStruct("integrante", "id"))
        out, _ = capfd.readouterr()
        assert "El ___integrante___ ha sido actualizado con exito." in out

@pytest.mark.asyncio
async def test_updMemberId_nameexist(capfd):
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
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:id", app.updateData,
                           Helpers.updStruct("integrante", "id"))
        out, _ = capfd.readouterr()
        assert f"El ___integrante___ de **_Nombre_** "\
           f"\'{testData['nameexist']}\' "\
            "ya se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def test_updMemberName(capfd):
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
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:name", app.updateData,
                           Helpers.updStruct("integrante", "name"))
        out, _ = capfd.readouterr()
        assert "El ___integrante___ ha sido actualizado con exito." in out

@pytest.mark.asyncio
async def test_listMember(capfd):
    commands = [f"$listMember",
                f"$listMember ",
                f"$listMemberFILL",
                f"$listMember FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember", app.getDatas,
                         Helpers.getStruct("integrante"))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**" in out
        assert f"{testData['id']}" in out
        assert f"{testData['nameupdate']}" in out
        assert f"{testData['ranupdate']}" in out
        assert f"{testData['datecreate'].replace('-','/')}" in out
        assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def test_listMemberId(capfd):
    commands = [f"$listMember:id[{testData['id']}]",
                f"$listMember:id [{testData['id']}]",
                f"$listMember:id [ {testData['id']} ] ",
                f"$listMember:id [ {testData['id']} ]FILL",
                f"$listMember:id [ {testData['id']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:id", app.getDatas,
                         Helpers.getStruct("integrante", ["id"]))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**" in out
        assert f"{testData['id']}" in out
        assert f"{testData['nameupdate']}" in out
        assert f"{testData['ranupdate']}" in out
        assert f"{testData['datecreate'].replace('-','/')}" in out
        assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def test_listMemberName(capfd):
    commands = [f"$listMember:name[{testData['nameupdate']}]",
                f"$listMember:name [{testData['nameupdate']}]",
                f"$listMember:name [ {testData['nameupdate']} ] ",
                f"$listMember:name [ {testData['nameupdate']} ]FILL",
                f"$listMember:name [ {testData['nameupdate']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:name", app.getDatas,
                         Helpers.getStruct("integrante", ["name"]))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**" in out
        assert f"{testData['id']}" in out
        assert f"{testData['nameupdate']}" in out
        assert f"{testData['ranupdate']}" in out
        assert f"{testData['datecreate'].replace('-','/')}" in out
        assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def test_listMemberRange(capfd):
    commands = [f"$listMember:range[{testData['ranupdate']}]",
                f"$listMember:range [{testData['ranupdate']}]",
                f"$listMember:range [ {testData['ranupdate']} ] ",
                f"$listMember:range [ {testData['ranupdate']} ]FILL",
                f"$listMember:range [ {testData['ranupdate']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:range", app.getDatas,
                         Helpers.getStruct("integrante", ["rango"]))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**" in out
        assert f"{testData['id']}" in out
        assert f"{testData['nameupdate']}" in out
        assert f"{testData['ranupdate']}" in out
        assert f"{testData['datecreate'].replace('-','/')}" in out
        assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def test_listMemberDate(capfd):
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
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listMember:date", app.getDatas,
                         Helpers.getStruct("integrante", ["date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "**___Integrantes___** **___encontrados:___**" in out
        assert f"{testData['id']}" in out
        assert f"{testData['nameupdate']}" in out
        assert f"{testData['ranupdate']}" in out
        assert f"{testData['datecreate'].replace('-','/')}" in out
        assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def test_listMember_e(capfd):
    commands = [f"$listMember"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember", app.getDatas,
                             Helpers.getStruct("integrante"))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_listMemberId_e(capfd):
    commands = [f"$listMember:id[{testData['id']}]",
                f"$listMember:id [{testData['id']}]",
                f"$listMember:id [ {testData['id']} ]"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember:id", app.getDatas,
                             Helpers.getStruct("integrante", ["id"]))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_listMemberName_e(capfd):
    commands = [f"$listMember:name[{testData['nameupdate']}]",
                f"$listMember:name [{testData['nameupdate']}]",
                f"$listMember:name [ {testData['nameupdate']} ]"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember:name", app.getDatas,
                             Helpers.getStruct("integrante", ["name"]))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_listMemberRange_e(capfd):
    commands = [f"$listMember:range[{testData['ranupdate']}]",
                f"$listMember:range [{testData['ranupdate']}]",
                f"$listMember:range [ {testData['ranupdate']} ]"]
    eparams = [">e", " >e", " > e", " > e ", " > e FILL"
               ">E", " >E", " > E", " > E ", " > E FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember:range", app.getDatas,
                             Helpers.getStruct("integrante", ["rango"]))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_listMemberDate_e(capfd):
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
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember:date", app.getDatas,
                             Helpers.getStruct("integrante",
                             ["date_1", "date_2"]))
            out, _ = capfd.readouterr()
            assert "**___Integrantes___** **___encontrados:___**" in out
            assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_listMember_e_incomplete(capfd):
    commands = [f"$listMember"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember", app.getDatas,
                             Helpers.getStruct("integrante"))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert "**$listMember** **> e**\n" in out

@pytest.mark.asyncio
async def test_listMemberId_e_incomplete(capfd):
    commands = [f"$listMember:id[{testData['id']}]",
                f"$listMember:id [{testData['id']}]",
                f"$listMember:id [ {testData['id']} ]"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember:id", app.getDatas,
                             Helpers.getStruct("integrante", ["id"]))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert f"**$listMember:id** **[**{testData['id']}**]** "\
                    "**> e**\n" in out

@pytest.mark.asyncio
async def test_listMemberName_e_incomplete(capfd):
    commands = [f"$listMember:name[{testData['nameupdate']}]",
                f"$listMember:name [{testData['nameupdate']}]",
                f"$listMember:name [ {testData['nameupdate']} ]"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember:name", app.getDatas,
                             Helpers.getStruct("integrante", ["name"]))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert f"**$listMember:name** **[**{testData['nameupdate']}**]** "\
                    "**> e**\n" in out

@pytest.mark.asyncio
async def test_listMemberRange_e_incomplete(capfd):
    commands = [f"$listMember:range[{testData['ranupdate']}]",
                f"$listMember:range [{testData['ranupdate']}]",
                f"$listMember:range [ {testData['ranupdate']} ]"]
    eparams = [">", " >", "> ", " > ", " > FILL",
               "FILL >", " FILL >", " FILL > FILL"]
    for command in commands:
        for eparam in eparams:
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember:range", app.getDatas,
                             Helpers.getStruct("integrante", ["rango"]))
            out, _ = capfd.readouterr()
            assert "Se ha detectado el uso del operador **>** despues del "\
                   "comando inicial, si desea obtener los datos en un "\
                   "archivo de excel, debe completar el comando ingresadolo "\
                   "de la siguiente forma:\n" in out
            assert f"**$listMember:range** **[**{testData['ranupdate']}**]** "\
                    "**> e**\n" in out

@pytest.mark.asyncio
async def test_listMemberDate_e_incomplete(capfd):
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
            message = Message(author="test", content=f"{command}{eparam}")
            client = Client(user="test")
            hdlr = MessageHandler(message, client, True)
            await hdlr.dFMsg("listMember:date", app.getDatas,
                             Helpers.getStruct("integrante",
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
async def test_delMemberId(capfd):
    command = f"$delMember:id [{testData['id']}]"
    message = Message(author="test", content=command)
    client = Client(user="test")
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delMember:id", app.deleteData,
                       Helpers.delStruct("integrante", "id"))
    out, _ = capfd.readouterr()
    assert "El ___integrante___ ha sido eliminado con exito." in out

@pytest.mark.asyncio
async def test_addMember_DelName(capfd):
    command = f"$addMember [{testData['namecreate']}, "\
              f"{testData['rancreate']}, {testData['datecreate']}]"
    message = Message(author="test", content=command)
    client = Client(user="test")
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addMember", app.setData,
                       Helpers.setStruct("integrante"))
    out, _ = capfd.readouterr()
    idTest = out[out.find("**_ID_** '"):]
    testData["id"] = idTest[idTest.find("'")+1:idTest.find("'.")]
    assert "El ___integrante___ ha sido creado con exito sobre el " in out
    assert f"**_ID_** \'{testData['id']}\'." in out

@pytest.mark.asyncio
async def test_delMemberName(capfd):
    command = f"$delMember:name [{testData['namecreate']}]"
    message = Message(author="test", content=command)
    client = Client(user="test")
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("delMember:name", app.deleteData,
                       Helpers.delStruct("integrante", "name"))
    out, _ = capfd.readouterr()
    assert "El ___integrante___ ha sido eliminado con exito." in out

@pytest.mark.asyncio
async def test_addMember_rangenoexist(capfd):
    command = f"$addMember [{testData['namecreate']}, "\
              f"{testData['ranoexist']}, {testData['datecreate']}]"
    message = Message(author="test", content=command)
    client = Client(user="test")
    hdlr = MessageHandler(message, client, True)
    await hdlr.contMsg("addMember", app.setData,
                       Helpers.setStruct("integrante"))
    out, _ = capfd.readouterr()
    assert f"El valor '{testData['ranoexist']}' "\
            "ingresado en el campo "\
            "**_Rango_** no fue encontrado en la "\
            "base de datos.\n" in out

@pytest.mark.asyncio
async def test_updMemberId_idnoexist(capfd):
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
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:id", app.updateData,
                           Helpers.updStruct("integrante", "id"))
        out, _ = capfd.readouterr()
        assert f"El ___integrante___ de **_ID_** '{testData['id']}' "\
                "no se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def test_updMemberId_rangenoexist(capfd):
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
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:id", app.updateData,
                           Helpers.updStruct("integrante", "id"))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['ranoexist']}' "\
                "ingresado en el campo "\
                "**_Rango_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def test_updMemberName_namenoexist(capfd):
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
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:name", app.updateData,
                           Helpers.updStruct("integrante", "name"))
        out, _ = capfd.readouterr()
        assert f"El ___integrante___ de **_Nombre_** "\
               f"'{testData['nameupdate']}' "\
                "no se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def test_updMemberName_rangenoexist(capfd):
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
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updMember:name", app.updateData,
                           Helpers.updStruct("integrante", "name"))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['ranoexist']}' "\
                "ingresado en el campo "\
                "**_Rango_** no fue encontrado en la "\
                "base de datos.\n" in out

@pytest.mark.asyncio
async def test_delMemberId_idnoexist(capfd):
    commands = [f"$delMember:id[{testData['id']}]",
                f"$delMember:id [{testData['id']}]",
                f"$delMember:id [ {testData['id']} ]",
                f"$delMember:id [ {testData['id']} ]FILL",
                f"$delMember:id [ {testData['id']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delMember:id", app.deleteData,
                           Helpers.delStruct("integrante", "id"))
        out, _ = capfd.readouterr()
        assert f"El ___integrante___ de **_ID_** '{testData['id']}' "\
                "no se encuentra en la base de datos.\n" in out

@pytest.mark.asyncio
async def test_delMemberName_namenoexist(capfd):
    commands = [f"$delMember:name[{testData['namecreate']}]",
                f"$delMember:name [{testData['namecreate']}]",
                f"$delMember:name [ {testData['namecreate']} ]",
                f"$delMember:name [ {testData['namecreate']} ]FILL",
                f"$delMember:name [ {testData['namecreate']} ] FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delMember:name", app.deleteData,
                           Helpers.delStruct("integrante", "name"))
        out, _ = capfd.readouterr()
        assert f"El ___integrante___ de **_Nombre_** "\
               f"'{testData['namecreate']}' "\
                "no se encuentra en la base de datos.\n" in out