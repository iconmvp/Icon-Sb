import discord
import json
import asyncio
import os
import requests
from discord.ext import command
from discord import embed


with open('config.json', 'r') as file:
    config_data = json.load(file)
    token = config_data["token"]
    prefix = config_data["prefix"]


intents = discord.Intents.default()

client = commands.Bot(prefix, intents=intents, help_command=None)

@client.event
async def on_ready():
  print(f"[+] Logged in as {client.user.name})
  print(f"[+] Client id : {client.user.id}")


@client.command(name='calc')
async def calculate(ctx, *, expression: str):
    await ctx.message.delete()
    try:

        result = eval(expression, {'__builtins__': None}, {})
    except Exception as e:

        await ctx.send(f"Error: {e}")
        return
    

    sent_msg = await ctx.send(f"# Calculation\n**__Input__** : {expression}\n**__Output__** : {result}")
    await asyncio.sleep(20)
    await sent_msg.delete()

@client.command(name='spam')
async def spam(ctx, count: int, *, message: str):

    for _ in range(count):
        sent_msg = await ctx.send(message)
        await asyncio.sleep(5)
        await sent_msg.delete()

