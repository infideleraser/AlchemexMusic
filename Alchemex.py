import discord
from discord import guild
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import random
import sys, os
import datetime
import sys, os
import logging
import music

def get_prefix(bot, message):
    """A callable Prefix for my bot."""
    prefix = ['music ']
    return commands.when_mentioned_or(*prefix)(bot, message)
bot = commands.Bot(command_prefix=get_prefix, description="Alchemex Music Bot")

extensions = ['music']

for ext in extensions:
    bot.load_extension(ext)

logging.basicConfig(level='INFO')
logger = logging.getLogger('Alchemex.py')



@bot.event
async def on_ready():
    print('\nI am ' + bot.user.name + f" bot with the id: {bot.user.id}\n")
    while True:
        await bot.change_presence( activity=discord.Activity(type=2, name=f'{len(bot.users)} users'))
        await asyncio.sleep(20)
        await bot.change_presence( activity=discord.Activity(type=3, name=f'{len(bot.guilds)} servers'))
        await asyncio.sleep(30)

with open("Token.txt") as fp:
    token = fp.read().strip()

bot.run(token)







