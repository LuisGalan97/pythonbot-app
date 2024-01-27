import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Helpers.helpers import Helpers
from collections import namedtuple

testData = {
  "id" : "",
  "namecreate" : "TestMember",
  "nameupdate" : "TestMemberUpd",
  "rancreate" : "General de alianza",
  "ranupdate" : "General",
  "datecreate" : "25-01-2020",
  "dateupdate" : "26-01-2021"
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
  command = f"$updMember:id [{testData['id']}, {testData['nameupdate']}, "\
            f"{testData['rancreate']}, {testData['dateupdate']}]"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.contMsg("updMember:id", app.updateData, 
                     Helpers.updStruct("integrante", "id"))
  out, _ = capfd.readouterr()
  assert "El ___integrante___ ha sido actualizado con exito." in out

@pytest.mark.asyncio
async def test_updMemberName(capfd):
  command = f"$updMember:name [{testData['nameupdate']}, "\
            f"{testData['ranupdate']}, {testData['dateupdate']}]"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.contMsg("updMember:name", app.updateData, 
                     Helpers.updStruct("integrante", "name"))
  out, _ = capfd.readouterr()
  assert "El ___integrante___ ha sido actualizado con exito." in out

@pytest.mark.asyncio
async def test_listMember(capfd):
  command = "$listMember"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listMember", app.getDatas, 
                   Helpers.getStruct("integrante"))
  out, _ = capfd.readouterr()
  assert "**___Integrantes___** **___encontrados:___**" in out
  assert f"{testData['id']}" in out
  assert f"{testData['namecreate']}" in out
  assert f"{testData['rancreate']}" in out
  assert f"{testData['datecreate'].replace('-','/')}" in out
  assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def test_listMemberId(capfd):
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
  assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def test_listMemberName(capfd):
  command = f"$listMember:name [{testData['nameupdate']}]"
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
  assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def test_listMemberRange(capfd):
  command = f"$listMember:range [{testData['ranupdate']}]"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listMember:range", app.getDatas, 
                   Helpers.getStruct("integrante", ["rango"]))
  out, _ = capfd.readouterr()
  assert "**___Integrantes___** **___encontrados:___**" in out
  assert f"{testData['id']}" in out
  assert f"{testData['namecreate']}" in out
  assert f"{testData['rancreate']}" in out
  assert f"{testData['datecreate'].replace('-','/')}" in out
  assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def test_listMemberDate(capfd):
  command = f"$listMember:date [{testData['datecreate']}, "\
            f"{'datecreate'}]"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listMember:date", app.getDatas, 
                   Helpers.getStruct("integrante", ["date_1", "date_2"]))
  out, _ = capfd.readouterr()
  assert "**___Integrantes___** **___encontrados:___**" in out
  assert f"{testData['id']}" in out
  assert f"{testData['namecreate']}" in out
  assert f"{testData['rancreate']}" in out
  assert f"{testData['datecreate'].replace('-','/')}" in out
  assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def test_listMember_e(capfd):
  command = "$listMember > e"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listMember", app.getDatas, 
                   Helpers.getStruct("integrante"))
  out, _ = capfd.readouterr()
  assert "**___Integrantes___** **___encontrados:___**" in out
  assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_listMemberId_e(capfd):
  command = f"$listMember:id [{testData['id']}] > e"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listMember:id", app.getDatas, 
                   Helpers.getStruct("integrante", ["id"]))
  out, _ = capfd.readouterr()
  assert "**___Integrantes___** **___encontrados:___**" in out
  assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_listMemberName_e(capfd):
  command = f"$listMember:name [{testData['nameupdate']}] > e"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listMember:name", app.getDatas, 
                   Helpers.getStruct("integrante", ["name"]))
  out, _ = capfd.readouterr()
  assert "**___Integrantes___** **___encontrados:___**" in out
  assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_listMemberRange_e(capfd):
  command = f"$listMember:range [{testData['ranupdate']}] > e"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listMember:range", app.getDatas, 
                   Helpers.getStruct("integrante", ["rango"]))
  out, _ = capfd.readouterr()
  assert "**___Integrantes___** **___encontrados:___**" in out
  assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_listMemberDate_e(capfd):
  command = f"$listMember:date [{testData['datecreate']}, "\
            f"{'datecreate'}] > e"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listMember:date", app.getDatas, 
                   Helpers.getStruct("integrante", ["date_1", "date_2"]))
  out, _ = capfd.readouterr()
  assert "**___Integrantes___** **___encontrados:___**" in out
  assert "discord.file.File object" in out

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