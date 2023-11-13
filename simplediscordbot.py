import discord
from discord.ext import commands

def bot():

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

bot.run('MTE0OTEwODgwNzYyOTI5MTU1NA.GNHcPY.32rvJNkdc3UCUcV7JeexKvpoU4q1enTXw-k30A')