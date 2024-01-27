import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Helpers.helpers import Helpers
from collections import namedtuple

testData = {
  "id" : "",
  "namecreate" : "TestEvent",
  "nameupdate" : "TestEventUpd",
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
  assert f"{testData['descreate'].replace('-','/')}" in out

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
  assert f"{testData['descreate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def test_updEventId(capfd):
  command = f"$updEvent:id [{testData['id']}, {testData['nameupdate']}, "\
            f"{testData['pointupdate']}, {testData['descreate']}]"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.contMsg("updEvent:id", app.updateData, 
                     Helpers.updStruct("evento", "id"))
  out, _ = capfd.readouterr()
  assert "El ___evento___ ha sido actualizado con exito" in out

@pytest.mark.asyncio
async def test_updEventName(capfd):
  command = f"$updEvent:name [{testData['nameupdate']}, "\
            f"{testData['pointupdate']}, {testData['desupdate']}]"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.contMsg("updEvent:name", app.updateData, 
                     Helpers.updStruct("evento", "name"))
  out, _ = capfd.readouterr()
  assert "El ___evento___ ha sido actualizado con exito" in out

@pytest.mark.asyncio
async def test_listEvent(capfd):
  command = "$listEvent"
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
  assert f"{testData['desupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def test_listEventId(capfd):
  command = f"$listEvent:id [{testData['id']}]"
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
  assert f"{testData['desupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def test_listEventName(capfd):
  command = f"$listEvent:name [{testData['nameupdate']}]"
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
  assert f"{testData['desupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def test_listEvent_e(capfd):
  command = "$listEvent > e"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listEvent", app.getDatas, 
                   Helpers.getStruct("evento"))
  out, _ = capfd.readouterr()
  assert "**___Eventos___** **___encontrados:___**" in out
  assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_listEventId_e(capfd):
  command = f"$listEvent:id [{testData['id']}] > e"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listEvent:id", app.getDatas, 
                   Helpers.getStruct("evento", ["id"]))
  out, _ = capfd.readouterr()
  assert "**___Eventos___** **___encontrados:___**" in out
  assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_listEventName_e(capfd):
  command = f"$listEvent:name [{testData['nameupdate']}] > e"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listEvent:name", app.getDatas, 
                   Helpers.getStruct("evento", ["name"]))
  out, _ = capfd.readouterr()
  assert "**___Eventos___** **___encontrados:___**" in out
  assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_delEventId(capfd):
  command = f"$delEvent:id [{testData['id']}]"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.contMsg("delEvent:id", app.deleteData, 
                     Helpers.delStruct("evento", "id"))
  out, _ = capfd.readouterr()
  assert "El ___evento___ ha sido eliminado con exito" in out

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
  command = f"$delEvent:Name [{testData['namecreate']}]"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.contMsg("delEvent:name", app.deleteData, 
                     Helpers.delStruct("evento", "name"))
  out, _ = capfd.readouterr()
  assert "El ___evento___ ha sido eliminado con exito" in out