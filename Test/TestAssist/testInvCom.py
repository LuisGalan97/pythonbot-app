import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Helpers.helpers import Helpers
from collections import namedtuple

Message = namedtuple('Message', ['author', 'content'])
Client = namedtuple('Client', ['user'])
app = AppHandler()

@pytest.mark.asyncio
async def test_addAssist_invalidStruct(capfd):
    commands = ["$addAssist", "$addAssist ",
                "$addAssist[", "$addAssist [",
                "$addAssistFILL[", "$addAssist]",
                "$addAssist ]", "$addAssistFILL []",
                "$addAssist FILL []", "$addAssist [FILL",
                "$addAssist[FILL", "$addAssist [ FILL",
                "$addAssist FILL]", "$addAssist FILL ] "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addAssist", app.setData,
                           Helpers.setStruct("asistencia"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$addAssist [_Integrante, Evento, Fecha_]**\n" in out

@pytest.mark.asyncio
async def test_updAssistId_invalidStruct(capfd):
    commands = ["$updAssist:id", "$updAssist:id ",
                "$updAssist:id[", "$updAssist:id [",
                "$updAssist:idFILL[", "$updAssist:id]",
                "$updAssist:id ]", "$updAssist:idFILL []",
                "$updAssist:id FILL []", "$updAssist:id [FILL",
                "$updAssist:id[FILL", "$updAssist:id [ FILL",
                "$updAssist:id FILL]", "$updAssist:id FILL ] "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("updAssist:id", app.updateData,
                           Helpers.updStruct("asistencia", "id"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$updAssist:id [_ID, Integrante, Evento, Fecha_]**\n" in out

@pytest.mark.asyncio
async def test_delAssistId_invalidStruct(capfd):
    commands = ["$delAssist:id", "$delAssist:id ",
                "$delAssist:id[", "$delAssist:id [",
                "$delAssist:idFILL[", "$delAssist:id]",
                "$delAssist:id ]", "$delAssist:idFILL []",
                "$delAssist:id FILL []", "$delAssist:id [FILL",
                "$delAssist:id[FILL", "$delAssist:id [ FILL",
                "$delAssist:id FILL]", "$delAssist:id FILL ] "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("delAssist:id", app.deleteData,
                           Helpers.delStruct("asistencia", "id"))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$delAssist:id [_ID_]**\n" in out

@pytest.mark.asyncio
async def test_listAssistId_invalidStruct(capfd):
    commands = ["$listAssist:id", "$listAssist:id ",
                "$listAssist:id[", "$listAssist:id [",
                "$listAssist:idFILL[", "$listAssist:id]",
                "$listAssist:id ]", "$listAssist:idFILL []",
                "$listAssist:id FILL []", "$listAssist:id [FILL",
                "$listAssist:id[FILL", "$listAssist:id [ FILL",
                "$listAssist:id FILL]", "$listAssist:id FILL ] "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:id", app.getDatas,
                         Helpers.getStruct("asistencia", ["id"]))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listAssist:id [_ID_]**\n" in out

@pytest.mark.asyncio
async def test_listAssistMember_invalidStruct(capfd):
    commands = ["$listAssist:member", "$listAssist:member ",
                "$listAssist:member[", "$listAssist:member [",
                "$listAssist:memberFILL[", "$listAssist:member]",
                "$listAssist:member ]", "$listAssist:memberFILL []",
                "$listAssist:member FILL []", "$listAssist:member [FILL",
                "$listAssist:member[FILL", "$listAssist:member [ FILL",
                "$listAssist:member FILL]", "$listAssist:member FILL ] "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member", app.getDatas,
                         Helpers.getStruct("asistencia", ["integrante"]))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listAssist:member [_Integrante_]**\n" in out

@pytest.mark.asyncio
async def test_listAssistEvent_invalidStruct(capfd):
    commands = ["$listAssist:event", "$listAssist:event ",
                "$listAssist:event[", "$listAssist:event [",
                "$listAssist:eventFILL[", "$listAssist:event]",
                "$listAssist:event ]", "$listAssist:eventFILL []",
                "$listAssist:event FILL []", "$listAssist:event [FILL",
                "$listAssist:event[FILL", "$listAssist:event [ FILL",
                "$listAssist:event FILL]", "$listAssist:event FILL ] "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:event", app.getDatas,
                         Helpers.getStruct("asistencia", ["evento"]))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listAssist:event [_Evento_]**\n" in out

@pytest.mark.asyncio
async def test_listAssistDate_invalidStruct(capfd):
    commands = ["$listAssist:date", "$listAssist:date ",
                "$listAssist:date[", "$listAssist:date [",
                "$listAssist:dateFILL[", "$listAssist:date]",
                "$listAssist:date ]", "$listAssist:dateFILL []",
                "$listAssist:date FILL []", "$listAssist:date [FILL",
                "$listAssist:date[FILL", "$listAssist:date [ FILL",
                "$listAssist:date FILL]", "$listAssist:date FILL ] "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listAssist:date [_Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def test_listAssistMemberEvent_invalidStruct(capfd):
    commands = ["$listAssist:member&event", "$listAssist:member&event ",
                "$listAssist:member&event[", "$listAssist:member&event [",
                "$listAssist:member&eventFILL[", "$listAssist:member&event]",
                "$listAssist:member&event ]",
                "$listAssist:member&eventFILL []",
                "$listAssist:member&event FILL []",
                "$listAssist:member&event [FILL",
                "$listAssist:member&event[FILL",
                "$listAssist:member&event [ FILL",
                "$listAssist:member&event FILL]",
                "$listAssist:member&event FILL ] "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "evento"]))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listAssist:member&event [_Integrante, Evento_]**\n" in out

@pytest.mark.asyncio
async def test_listAssistMemberDate_invalidStruct(capfd):
    commands = ["$listAssist:member&date", "$listAssist:member&date ",
                "$listAssist:member&date[", "$listAssist:member&date [",
                "$listAssist:member&dateFILL[", "$listAssist:member&date]",
                "$listAssist:member&date ]", "$listAssist:member&dateFILL []",
                "$listAssist:member&date FILL []",
                "$listAssist:member&date [FILL",
                "$listAssist:member&date[FILL",
                "$listAssist:member&date [ FILL",
                "$listAssist:member&date FILL]",
                "$listAssist:member&date FILL ] "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listAssist:member&date "\
               "[_Integrante, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def test_listAssistEventDate_invalidStruct(capfd):
    commands = ["$listAssist:event&date", "$listAssist:event&date ",
                "$listAssist:event&date[", "$listAssist:event&date [",
                "$listAssist:event&dateFILL[", "$listAssist:event&date]",
                "$listAssist:event&date ]", "$listAssist:event&dateFILL []",
                "$listAssist:event&date FILL []",
                "$listAssist:event&date [FILL",
                "$listAssist:event&date[FILL",
                "$listAssist:event&date [ FILL",
                "$listAssist:event&date FILL]",
                "$listAssist:event&date FILL ] "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:event&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["evento", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listAssist:event&date "\
               "[_Evento, Fecha 1, Fecha 2_]**\n" in out

@pytest.mark.asyncio
async def test_listAssistMemberEventDate_invalidStruct(capfd):
    commands = ["$listAssist:member&event&date",
                "$listAssist:member&event&date ",
                "$listAssist:member&event&date[",
                "$listAssist:member&event&date [",
                "$listAssist:member&event&dateFILL[",
                "$listAssist:member&event&date]",
                "$listAssist:member&event&date ]",
                "$listAssist:member&event&dateFILL []",
                "$listAssist:member&event&date FILL []",
                "$listAssist:member&event&date [FILL",
                "$listAssist:member&event&date[FILL",
                "$listAssist:member&event&date [ FILL",
                "$listAssist:member&event&date FILL]",
                "$listAssist:member&event&date FILL ] "]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.dFMsg("listAssist:member&event&date", app.getDatas,
                         Helpers.getStruct("asistencia",
                         ["integrante", "evento", "date_1", "date_2"]))
        out, _ = capfd.readouterr()
        assert "El comando debe mantener la forma:\n" in out
        assert "**$listAssist:member&event&date "\
               "[_Integrante, Evento, Fecha 1, Fecha 2_]**\n" in out