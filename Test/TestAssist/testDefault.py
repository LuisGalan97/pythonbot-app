import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Helpers.helpers import Helpers
from collections import namedtuple

testData = {
  "id" : "",
  "memcreate" : "Avalonicus",
  "memupdate" : "Ammy",
  "evcreate" : "defprismaganada",
  "evupdate" : "avaconpelea",
  "datecreate" : "25-01-2100",
  "dateupdate" : "26-01-2100"
}

Message = namedtuple('Message', ['author', 'content'])
Client = namedtuple('Client', ['user'])
app = AppHandler()

@pytest.mark.asyncio
async def test_addAssist(capfd):
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
  assert "La ___asistencia___ ha sido creada con exito sobre el " in out
  assert f"**_ID_** \'{testData['id']}\'." in out

@pytest.mark.asyncio
async def test_listAssistId_add(capfd):
  command = f"$listAssist:id [{testData['id']}]"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listAssist:id", app.getDatas,
                    Helpers.getStruct("asistencia", ["id"]))
  out, _ = capfd.readouterr()
  assert "**___Asistencias___** **___encontradas:___**" in out
  assert f"{testData['id']}" in out
  assert f"{testData['memcreate']}" in out
  assert f"{testData['evcreate']}" in out
  assert f"{testData['datecreate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def test_updAssistId(capfd):
  command = f"$updAssist:id [{testData['id']}, {testData['memupdate']}, "\
            f"{testData['evupdate']}, {testData['dateupdate']}]"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.contMsg("updAssist:id", app.updateData,
                     Helpers.updStruct("asistencia", "id"))
  out, _ = capfd.readouterr()
  assert "La ___asistencia___ ha sido actualizada con exito." in out

@pytest.mark.asyncio
async def test_listAssist(capfd):
  command = "$listAssist"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listAssist", app.getDatas,
                    Helpers.getStruct("asistencia"))
  out, _ = capfd.readouterr()
  assert "**___Asistencias___** **___encontradas:___**" in out
  assert f"{testData['id']}" in out
  assert f"{testData['memupdate']}" in out
  assert f"{testData['evupdate']}" in out
  assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def test_listAssistId(capfd):
  command = f"$listAssist:id [{testData['id']}]"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listAssist:id", app.getDatas,
                    Helpers.getStruct("asistencia", ["id"]))
  out, _ = capfd.readouterr()
  assert "**___Asistencias___** **___encontradas:___**" in out
  assert f"{testData['id']}" in out
  assert f"{testData['memupdate']}" in out
  assert f"{testData['evupdate']}" in out
  assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def test_listAssistMember(capfd):
  command = f"$listAssist:member [{testData['memupdate']}]"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listAssist:member", app.getDatas,
                    Helpers.getStruct("asistencia", ["integrante"]))
  out, _ = capfd.readouterr()
  assert "**___Asistencias___** **___encontradas:___**" in out
  assert f"{testData['id']}" in out
  assert f"{testData['memupdate']}" in out
  assert f"{testData['evupdate']}" in out
  assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def test_listAssistEvent(capfd):
  command = f"$listAssist:event [{testData['evupdate']}]"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listAssist:event", app.getDatas,
                    Helpers.getStruct("asistencia", ["evento"]))
  out, _ = capfd.readouterr()
  assert "**___Asistencias___** **___encontradas:___**" in out
  assert f"{testData['id']}" in out
  assert f"{testData['memupdate']}" in out
  assert f"{testData['evupdate']}" in out
  assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def test_listAssistDate(capfd):
  command = f"$listAssist:date [{testData['dateupdate']}, "\
            f"{testData['dateupdate']}]"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listAssist:date", app.getDatas,
                   Helpers.getStruct("asistencia", ["date_1", "date_2"]))
  out, _ = capfd.readouterr()
  assert "**___Asistencias___** **___encontradas:___**" in out
  assert f"{testData['id']}" in out
  assert f"{testData['memupdate']}" in out
  assert f"{testData['evupdate']}" in out
  assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def test_listAssistMemberEvent(capfd):
  command = f"$listAssist:member&event [{testData['memupdate']}, "\
            f"{testData['evupdate']}]"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listAssist:member&event", app.getDatas,
                   Helpers.getStruct("asistencia", ["integrante", "evento"]))
  out, _ = capfd.readouterr()
  assert "**___Asistencias___** **___encontradas:___**" in out
  assert f"{testData['id']}" in out
  assert f"{testData['memupdate']}" in out
  assert f"{testData['evupdate']}" in out
  assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def test_listAssistMemberDate(capfd):
  command =f"$listAssist:member&date [{testData['memupdate']}, "\
           f"{testData['dateupdate']}, {testData['dateupdate']}]"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                   Helpers.getStruct("asistencia",
                                     ["integrante", "date_1", "date_2"]))
  out, _ = capfd.readouterr()
  assert "**___Asistencias___** **___encontradas:___**" in out
  assert f"{testData['id']}" in out
  assert f"{testData['memupdate']}" in out
  assert f"{testData['evupdate']}" in out
  assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def test_listAssistEventDate(capfd):
  command = f"$listAssist:event&date [{testData['evupdate']}, "\
            f"{testData['dateupdate']}, {testData['dateupdate']}]"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                    Helpers.getStruct("asistencia",
                                      ["evento", "date_1", "date_2"]))
  out, _ = capfd.readouterr()
  assert "**___Asistencias___** **___encontradas:___**" in out
  assert f"{testData['id']}" in out
  assert f"{testData['memupdate']}" in out
  assert f"{testData['evupdate']}" in out
  assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def test_listAssistMemberEventDate(capfd):
  command = f"$listAssist:member&event&date [{testData['memupdate']}, "\
            f"{testData['evupdate']}, {testData['dateupdate']}, "\
            f"{testData['dateupdate']}]"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listAssist:member&event&date",
                    app.getDatas, Helpers.getStruct("asistencia",
                    ["integrante", "evento", "date_1", "date_2"]))
  out, _ = capfd.readouterr()
  assert "**___Asistencias___** **___encontradas:___**" in out
  assert f"{testData['id']}" in out
  assert f"{testData['memupdate']}" in out
  assert f"{testData['evupdate']}" in out
  assert f"{testData['dateupdate'].replace('-','/')}" in out

