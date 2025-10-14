from discord import app_commands, Object, Interaction
from utils.commands import get_all_commands

def register(tree: app_commands.CommandTree, guild_id: int):
    guild = Object(id=guild_id)

    @tree.command(name="allCommands", description="List all available commands", guild=guild)
    async def allCommands(interaction: Interaction):
        commands_text = get_all_commands(tree)
        
        message = f"""
        **Available Commands:**

        {commands_text}
        """
        
        await interaction.response.send_message(message, ephemeral=True)