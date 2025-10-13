from discord import app_commands, Object, Interaction
from permissions import require_role

def register(tree, guild_id):
    guild = Object(id=guild_id)

    @tree.command(name="shutdown", description="Shut down the bot", guild=guild)
    @require_role("admin")
    async def shutdown(interaction: Interaction):
        await interaction.response.send_message("Bot shutting down...", ephemeral=True)
        await interaction.client.close()
