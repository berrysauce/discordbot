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

bot = commands.Bot(command_prefix='>')

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
  guild_count = 0
  
  print('Logged in as')
  print(bot.user.name)
  print(bot.user.id)
  print('------')
  
  for guild in bot.guilds:
    print('{0} : {1}'.format(guild.id, guild.name))
    guild_count = guild_count + 1
  
  await bot.change_presence(activity=discord.Game(name="on " + str(guild_count) + " servers | >help"))
  
  print("Bot is in " + str(guild_count) + " guilds")
    
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def random(ctx, min, max):
    try:
      min = int(min)
      max = int(max)
      await ctx.send(str(randint(min, max)))
    except:
      await ctx.send(str(ctx.author) + ", how do you think I can calculate with text? Go back to school.")
    
bot.run(DISCORD_TOKEN)