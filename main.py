# from time import sleep
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import query_server
from ast import For, arg
import asyncio
from cgi import test
from concurrent.futures import thread
from email import message
from turtle import ontimer
from unicodedata import name
from commands import Commands
from apiDiscord import APIDiscord
# import logging
from time import sleep, time
import threading
import discord
from commands import Commands


com = Commands
client = discord.Client()
simp_api = APIDiscord()
discord_token = open("disc_token.cfg", "rt")

@client.event
async def on_ready():
        await client.change_presence(status=discord.Status.online, activity=discord.Game('enter "pwi help" for commands'))
        print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
        if message.author == client.user:
            return
        if message.content.lower().startswith('pwi'):
            tmp = await com.whichCommand(message.content)
            poop = await simp_api.determineWhat(tmp)
            #poop = await genericBuilder(tmp)
            await message.channel.send(embed=poop)

@client.event
async def sendAutoMesg(poop, message) :
        await message.channel.send(embed=poop)

# @client.event
# async def on_timer() :
#     # if message.content.startswith("timer"):
#         print("Im in boobies! Thread 2 started.")
#         latency = await com.whichCommand("ping")
#         poop = await simp_api.determineWhat(latency)
#         await sendAutoMesg(poop, message)

# def start_bot() :
#     print("im here")
#     print("Atfer the running client.")

# def test() :
#     print("This is just a test")

# t1 = threading.Thread(target=start_bot)
# # t2 = threading.Thread(target=boobies)
# t3 = threading.Thread(target=test)
# # t1.start()
# # t1.join()
# #on_timer()
client.run(discord_token.readline())









#bot_start.join()
#timer_loop_thread.join()

    # tmp = await com.whichCommand(message.content)
    # poop = await determineWhat(tmp)
    # #poop = await genericBuilder(tmp)
    # await message.channel.send(embed=poop)
    # time.sleep(60)


# totalTime = c.pingServer()
# print(totalTime)
# bob = APIDiscord()

# logging.basicConfig(level=logging.INFO)
# url = "https://www.pwdatabase.com/pwi/npc/44395"
# url2 = "https://www.pwdatabase.com/pwi/search_item finger+bead"
# page = urlopen(url)
# html = page.read().decode("utf-8")
# soup = BeautifulSoup(html, "html.parser")
# foo = soup.find(width=200)
# bar = list(foo.children)[3]
# print(bar.get_text())
# resp = urlopen(url)
# parsed = resp.read().decode("utf-8")
#print(parsed)
#print(totalTime)
#print(repr(response))