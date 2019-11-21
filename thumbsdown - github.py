import random
import time
import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
bot = commands.Bot(command_prefix='~')


class MyClient(discord.Client):
    async def on_message(self, message):
        if str(message.author.id) == '':   # insert user ID here
            await message.add_reaction('👎')


client = MyClient()
client.run('')

