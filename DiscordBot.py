#Author Name: Kylie Fauquher
#Date: 3/5/2022
#Program Name: Fauquher_DiscordWelcomeBot
#Purpose: Connection to a Discord server that bot can welcome and mention new members in a channel of your choice.

import discord      
import random

#Your bot token you should have gotten from Discord Dev Portal.
TOKEN = 'INSERT TOKEN HERE'

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents = intents)

#This event is to turn on your bot and to let you know its working as intended.
@client.event
async def on_ready():
    print('{0.user} has gone online and is ready to get to work!'.format(client))

#This event will be how our bot welcomes new members
@client.event
async def on_member_join(member):

    #This number is my server ID, you can find this in your server settings under 'Widget'
    guild = client.get_guild(INSERT SERVER ID HERE)

    #This is your channel ID, this can be found by right clicking your channel. Make sure Developer Mode is on.
    channel = guild.get_channel(INSERT CHANNEL ID HERE)
    await channel.send(f'Welcome to the server {member.mention}! Thank you for the support! Stay cool! :sunglasses:')
   
   



#This will flip your bot online, you can confirm this by checking the channel your bot is in.
client.run(TOKEN)
