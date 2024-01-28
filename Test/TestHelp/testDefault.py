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
  assert "**___Guia de usuario de Avalon-bot___**" in out
  assert "Bienvenido/a a la guia de usuario del "\
         "bot de **⚜Avalon⚜** para discord. " in out
  assert "En esta seccion realizaremos una breve introduccion, "\
         "de las funciones principales que dispone **_Avalon-bot_**, "\
         "la estructura de la informacion con la que trabaja, "\
         "y como podemos utilizarlo para obtener importantes beneficios, "\
         "en el manejo y gestion de los datos asociados con la alianza."
  assert "**_¿Que es Avalon-bot?_**"
  assert "**_Avalon-bot_** es una herramienta pensada y diseñada "\
         "para facilitar al usuario la gestion de los "\
         "datos asociados con la alianza **⚜Avalon⚜**, "\
         "mediante la comprension de la estructura "\
         "de la informacion planteada para este proposito, "\
         "y la correcta utilizacion de los comandos dispuestos "\
         "para poder acceder y manipular dicha informacion. "\
         "Dicho esto, con Avalon-bot podras generar un "\
         "seguimiento automatizado y estructurado, "\
         "de datos relacionados con los ___integrantes___, "\
         "las ___asistencias___, los ___rangos___, "\
         "y los ___eventos___ establecidos en la alianza, "\
         "en conjunto con la capacidad de generar informes "\
         "personalizados en excel, gracias a la implementacion "\
         "de bases de datos SQL."
  assert "**_¿Como se encuentra estructurada la informacion?_**"
  
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