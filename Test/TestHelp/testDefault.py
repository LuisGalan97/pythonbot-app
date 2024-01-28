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
         "bot de **⚜Avalon⚜** para discord. "\
         "En esta seccion realizaremos una breve introduccion, "\
         "de las funciones principales que dispone **_Avalon-bot_**, "\
         "la estructura de la informacion con la que trabaja, "\
         "y como podemos utilizarlo para obtener importantes beneficios, "\
         "en el manejo y gestion de los datos asociados "\
         "con la alianza.\n" in out
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
  assert "_Si desea visualizar el diagrama de la estructura de "\
         "los datos, puede emplear el comando de ayuda:_\n" in out
  assert "* **$help:diagram**\n" in out
  assert "**_¿Como puedo empezar a utilizar Avalon-bot?_**\n" in out
  assert "Para poder utilizar **_Avalon-bot_**, debes emplear "\
         "los comandos dispuestos por este mismo, los cuales "\
         "varian dependiendo de la tabla con la que deseas "\
         "interactuar, y el tipo de solicitud que deseas realizar "\
         "(consulta, creacion, actualizacion o eliminacion). "\
         "Con lo anterior, dada la extension de los comandos, "\
         "estos se han especificado y detallado en su propia "\
         "seccion asociada con cada tabla respectiva, siendo "\
         "visibles mediante los comandos de ayuda que se "\
         "presentan a continuacion.\n" in out
  assert "_Comandos de_ ___asistencias___:\n" in out
  assert "** * $help:assist**\n" in out
  assert "_Comandos de_ ___eventos___:\n" in out
  assert "** * $help:event**\n" in out
  assert "_Comandos de_ ___integrantes___:\n" in out
  assert "** * $help:member**\n" in out
  assert "_Comandos de_ ___rangos___:\n" in out
  assert "** * $help:range**\n" in out

