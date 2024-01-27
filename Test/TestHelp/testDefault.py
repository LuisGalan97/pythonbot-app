import pytest
from messageHandler import MessageHandler
from collections import namedtuple

Message = namedtuple('Message', ['author', 'content'])
Client = namedtuple('Client', ['user'])

@pytest.mark.asyncio
async def test_command(capfd):
  command = "$command"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.inMsg()
  await hdlr.sendText()
  out, _ = capfd.readouterr()
  assert "hola mundo" in out

@pytest.mark.asyncio
async def test_help(capfd):
  command = "$help"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.inMsg()
  await hdlr.helpMsg()
  out, _ = capfd.readouterr()
  assert "Guia de usuario" in out
  assert "$help:range" in out

@pytest.mark.asyncio
async def test_helpDiagram(capfd):
  command = "$help:diagram"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.inMsg()
  await hdlr.helpMsg()
  out, _ = capfd.readouterr()
  assert "Diagrama de la estructura de los datos" in out
  assert "discord.file.File object" in out

@pytest.mark.asyncio
async def test_helpAssist(capfd):
  command = "$help:assist"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.inMsg()
  await hdlr.helpMsg()
  out, _ = capfd.readouterr()
  assert "Asistencias" in out
  assert "listAssist:member&event&date" in out

@pytest.mark.asyncio
async def test_helpEvent(capfd):
  command = "$help:event"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.inMsg()
  await hdlr.helpMsg()
  out, _ = capfd.readouterr()
  assert "Eventos" in out
  assert "listEvent:name" in out

@pytest.mark.asyncio
async def test_helpMember(capfd):
  command = "$help:member"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.inMsg()
  await hdlr.helpMsg()
  out, _ = capfd.readouterr()
  assert "Integrantes" in out
  assert "listMember:date" in out

@pytest.mark.asyncio
async def test_helpRange(capfd):
  command = "$help:range"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.inMsg()
  await hdlr.helpMsg()
  out, _ = capfd.readouterr()
  assert "Rangos" in out
  assert "listRange:name" in out