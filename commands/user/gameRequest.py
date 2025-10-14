from discord import app_commands, Object, Interaction
from channel import require_channel
from SQLManager import SQLManager

database = SQLManager()

def register(tree: app_commands.CommandTree, guild_id: int):
    guild = Object(id=guild_id)

    @tree.command(name="request", description="Request a new game", guild=guild)
    @app_commands.describe(
        game="The game you want to request.",
        platform="The platform the game is on."
    )
    @require_channel("game-requests")
    async def request(interaction: Interaction, game: str, platform: str = "N/A"):
        success, message = database.add_game_request(interaction.user.id, game, platform)
        
        if success:
            await interaction.response.send_message(
                f"Your request for **{game}** on **{platform}** has been received.",
                ephemeral=True
            )
        else:
            await interaction.response.send_message(
                f"Error: {message}",
                ephemeral=True
            )
