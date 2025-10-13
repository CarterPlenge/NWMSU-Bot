from . import user, board, admin

def register_all(tree, guild_id):
    """Register commands from all categories."""
    print("Loading user commands...")
    user.register_all(tree, guild_id)

    print("Loading board commands...")
    board.register_all(tree, guild_id)

    print("Loading admin commands...")
    admin.register_all(tree, guild_id)
