def handle_response(user_message) -> str:
    p_message = user_message.lower()
    print(p_message)

    match p_message:
        case "hello":
            return "hiya"
        
        case "!help":
            return "help called"
        