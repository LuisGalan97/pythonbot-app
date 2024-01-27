import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Helpers.helpers import Helpers
from collections import namedtuple

testData = {
  "id" : "",
  "namecreate" : "TestRange",
  "nameupdate" : "TestRangeUpd",
  "controlcreate" : 2,
  "controlupdate" : 3,
  "descreate" : "Descripción creada",
  "desupdate" : "Descripción modificada"
}

Message = namedtuple('Message', ['author', 'content'])
Client = namedtuple('Client', ['user'])
app = AppHandler()

@pytest.mark.asyncio
async def test_addRange(capfd):
  command = f"$addRange [{testData['namecreate']}, "\
            f"{testData['controlcreate']}, {testData['descreate']}]"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.contMsg("addRange", app.setData,
                     Helpers.setStruct("rango"))
  out, _ = capfd.readouterr()
  idTest = out[out.find("**_ID_** '"):]
  testData["id"] = idTest[idTest.find("'")+1:idTest.find("'.")]
  assert "El ___rango___ ha sido creado con exito sobre el " in out
  assert f"**_ID_** \'{testData['id']}\'." in out

@pytest.mark.asyncio
async def test_listRangeId_add(capfd):
  command = f"$listRange:id [{testData['id']}]"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listRange:id", app.getDatas,
                   Helpers.getStruct("rango", ["id"]))
  out, _ = capfd.readouterr()
  assert "**___Rangos___** **___encontrados:___**" in out
  assert f"{testData['id']}" in out
  assert f"{testData['namecreate']}" in out
  assert f"{testData['controlcreate']}" in out
  assert f"{testData['descreate']}" in out

@pytest.mark.asyncio
async def test_listRangeName_add(capfd):
  command = f"$listRange:name [{testData['namecreate']}]"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listRange:name", app.getDatas,
                   Helpers.getStruct("rango", ["name"]))
  out, _ = capfd.readouterr()
  assert "**___Rangos___** **___encontrados:___**" in out
  assert f"{testData['id']}" in out
  assert f"{testData['namecreate']}" in out
  assert f"{testData['controlcreate']}" in out
  assert f"{testData['descreate']}" in out

@pytest.mark.asyncio
async def test_updRangeId(capfd):
  command = f"$updRange:id [{testData['id']}, {testData['nameupdate']}, "\
            f"{testData['controlupdate']}, {testData['descreate']}]"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.contMsg("updRange:id", app.updateData,
                     Helpers.updStruct("rango", "id"))
  out, _ = capfd.readouterr()
  assert "El ___rango___ ha sido actualizado con exito." in out

@pytest.mark.asyncio
async def test_updRangeName(capfd):
  command = f"$updRange:name [{testData['nameupdate']}, "\
            f"{testData['controlupdate']}, {testData['desupdate']}]"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.contMsg("updRange:name", app.updateData,
                     Helpers.updStruct("rango", "name"))
  out, _ = capfd.readouterr()
  assert "El ___rango___ ha sido actualizado con exito." in out

@pytest.mark.asyncio
async def test_listRange(capfd):
  command = "$listRange"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listRange", app.getDatas,
                   Helpers.getStruct("rango"))
  out, _ = capfd.readouterr()
  assert "**___Rangos___** **___encontrados:___**" in out
  assert f"{testData['id']}" in out
  assert f"{testData['nameupdate']}" in out
  assert f"{testData['controlupdate']}" in out
  assert f"{testData['desupdate']}" in out

@pytest.mark.asyncio
async def test_listRangeId(capfd):
  command = f"$listRange:id [{testData['id']}]"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listRange:id", app.getDatas,
                   Helpers.getStruct("rango", ["id"]))
  out, _ = capfd.readouterr()
  assert "**___Rangos___** **___encontrados:___**" in out
  assert f"{testData['id']}" in out
  assert f"{testData['nameupdate']}" in out
  assert f"{testData['controlupdate']}" in out
  assert f"{testData['desupdate']}" in out

@pytest.mark.asyncio
async def test_listRangeName(capfd):
  command = f"$listRange:name [{testData['nameupdate']}]"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listRange:name", app.getDatas,
                   Helpers.getStruct("rango", ["name"]))
  out, _ = capfd.readouterr()
  assert "**___Rangos___** **___encontrados:___**" in out
  assert f"{testData['id']}" in out
  assert f"{testData['nameupdate']}" in out
  assert f"{testData['controlupdate']}" in out
  assert f"{testData['desupdate']}" in out

@pytest.mark.asyncio
async def test_listRange_e(capfd):
  command = "$listRange > e"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listRange", app.getDatas,
                   Helpers.getStruct("rango"))
  out, _ = capfd.readouterr()
  assert "**___Rangos___** **___encontrados:___**" in out
  assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_listRangeId_e(capfd):
  command = f"$listRange:id [{testData['id']}] > e"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listRange:id", app.getDatas,
                   Helpers.getStruct("rango", ["id"]))
  out, _ = capfd.readouterr()
  assert "**___Rangos___** **___encontrados:___**" in out
  assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_listRangeName_e(capfd):
  command = f"$listRange:name [{testData['nameupdate']}] > e"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listRange:name", app.getDatas,
                   Helpers.getStruct("rango", ["name"]))
  out, _ = capfd.readouterr()
  assert "**___Rangos___** **___encontrados:___**" in out
  assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_delRangeId(capfd):
  command = f"$delRange:id [{testData['id']}]"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.contMsg("delRange:id", app.deleteData,
                     Helpers.delStruct("rango", "id"))
  out, _ = capfd.readouterr()
  assert "El ___rango___ ha sido eliminado con exito." in out

@pytest.mark.asyncio
async def test_addRange_DelName(capfd):
  command = f"$addRange [{testData['namecreate']}, "\
            f"{testData['controlcreate']}, {testData['descreate']}]"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.contMsg("addRange", app.setData,
                     Helpers.setStruct("rango"))
  out, _ = capfd.readouterr()
  idTest = out[out.find("**_ID_** '"):]
  testData["id"] = idTest[idTest.find("'")+1:idTest.find("'.")]
  assert "El ___rango___ ha sido creado con exito sobre el " in out
  assert f"**_ID_** \'{testData['id']}\'." in out

@pytest.mark.asyncio
async def test_delRangeName(capfd):
  command = f"$delRanges:name [{testData['namecreate']}]"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.contMsg("delRange:name", app.deleteData,
                     Helpers.delStruct("rango", "name"))
  out, _ = capfd.readouterr()
  assert "El ___rango___ ha sido eliminado con exito." in out