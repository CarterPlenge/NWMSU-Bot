from discord import app_commands, Object, Interaction
from permissions import require_any_role

def register(tree, database, guild_id):
    guild = Object(id=guild_id) if guild_id else None

    @tree.command(name="database-query", description="Query the database for information", guild=guild)
    @require_any_role("Esports Staff", "President", "Trusted bot contributor")
    @app_commands.describe(
        databasequery="What do you want to query for?"
    )
    @app_commands.choices(
        databasequery=[
            app_commands.Choice(name="gameRequest", value="gameRequest")
        ]
    )
    async def database_query(interaction: Interaction, databasequery: str):
        try:
            if databasequery == "gameRequest":
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