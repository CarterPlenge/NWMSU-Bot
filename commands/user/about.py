from discord import app_commands, Object, Interaction

def register(tree: app_commands.CommandTree, database, guild_id: int):
    guild = Object(id=guild_id)

    @tree.command(name="about", description="About this bot", guild=guild)
    async def about(interaction: Interaction):
        """Print info about the bot"""
        
        message = """This bot is created by the collaborative effort of NWMSU Students.
        
        --Check out the code and consider contributing at--
            https://github.com/GameMagma/NWMSU-Bot.git
        
        Its purpose is to aid in the management of NWMSU esports' discord servers
        Type "/allCommands" to see a full list of commands.
        """
        
        await interaction.response.send_message(
            message,
            ephemeral=True
        )
