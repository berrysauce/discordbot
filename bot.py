import discord
from dotenv import load_dotenv
import os
import sys
from random import randint

bot = discord.Client()

@bot.event
async def on_ready():
  guild_count = 0
  
  for guild in bot.guilds:
    print('{0}:{1}'.format(guild.id, guild.name))
    guild_count = guild_count + 1
  
  await bot.change_presence(activity=discord.Game(name="on " + str(guild_count) + " servers | >help"))
  
  print("Bot is in " + str(guild_count) + " guilds")
  
@bot.event
async def on_message(message):
  if message.content == "hello":
    await message.channel.send("hey dirtbag")
    
bot.run('NzY1MjMzMzA5MTU1MzI4MDky.X4R1Dg.twuY9hToThfKfo15Y0EDoL3r6tU')