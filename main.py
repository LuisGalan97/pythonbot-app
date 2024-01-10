# This example requires the 'message_content' intent.
import sys
sys.path.insert(1, './Config')
from config import Config
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$comando'):
        await message.channel.send('Respuesta del bot en discord')

client.run(Config.TOKEN)
#Este token es valido unicamente para el servidor Omega-xis