import discord
from dotenv import load_dotenv
import os
import sys
from random import randint

bot = discord.Client()
#load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")
    #bot.Game("Online on {0} servers".format(guild_count))

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
	if message.content == "hello":
		await message.channel.send("hey dirtbag")


bot.run('NzY1MjMzMzA5MTU1MzI4MDky.X4R1Dg.twuY9hToThfKfo15Y0EDoL3r6tU')
