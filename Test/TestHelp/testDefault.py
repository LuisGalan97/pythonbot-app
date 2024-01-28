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
  assert "**___Guia de usuario de Avalon-bot___**\n" in out
  assert "Bienvenido/a a la guia de usuario del "\
         "bot de **⚜Avalon⚜** para discord.\n" in out
  assert "En esta seccion realizaremos una breve introduccion, "\
         "de las funciones principales que dispone **_Avalon-bot_**, "\
         "la estructura de la informacion con la que trabaja, "\
         "y como podemos utilizarlo para obtener importantes beneficios, "\
         "en el manejo y gestion de los datos asociados con la alianza.\n"
  assert "**_¿Que es Avalon-bot?_**\n" in out
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
         "de bases de datos SQL.\n" in out
  assert "**_¿Como se encuentra estructurada la informacion?_**\n" in out
  assert "Para la organizacion, gestion y guardado de la informacion, "\
         "**_Avalon-bot_** tiene programada la interaccion con "\
         "una base de datos SQLite en lenguaje python, "\
         "teniendo acceso a un gestor de base de datos ligero, "\
         "donde se encuentra cargada una estructura de 4 tablas "\
         "relacionadas entre si, pensadas para almacenar la "\
         "informacion de 4 datos principales: ___integrantes___, "\
         "___asistencias___, ___rangos___ y ___eventos___, "\
         "con el fin de permitir la disposicion de por ejemplo "\
         "una tabla de ___rangos___ de alianza, que "\
         "posteriormente podra ser relacionada a un "\
         "___integrante___ de la tabla de ___integrantes___, "\
         "conservando la independencia de ambas tablas con sus "\
         "datos propios y facilitando de esta forma su "\
         "manipulacion. De forma similar la tabla ___eventos___ "\
         "e ___integrantes___ pueden relacionarse o asociarse "\
         "con la tabla de ___asistencias___, con el fin de "\
         "registrar, que en una ___asistencia___ estuvo "\
         "presente un ___integrante___ y fue con respecto a un "\
         "___evento___ especifico, los cuales tambien se "\
         "encuentran en sus respectivas tablas.\n" in out
  
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