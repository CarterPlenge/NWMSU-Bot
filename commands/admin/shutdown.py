from discord import app_commands, Object, Interaction

def register(tree, guild_id):
    guild = Object(id=guild_id)

    @tree.command(name="shutdown", description="Shut down the bot", guild=guild)
    @app_commands.default_permissions(administrator=True)
    async def shutdown(interaction: Interaction):
        await interaction.response.send_message("Bot shutting down...", ephemeral=True)
        await interaction.client.close()
