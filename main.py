import discord
import json
import asyncio
import os
from discord.ext import commands



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

  
