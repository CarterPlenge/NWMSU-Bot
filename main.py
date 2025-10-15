import os
from dotenv import load_dotenv
from discordBot import DiscordBot
from SQLManager import SQLManager

load_dotenv()

db = SQLManager(min_conn=2, max_conn=10)

if __name__ == "__main__":
    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD_ID = int(os.getenv('GUILD_ID')) if os.getenv('GUILD_ID') else None

    if not db.test_connection():
        print("Failed to connect to database. Exiting...")
        exit(1)
    
    try:
        bot = DiscordBot(database=db, guild_id=GUILD_ID)
        bot.run(TOKEN)
    finally:
        db.close_pool()