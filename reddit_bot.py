from discord import Game
from discord.ext.commands import Bot
import praw


BOT_PREFIX = "!"
TOKEN = "NTI1NzE5NDU3MTkzMjYzMTE0.Dv7hcg.yUUTBPFZKpdQrfVKnR5Fk-2-X2U"

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="memes"))
    print( "Logged in as " + client.user.name)

@client.command(name="searchred",description='searchs reddit for subredits based on user input')
async def searchred(t, c, l):
    try:
        reddit = praw.Reddit(client_id ="fuBC5Y6gFB2UJQ", client_secret="75JGu6vAiSS6Fa8XDok4eKHx5lw", username="LandedUnicorn",password="MAsseff3ct!",user_agent="pdiscordbotv1")
    except:
        client.say("Cannont connect to reddit at the moment, try again later?")
    
    topic = reddit.subreddit("%s" (t))
    if c == "hot":
        new_topic = topic.hot(limit = l)
    elif c == "new":
        new_topic = topic.new(limit = l)
    elif c == "rising":
        new_topic = topic.rising(limit = l)
    elif c == "controversial":
        new_topic = topic.controversial(limit = l)
    else:
        client.say("Sorry, Thats not a category i know")
    
    if new_topic:
        for sub in new_topic:
            if not sub.stickied:
                client.say("Title : {} ups: {}, downs:{} ".format(sub.title, sub.ups, sub.downs)


client.run(TOKEN)