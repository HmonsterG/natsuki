import discord, os, time
from discord.ext import commands
bot = commands.Bot(command_prefix=">")
bot.remove_command("help")
class init:
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")
    @bot.event
    async def on_ready():
        await bot.change_presence(activity=discord.Game("You're cute | >help"))
        print(f'{bot.user.name} has connected!')      
bot.run("NzY2NzI1ODI2NDI2OTYxOTkw.X4njEg.S53dKTPsz5rlBywLNXmglUO5BI0")
