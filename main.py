# This example requires the 'message_content' intent.
import sys
import os
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
    
    if message.content.startswith('$enviar_archivo'):
        # Crear un archivo de ejemplo
        contenido_archivo = "Contenido del archivo de ejemplo."
        with open("archivo_ejemplo.txt", "w", encoding="utf-8") as archivo:
            archivo.write(contenido_archivo)

        # Crear un objeto de tipo discord.File con el archivo
        archivo_discord = discord.File("archivo_ejemplo.txt")

        # Enviar el archivo al canal donde se recibió el mensaje
        await message.channel.send(file=archivo_discord)

        # Eliminar el archivo local (opcional)
        os.remove("archivo_ejemplo.txt")

    if message.content.startswith('$comando'):
        await message.channel.send('Respuesta del bot en discord')

client.run(Config.TOKEN)
#Este token es valido unicamente para el servidor Omega-xis