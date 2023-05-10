import random


def handle_hello() -> str:
    greetings = ["Hello.", "Hi.", "Hey.", "Hey there.", "Hi there.", "Greetings."]
    return random.choice(greetings)
