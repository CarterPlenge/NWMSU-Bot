from discord import app_commands, Object, Interaction

def register_commands(tree: app_commands.CommandTree, guild_id: int):
    guild = Object(id=guild_id)

    @tree.command(name="request", description="Request a new game", guild=guild)
    async def hello(interaction: Interaction, game: str, platform: str):
        await interaction.response.send_message("Hello from another file!")

    @tree.command(name="add", description="Add two numbers", guild=guild)
    async def add(interaction: Interaction, a: int, b: int):
        await interaction.response.send_message(f"{a} + {b} = {a + b}")
