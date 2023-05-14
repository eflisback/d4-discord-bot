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


def handle_response(user_message, user) -> str:
    p_message = user_message.lower().split()[0]
    p_id = user.id
    p_name = user.name

    match p_message:
        case "hello":
            return handle_hello(p_name)

        case "help":
            return handle_help()

        case "lore":
            return handle_lore()

        case "gpt":
            return handle_gpt(user_message, p_name, p_id)

        case "add":
            return handle_add(user_message, p_id)

        case _:
            return "Did not understand."
