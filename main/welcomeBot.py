import discord
from discord import Intents
from discord import client
from discord.ext import commands

intents = discord.Intents.default()

client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!')

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
        
#command add role

@bot.command()
async def add_role(ctx, member: discord.Member, role_name: str):
    role = discord.utils.get(ctx.guild.roles, name=role_name)
    if role:
        await member.add_roles(role)
        await ctx.send(f"Added {role_name} role to {member.display_name}")
    else:
        await ctx.send(f"Role {role_name} not found.")
        
## command remove role

@bot.command()
async def remove_role(ctx, member: discord.Member, role_name: str):
    role = discord.utils.get(ctx.guild.roles, name=role_name)
    if role:
        await member.remove_roles(role)
        await ctx.send(f"Removed {role_name} role from {member.display_name}")
    else:
        await ctx.send(f"Role {role_name} not found.")

@bot.command()
async def ban_user(ctx, member: discord.Member):
    await member.ban()
    await ctx.send(f"{member.display_name} has been banned from the server.")

client.run('MTEwNzkxODk2MTE1ODQwNjE4NA.G6oJ8o.LD0g-FFOB0AuqwFY6-RXtTdpisuGkJipQBr3Xk')