import json


def handle_mod(user_command, guild_id):
    # Parse the command
    _, variable, value = user_command.split()

    # Load the settings from JSON file
    try:
        with open("config/server_variables.json", "r") as file:
            settings = json.load(file)
    except FileNotFoundError:
        settings = {"default": {"upvote_threshold": 250, "post_history_limit": 100}}

    # Get settings for the specific server if available, otherwise use default settings
    server_settings = settings.get(str(guild_id), settings["default"].copy())

    # Update the specific variable
    server_settings[variable] = int(value)  # Assuming value is an integer

    # Save the updated settings
    settings[str(guild_id)] = server_settings
    with open("config/server_variables.json", "w") as file:
        json.dump(settings, file)

    return f"Changed {variable} to {value} for this server."
