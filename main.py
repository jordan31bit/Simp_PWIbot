from commands import Commands
from apiDiscord import APIDiscord
import discord
from commands import Commands


com = Commands
client = discord.Client()
simp_api = APIDiscord()
discord_token = open("disc_token.cfg", "rt")

@client.event
async def on_ready():
        await client.change_presence(status=discord.Status.online, activity=discord.Game('Type "pwi help" for commands'))
        print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
        if message.author == client.user:
            return
        if message.content.lower().startswith('pwi'):
            tmp = await com.whichCommand(message.content)
            poop = await simp_api.determineWhat(tmp)
            await message.channel.send(embed=poop)

@client.event
async def sendAutoMesg(poop, message) :
        await message.channel.send(embed=poop)

client.run(discord_token.readline())