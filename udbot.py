import discord
from discord import Member
from discord.ext import commands
from discord.ext.commands import Bot
import urbandictionary as ud
import json
bot = commands.Bot(command_prefix='~')


@bot.command()
async def random(ctx):
    rand = ud.random()
    for things in rand:
        thing = str(things)
        await ctx.send("```" + thing + "```")
        break
bot.run('')