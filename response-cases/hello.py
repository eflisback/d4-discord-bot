import random


def handle_hello() -> str:
    greetings = ["Hello", "Hi.", "Hey.", "Hey there.", "Hi there."]
    return random.choice(greetings)
