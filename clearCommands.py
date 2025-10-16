"""In the event you fuck up the commands by using a guild_id and global. use this to fix it"""

import discord
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    
    tree.clear_commands(guild=None)
    await tree.sync()
    print("Cleared global commands")
    
    guild_id = int(os.getenv('GUILD_ID')) if os.getenv('GUILD_ID') else None
    if guild_id:
        tree.clear_commands(guild=discord.Object(id=guild_id))
        await tree.sync(guild=discord.Object(id=guild_id))
        print(f"Cleared guild {guild_id} commands")
    
    await client.close()

client.run(os.getenv('DISCORD_TOKEN'))