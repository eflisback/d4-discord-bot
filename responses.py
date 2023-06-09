import sys
import os

current_directory = os.path.dirname(os.path.realpath(__file__))
responses_directory = os.path.join(current_directory, "response-cases")

sys.path.append(responses_directory)

from hello import handle_hello
from help import handle_help
from lore import handle_lore
from gpt import handle_gpt
from add import handle_add
from countdown import handle_countdown
from image import handle_image


def handle_response(user_message, user) -> tuple:
    p_message = user_message.lower().split()[0]
    p_id = user.id
    p_name = user.name

    match p_message:
        case "hello":
            return handle_hello(p_name), False

        case "help":
            return handle_help(), False

        case "lore":
            return handle_lore(), False

        case "gpt":
            return handle_gpt(user_message, p_name, p_id), False

        case "add":
            return handle_add(user_message, p_id), False

        case "countdown":
            return handle_countdown(user_message), False

        case "image":
            return handle_image(user_message, p_name, p_id), True

        case _:
            return "I'm afraid that's beyond my wisdom, adventurer...", False
