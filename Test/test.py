import asyncio
from io import StringIO
from collections import namedtuple
from messageHandler import MessageHandler

Message = namedtuple('Message', ['author', 'content'])
Client = namedtuple('Client', ['user'])

async def test():
  message = Message(author="test", content="$probando")
  client = Client(user="test")
  hdlr = MessageHandler(message, client, True)
  await hdlr.inMsg()
  await hdlr.sendText()


asyncio.run(test())
