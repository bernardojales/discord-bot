import discord
from discord import Intents
from discord import client

intents = discord.Intents.default()

client = discord.Client(intents=intents)

intents.message_content = True

@client.event
async def on_ready():

    print ("The bot is online")
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if str(message.author) == "Kazuki#4933":
        #if str(message.content).lower() == "hello":
            await message.channel.send("Olá")
            await message.channel.send("Como posso ajudar?")
    if str(message.content).lower() == "hello bot":
        await message.add_reaction("\U0001F44B")

client.run('MTEwNzkxODk2MTE1ODQwNjE4NA.G6oJ8o.LD0g-FFOB0AuqwFY6-RXtTdpisuGkJipQBr3Xk')