from discord import app_commands, Object, Interaction
from permissions import require_any_role

def register(tree: app_commands.CommandTree, database, guild_id: int):
    guild = Object(id=guild_id)

    @tree.command(name="say", description="Makes the bot say what you type", guild=guild)
    @require_any_role("Board Member", "Esports Staff", "President", "Trusted bot contributor")
    @app_commands.describe(
        text="text",
    )
    async def say(interaction: Interaction, text: str):

        await interaction.response.send_message(
            text
        )
