import pytest
import asyncio
from messageHandler import MessageHandler
from appHandler import AppHandler
from Helpers.helpers import Helpers
from io import StringIO
from collections import namedtuple

testData = {
  "id" : "",
  "memcreate" : "Avalonicus",
  "memupdate" : "Ammy",
  "evcreate" : "defprismaganada",
  "evupdate" : "avaconpelea",
  "datecreate" : "25-01-2020",
  "dateupdate" : "26-01-2021"
}

Message = namedtuple('Message', ['author', 'content'])
Client = namedtuple('Client', ['user'])
app = AppHandler()

@pytest.mark.asyncio
async def test_addAssist(capfd):  
  message = Message(author="test", content="$addAssist "\
                    f"[{testData['memcreate']}, {testData['evcreate']}, "\
                    f"{testData['datecreate']}]")
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.contMsg("addAssist", app.setData, 
                     Helpers.setStruct("asistencia"))
  out, _ = capfd.readouterr()
  idTest = out[out.find("**_ID_** '"):]
  testData["id"] = idTest[idTest.find("'")+1:idTest.find("'.")]
  assert f"**_ID_** \'{testData['id']}\'" in out

@pytest.mark.asyncio
async def test_listAssistId_add(capfd):  
  message = Message(author="test", content=f"$listAssist:id "\
                    f"[{testData['id']}]")
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
  message = Message(author="test", content="$updAssist:id "\
                    f"[{testData['id']}, {testData['memupdate']}, "\
                    f"{testData['evupdate']}, {testData['dateupdate']}]")
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.contMsg("updAssist:id", app.updateData, 
                     Helpers.updStruct("asistencia", "id"))
  out, _ = capfd.readouterr()
  assert "La ___asistencia___ ha sido actualizada con exito" in out

@pytest.mark.asyncio
async def test_listAssist(capfd):  
  message = Message(author="test", content="$listAssist")
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listAssist", app.getDatas, 
                    Helpers.getStruct("asistencia"))
  out, _ = capfd.readouterr()
  assert "**___Asistencias___** **___encontradas:___**" in out
  assert f"{testData['id']}" in out

@pytest.mark.asyncio
async def test_listAssistId(capfd):  
  message = Message(author="test", content=f"$listAssist:id "\
                    f"[{testData['id']}]")
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
  message = Message(author="test", content=f"$listAssist:member "\
                    f"[{testData['memupdate']}]")
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
  message = Message(author="test", content=f"$listAssist:event "\
                    f"[{testData['evupdate']}]")
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
  message = Message(author="test", content=f"$listAssist:date "\
                    f"[{testData['dateupdate']}, {testData['dateupdate']}]")
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
async def test_listAssist_e(capfd):  
  message = Message(author="test", content="$listAssist > e")
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listAssist", app.getDatas, 
                    Helpers.getStruct("asistencia"))
  out, _ = capfd.readouterr()
  assert "**___Asistencias___** **___encontradas:___**" in out
  assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_listAssistId_e(capfd):  
  message = Message(author="test", content=f"$listAssist:id "\
                    f"[{testData['id']}] > e")
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listAssist:id", app.getDatas, 
                    Helpers.getStruct("asistencia", ["id"]))
  out, _ = capfd.readouterr()
  assert "**___Asistencias___** **___encontradas:___**" in out
  assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_listAssistMember_e(capfd):  
  message = Message(author="test", content=f"$listAssist:member "\
                    f"[{testData['memupdate']}] > e")
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listAssist:member", app.getDatas, 
                    Helpers.getStruct("asistencia", ["integrante"]))
  out, _ = capfd.readouterr()
  assert "**___Asistencias___** **___encontradas:___**" in out
  assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_listAssistEvent_e(capfd):  
  message = Message(author="test", content=f"$listAssist:event "\
                    f"[{testData['evupdate']}] > e")
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.dFMsg("listAssist:event", app.getDatas, 
                    Helpers.getStruct("asistencia", ["evento"]))
  out, _ = capfd.readouterr()
  assert "**___Asistencias___** **___encontradas:___**" in out
  assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_delAssistId(capfd):  
  message = Message(author="test", content="$delAssist:id "\
                    f"[{testData['id']}]")
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.contMsg("delAssist:id", app.deleteData, 
                     Helpers.delStruct("asistencia", "id"))
  out, _ = capfd.readouterr()
  assert "La ___asistencia___ ha sido eliminada con exito" in out
