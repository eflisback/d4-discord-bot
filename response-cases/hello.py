import random


def handle_hello() -> str:
    greetings = [
        "Hello.",
        "Hi.",
        "Hey.",
        "Hey there.",
        "Hi there.",
        "Greetings.",
        "🎵 Is it me you're looking fooor? 🎶",
    ]
    return random.choice(greetings)
