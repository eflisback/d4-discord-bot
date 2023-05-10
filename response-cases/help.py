def handle_help() -> str:
    response = "Stay ahile and listen! I am Deckard Cain, your personal guide to Diablo 4. Here are some commands you can use:\n\n"
    response += "`!help`: Displays this list of commands.\n"
    response += "`!lore`: Shares a random piece of Diablo 4 lore with you.\n"
    response += (
        "`!build <class>`: Provides a recommended build for the specified class.\n"
    )
    response += "`!items <type>`: Shows a list of top items of the specified type.\n"
    response += "`!news`: Fetches the latest news on Diablo 4 from official sources.\n"
    response += (
        "`!stats <class>`: Displays the latest statistics for the specified class.\n"
    )
    response += "\nIf you have any questions or need help, just type `!help` again and I'll be happy to assist you!"
    return response
