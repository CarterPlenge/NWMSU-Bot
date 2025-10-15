from discord import app_commands, Object, Interaction
from permissions import require_any_role

def register(tree, database, guild_id):
    guild = Object(id=guild_id)

    @tree.command(name="shutdown", description="Shut down the bot", guild=guild)
    @require_any_role("Esports Staff", "President", "Trusted bot contributor")
    async def shutdown(interaction: Interaction):
        await interaction.response.send_message("Bot shutting down...", ephemeral=True)
        await interaction.client.close()
