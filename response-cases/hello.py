import random


def handle_hello(name) -> str:
    greetings = [
        "Hello",
        "Hi",
        "Hey",
        "Hey there",
        "Hi there",
        "Greetings",
    ]
    return f"{random.choice(greetings)}, {name}."
