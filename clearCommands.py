"""

In the event the commands are fucked up use this to purge them all.
I think i got the issue fixed but imma leave this here just in case. 

"""


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