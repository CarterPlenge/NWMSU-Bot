from discordBot import DiscordBot
import os

TOKEN = os.getenv('DISCORD_TOKEN')

bobbyBearcat = DiscordBot()
bobbyBearcat.run(TOKEN)
