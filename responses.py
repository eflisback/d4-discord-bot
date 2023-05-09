def handle_response(message) -> str:
    p_message = message.lower()

    match p_message:
        case "hello":
            return "hiya"
        
        case "!help":
            return "help called"
        
        case _:
            return "Don't understand..."