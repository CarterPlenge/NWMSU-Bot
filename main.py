import os
from dotenv import load_dotenv

import interactions
from interactions import slash_command, SlashContext, OptionType, slash_option, listen, ModalContext, User, \
    SlashCommandChoice
from interactions import message_context_menu, ContextMenuContext, Message, Modal, ShortText
from interactions.api.events import MessageCreate

from SQLManager import SQLManager

load_dotenv()

bot = interactions.Client(intents=interactions.Intents.ALL)

# === GLOBALS ===
# One day I'll integrate this into a place that uses less memory. Today is not that day, and neither is tomorrow
database = SQLManager()  # Database connection
_VERSION = "0.1.0"  # MAJOR.MINOR.PATCH

# === EVENTS ===


@listen()
async def on_startup():
    print(f"Bot Version {_VERSION}, Interactions Library version {interactions.__version__}")
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------\n")


# === COMMANDS ===


@slash_command(
    name="ping",
    description="Ping the bot to see if it's alive."
)
async def ping(ctx: SlashContext):
    await ctx.send("Pong!")


@slash_command(
    name="about",
    description="General information about the bot",
)
async def about(ctx: SlashContext):
    await ctx.send(f"Created by Connor Midgley.\n"
                   "Source code available at https://github.com/GameMagma/NewNakamoto \n"
                   f"Version {_VERSION}\n\n"

                   "New features for 0.1.0:\n"
                   "It functions",
                   ephemeral=True)


@slash_command(
    name="dbtest",
    description="Tests the database connection.",
    scopes=[os.getenv("TEST_GUILD_ID")]
)
async def dbtest(ctx: SlashContext):
    await ctx.send(database.get_wallet(ctx.author.id)[1])


# === Admin ===
@slash_command(
    name="admin",
    description="Commands for the bot administrator",
    scopes=[os.getenv("TEST_GUILD_ID")],
    sub_cmd_name="close_connection",
    sub_cmd_description="Closes connection to the database"
)
async def admin_close_connection(ctx: SlashContext):
    database.close()
    await ctx.send("Connection to the database closed.")


# Command to restart the connection to the database. Check if it's closed already. If so, close it. Finally,
# open a new connection.
@slash_command(
    name="admin",
    description="Commands for the bot administrator",
    scopes=[os.getenv("TEST_GUILD_ID")],
    sub_cmd_name="restart_connection",
    sub_cmd_description="Restarts the connection to the database"
)
async def admin_restart_connection(ctx: SlashContext):
    if database.is_closed():
        database.close()

    globals()['database'] = SQLManager()  # Reset the database connection

    await ctx.send("Connection to the database restarted.")


@slash_command(
    name="admin",
    description="Commands for the bot administrator",
    sub_cmd_name="say",
    sub_cmd_description="Make the bot say something."
)
@slash_option(
    name="message",
    description="The message for the bot to say.",
    required=True,
    opt_type=OptionType.STRING
)
async def admin_say(ctx: SlashContext, message: str):
    if ctx.author_id == 456269883873951744:
        await ctx.send("Repeating:", ephemeral=True)
        await ctx.channel.send(message)
    else:
        await ctx.send("You do not have permission to use this command.", ephemeral=True)


@slash_command(
    name="status",
    description="Commands for status management",
    sub_cmd_name="set",
    sub_cmd_description="Set the bot status."
)
@slash_option(
    name="status",
    description="The status to set.",
    required=True,
    opt_type=OptionType.STRING,
    choices=[
        SlashCommandChoice(name="online", value="online"),
        SlashCommandChoice(name="idle", value="idle"),
        SlashCommandChoice(name="dnd", value="dnd"),
        SlashCommandChoice(name="invisible", value="invisible")
    ],
)
@slash_option(
    name="activity_type",
    description="The activity to set. Only used if status is online",
    required=False,
    opt_type=OptionType.STRING,
    choices=[
        SlashCommandChoice(name="playing", value="playing"),
        SlashCommandChoice(name="streaming", value="streaming"),
        SlashCommandChoice(name="listening", value="listening"),
        SlashCommandChoice(name="watching", value="watching"),
        SlashCommandChoice(name="competing", value="competing")
    ]
)
@slash_option(
    name="activity",
    description="The activity to set. If you set an activity type, you need to set this too.",
    required=False,
    opt_type=OptionType.STRING
)
async def status_set(ctx: SlashContext, status: str, activity_type: str = None, activity: str = None):
    if ctx.author_id == 456269883873951744:
        if status == "online":
            if activity_type is not None and activity is not None:
                # Convert activity type to the correct type
                match activity_type:
                    case "playing":
                        activity_type = interactions.ActivityType.PLAYING
                    case "streaming":
                        activity_type = interactions.ActivityType.STREAMING
                    case "listening":
                        activity_type = interactions.ActivityType.LISTENING
                    case "watching":
                        activity_type = interactions.ActivityType.WATCHING
                    case "competing":
                        activity_type = interactions.ActivityType.COMPETING
                    case _:
                        activity_type = interactions.ActivityType.PLAYING

                # Set the status
                await bot.change_presence(
                    status=status, activity=interactions.Activity(name=activity, type=activity_type))
            else:
                await bot.change_presence(status=status)
        else:
            await bot.change_presence(status=status)
        await ctx.send("Status set.")
    else:
        await ctx.send("You do not have permission to use this command.", ephemeral=True)


@slash_command(
    name="admin",
    description="Commands for the bot administrator",
    sub_cmd_name="shutdown",
    sub_cmd_description="Shuts down the bot."
)
async def shutdown(ctx: SlashContext):
    if ctx.author_id == 456269883873951744:
        print("Asked to shut down. Goodbye.")
        await ctx.send("Shutting down.")
        if not database.is_closed():
            database.close()
        await bot.stop()
    else:
        await ctx.send("You do not have permission to use this command.", ephemeral=True)


bot.start(os.getenv("DISCORD_TOKEN"))
