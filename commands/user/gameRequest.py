from discord import app_commands, Object, Interaction

def register(tree: app_commands.CommandTree, guild_id: int):
    guild = Object(id=guild_id)

    @tree.command(name="request", description="Request a new game", guild=guild)
    @app_commands.describe(
        game="The game you want to request.",
        platform="The platform the game is on."
    )
    async def request(interaction: Interaction, game: str, platform: str = "N/A"):
        """Request a new game to be added to the esports library."""

        # TODO: handle request
        print(f"Request recived for {game} on {platform}.")
        
        
        await interaction.response.send_message(
            f"Your request for **{game}** on **{platform}** has been received.",
            ephemeral=True
        )
