def handle_help() -> str:
    response = "Stay awhile and listen! I am Deckard Cain, your personal guide to Diablo 4. Here are some commands you can use:\n\n"
    response += "`!help`: Displays this list of commands.\n"
    response += "`!hello`: Say hello.\n"
    response += "`!lore`: Shares a random piece of Diablo 4 lore with you.\n"
    response += "`!countdown <event>`: Shows the remaining time until chosen event.\n"
    response += "`!gpt <prompt>`: Talk to CainGPT!\n"
    response += "`!image <prompt>`: Have Dall-E 2 generate an epic image based on your prompt.\n"
    response += (
        "`!add <key type> <api key>`: Register your API key to my secret JSON file.\n"
    )
    response += "\nIf you have any questions or need help, just type `!help` again and I'll be happy to assist you! Remember that you can always send me a direct message."
    return response
