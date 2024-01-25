import os
dir = os.path.dirname(os.path.abspath(__file__))
dir = os.path.dirname(dir)
import sys
sys.path.insert(1, f'{dir}')
import pytest
from io import StringIO
from collections import namedtuple
from messageHandler import MessageHandler

Message = namedtuple('Message', ['author', 'content'])
Client = namedtuple('Client', ['user'])

@pytest.mark.asyncio
async def test_1(capfd):
  message = Message(author="test", content="$command")
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.inMsg()
  await hdlr.sendText()
  out, _ = capfd.readouterr()
  assert "hola mundo" in out

@pytest.mark.asyncio
async def test_2(capfd):
  message = Message(author="test", content="$help")
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.inMsg()
  await hdlr.helpMsg()
  out, _ = capfd.readouterr()
  assert "Guia de usuario" in out

  


