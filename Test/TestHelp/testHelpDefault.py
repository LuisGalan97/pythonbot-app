from messageHandler import MessageHandler
import pytest
from io import StringIO
from collections import namedtuple

Message = namedtuple('Message', ['author', 'content'])
Client = namedtuple('Client', ['user'])

@pytest.mark.asyncio
async def testDefault(capfd):
  message = Message(author="test", content="$command")
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.inMsg()
  await hdlr.sendText()
  out, _ = capfd.readouterr()
  assert "hola mundo" in out

@pytest.mark.asyncio
async def testHelp(capfd):
  message = Message(author="test", content="$help")
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.inMsg()
  await hdlr.helpMsg()
  out, _ = capfd.readouterr()
  assert "Guia de usuario" in out
  assert "$help:range" in out

@pytest.mark.asyncio
async def testHelpDiagram(capfd):
  message = Message(author="test", content="$help:diagram")
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.inMsg()
  await hdlr.helpMsg()
  out, _ = capfd.readouterr()
  assert "discord.file.File object" in out

@pytest.mark.asyncio
async def testHelpAssist(capfd):
  message = Message(author="test", content="$help:assist")
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.inMsg()
  await hdlr.helpMsg()
  out, _ = capfd.readouterr()
  assert "Asistencias" in out
  assert "listAssist:member&event&date" in out

@pytest.mark.asyncio
async def testHelpEvent(capfd):
  message = Message(author="test", content="$help:event")
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.inMsg()
  await hdlr.helpMsg()
  out, _ = capfd.readouterr()
  assert "Eventos" in out
  assert "listEvent:name" in out

@pytest.mark.asyncio
async def testHelpMember(capfd):
  message = Message(author="test", content="$help:member")
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.inMsg()
  await hdlr.helpMsg()
  out, _ = capfd.readouterr()
  assert "Integrantes" in out
  assert "listMember:date" in out

@pytest.mark.asyncio
async def testHelpRange(capfd):
  message = Message(author="test", content="$help:range")
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.inMsg()
  await hdlr.helpMsg()
  out, _ = capfd.readouterr()
  assert "Rangos" in out
  assert "listRange:name" in out