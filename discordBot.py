import discord
from discord import app_commands

from dotenv import load_dotenv

load_dotenv()

class DiscordBot:
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        self.client = discord.Client(intents=intents)
        self.tree = app_commands.CommandTree(self.client)

    def _setup_events(self):
        """Sets up event handlers"""

        @self.client.event
        async def on_ready(): # Print info once bot is ready
            await self.tree.sync(guild=discord.Object(id=))
            print(f"Logged in as {self.client.user}")

        @self.client.event 
        async def on_message(message): # when a message is sent
            await self.handle_message(message)

        @self.tree.command(
            name="commandname",
            description="My first application Command"
        )
        async def first_command(interaction):
            await interaction.response.send_message("Hello!")

        @self.client.event
        async def on_message(message):
            await self.handle_message(message)

    async def handle_message(message):
        """
        Put functionality here if you want to do
        somthing on basic messages.
        """
        return
    
    def run(self, token):


if __name__ == "__main__":
    bobbyBearcat = DiscordBot()
    bobbyBearcat.run(DISCORD_TOKEN)
            