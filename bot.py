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

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.reactions = True
intents.messages = True
intents.emojis = True


#client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)
####################################################
# client commands are working:
# Client on_ready connect to Discord:


@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
    print(f'{bot.user} has connected to Discord!')
    print(f'{guild.name}(id: {guild.id})')

# Very basic hi/hello on_message event:
#@bot.event
#async def on_message(message):
    # if message.author == client.user:
    #     return
    #
    # if message.content.startswith('hi'):
    #     await message.channel.send('Hello!')

    #await bot.process_commands(message)


@bot.command()
async def react(ctx):
    def check(reaction, user):  # Our check for the reaction
        return user == ctx.message.author  # We check that only the authors reaction counts

    await ctx.send("Please react to the message!")  # Message to react to

    reaction = await bot.wait_for("reaction_add", check=check)  # Wait for a reaction
    await ctx.send(f"You reacted with: {reaction[0]}")  # With [0] we only display the emoji
    print(type(reaction[0]))

    myreact = str(reaction[0])
    if myreact in flag_to_lang:
        target_lang = flag_to_lang[myreact]
        response = f"You want to translate to: {target_lang}"
        print("If triggered.")
        await ctx.send(response)

# run the bot:
bot.run(TOKEN)
