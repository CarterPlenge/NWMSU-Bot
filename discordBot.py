import discord
from discord import app_commands
from dotenv import load_dotenv
from commands import register_all

load_dotenv()

class DiscordBot:
    def __init__(self, guild_id):
        intents = discord.Intents.default()
        self.client = discord.Client(intents=intents)
        self.tree = app_commands.CommandTree(self.client)
        self.guild_id = guild_id    # guild id == server id; leave as None to omit this
        
        self._setup_events()

    def _setup_events(self):
        """Sets up event handlers"""

        @self.client.event
        async def on_ready(): # Print info once bot is ready
            register_all(self.tree, self.guild_id)
            await self.tree.sync(guild=discord.Object(id=self.guild_id))
            print(f"Logged in as {self.client.user}")

        @self.client.event 
        async def on_message(message): # when a message is sent
            await self.handle_message(message)
            
    async def handle_message(self, message):
        """
        Put functionality here if you want to do
        somthing on basic messages.
        """
        return
    
    def run(self, token):
        self.client.run(token)

if __name__ == "__main__":
    import os
    
    TOKEN = os.getenv('DISCORD_TOKEN')
    
    bobbyBearcat = DiscordBot()
    bobbyBearcat.run(TOKEN)
            