from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ""
TOKEN = ""

cleint - Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="your emotions"))
    print("Logged in as " + client.user.name)

@client.command(name='greet',
                description='greets the person who mention the bot',)
async def greet(context):
    await client.say("Hello " + context.message.author.mention, + ":wave:")
