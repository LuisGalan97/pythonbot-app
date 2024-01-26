import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Helpers.helpers import Helpers
from io import StringIO
from collections import namedtuple

Message = namedtuple('Message', ['author', 'content'])
Client = namedtuple('Client', ['user'])
app = AppHandler()

@pytest.mark.asyncio
async def testCRUDAssist(capfd):  
  #----------------------------Create---------------------------------------
  message = Message(author="test", content="$addAssist "\
                    "[Avalonicus, defprismaganada, 25-01-2024]")
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.contMsg("addAssist", app.setData, 
                     Helpers.setStruct("asistencia"))
  out, _ = capfd.readouterr()
  idTest = out[out.find("**_ID_** '"):]
  idTest = idTest[idTest.find("'")+1:idTest.find("'.")]
  assert f"**_ID_** '{idTest}'" in out
  #--------------------------Update:id--------------------------------------
  message = Message(author="test", content="$updAssist:id "\
                    f"[{idTest}, Avalonicus, defprismaganada, 25-01-2024]")
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.contMsg("updAssist:id", app.updateData, 
                     Helpers.updStruct("asistencia", "id"))
  out, _ = capfd.readouterr()
  assert "actualizado con exito" in out or "actualizada con exito" in out
    #--------------------------Delete:id--------------------------------------
  message = Message(author="test", content="$delAssist:id "\
                    f"[{idTest}]")
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.contMsg("delAssist:id", app.deleteData, 
                     Helpers.delStruct("asistencia", "id"))
  out, _ = capfd.readouterr()
  assert "eliminado con exito" in out or "eliminada con exito" in out