@pytest.mark.asyncio
async def test_listAssist_e(capfd):
  command = "$listAssist > e"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listAssist", app.getDatas,
                    Helpers.getStruct("asistencia"))
  out, _ = capfd.readouterr()
  assert "**___Asistencias___** **___encontradas:___**" in out
  assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_listAssistId_e(capfd):
  command = f"$listAssist:id [{testData['id']}] > e"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listAssist:id", app.getDatas,
                    Helpers.getStruct("asistencia", ["id"]))
  out, _ = capfd.readouterr()
  assert "**___Asistencias___** **___encontradas:___**" in out
  assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_listAssistMember_e(capfd):
  command = f"$listAssist:member [{testData['memupdate']}] > e"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listAssist:member", app.getDatas,
                    Helpers.getStruct("asistencia", ["integrante"]))
  out, _ = capfd.readouterr()
  assert "**___Asistencias___** **___encontradas:___**" in out
  assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_listAssistEvent_e(capfd):
  command = f"$listAssist:event [{testData['evupdate']}] > e"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listAssist:event", app.getDatas,
                    Helpers.getStruct("asistencia", ["evento"]))
  out, _ = capfd.readouterr()
  assert "**___Asistencias___** **___encontradas:___**" in out
  assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_listAssistDate_e(capfd):
  command = f"$listAssist:date [{testData['dateupdate']}, "\
            f"{testData['dateupdate']}] > e"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listAssist:date", app.getDatas,
                   Helpers.getStruct("asistencia", ["date_1", "date_2"]))
  out, _ = capfd.readouterr()
  assert "**___Asistencias___** **___encontradas:___**" in out
  assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_listAssistMemberDate_e(capfd):
  command = f"$listAssist:member&date [{testData['memupdate']}, "\
            f"{testData['dateupdate']}, {testData['dateupdate']}] > e"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                   Helpers.getStruct("asistencia",
                                     ["integrante", "date_1", "date_2"]))
  out, _ = capfd.readouterr()
  assert "**___Asistencias___** **___encontradas:___**" in out
  assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_listAssistEventDate_e(capfd):
  command = f"$listAssist:event&date [{testData['evupdate']}, "\
            f"{testData['dateupdate']}, {testData['dateupdate']}] > e"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                    Helpers.getStruct("asistencia",
                                      ["evento", "date_1", "date_2"]))
  out, _ = capfd.readouterr()
  assert "**___Asistencias___** **___encontradas:___**" in out
  assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_listAssistMemberEventDate_e(capfd):
  command = f"$listAssist:member&event&date [{testData['memupdate']}, "\
            f"{testData['evupdate']}, {testData['dateupdate']}, "\
            f"{testData['dateupdate']}] > e"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listAssist:member&event&date",
                    app.getDatas, Helpers.getStruct("asistencia",
                                                    ["integrante", "evento",
                                                     "date_1", "date_2"]))
  out, _ = capfd.readouterr()
  assert "**___Asistencias___** **___encontradas:___**" in out
  assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_delAssistId(capfd):
  command = f"$delAssist:id [{testData['id']}]"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.contMsg("delAssist:id", app.deleteData,
                     Helpers.delStruct("asistencia", "id"))
  out, _ = capfd.readouterr()
  assert "La ___asistencia___ ha sido eliminada con exito." in out