import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv


def get_language_code(flag_emoji):
    # Mapping of flag emojis to language codes
    flag_to_lang = {
        '🇺🇸': 'EN',  # English
        '🇪🇸': 'ES',  # Spanish
        '🇫🇷': 'FR',  # French
        '🇩🇪': 'DE',  # German
        '🇮🇹': 'IT',  # Italian
        '🇵🇹': 'PT',  # Portuguese
        '🇳🇱': 'NL',  # Dutch
        '🇸🇪': 'SV',  # Swedish
        '🇩🇰': 'DA',  # Danish
        '🇳🇴': 'NO',  # Norwegian
        '🇫🇮': 'FI',  # Finnish
        '🇷🇺': 'RU',  # Russian
        '🇨🇳': 'ZH',  # Chinese
        '🇯🇵': 'JA',  # Japanese
        '🇰🇷': 'KO',  # Korean
    }
    return flag_to_lang.get(flag_emoji)

flag_to_lang = {
        '🇺🇸': 'EN',  # English
        '🇪🇸': 'ES',  # Spanish
        '🇫🇷': 'FR',  # French
        ':flag_de:': 'German',  # German
        '🇮🇹': 'IT',  # Italian
        '🇵🇹': 'PT',  # Portuguese
        '🇳🇱': 'NL',  # Dutch
        '🇸🇪': 'SV',  # Swedish
        '🇩🇰': 'DA',  # Danish
        '🇳🇴': 'NO',  # Norwegian
        '🇫🇮': 'FI',  # Finnish
        '🇷🇺': 'RU',  # Russian
        '🇨🇳': 'ZH',  # Chinese
        '🇯🇵': 'JA',  # Japanese
        '🇰🇷': 'KO',  # Korean
    }

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)
# bot commands aren't working:
@bot.command(name='ping')
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


@bot.command()
async def test(ctx, arg):
    pass
    await ctx.send(arg)
####################################################
# client commands are working:
# Client on_ready connect to Discord:
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(f'{client.user} has connected to Discord!')
    print(f'{guild.name}(id: {guild.id})')

# Very basic hi/hello on_message event:
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hi'):
        await message.channel.send('Hello!')

@bot.command()
async def react(ctx):
    #def check(reaction, user):  # Our check for the reaction
    reaction = await bot.wait_for("reaction_add", check=check)  # Wait for a reaction
    await ctx.send(f"You reacted with: {reaction[0]}")  # With [0] we only display the emoji

    # if message.content.split()[1] in flag_to_lang:
    #     flag_emoji = message.content.split()[1]
    #     target_lang = get_language_code(flag_emoji)
    #     response = f"You want to translate to: {target_lang}"
    #     await message.channel.send(response)

# run the bot:
client.run(TOKEN)
