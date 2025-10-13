from discord import app_commands, Object, Interaction

def register(tree: app_commands.CommandTree, guild_id: int):
    guild = Object(id=guild_id)

    @tree.command(name="say", description="Makes the bot say what you type", guild=guild)
    @app_commands.describe(
        text="text",
    )
    async def say(interaction: Interaction, text: str):

        await interaction.response.send_message(
            text,
            ephemeral=True
        )