@pytest.mark.asyncio
async def test_helpDiagram(capfd):
  command = "$help:diagram"
  message = Message(author="test", content=command)
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.inMsg()
  await hdlr.helpMsg()
  out, _ = capfd.readouterr()
  assert "**___Diagrama de la estructura de los datos:___**" in out
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
  assert "**___Asistencias___**\n" in out
  assert "Las ___asistencias___ hacen referencia a una serie de "\
         "registros de todas las participaciones, en las cuales "\
         "los integrantes de **⚜Avalon⚜** han podido hacer parte, "\
         "para actividades o eventos tales como ataques, defensas, "\
         "AVAs, entre otros. Una ___asistencia___ por defecto "\
         "contiene informacion de un ___integrante___ y "\
         "___evento___ asociado, junto con la fecha del suceso "\
         "en cuestion. Con lo anterior, se presentan una lista "\
         "de todos los comandos que permiten interactuar con los "\
         "registros de ___asistencias___.\n" in out
  assert "_Comandos de modificacion:_\n" in out
  assert "- **$addAssist [_Integrante, Evento, Fecha_]**   ->   "\
         "Añade una nueva ___asistencia___, ingresando dentro "\
         "de los corchetes **[ ]** un parametro **_Integrante_** "\
         "como valor de texto asociado al nombre de un "\
         "___integrante___, un parametro **_Evento_** como valor "\
         "de texto asociado al nombre de un ___evento___ y un "\
         "parametro **_Fecha_** como valor de fecha en "\
         "'Día-Mes-Año'.\n" in out
  assert "- **$updAssist:id [_ID, Integrante, Evento, Fecha_]**   "\
         "->   Actualiza los datos de una ___asistencia___ "\
         "apuntando a su identificador, ingresando dentro de los "\
         "corchetes **[ ]** un parametro **_ID_** como valor "\
         "numerico, un parametro **_Integrante_** como valor de "\
         "texto asociado al nombre de un ___integrante___, un "\
         "parametro **_Evento_** como valor de texto asociado "\
         "al nombre de un ___evento___ y un parametro **_Fecha_** "\
         "como valor de fecha en 'Día-Mes-Año'.\n" in out
  assert "- **$delAssist:id [_ID_]**   ->   Elimina una "\
         "___asistencia___ apuntando a su identificador, "\
         "ingresando dentro de los corchetes **[ ]** un parametro "\
         "**_ID_** como valor numerico.\n" in out
  assert "_Comandos de consulta:_\n" in out
  assert "- **$listAssist**   ->   Lista todas las "\
         "___asistencias___.\n" in out
  assert "- **$listAssist:id [_ID_]**    ->   Lista la "\
         "___asistencia___ asociada al parametro **_ID_** ingresado "\
         "dentro de los corchetes **[ ]**. Este parametro **_ID_** "\
         "deberá corresponder a un valor numerico.\n" in out
  assert "- **$listAssist:member [_Integrante_]**    ->   Lista "\
         "todas las ___asistencias___ asociadas al parametro "\
         "**_Integrante_** ingresado dentro de los corchetes "\
         "**[ ]**, en relacion al nombre del ___integrante___ "\
         "presente en la ___asistencia___. Este parametro "\
         "**_Integrante_** deberá corresponder "\
         "a un valor de texto.\n" in out
  assert "- **$listAssist:event [_Evento_]**    ->   Lista todas "\
         "las ___asistencias___ asociadas al parametro "\
         "**_Evento_** ingresado dentro de los corchetes **[ ]**, "\
         "en relacion al nombre del ___evento___ presente en la "\
         "___asistencia___. Este parametro **_Evento_** deberá "\
         "corresponder a un valor de texto.\n" in out
  assert "- **$listAssist:date [_Fecha 1, Fecha 2_]**    ->   "\
         "Lista todas las ___asistencias___ registradas entre "\
         "las fechas **_Fecha 1_** y **_Fecha 2_**, ingresadas "\
         "como parametros dentro de los corchetes **[ ]**. "\
         "Estos parametros **_Fecha 1_** y **_Fecha 2_** deberán "\
         "corresponder a valores de fecha en 'Día-Mes-Año'.\n" in out
  assert "- **$listAssist:member&event [_Integrante, Evento_]**    "\
         "->   Lista todas las ___asistencias___ asociadas a los "\
         "parametros **_Integrante_** y **_Evento_** ingresados "\
         "dentro de los corchetes **[ ]**, en relacion al nombre "\
         "del ___integrante___ y al nombre del ___evento___ "\
         "presentes en la ___asistencia___. Ambos parametros "\
         "**_Integrante_** y **_Evento_** deberán "\
         "corresponder a valores de texto.\n" in out
  assert "- **$listAssist:member&date [_Integrante, Fecha 1, "\
         "Fecha 2_]**    ->   Lista todas las ___asistencias___ "\
         "asociadas al parametro **_Integrante_** en relacion "\
         "al nombre del ___integrante___ presente en la "\
         "___asistencia___, y registradas entre las fechas "\
         "**_Fecha 1_** y **_Fecha 2_**, todos ingresados como "\
         "parametros dentro de los corchetes **[ ]**. El parametro "\
         "**_Integrante_** deberá corresponder a un valor de "\
         "texto y los parametros **_Fecha 1_** y **_Fecha 2_** "\
         "deberán corresponder a valores "\
         "de fecha en 'Día-Mes-Año'.\n" in out
  assert "- **$listAssist:event&date [_Evento, Fecha 1, "\
         "Fecha 2_]**    ->   Lista todas las ___asistencias___ "\
         "asociadas al parametro **_Evento_** en relacion al "\
         "nombre del ___evento___ presente en la ___asistencia___, "\
         "y registradas entre las fechas **_Fecha 1_** y "\
         "**_Fecha 2_**, todos ingresados como parametros dentro "\
         "de los corchetes **[ ]**. El parametro **_Evento_** "\
         "deberá corresponder a un valor de texto y los parametros "\
         "**_Fecha 1_** y **_Fecha 2_** deberán corresponder a "\
         "valores de fecha en 'Día-Mes-Año'.\n" in out
  assert "- **$listAssist:member&event&date [_Integrante, Evento, "\
         "Fecha 1, Fecha 2_]**    ->   Lista todas las "\
         "___asistencias___ asociadas a los parametros "\
         "**_Integrante_** y **_Evento_**, en relacion al nombre "\
         "del ___integrante___ y al nombre del ___evento___ "\
         "presentes en la ___asistencia___, y registradas entre "\
         "las fechas **_Fecha 1_** y **_Fecha 2_**, todos "\
         "ingresados como parametros dentro de los corchetes "\
         "**[ ]**. Los parametros **_Integrante_** y **_Evento_** "\
         "deberán corresponder a valores de texto, y los parametros "\
         "**_Fecha 1_** y **_Fecha 2_** deberán corresponder a "\
         "valores de fecha en 'Día-Mes-Año'.\n" in out
  assert "_Comandos de consulta con impresion en excel:_\n" in out
  assert "Por defecto, los comandos de consulta imprimen los "\
         "registros en el canal de discord, sin embargo, tambien "\
         "pueden ser impresos dentro de una hoja de excel, si "\
         "despues del comando se especifica "\
         "el parametro **> e**.\n" in out
  assert "- **$listAssist > e**   ->   Lista "\
         "en una hoja de excel todas las "\
         "___asistencias___.\n" in out
  assert "- **$listAssist:id [_ID_] > e**   ->   Lista "\
         "en una hoja de excel la "\
         "___asistencia___ asociada al parametro **_ID_** ingresado "\
         "dentro de los corchetes **[ ]**. Este parametro **_ID_** "\
         "deberá corresponder a un valor numerico.\n" in out
  assert "- **$listAssist:member [_Integrante_] > e**   ->   Lista "\
         "en una hoja de excel "\
         "todas las ___asistencias___ asociadas al parametro "\
         "**_Integrante_** ingresado dentro de los corchetes "\
         "**[ ]**, en relacion al nombre del ___integrante___ "\
         "presente en la ___asistencia___. Este parametro "\
         "**_Integrante_** deberá corresponder "\
         "a un valor de texto.\n" in out
  assert "- **$listAssist:event [_Evento_] > e**   ->   Lista "\
         "en una hoja de excel todas "\
         "las ___asistencias___ asociadas al parametro "\
         "**_Evento_** ingresado dentro de los corchetes **[ ]**, "\
         "en relacion al nombre del ___evento___ presente en la "\
         "___asistencia___. Este parametro **_Evento_** deberá "\
         "corresponder a un valor de texto.\n" in out
  assert "- **$listAssist:date [_Fecha 1, Fecha 2_] > e**   ->   "\
         "Lista en una hoja de excel "\
         "todas las ___asistencias___ registradas entre "\
         "las fechas **_Fecha 1_** y **_Fecha 2_**, ingresadas "\
         "como parametros dentro de los corchetes **[ ]**. "\
         "Estos parametros **_Fecha 1_** y **_Fecha 2_** deberán "\
         "corresponder a valores de fecha en 'Día-Mes-Año'.\n" in out
  assert "- **$listAssist:member&event [_Integrante, Evento_] > e**   "\
         "->   Lista en una hoja de excel "\
         "todas las ___asistencias___ asociadas a los "\
         "parametros **_Integrante_** y **_Evento_** ingresados "\
         "dentro de los corchetes **[ ]**, en relacion al nombre "\
         "del ___integrante___ y al nombre del ___evento___ "\
         "presentes en la ___asistencia___. Ambos parametros "\
         "**_Integrante_** y **_Evento_** deberán "\
         "corresponder a valores de texto.\n" in out
  assert "- **$listAssist:member&date [_Integrante, Fecha 1, "\
         "Fecha 2_] > e**   ->   Lista en una hoja de excel"\
         "todas las ___asistencias___ "\
         "asociadas al parametro **_Integrante_** en relacion "\
         "al nombre del ___integrante___ presente en la "\
         "___asistencia___, y registradas entre las fechas "\
         "**_Fecha 1_** y **_Fecha 2_**, todos ingresados como "\
         "parametros dentro de los corchetes **[ ]**. El parametro "\
         "**_Integrante_** deberá corresponder a un valor de "\
         "texto y los parametros **_Fecha 1_** y **_Fecha 2_** "\
         "deberán corresponder a valores "\
         "de fecha en 'Día-Mes-Año'.\n" in out
  assert "- **$listAssist:event&date [_Evento, Fecha 1, "\
         "Fecha 2_] > e**   ->   Lista en una hoja de excel "\
         "todas las ___asistencias___ "\
         "asociadas al parametro **_Evento_** en relacion al "\
         "nombre del ___evento___ presente en la ___asistencia___, "\
         "y registradas entre las fechas **_Fecha 1_** y "\
         "**_Fecha 2_**, todos ingresados como parametros dentro "\
         "de los corchetes **[ ]**. El parametro **_Evento_** "\
         "deberá corresponder a un valor de texto y los parametros "\
         "**_Fecha 1_** y **_Fecha 2_** deberán corresponder a "\
         "valores de fecha en 'Día-Mes-Año'.\n" in out
  assert "- **$listAssist:member&event&date [_Integrante, Evento, "\
         "Fecha 1, Fecha 2_] > e**   ->   Lista "\
         "en una hoja de excel todas las "\
         "___asistencias___ asociadas a los parametros "\
         "**_Integrante_** y **_Evento_**, en relacion al nombre "\
         "del ___integrante___ y al nombre del ___evento___ "\
         "presentes en la ___asistencia___, y registradas entre "\
         "las fechas **_Fecha 1_** y **_Fecha 2_**, todos "\
         "ingresados como parametros dentro de los corchetes "\
         "**[ ]**. Los parametros **_Integrante_** y **_Evento_** "\
         "deberán corresponder a valores de texto, y los parametros "\
         "**_Fecha 1_** y **_Fecha 2_** deberán corresponder a "\
         "valores de fecha en 'Día-Mes-Año'.\n" in out

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