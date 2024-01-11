import sys
sys.path.insert(1, './DF')
from dataframe import DataFrame
from appHandler import AppHandler

class MessageHandler:
    def __init__(self, message, client):
        self.__message = message
        self.__client = client
        self.__appHandler = AppHandler()
        self.handle_initial_message()
    
    async def handle_initial_message(self):
        if self.message.author == self.client.user:
            return
    
    async def handle_message(self, command, message):
        if self.message.content.startswith(f'${command}'):
            await self.send_integrantes_message(message)


    
