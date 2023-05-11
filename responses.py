import sys
import os

current_directory = os.path.dirname(os.path.realpath(__file__))
responses_directory = os.path.join(current_directory, "response-cases")

sys.path.append(responses_directory)

from hello import handle_hello
from help import handle_help
from lore import handle_lore
from mod import handle_mod


def handle_response(user_message, guild_id) -> str:
    p_message = user_message.lower().split()[0]
    print(p_message)

    match p_message:
        case "hello":
            return handle_hello()

        case "help":
            return handle_help()

        case "lore":
            return handle_lore()

        case "mod":
            return handle_mod(user_message, guild_id)

        case _:
            return "Did not understand."
