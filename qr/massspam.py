import discord
import random
import os

token = input('Entrer your token > ')
guild = input('Entrer server id > ')
client = discord.Client(status=discord.Status.online)

sentList = []

@client.event
async def on_ready():
    print("I am logged into the account {0.user}".format(client))
    print("I am waiting for a message to be sent to the server and I will send the QR Code")

@client.event
async def on_message(message):
    if message.guild.id == int(guild) and message.author.id not in sentList:
        sentList.append(message.author.id)
        print(f"sending -> {message.author.name}")
        await message.author.send("V")
        await message.author.send(file=discord.File(f"out/{random.choice(os.listdir('out'))}"))
client.run(token, bot=False)
