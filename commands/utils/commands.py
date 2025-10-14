def get_all_commands(tree) -> str:
    """ Returns commands list"""
    if not tree.get_commands():
        return "No commands registered yet."
    
    commands_list = []
    
    for command in tree.get_commands():
        name = command.name
        description = command.description or "No description"
        commands_list.append(f"/{name} - {description}")
    
    return "\n".join(commands_list)