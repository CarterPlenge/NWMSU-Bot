from discord import app_commands, Object, Interaction

def register(tree: app_commands.CommandTree, guild_id: int):
    guild = Object(id=guild_id)

    @tree.command(name="about", description="About this bot", guild=guild)
    async def request(interaction: Interaction):
        """Print info about the bot"""
        
        message = """
        This bot is created by the collabrative effor of NWMSU Students.
        Check out the code at https://github.com/GameMagma/NWMSU-Bot.git
        
        Its purpose is to aid in the management of NWMSU esports' discord servers
        Type "/allCommands" to see a full list of commands.
        """
        
        await interaction.response.send_message(
            message,
            ephemeral=True
        )
