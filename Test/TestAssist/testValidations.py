import pytest
from messageHandler import MessageHandler
from appHandler import AppHandler
from Helpers.helpers import Helpers
from collections import namedtuple

testData = {
    "id" : "",
    "member" : "Avalonicus",
    "memnoexist" : "Member-[noexist]",
    "event" : "defprismaganada",
    "evnoexist" : "Event-[noexist]",
    "date" : "25-01-2100",
}

Message = namedtuple('Message', ['author', 'content'])
Client = namedtuple('Client', ['user'])
app = AppHandler()

@pytest.mark.asyncio
async def test_addAssist_membernoexist(capfd):
    commands = [f"$addAssist [{testData['memnoexist']}, "\
                f"{testData['event']}, {testData['date']}]",
                f"$addAssist [  {testData['memnoexist']}  , "\
                f"{testData['event']}, {testData['date']}]",
                f"$addAssist [  {testData['memnoexist']}  , "\
                f"{testData['evnoexist']}, {testData['date']}]",
                f"$addAssist [  {testData['memnoexist']}  , "\
                f"  {testData['evnoexist']}  , {testData['date']}]",
                f"$addAssist [  {testData['memnoexist']}  , "\
                f"  {testData['evnoexist']}  , {testData['date']}] "\
                 "FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addAssist", app.setData,
                           Helpers.setStruct("asistencia"))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['memnoexist']}' "\
                "ingresado en el campo "\
                "**_Integrante_** no fue encontrado en la "\
                "base de datos.\n" in out
        
@pytest.mark.asyncio
async def test_addAssist_eventnoexist(capfd):
    commands = [f"$addAssist [{testData['member']}, "\
                f"{testData['evnoexist']}, {testData['date']}]",
                f"$addAssist [  {testData['member']}  , "\
                f"{testData['evnoexist']}, {testData['date']}]",
                f"$addAssist [  {testData['member']}  , "\
                f"{testData['evnoexist']}, {testData['date']}]",
                f"$addAssist [  {testData['member']}  , "\
                f"  {testData['evnoexist']}  , {testData['date']}]",
                f"$addAssist [  {testData['member']}  , "\
                f"  {testData['evnoexist']}  , {testData['date']}] "\
                 "FILL"]
    for command in commands:
        message = Message(author="test", content=command)
        client = Client(user="test")
        hdlr = MessageHandler(message, client, True)
        await hdlr.contMsg("addAssist", app.setData,
                           Helpers.setStruct("asistencia"))
        out, _ = capfd.readouterr()
        assert f"El valor '{testData['evnoexist']}' "\
                "ingresado en el campo "\
                "**_Integrante_** no fue encontrado en la "\
                "base de datos.\n" in out