import discord
import random
import time
from discord import Member
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot, has_permissions
bot = commands.Bot(command_prefix="~")

chances = range(1, 5)

uwus = ['uwu', '(´・ω・｀)', '(*´∇｀)ﾉ', '(◕‿◕✿)', 'ღ(U꒳Uღ)', '(⁄˘⁄ ⁄ ω⁄ ⁄ ˘⁄)♡']


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if " " in message.content:
            person = message.author
            shot = random.choice(chances)
            if shot == 4:
                if message.author == self.user:
                    return
                else:
                    user = message.author
                    message = str(message)
                    thing = []
                    for bread in message:
                        thing.append(bread)
                    if 'l' in thing:
                        message.replace('l', 'w')
                    await message.channel.send(message)


# l > w, r > w, th > w,
client = MyClient()
client.run('')
bot.run('')
