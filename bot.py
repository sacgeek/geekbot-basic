import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(command_prefix='>', intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(f'{client.user} has connected to Discord!')
    print(f'{guild.name}(id: {guild.id})')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hi'):
        await message.channel.send('Hello!')

@bot.command(name='ping')
async def ping(ctx, arg):
    await ctx.send("Pong! " +str(round(client.latency * 1000))+"ms")


@bot.command()
async def test(ctx, arg):
    pass
    await ctx.send(arg)

client.run(TOKEN)
