import discord
from discord.ext import commands
import os
import asyncio
from utils.config import basicconfig
from dotenv import load_dotenv


intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)
bot.help_command = None

loaded_extensions = []



# Loading all the cogs
async def load_all_extensions():
    """Asynchronously loads all the extensions (cogs) from the cogs folder."""
    
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"[LOGS] Successfully loaded {filename[:-3]}")
        else:
            pass
    

@bot.event
async def on_ready():
    if basicconfig.use_env is True or False or 'true' or 'false':   
        await load_all_extensions()
        

        synced = await bot.tree.sync()
        print(f"Synced slash commands: {len(synced)}")
        print(f'Bot username: {bot.user}')
    else:
        exit('\n[ERROR] The use_env setting only allows True or False\n')



import logging
handler = logging.FileHandler(filename="logs.log",mode="w", encoding="utf-8")

if basicconfig.use_env is True:
    load_dotenv()
    bot.run(token=os.getenv('TOKEN'), log_handler=handler)
else:
    bot.run(token=basicconfig.TOKEN, log_handler=handler)