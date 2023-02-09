import discord
from discord.ext import commands

import functionsList

intents = discord.Intents.default()

intents.message_content = True

app = commands.Bot(command_prefix='>',intents = intents)
 
@app.event
async def on_ready():
    print(f'logged in as {app.user}')
    await app.change_presence(status=discord.Status.online, activity=None)

@app.event
async def on_message(message):
    if message.author.bot: # 봇이 보낸 메시지이면 반응하지 않게 합니다
        return
    
    stringTemp = message.content
    print("bot returns")
    await message.channel.send(functionsList.aLine(stringTemp))
    return

@app.command()
async def bot(ctx):
    await ctx.reply('Hi, there!')
    
app.run('여기에는 토큰을 넣는 거에요.')