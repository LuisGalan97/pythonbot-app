import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Helpers.helpers import Helpers
from io import StringIO
from collections import namedtuple

Message = namedtuple('Message', ['author', 'content'])
Client = namedtuple('Client', ['user'])
app = AppHandler()
idTest = None

@pytest.mark.asyncio
async def testAddAssist(capfd):  
  message = Message(author="test", content="$addAssist [Avalonicus, defprismaganada, 25-01-2024]")
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.inMsg()
  await hdlr.contMsg("addAssist", app.setData, Helpers.setStruct("asistencia"))
  out, _ = capfd.readouterr()
  idTest = out[out.find("**_ID_** '"):]
  idTest = idTest[idTest.find("'")+1:idTest.find("'.")]
  assert f"**_ID_** '{idTest}'" in out

async def testDelAssist(capfd):  
  message = Message(author="test", content=f"$delAssist:id [{idTest}]")
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.inMsg()
  await hdlr.contMsg("delAssist:id", app.deleteData, Helpers.delStruct("asistencia", "id"))
  out, _ = capfd.readouterr()
  assert "exito" in out


