from discord import app_commands, Object, Interaction
from permissions import require_any_role

def register(tree: app_commands.CommandTree, guild_id: int):
    guild = Object(id=guild_id)

    @tree.command(name="healthCheck", description="Check bot and db health ", guild=guild)
    @require_any_role("board", "admin")
    async def healthCheck(interaction: Interaction):
        # TODO: handle health check
        serverHealth = "good"
        databaseHealth = "good"
        
        await interaction.response.send_message(
            f"Sever health {serverHealth}\n Database health {databaseHealth}",
            ephemeral=True
        )
