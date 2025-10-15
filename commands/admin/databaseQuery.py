from discord import app_commands, Object, Interaction
from permissions import require_any_role


def register(tree, database, guild_id):
    guild = Object(id=guild_id)

    @tree.command(name="databaseQuery", description="Query the database for information", guild=guild)
    @require_any_role("Esports Staff", "President", "Trusted bot contributor")
    @app_commands.describe(
        query_name="What do you want to query for?"
    )
    @app_commands.choices(
        databaseQuery=[
            app_commands.Choice(name="gameRequest", value="gameRequest")
        ]
    )
    async def databaseQuery(interaction: Interaction, databaseQuery: str):
        try:
            if databaseQuery == "gameRequest":
                status, response = database.get_game_requests()
                if not(status):
                    raise response
            
            
            await interaction.response.send_message(
                f"""```{response}```"""
            )

        except Exception as e:
            await interaction.response.send_message(
                f"An unexpected error has occured: {str(e)}", 
                ephemeral=True
            )

