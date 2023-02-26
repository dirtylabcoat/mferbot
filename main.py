import os
import discord
import string
from discord.ext import commands

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='.', intents=intents)


@client.event
async def on_ready():
  print('{0.user} is online'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  print(
    f'ChannelId: {message.channel.id}, Author: {message.author}, Message: {message.content}'
  )
  msg = message.content
  await message.channel.send(
    msg.rstrip(string.punctuation + ' ') + ', motherfucker.')


client.run(DISCORD_TOKEN)
