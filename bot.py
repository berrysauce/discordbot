import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import sys
from random import randint
import logging

#set up logger
#logger = logging.getLogger('discord')
#logger.setLevel(logging.DEBUG)
#handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
#handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
#logger.addHandler(handler)

description = "An example bot which was made with Python."
bot = commands.Bot(command_prefix='>', description=description)

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
  guild_count = 0
  
  print("Logged in as")
  print(bot.user.name)
  print(bot.user.id)
  print("------")
  
  for guild in bot.guilds:
    print("{0} : {1}".format(guild.id, guild.name))
    guild_count = guild_count + 1
  
  await bot.change_presence(activity=discord.Game(name="on " + str(guild_count) + " servers | >help"))
  
  print("Bot is in " + str(guild_count) + " guilds")
    
@bot.command(description="Test command which returns ping time", help="Test command which returns ping time")
async def ping(ctx):
  await ctx.send("Pong! Bot latency: {0}".format(bot.latency))
    
@bot.command(description="Generates random numbers", help="Generates random numbers")
async def random(ctx, min, max):
  try:
    min = int(min)
    max = int(max)
    await ctx.send(str(randint(min, max)))
  except:
    await ctx.send(str(ctx.author) + ", how do you think I can calculate with text? Go back to school.")

@bot.command(description="Lists some info about the bot", help="Lists some info about the bot")
async def about(ctx):
  embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
  embedVar.add_field(name="Field1", value="hi", inline=False)
  embedVar.add_field(name="Field2", value="hi2", inline=False)
  await ctx.channel.send(embed=embedVar)
    
bot.run(DISCORD_TOKEN)