from http import client
import discord
import os
import praw
import random

#importing reddit id from env files
reddit = praw.Reddit(
    client_id=os.environ['client-id'],
    client_secret=os.environ['client-secret'],
    user_agent="<console:DiscordBot18-1.0>",
)

client=discord.Client();
@client.event

async def on_ready():
  
    #shows that the bot is online in the console
    
    print("we have logged in as {0.user}".format(client))
    
@client.event

async def on_message(message):
    str = message.content
    
    if(message.author == client.user):
        return
      
    if(message.content.startswith("!r")):
      subs = reddit.subreddit(str[3:]).top()

      post_to_pick = random.randint(1,100)

      for i in range(0,post_to_pick):
        submission = next(x for x in subs if not x.stickied)
        
      await message.channel.send(submission.url)

my_secret = os.environ['token']

client.run(my_secret)

