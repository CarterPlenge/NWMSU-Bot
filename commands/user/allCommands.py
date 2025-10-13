from discord import app_commands, Object, Interaction

def register(tree: app_commands.CommandTree, guild_id: int):
    guild = Object(id=guild_id)

    @tree.command(name="about", description="About this bot", guild=guild)
    async def request(interaction: Interaction):
        """Print info about the bot"""
        
        allcommands = ""
        
        await interaction.response.send_message(
            allcommands,
            ephemeral=True
        )
