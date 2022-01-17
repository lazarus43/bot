import discord
from discord.ext.commands import bot
from discord.ext import commands
import random
import asyncio
import time
 
##prefix##
bot = commands.Bot(command_prefix='!')
 
##BOT IS READY##
@bot.event
async def on_ready():
    print("Bot Is Online! And Ready To Spam")
 
##SPAM COMMAND##
@bot.command(pass_context=True)
async def spam(ctx): #run "!spam" to run the command
    while True:
        await ctx.send("The Klan has existed in three distinct eras.The Klan has existed in three distinct eras.The Klan has existed in three distinct eras.")
        await ctx.send("The Klan has existed in three distinct eras.The Klan has existed in three distinct eras.The Klan has existed in three distinct eras.The Klan has existed in three distinct eras.The Klan has existed in three distinct eras.\n")
        await ctx.send("\The Klan has existed in three distinct eras.The Klan has existed in three distinct eras.The Klan has existed in three distinct eras.The Klan has existed in three distinct eras.The Klan has existed in three distinct eras.\n")
        
bot.run ("your token here")
